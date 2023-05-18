- http basic auth: use dict
- OAuth: use requests_oauthlib.OAuth1
- socks proxy: must install requests[socks]

SSL 证书：

```
1. requests.get() options set verfiy=False
2. urllib3.disbale_warnings()or logging.captureWarnings()
```

正则表达式 re

- match 从头开始匹配
- search 查找第一个符合条件的匹配
- findall 查找所有符合条件的匹配
- sub 查找并替换所有符合条件的字符
- compile 字符串编译成正则表达式对象

httpx 支持 HTTP/2.0

```bash
pip install httpx[http2]
```

```python
import httpx

client = httpx.Client(http2=True)
```

- pyquery 可以作为 html 的解析挑选工具之一。语法类似于 CSS 选择器，对于熟悉前端的人员非常友好。
- pool.map 方法是阻塞的，会等待所有任务完成后才会返回。如果需要更高级的控制，可以考虑使用 pool.imap 或 pool.imap_unordered
  方法。
  这些方法将返回一个迭代器，允许您按需获取结果，并在必要时处理异常。map 和 imap 都不会因为中间错误中断后续任务的执行。

```python
import multiprocessing


def foo(num):
    if num == 3:
        raise ValueError
    print(f'num={num}')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool.map(foo, range(1, 11))
    pool.close()
```

- pymongo upsert 做法更新 / 插入数据，这样即使程序出错也能重试。只要保证有一个唯一的 ID 标识。

---

网页解析三种方式：

- RE 原始，繁琐 => re
- XPath => lxml
- CSS Selector => pyquery
- 节点式访问 /find()/select(CSS 选择器) =>  bs4(支持多种解析器，多种查询方式)
- CSS/XPath/re => parsel

---

常见文本类型的读写：

- txt => file
- CSV => csv.writer(csvfile) /pandas dataframe
- json => json. `json.dumps(data, indent=2, ensure_ascii=False)` ensure_ascii 这个选项 False 可以支持中文，避免 utf-8
- mysql

```python
import pymysql

data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 21
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
db = pymysql.connect(host='localhost', user='root', password=None, port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                     values=values)
update = ','.join(["{key} = %ss".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
```

上面这个方式可以适应字段的添加与变更，不用手动拼接 SQL，只改变 data。

---

- redis
- Elasticsearch => 4.7 folder（move to wiki notes）
- rabbit mq => pika as a python client 4.8 folder

mongo python async client => motor

---

JS 动态计算渲染的页面，需要模拟浏览器来渲染，然后爬取。

selenium:

- browser.find_element/find_elements 查找
- input.send_keys('iPhone') 输入
- button.click() 按钮点击交互
- actions.drag_and_drop(source, target) 鼠标拖拽模拟
- browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') js 脚本执行
- logo.get_attribute('src') 获取节点属性
- browser.implicitly_wait(10) 隐式等待
- wait = WebDriverWait(browser, 10) 显式等待
- browser.back()、browser.forward() 页面导航
- browser.get_cookies()、set_cookies() cookie 设置
- browser.switch_to.window() 选项卡管理
- option.add_experimental_option()/browser.execute_cdp_cmd() 设置 chrome 启动参数，开启某些特性。例如自定义 navigator
  绕过反爬虫
- option.add_argument('--headless') 无头模式，节省资源

> 示例项目参阅: 7.5
---

splash 基于 LUA，也可以分析网站的爬取。
Splash 可以将 JavaScript 动态渲染的操作托管到—个服务器上，爬虫爬取的时候不需要再依赖 Selenium 等库。

---

pyppeteer 依赖 chromium 开源项目，会自动安装这个依赖。

- headless 开关
- devtools 模式
- await launch(headless=False, args=['--disable-infobars']) 禁用提示条
- await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})') 设置
  navigator
- 设置 windows size

```
browser = await launch(headless=False, args=['--disable-infobars', f'--window-size={width},{height}'])
await page.setViewport({'width': width, 'height': height}) 
```

- 持久化用户登录数据。在当前代码目录下。

```python
browser = await launch(headless=False, userDataDir='./userdata',
                       args=['--disable-infobars', f'--window-size={width},{height}'])
```

- context = await browser.createIncognitoBrowserContext() 无痕模式
- page1.bringToFront() 选择某个页面到前台

---
Playwright:

- headless 模式
- 多浏览器支持，移动端浏览器模拟
- 屏幕操作录制并自动输出为代码脚本
- 所有 response 捕获
- page.route() 网络劫持

---

笔记整理建议：0-7.5 的部分目录需要整理到个人笔记仓库，后续代码参考另一个 github 项目。
https://github.com/Relph1119/python3-web-spider-learning/blob/master/src/ch07/pyppeteer_scrape.py

---

## chapter 7

- CSS 样式偏移文字解析
- icon-font 文本解析

## chapter 8

- tesserocr 识别传统验证码，光学识别
- https://pypi.org/project/retrying/ python 一个轻便的重试工具库

tesserocr 使用注意，tessdata 路径很可能识别不到，可以通过显式指定来解决。

```python
result = tesserocr.image_to_text(image, path="C:\Tesseract-OCR\\tessdata")
```

提高识别正确率的思路：

- 设置合理的阈值，二值化图像 (利用 LUT 表或者 numpy 查询)，然后识别。
- 直接转为灰度图像 (piilow)，然后识别。
  这些思路都是为了去噪。

---

OpenCV 识别滑动验证码
> 8.2 需要复现，主要是 YOLO 训练。

captcha.image 可以生成指定字符的图形验证码。
> 8.3 https://github.com/Python3WebSpider/DeepLearningImageCaptcha

8.4 yolo 滑动验证码检测

打码平台 API

SMSForwarder Android 开源应用，实现短信的接受和转发。

## chapter 9

介绍 aiohttp/requests/httpx/playwright/pyppeteer/selenium/urllib 代理的设置

免费代理池：

- 一个 free 的代理网站：https://pzzqz.com/
- github ProxyPool 这个项目值得去 fork 和完善。

付费代理池，一般是购买服务。

ADSL 动态 IP 代理池，也是购买云主机。然后配置暴露 HTTP API 服务，以及需要配置定期刷新 IP。需要高可用的话，需要多台主机均衡做冗余。

9.5 这个例子不错。

## chapter 10

模拟登陆，这个章节是重点。

- 基于 Session 和 Cookie，一般见于前后端不分离（后端渲染）的 web app。服务器必须维护 session 状态例如，集中于 redis 进行记录。
- 基于 JWT，一般见于前后端分离的 Web app。JWT 是 base64 编码的字符串，服务器不需要维护一个登录状态管理器。header+payload+signature

基于 session 和 cookie

- 如果已在真实浏览器登陆，那就直接将 cookie 复制到爬虫脚本中。
- 如果需要让爬虫脚本自动化 cookie 的获取，那就需要用户 + 密码，而且客户端手动设置 cookie 比较麻烦，推荐用session持久化会话。
=> 10.2/spider2.py spider3.py
- 也可以使用无头浏览器模拟登陆，然后保存 cookie。=> 这个跟session中取cookie本质没有区别。

如果网站对单用户有并发限流机制，那就需要账号池技术来越过风控。

- 批量账号 + 对应的登陆凭证保存，然后随机抽取账号来登录。

JWT 登录 headers 例子：

```
Authorization: jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjgzNTcxMTIxLCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsIm9yaWdfaWF0IjoxNjgzNTI3OTIxfQ.25bfKMMJkLmpinMAnkbWDzgie34atRU0EyyaZ15VYG4
```

大规模账号池的搭建： 10.4 代码

## JS 逆向

URL/API 字段加密。

登录状态的校验也可以看作此类方案’比如一个 API 的调用必须传一个 token’这个 token
必须在用户登录之后才能获取, 如果请求的时候不带该 token,API 就不会返回任何数据。

举个例子：客户端和服务器约定某个 API 的 sign 验证机制。

```
base64(md5(URL) + 某个字段值 ) => signature
```

服务器会验证这个签名的正确性。只要客户端和服务端约定好一致的加密，那么就能建议共识。

但是客户端 JS 的代码如果不加以混淆，那么很容易被识别分析破解，从而伪造模仿。因此 JS 代码混淆有时是必要的。

JS 混淆的思路就是写得一手烂代码。

- javascript-obfuscator
- terser

或者使用 WASM 编译。

JS hook 打印关键信息

```js
// ==UserScript==
// @name        New script - scrape.center
// @namespace   Violentmonkey Scripts
// @match       https://login1.scrape.center/
// @grant       none
// @version     1.0
// @author      -
// @description 2023/5/8 21:56:20
// ==/UserScript==
(function () {
    function hook(object, attr) {
        let func = object[attr]
        object[attr] = function () {
            console.log('hooked', object, attr)
            let res = func.apply(object, arguments)
            debugger;
            return res
        }
    }

    hook(window, 'btoa')
})()
```

JS 无限断点 debugger 的解决思路：

- 全局禁用断点调试，副作用很大。
- 定位到 debugger 行，在行号鼠标右键，选择 Never pause here
- JS 本地文件替换，使用 ReRes 或者 chrome overrides 实现。去掉对应的 debugger 行。

python 模拟 JS 环境执行：11.5。注意点，手动声明 Node 环境下的全局变量 CryptoJS。

Playwright 辅助 JS 逆向，

- 例如 window.encry=XXXXMethod(),XXXXMethod 就是加密方法，需要在浏览器环境进行运行。
- 将修改后的这个文件下载来本地，例如命名为 chunk.js。
- 书写特定脚本，使用 playwright 的 route 替换功能，将远程对应的原始 chunk.XXX.js 替换为本地的这个 chunk.js
- 书写特定的 JS 调用函数，来模拟之前的请求，获得响应。

AST 语法树探索，词法分析、语法分析、语法树。老生常谈的东西，https://astexplorer.net/
babel-parser 这个仓库对于写 AST 解析很有启发意义。

AST 可以计算一些混淆 JS 的实际值。

JS 常见混淆方案：

- JavaScript-Obfuscator
- JSFunck
- JJEncode => 解密方法同 AAEncode
- AAEncode => 去掉立即调研函数后面的 ()，调用.toString()，然后保存就是明文代码。

WASM 解密：

```
(func $encrypt (;4;) (export "encrypt") (param $var0 i32) (param $var1 i32) (result i32)
  local.get $var0
  local.get $var1
  i32.const 3
  i32.div_s
  i32.add
  i32.const 16358
  i32.add
)
```

找到对应 wasm 文件，利用 python（pywasm 或者 wasmer-python）来模拟 js 的执行。

11.8

## chapter 12

抓包原理：将手机或者模拟器的代理设置为代理软件所暴露的端口地址，这样手机流量就会流向代理软件，然后才是真实的访问目标。
代理软件就可以从途中截取流量和分析。

- charles 抓包分析 API
- mitmproxy 抓包分析 API
- Appjum 是一个跨平台的移动端自动化测试工具。
- Airtest UI 自动化测试

## chapter 13

安卓逆向

apk 反编译和逆向 => jadx、JEB 工具

- https://github.com/skylot/jadx

JEB Android 的使用。

- https://www.pnfsoftware.com/jeb/android

Xposed/EdXposed 这东西已经是时代的眼泪。请寻找他的后继者。

```
替换系统级别的／system／bin／app-process 程序, 控制 zygote
进程, 使得 app—process 在启动过程中加载 XposedBridge.jar 包, 这个 jar 包里定义了对系统方法、属
性所做的一系列 Hook 操作，同时提供了几个 HookAPI 供我们编写 Xposed 模块使用°
```

13.3 Xposed demo。

Xposed 的局限性，只能 hook java 层级，不能深入到 native 层级。此时可以选择 Frida。
Frida 是使用 Python 注入 JavaScript 脚本实现, 通过 JavaScript 脚本操作手机上的 Java 代码,
Python 脚本和 JavaScript 脚本的编写跟执行是在电脑上进行的，而且无须在手机上额外安装 APP 和插件。

Frida 的使用：（13.5）

- 在电脑上安装好 frida-tools，并可以成功导人使用。
- 在手机上下载并运行 frida-server 文件, 即在手机上启动—个服务, 以便电脑上的 Frida 客户端程序与之连接.
- 让电脑和手机处在同一个局域网下，并且能在电脑上用 adb 命令成功连接到手机。

解决 SSL Pining 拒绝问题。

SSL Pining 技术的原理: 客户端和服务端在握手过程中，客户端对服务端返回的证书进行校验，如果证书不是自己信任的，就拒绝后续的数据传输过程。
这样抓包工具自然抓不到有效的信息。

解决方案：

- Xposed/VirtualXposed+JustTrustMe
- Frida＋DroidSSLUnpinning

Andorid 脱壳技术演化：

- 一代壳：frida_dump，frida_dexdump
- 二代壳: FART
- 三代壳：无稳定破解办法

IDA Pro 静态分析和动态调试 so 文件。13.8

Frida-RPC 模拟执行 so 文件。13.9

AndServer-RPC 在 Android 端启动一个 http server. 13.10

unidbg ~~13.11~~ 代码不需要保留。

- https://github.com/zhkl0228/unidbg

## chapter 14

页面智能解析，基本是利用 XPath 来定义页面提取的规则，逐步完善解析。

- demo 小玩具参考：https://github.com/Gerapy/GerapyAutoExtractor

一般的二元分类问题，可以使用 SVM（支持向量机），例如对于特定的一个网页内容，判定是列表页还是详情页。

## chapter 15

scrapy 框架的基本使用 15.2 :Item Pipeline 可以持久化到 mongodb

15.5 DownloaderMiddleWare 的使用

15.6 SpiderMiddleWare 的使用，可用于修改 resp 或者对即将输出的 Item 进行修改。

15.7 Item Pipeline

ItemPipeline 即项目管道, 它的调用发生在 Spider 产生 Item 之后。当 Spider 解析完 Response,Item 就会被 Engjne 传递到 Item
Pipeline。
一般用于写数据库，或者图片列表下载到本地。

15.8 Extensions 用于 日志统计、内存用量统计、邮件通知。

15.9 scrapy + selenium 思路就是在 dowdload 这一步，使用 selenium 来进行实际的请求，返回 HtmlResponse.

作者自己实现了一个工具库，具备更加完善的爬虫功能。

15.11 scrapy+pyppeteer

15.12 规则化爬虫，本质是将规则抽取为 json 文件作为配置，也就是将变化点集中起来。

15.13 结合账号池和 IP 代理池，进行爬虫的 demo

## 分布式爬虫

一个共享的 request 队列 + 多个调度器

防止请求重复：

- 对每一个请求，遍历其中的 headers+ 请求标识（例如 method、url、body 等），生成指纹。
- app 中使用 set 数据结构添加每一个请求的指纹
- 利用单点 Redis 建立共享的指纹管理。

防止中断，因为请求队列在内存中，出现意外的话会直接消失。

- 单机：可以利用 scrapy 的 JOBDIR 持久化请求队列。
- 对于分布式爬虫，不需要这个机制，因为 Redis 中的请求队列本身就可以持久化了。

架构实现，已经有社区包 scrapy-redis

16.3 原始 redis set 去重，内存占用较大。
16.4 redis bloom filter remove duplicate。内存占用较小。可能误判。
> demo: https://github.com/Python3WebSpider/ScrapyRedisBloomFilter

16.5 GerapyRabbitMQ python 库
> ScrapyCompositeDemo 对应 github 仓库

## 17 爬虫程序的 Ops

- scrapyd 守护程序
- scrapyAPI 以 api 的方式执行 scrapy 爬虫。
- scrapyClient的使用
  - 将项目打包成egg文件。
  - 将打包生成的egg文件通过addversionjson接口部署到Scrapyd上
  - 执行 scrapyd-deploy 命令

docker env setting:

```
host.docker.i∩ternal,这代表Docker所在宿主机的IP地址
```

附加env文件配置来运行：

```
docker run --env-file .env XXX/XXX
```

DockerCompose 是一种运行多容器docker 程序的方式，比较古老。

K8s use `docker-desktop` as a context

```bash
kubectl config use-context docker-desktop
```

1. 创建deployment
2. 创建service
3. 选择 service 的类型为NodePort。或者使用Ingress进一步暴露服务API。
4. 直接使用端口转发

```bash
kubectl port-forward XXX/XXX 9999:8888 -n service
```

redis => 生产环境一般使用Helm管理

k8s 官方有web-ui-dashboard，推荐安装使用。

安装之后，运行：

```bash
kubectl proxy
```

---

scrapy 分布式爬虫的数据统计方案 ：scrapy-redis 重写 StatsCollector类

---

可视化和告警

1. 第一步便是生成Scrapy的Exporter,用于收集统计数据; => 17.9
2. 第二步便是将Grafana与Prometheus对接起来,构建可视化面板; Helm install kube-prometheus-stack
3. 第三步便是配置告警.

---

爬虫与法律约束

- 动机：研究学习还是商业盈利？
- 行为：是否构成DDOS攻击，还是低频率爬取？
- 结果：是否造成他人信息泄露？

注意不要违法犯罪。

TODO: 删减不需要的源码文件夹，仅保留难度较高的。