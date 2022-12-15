import requests
from requests.adapters import HTTPAdapter
import re
from bs4 import BeautifulSoup
from adsolver import PC_UA, MOBILE_UA
"""
    小说实体类，传入链接解析相关小说信息
"""

class Novel:
    __novelId = None
    __novelType = None
    __baseUrl = None
    __inputUrl = None
    __reqRes = None
    __index = 1
    chapterList = ""
    title = None
    author = None
    wordCount = 0
    pageCount = 0
    baseUrl = None
    useMobileUa = False

    """
        初始化
    """
    def __init__(self, inputUrl='http://www.bz1111.xyz/4/4477/') -> None:
        if inputUrl is None or len(inputUrl) == 0:
            print('输入链接为空')
            return
        
        self.__inputUrl = inputUrl
        self.__matchParam()

        


    """
        设置链接重试和超时，返回请求结果
    """
    def __testUrl(self) -> str:
        req = requests.Session()
        req.mount('http://', HTTPAdapter(max_retries=3))
        resp = req.get(url=self.__inputUrl, timeout=1618, headers={
            'user-agent' : MOBILE_UA if self.useMobileUa else PC_UA
        })
        res = None
        if resp.status_code == 200:
            res = resp.text
        return res
    """
        正则匹配链接获取小说分类，id参数
    """
    def __matchParam(self) -> None:
        pattern = re.compile(r'(http://|https://)?([^/]*)').search(self.__inputUrl)
        baseUrl = pattern.group()
        novelArr = self.__inputUrl[pattern.span()[1] + 1:].split('/')
        
        # 出现了单页的链接，处理成目录链接
        
        novelType = novelArr[0]
        novelId = novelArr[1]

        if '_' in novelId:
            novelId = novelId[:novelId.index('_')]
        self.__inputUrl = f"{baseUrl}/{novelType}/"
        if len(novelArr) > 2:
            self.__inputUrl = f"{baseUrl}/{novelType}/{novelId}_{self.__index}/"
            pass
        
        self.__baseUrl = baseUrl
        self.__novelId = novelId
        self.__novelType = novelType
    
    """
        解析网页获取小说信息
    """
    def __parseInfo(self) -> bool:
        try:
            soup = BeautifulSoup(self.__reqRes,'lxml')
            novelTitle =  soup.h1.get_text()

            # 处理小说信息
            novelInfoText = soup.find('p', class_='info').get_text()

            reg = re.compile(r'[\u4e00-\u9fa5]{2,}：')
            novelInfoText = reg.sub('',novelInfoText).split('\n')[1:];
            novelAuthor = novelInfoText[0]
            novelWordCount = novelInfoText[2]

            allPage = soup.find('a', class_='endPage')
            allPage = allPage.attrs['href']
            allPage = allPage[allPage.index('_') + 1:allPage.index('/',-1)]
            
            self.title = novelTitle
            self.author = novelAuthor
            self.wordCount = int(novelWordCount)
            self.pageCount = int(allPage)
            return True
        except:
            print('解析错误，可能该链接并非目的网页或原网页结构发生变动')
        
        return False


    """
        获取章节以处理
    """
    def __get_chapter(self) -> None:
        sub_soup = BeautifulSoup(self.__reqRes,'lxml')
        chapter_list = sub_soup.find_all('ul', class_='list')[1]
        for chapter in chapter_list:
            chapter_link = BeautifulSoup(str(chapter),'lxml')
            if not chapter_link.a is None:
                self.chapterList += self.__baseUrl+chapter_link.a['href'] + "\n"
        
    

    def connect(self) -> str:
        self.__reqRes = self.__testUrl()
        if self.__reqRes is None:
            print('网页链接失败，可能原网页链接已变动或当前使用代理链接')
        else:
            if self.__parseInfo():
                self.__get_chapter()
        # 翻页
        if self.__index >= self.pageCount:
            print('爬取结束')
            return
        else:
            self.__index += 1
            self.__inputUrl = f"{self.__baseUrl}/{self.__novelType}/{self.__novelId}_{self.__index}/"
            self.connect()


