import asyncio
import json

from mjsoul import MJSoul, GameDataAnalysis
from utils import *


async def main_lobby(_user):
    data_analysis = GameDataAnalysis()

    mgr = MJSoul()
    loop = asyncio.create_task(mgr.run())
    login = asyncio.create_task(mgr.login(_user['user'], _user['passwd'], callback=None))
    await login

    # login and start query
    # await mgr.send('fetchGameRecordList', print, msg={'start': 0, 'count':30, 'type': 2})
    await mgr.fetch_record(start=1, count=50, game_type=GAME_CATEGORY_RANK, callback=data_analysis.load_records)

    # mgr.bind('NotifyContestMatchingPlayer', print)
    await loop  # run_forever


if __name__ == '__main__':
    with open('.\key.json', 'r') as f:
        user = json.load(f)
        f.close()

    asyncio.run(main_lobby(user))
