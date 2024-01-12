import random
import pprint
from dataclasses import dataclass
from typing import Callable, Generator

from dhs import DHSMgr
from utils import *


class MJSoul(DHSMgr):

    def __init__(self):
        super().__init__()
        self.version = '0.11.11.w'  # game version
        # expired websocket url
        # wss://mj-srv-7.majsoul.com:4131/
        # wss://mj-srv-7.majsoul.com:4130
        # wss://mj-srv-7.majsoul.com:4131
        # wss://mj-srv-7.majsoul.com:4132
        # wss://mj-srv-7.majsoul.com:4133
        # wss://mj-srv-5.majsoul.com:4100
        # wss://mj-srv-5.majsoul.com:4102
        # wss://mj-srv-5.majsoul.com:4101
        # wss://mj-srv-5.majsoul.com:4103
        # wss://gateway-cdn.maj-soul.com/gateway
        # wss://gateway-vexcdn.maj-soul.com/gateway
        self._url = 'wss://gateway-hw.maj-soul.com/gateway'
        self._serviceRoot = 'Lobby'

    async def login(self, user, passwd, callback=print):
        k = lambda cnt: float.hex(random.random())[-4 - cnt:-cnt]
        msg = {
            'account': user,
            'password': self._hash(passwd),
            'reconnect': True,
            'device': {
                'platform': 'pc',
                'hardware': 'pc',
                'os': 'windows',
                'os_version': 'win10',
                'is_browser': True,
                'software': 'chrome',
                'sale_platform': 'web',
            },
            'random_key': "-".join([k(4) + k(4), k(4), k(4), k(4), k(4) + k(4) + k(4)]),
            'client_version': {'resource': self.version},
            'gen_access_token': False,
            'type': 0,
            'currency_platforms': [],
            'client_version_string': 'web-0.11.11',  # version
            'tag': 'cn'
        }
        await self.send('login', callback, msg)
        print('login...')

    async def fetch_record(self, start: int, count: int, game_type: int, callback: Callable[[dict], None] = print):
        """

        Args:
            start: start retrieval index, must be greater than 0
            count: record count, must be greater than 0
            game_type: type of game, refer to const parameter GAME_MODE_XXX
            callback: callback function after the return of data

        Returns:

        """
        await self.send('fetchGameRecordList', callback, {'start': start,
                                                          'count': count,
                                                          'type': game_type})

class GameDataAnalysis:
    def __init__(self, user_name: str):
        self.game_records: dict[int, GameRecord] = {}  # sorted by timestamp in descending order
        self.user_name = user_name
        self.user_records: list[tuple[Player, PlayerResult]] = []


    def load_records(self, record_data: dict):
        record_data = record_data.get('recordList', [])
        for match_data in record_data:
            players = {}
            for player_data in match_data['accounts']:
                character_data = player_data['character']
                character = Character(character_id=character_data['charid'],
                                      favor_level=character_data.get('level', 0),
                                      skin=character_data['skin'],
                                      is_upgraded=character_data.get('isUpgraded', False))

                seat = player_data.get('seat', 0)
                player = Player(account_id=player_data['accountId'],
                                name=player_data['nickname'],
                                seat=seat,
                                character=character)
                players[seat] = player

            player_results = {}
            for player_result_data in match_data['result']['players']:
                seat = player_result_data.get('seat', 0)
                player_result = PlayerResult(game_point=player_result_data['partPoint1'],
                                             score_gain=player_result_data.get('gradingScore', 0),
                                             gold_gain=player_result_data.get('gold', 0))
                player_results[seat] = player_result
            game_result = GameResult(player_results=player_results)

            game_record = GameRecord(uuid=match_data['uuid'],
                                     category=match_data['config']['category'],
                                     mode=match_data['config']['mode']['mode'],
                                     players=players,
                                     game_result=game_result,
                                     start_timestamp=match_data['startTime'])
            self.game_records[game_record.start_timestamp] = game_record
        pprint.pprint(self.game_records)

    def _character_info_collect(self):
        for record in self.game_records.values():
            matching_player = self._player_name_matching(record.players)
            result = record.game_result.player_results[matching_player.seat]
            yield matching_player, result

    def _player_name_matching(self, players: dict[int, 'Player']) -> 'Player':
        for player in players.values():
            if player.name == self.user_name:
                return player
        raise ValueError(f'Cannot find player {self.user_name} '
                         f'among game players {[player.name for player in players.values()]}')

    def analysis_character_relation(self):
        for player, result in self._character_info_collect():
            pass
        print('MizuSakana')  # TODO


@dataclass
class GameRecord:
    uuid: str
    category: int
    mode: int
    players: dict[int, 'Player']  # seat: player
    game_result: 'GameResult'
    start_timestamp: int


@dataclass
class Player:
    account_id: int
    name: str
    seat: int
    character: 'Character'


@dataclass
class Character:
    character_id: int
    favor_level: int
    skin: int
    is_upgraded: bool


@dataclass
class GameResult:
    player_results: dict[int, 'PlayerResult']  # seat, player result


@dataclass
class PlayerResult:
    game_point: int
    score_gain: int = 0
    gold_gain: int = 0
