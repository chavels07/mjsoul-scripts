# mjsoul-py
这是雀魂游戏的一个工具,能使用websocket调用官方提供的API,支持游戏前端以及后台比赛管理系统. 本程序是[mjsoul](https://github.com/takayama-lily/mjsoul)的Python版本

## Dependency

+ protobuf
+ protobuf-to-dict
+ websockets
+ asyncio

## Demo

```
async def main_dhs():
    mgr = DHSMgr()
    #loop task用于异步接收消息
    loop = asyncio.create_task(mgr.run())
    #第一步必须是login
    login = asyncio.create_task(mgr.login(User['user'], User['passwd']))
    await login

    #接下来调用所需的命令
    await mgr.send('fetchRelatedContestList', print)
    await loop #run_forever

asyncio.run(main_dhs())
```
