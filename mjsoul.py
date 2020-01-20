from dhs import DHSMgr
import importlib
import random
class MJSoul(DHSMgr):

    def __init__(self):
        super().__init__()
        self.version = "0.6.97.w"
        self._url = "wss://mj-srv-5.majsoul.com:4101"
        self._addrBook = importlib.import_module('mjsoul_pb2')
        self._serviceRoot = 'Lobby'

    async def login(self,user, passwd):
        k = lambda cnt: float.hex(random.random())[-4-cnt:-cnt]
        msg = {
            'account': user,
            'password': self._hash(passwd),
            'reconnect': False,
            'device': {'device_type': "pc", 'os': "", 'os_version': "", 'browser': "chrome"},
            'random_key': "-".join([k(4) + k(4), k(4), k(4), k(4), k(4) + k(4) + k(4)]),
            'client_version': self.version,
            'gen_access_token': False,
            'currency_platforms': [2]
        }
        await self.send('login', print, msg)
