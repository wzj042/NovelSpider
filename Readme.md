# Readme

## 一、项目结构

```bash
── adsolver.py		-- 自定义过滤广告文本
├── release       -- 如果你只需要使用直接下载该文件夹内容即可
├── chapter.py		-- 章节爬取，图片爬取等方法
├── chromedriver.exe -- 自动化测试时用的驱动
├── config.ini		-- 配置文件
├── novelList.txt	-- 分行传入要爬取的链接
├── solveList.txt	-- 分行传入要替换为空的文本
├── img				-- 文字图片，不是必须的
   └── original		 -- 如果爬取的小说出现未匹配的字，调用获取图片方法，reverse.py将图片添加映射json，手动识别图片修改texts.json内容
      ├── 0117530724.png
      ├── ...........png
      └── a85090415a.png
├── main.py			-- 在此处填入要爬取的小说链接
├── novel.py		-- 小说章节内容获取类
├── output
   └── text.json	-- 图片和文字映射的json, 很重要
├── Readme.md		-- 您在此处()
├── requirements.txt -- pip install -r requirements.txt
├── reverse.py		-- 将图片和文字的映射添加到文本
└── ujson.py		-- json 操作封装
```

## 二、部署和使用

> 安装requirements.txt中对应的库
>
> 将要爬取的小说链接扔进novelList.txt，然后运行main.py

注意因为使用了selenium爬取所以需要下载与chrome浏览器匹配版本的chromedriver.exe

chrome浏览器输入chrome://version查看版本

[chromedriver 下载镜像](https://registry.npmmirror.com/binary.html?path=chromedriver/)

chromedriver.exe放在chrome安装目录下,如C:\Program Files\Google\Chrome\Application\

如果只是想要爬取使用的话
点击该链接也可下载对应[可执行文件](https://wwi.lanzoup.com/iC0x90ixnrpc)

​     



