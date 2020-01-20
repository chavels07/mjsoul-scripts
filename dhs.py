# coding:utf-8
import importlib
import hmac
import asyncio
import websockets
from google.protobuf import reflection
from protobuf_to_dict import protobuf_to_dict, dict_to_protobuf

class DHSMgr:
    _msgType = {'notify': b'\x01', 'req': b'\x02', 'res': b'\x03'}
    def __init__(self):
        self._url = "wss://mj-srv-3.majsoul.com:4021"
        self._msgPool = {} # msgIndex:(resType, callback func)
        self._msgIndex = 0
        self._msgQueue = []
        self._addrBook = importlib.import_module('dhs_pb2')
        self._wrapper = self._addrBook.Wrapper()
        self._serviceRoot = 'CustomizedContestManagerApi'
        self._ws = None
    @staticmethod
    def _hash(passwd : str) -> bytearray:
        return hmac.new(b'lailai', bytearray(passwd.encode('utf-8')), 'sha256').hexdigest()

    async def login(self,user, passwd):
        data = {
            'account': user,
            'password': self.__class__._hash(passwd),
            'gen_access_token': True,
            'type': 0
        }
        await self.send("loginContestManager", print, data)

    async def run(self):
        def on_message(msg):
            if msg[0] == ord(self.__class__._msgType['notify']):
                wrapper = self._addrBook.Wrapper()
                wrapper.ParseFromString(msg[3:])
                print(wrapper.data)
            elif msg[0] == ord(self.__class__._msgType['res']):
                # get index
                index = msg[1] + msg[2] * 256
                if index in self._msgPool.keys():
                    # callback
                    self._wrapper.ParseFromString(msg[3:])
                    res = self._msgPool[index][0]()
                    res.ParseFromString(self._wrapper.data)
                    self._msgPool[index][1](res)
                    self._msgPool.pop(index)
        async with websockets.connect(self._url) as ws:
            self._ws = ws
            while True:
                on_message(await ws.recv())

    async def send(self, path, callback, msg = None):
        try:
            while self._ws is None:
                await asyncio.sleep(1)
            self._msgIndex %= 60007
            method = self._addrBook.DESCRIPTOR.services_by_name[self._serviceRoot].methods_by_name[path]
            obj = reflection.MakeClass(method.input_type)()
            self._msgPool[self._msgIndex] = (reflection.MakeClass(method.output_type), callback)
            if msg is not None:
                dict_to_protobuf(obj, msg)
            self._wrapper.name = bytes('.' + method.full_name, 'utf-8')
            self._wrapper.data = obj.SerializeToString()
            req = self.__class__._msgType['req'] + bytes([self._msgIndex % 256, self._msgIndex // 256]) + self._wrapper.SerializeToString()
            self._msgIndex += 1
            await self._ws.send(req)
        except KeyError:
            print('API not exist')
            return
