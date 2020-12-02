
##### 1、方案一 

本地执行、云服务器、云函数等等

下载到本地，填写 `qqreadCookie.py` 中的 `qqreadheaders` `qqreadtimeheaders` `qqreadtimeurl` 等信息  
云函数请善用搜索以及对应官方文档

##### 2、方案二

GitHub action自动运行，账号信息读取自 `Repo-Setting-Secrets`  
**！请勿滥用！**



### 通知服务

默认不开启，需要通知服务的需修改 `NOTIFYCFG` 参数

目前会发送通知的情况有: 账号headers过期; 全部通知；收获宝箱通知；每收获15个宝箱通知  

支持两种通知方式，后续看心情添加其他通知方式

```
  [0，1，2]  0:不通知     1:server酱      2:bark服务
```

1. 使用Server酱的需要参数 `SCKEY` ，支持GitHub action
2. 使用bark的填写 `BARK` ，支持GitHub action

### 通知类型

默认为每领15个宝箱通知一次，需要其他通知类型请修改 `NOTIFYTYPE` 参数

支持三种通知类型

```
  [0，1，2，3]  0：关闭通知   1：所有通知   2：领取宝箱成功通知   3：每领15个宝箱通知一次
```

### 特别感谢(排名不分先后)：
* [@ziye12](https://github.com/ziye12)

* [@Zero-S1](https://github.com/Zero-S1)

