from dhs import DHSMgr
import importlib
import random
class MJSoul(DHSMgr):

    def __init__(self):
        super().__init__()
        self.version = '0.11.9.w'  # "0.6.97.w"
        # "mj-srv-7.majsoul.com:4130","mj-srv-7.majsoul.com:4131","mj-srv-7.majsoul.com:4132","mj-srv-7.majsoul.com:4133","mj-srv-5.majsoul.com:4100","mj-srv-5.majsoul.com:4102","mj-srv-5.majsoul.com:4101","mj-srv-5.majsoul.com:4103"
        self._url = 'wss://gateway-hw.maj-soul.com/gateway'  # 'wss://gateway-cdn.maj-soul.com/gateway' 'wss://gateway-vexcdn.maj-soul.com/gateway' 'wss://mj-srv-7.majsoul.com:4131/' "wss://mj-srv-5.majsoul.com:4101"
        self._addrBook = importlib.import_module('my_proto_pb2')
        self._serviceRoot = 'Lobby'

    async def login(self,user, passwd):
        k = lambda cnt: float.hex(random.random())[-4-cnt:-cnt]
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
            'client_version_string': 'web-0.11.9',
            'tag': 'cn'
        }
        print('before login')
        await self.send('login', print, msg)
        print('login success')
