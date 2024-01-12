# mjsoul-py
这是雀魂游戏的一个工具,能使用websocket调用官方提供的API,用于牌谱数据分析统计。本程序Fork于[mjsoul](https://github.com/lostkevin/mjsoul-py)

## Dependency

+ protobuf
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

## pb2生成
使用liqi.proto通过[在线网站](https://www.grpcgenerator.com/)生成的pb2文件可使用

通过protoc生成的pb数据结构文件无法运行

## TODO
* 从雀魂主网页获取当前版本信息，如发现无法获取数据，运行**base.py**获取雀魂最新版本，并替换**mjsoul.py**中的版本信息