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
    login = asyncio.create_task(mgr.login(User['user'], User['passwd']))
    await login
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
    await loop #run_forever
asyncio.run(main_dhs())

