import requests
import os
import time


#######################
# 通知服务
#######################

# [0,1,2]  0:不通知     1:server酱      2:bark服务

NOTIFYCFG = 0

SCKEY = ''        # Server酱的SCKEY

BARK = ''         # bark服务,自行搜索
##################################################################


def n0(a, b):
    """空函数,即不使用通知服务"""
    print(">>>>未开启通知服务")
    return


def serverJ(title, content):
    """server酱服务"""
    sckey = SCKEY
    if "SCKEY" in os.environ:
        """
        判断是否运行自GitHub action,"SCKEY" 该参数与 repo里的Secrets的名称保持一致
        """
        sckey = os.environ["SCKEY"]

    if not sckey:
        print("server酱服务的SCKEY未设置!!\n取消推送")
        return
    print("serverJ服务启动")
    data = {
        "text": title,
        "desp": content
    }
    response = requests.post(f"https://sc.ftqq.com/{sckey}.send", data=data)
    print(response.text)


def bark(title, content):
    """bark服务"""
    bark_token = BARK
    title = content.replace("#", "")
    content = content.replace("#", "")
    if "BARK" in os.environ:
        """
        判断是否运行自GitHub action,"BARK" 该参数与 repo里的Secrets的名称保持一致
        """
        bark_token = os.environ["BARK"]
    if not bark_token:
        print("bark服务的bark_token未设置!!\n取消推送")
        return
    response = requests.get(
        f"""https://api.day.app/{bark_token}/{title}/{content}""")
    print(response.text)

if "NOTIFYCFG" in os.environ and os.environ["NOTIFYCFG"].strip():
    NOTIFYCFG = eval(os.environ["NOTIFYCFG"])
    
notify = [n0, serverJ, bark][NOTIFYCFG]

if __name__ == "__main__":
    print("通知服务测试")
    start = time.time()
    notify("QQRead脚本通知服务", "needYou2Know\n通知服务测试")
    print("耗时: ", time.time()-start, "s")
