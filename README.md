留着学习

# qqreader 
https://m.q.qq.com/a/s/623327eab13a1c84018e9e9b002ef0af

https://github.com/ziye12/JavaScript        

https://github.com/Water008/qqread

企鹅读书


QQREADHEADERS QQREADTIMEHEADERS 两个参数格式为
{"Cookie":"ywguid=*****;ywkey=******;platform=ios;channel=mqqmina;mpVersion=0.30.0"}

{"Cookie":"ywguid=*****;ywkey=*****;platform=ios;channel=mqqmina;mpVersion=0.31.0;qq_ver=8.4.17;os_ver=iOS 12.4.9;mpos_ver=1.21.0;platform=ios;openid=*****","Content-Type":"application/json","User-Agent":"QQ/8.4.17.638 CFNetwork/978.0.7 Darwin/18.7.0","Connection":"keep-alive","Accept-Language":"zh-cn","mpversion":"0.31.0","Accept-Encoding":"br, gzip, deflate"}

加引号，需要完整的cookie


body 包含    
$request.body.indexOf("bookDetail_bottomBar_read_C") >= 0 &&
$request.body.indexOf("bookLib2_bookList_bookClick_C") >= 0 &&
$request.body.indexOf("bookRead_show_I") >= 0 &&

不包含
$request.body.indexOf("topBar_left_back_C") < 0 &&
$request.body.indexOf("bookRead_dropOut_shelfYes_C") < 0
