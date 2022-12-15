from novel import Novel
from chapter import Chapter
import os
from adsolver import solveAd, initConfg, BAN_TEXT_LIST, NOVEL_LIST, AUTO_SOLVE_TEXT, DRIVER_URL, USE_MOBILE_UA, MOBILE_UA, PC_UA
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 输出目录结构时屏蔽的目录
# 发现一开始写的测试例子忘记重构了，居然每章翻页都重新开一个driver，赶紧重构一下
driver = None
def getNovel(url,driver=None, overwride=False):
    novel = Novel(url)
    novel.useMobileUa = USE_MOBILE_UA
    novel.connect()
    novelTilte = novel.title
    novelAuthor = novel.author
    print(novelTilte)
    if not overwride:
        # 如果当前已存在文件则跳过
        if novelAuthor is None:
            novelAuthor = '不详'
        if novelTilte is None:
            novelTilte = '啥啊这'
        path = 'novel\\' + novelAuthor + '\\' + novelTilte + '.txt'
        if os.path.exists(path):
            print('文件已存在')
            return
    for url in novel.chapterList.split('\n'):
        print('chapterUrl:', url)
        chapter = Chapter(url)
        chapter.setDriver(driver)
        chapter.BAN_TEXT_LIST = BAN_TEXT_LIST
        chapter.chapterIndex = index
        chapter.novelTitle = novelTilte
        chapter.author = novelAuthor
        chapter.connect()


def getChapter(url):
    novel = Novel(url)
    novel.connect()
    print(novel.title)
    print('作者', novel.author)
    chapter = Chapter(input=url)
    chapter.author = novel.author
    chapter.getChapter(url=url)


def getImg(url):
    novel = Novel(url)
    novel.connect()
    print(novel.title)
    print('作者', novel.author)
    for url in novel.chapterList.split('\n'):
        print('chapterUrl', url)
        chapter = Chapter(url)
        chapter.getImgList()


def print_folder_tree(path, depth=0):
    files = []
    items = os.listdir(path)
    for index, i in enumerate(items):
        # 是否是最后一个元素
        is_last = index == len(items) - 1
        # 拼接文件路径
        i_path = path + "/" + i
        
        if '.git' in path  or '__pycache__' in path or 'novel' in path:
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


def getDriver() -> webdriver:
    driver = None
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=' + MOBILE_UA if USE_MOBILE_UA else PC_UA)
        service = Service(DRIVER_URL)
        driver = webdriver.Chrome(service=service, options= options)
        driver.minimize_window()
    except:
        print("""加载chromdriver.exe驱动失败，可以尝试下载与chrome浏览器匹配版本
        chrome浏览器输入chrome://version查看版本的chromedriver.exe
        https://registry.npmmirror.com/binary.html?path=chromedriver/
        放在chrome安装目录下,如
        C:\Program Files\Google\Chrome\Application\
        """)
    return driver

if __name__ == '__main__':
    
    # print_folder_tree('.', depth=0)
    config = initConfg()
    AUTO_SOLVE_TEXT = config['AUTO_SOLVE_TEXT']
    BAN_TEXT_LIST =  config['BAN_TEXT_LIST']
    NOVEL_LIST =  config['NOVEL_LIST']
    DRIVER_URL =  config['DRIVER_URL']
    USE_MOBILE_UA =  config['USE_MOBILE_UA']

    driver = getDriver()

    for url in NOVEL_LIST:
        index = 1
        getNovel(url, driver=driver)

    driver.close()
    if AUTO_SOLVE_TEXT:
        solveAd()




