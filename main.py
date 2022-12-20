#!/bin/env python3
from novel import Novel
from chapter import Chapter
import os
import adsolver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 输出目录结构时屏蔽的目录
# 发现一开始写的测试例子忘记重构了，居然每章翻页都重新开一个driver，赶紧重构一下
driver = None


def get_novel(href, chrome_driver=None, overwrite=False):
    """
    将页面小说内容输出到文本
    :param href: 页面URL
    :param chrome_driver:
    :param overwrite:
    :return:
    """
    novel = Novel(href)
    novel.use_mobile_ua = adsolver.USE_MOBILE_UA
    novel.connect()
    novel_title = novel.title
    novel_author = novel.author
    print(novel_title)
    if not overwrite:
        # 如果当前已存在文件则跳过
        if novel_author is None:
            novel_author = '不详'
        if novel_title is None:
            novel_title = '啥啊这'
        path = NOVEL_NAME_FORMAT.format(author=novel_author, title=novel_title)
        if os.path.exists(path):
            print('文件已存在')
            return
    for href in novel.chapter_list.split('\n'):
        print('chapterUrl:', href)
        chapter = Chapter(href)
        chapter.set_driver(chrome_driver)
        chapter.BAN_TEXT_LIST = adsolver.BAN_TEXT_LIST
        chapter.chapterIndex = index
        chapter.novelTitle = novel_title
        chapter.author = novel_author
        chapter.connect()


def get_chapter(href):
    novel = Novel(href)
    novel.connect()
    print(novel.title)
    print('作者', novel.author)
    chapter = Chapter(input_url=href)
    chapter.author = novel.author
    chapter.get_chapter(url=href)


def get_img(href):
    novel = Novel(href)
    novel.connect()
    print(novel.title)
    print('作者', novel.author)
    for href in novel.chapter_list.split('\n'):
        print('chapterUrl', href)
        chapter = Chapter(href)
        chapter.get_img_list()


def print_folder_tree(path, depth=0):
    files = []
    items = os.listdir(path)
    for idx, i in enumerate(items):
        # 是否是最后一个元素
        is_last = idx == len(items) - 1
        # 拼接文件路径
        i_path = path + "/" + i

        if '.git' in path or '__pycache__' in path or 'novel' in path:
            continue
        # 根据层数打印空格
        print("   " * depth, end="")
        if is_last:
            print("└── ", end="")
        else:
            print("├── ", end="")
        # 如果是文件夹, 递归
        if os.path.isdir(i_path):
            print(i)
            files.extend(print_folder_tree(path=i_path, depth=depth + 1))
        # 如果是文件就把路径添加到files数组
        else:
            print(i_path.split("/")[-1])
            files.append(i_path)
    return files


def get_driver() -> webdriver:
    chrome_driver = None
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=' + adsolver.MOBILE_UA if adsolver.USE_MOBILE_UA else adsolver.PC_UA)
        service = Service(adsolver.DRIVER_URL)
        chrome_driver = webdriver.Chrome(service=service, options=options)
        chrome_driver.minimize_window()
    except Exception as e:
        print("""加载chromdriver.exe驱动失败，可以尝试下载与chrome浏览器匹配版本
        chrome浏览器输入chrome://version查看版本的chromedriver.exe
        https://registry.npmmirror.com/binary.html?path=chromedriver/
        放在chrome安装目录下,如
        C:\\Program Files\\Google\\Chrome\\Application
        """)
        if adsolver.PRINT_ERROR:
            print(e)
    return chrome_driver


if __name__ == '__main__':

    # print_folder_tree('.', depth=0)
    config = adsolver.init_config()
    adsolver.AUTO_SOLVE_TEXT = config['AUTO_SOLVE_TEXT']
    adsolver.BAN_TEXT_LIST = config['BAN_TEXT_LIST']
    adsolver.NOVEL_LIST = config['NOVEL_LIST']
    adsolver.DRIVER_URL = config['DRIVER_URL']
    adsolver.USE_MOBILE_UA = config['USE_MOBILE_UA']
    adsolver.PRINT_ERROR = config['PRINT_ERROR']
    if config["NOVEL_NAME_FORMAT"]:
        NOVEL_NAME_FORMAT = config["NOVEL_NAME_FORMAT"]

    driver = get_driver()

    for url in adsolver.NOVEL_LIST:
        index = 1
        get_novel(url, chrome_driver=driver)

    driver.close()
    if adsolver.AUTO_SOLVE_TEXT:
        adsolver.solve_ad()
