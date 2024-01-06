from dhs import DHSMgr
from mjsoul import MJSoul
import asyncio
import json

with open('.\key.json', 'r') as f:
    User = json.load(f)
    f.close()

async def main_dhs():
    mgr = DHSMgr()
    loop = asyncio.create_task(mgr.run())
    print('start')
    login = asyncio.create_task(mgr.login(User['user'], User['passwd']))
    await login
    print('login success')
    #login and start query
    await mgr.send('fetchRelatedContestList', print)
    mgr.bind('NotifyContestMatchingPlayer', print)
    await loop #run_forever

async def main_lobby():
    mgr = MJSoul()
    loop = asyncio.create_task(mgr.run())
    login = asyncio.create_task(mgr.login(User['user'], User['passwd']))
    await login
    #login and start query
    # await mgr.send('fetchGameRecordList', print, msg={'start': 1, 'count':30, 'type': 0})
    # await mgr.send('fetchGameRecordList', print, msg={'start': 1, 'count':30, 'type': 1})
    await mgr.send('fetchGameRecordList', print, msg={'start': 1, 'count':30, 'type': 2})
    # await mgr.send('fetchGameRecordList', print, msg={'start': 1, 'count':30, 'type': 4})
    
    # mgr.bind('NotifyContestMatchingPlayer', print)
    await loop #run_forever
asyncio.run(main_lobby())

