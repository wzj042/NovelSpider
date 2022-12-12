# Readme

## 一、项目结构

```bash
── adsolver.py		-- 自定义过滤广告文本
├── chapter.py		-- 章节爬取，图片爬取等方法
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
> 将要爬取的小说链接扔进main.py，直接开始运行

注意因为使用了selenium爬取所以需要下载与chrome浏览器匹配版本的chromedriver.exe

chrome浏览器输入chrome://version查看版本

[chromedriver 下载镜像](https://registry.npmmirror.com/binary.html?path=chromedriver/)

chromedriver.exe放在chrome安装目录下,如C:\Program Files\Google\Chrome\Application\

​     



