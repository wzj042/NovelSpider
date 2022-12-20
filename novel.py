import requests
from requests.adapters import HTTPAdapter
import re
from bs4 import BeautifulSoup
import adsolver

"""
    小说实体类，传入链接解析相关小说信息
"""


class Novel:
    __novel_id = None
    __novel_type = None
    __base_url = None
    __input_url = None
    __req_res = None
    __index = 1
    chapter_list = ""
    title = None
    author = None
    word_count = 0
    page_count = 0
    base_url = None
    use_mobile_ua = False

    def __init__(self, input_url='http://www.bz1111.xyz/4/4477/') -> None:
        """
        初始化
        :param input_url:
        """
        if not input_url:
            print('输入链接为空')
            return

        self.__input_url = input_url
        self.__match_param()

    def __test_url(self) -> str:
        """
        设置链接重试和超时，返回请求结果
        :return:
        """
        req = requests.Session()
        req.mount('http://', HTTPAdapter(max_retries=3))
        resp = req.get(url=self.__input_url, timeout=1618, headers={
            'user-agent': adsolver.MOBILE_UA if self.use_mobile_ua else adsolver.PC_UA
        })
        res = None
        if resp.status_code == 200:
            res = resp.text
        return res

    def __match_param(self) -> None:
        """
        正则匹配链接获取小说分类，id参数
        :return:
        """
        pattern = re.compile(r'(http://|https://)?([^/]*)').search(self.__input_url)
        base_url = pattern.group()
        novel_arr = self.__input_url[pattern.span()[1] + 1:].split('/')

        # 出现了单页的链接，处理成目录链接
        novel_type = novel_arr[0]
        novel_id = novel_arr[1]

        if '_' in novel_id:
            novel_id = novel_id[:novel_id.index('_')]
        self.__input_url = f"{base_url}/{novel_type}/"
        if len(novel_arr) > 2:
            self.__input_url = f"{base_url}/{novel_type}/{novel_id}_{self.__index}/"

        self.__base_url = base_url
        self.__novel_id = novel_id
        self.__novel_type = novel_type

    def __parse_info(self) -> bool:
        """
        解析网页获取小说信息
        :return:
        """
        try:
            soup = BeautifulSoup(self.__req_res, 'lxml')
            novel_title = soup.h1.get_text()

            # 处理小说信息
            novel_info_text = soup.find('p', class_='info').get_text()

            reg = re.compile(r'[\u4e00-\u9fa5]{2,}：')
            novel_info_text = reg.sub('', novel_info_text).split('\n')[1:];
            novel_author = novel_info_text[0]
            novel_word_count = novel_info_text[2]

            all_page = soup.find('a', class_='endPage')
            all_page = all_page.attrs['href']
            all_page = all_page[all_page.index('_') + 1:all_page.index('/', -1)]

            self.title = novel_title
            self.author = novel_author
            self.word_count = int(novel_word_count)
            self.page_count = int(all_page)
            return True
        except Exception as e:
            print('解析错误，可能该链接并非目的网页或原网页结构发生变动')
            if adsolver.PRINT_ERROR:
                print(e)
        return False

    def __get_chapter(self) -> None:
        """
        获取章节以处理
        :return:
        """
        sub_soup = BeautifulSoup(self.__req_res, 'lxml')
        chapter_list = sub_soup.find_all('ul', class_='list')[1]
        for chapter in chapter_list:
            chapter_link = BeautifulSoup(str(chapter), 'lxml')
            if chapter_link.a:
                self.chapter_list += self.__base_url + chapter_link.a['href'] + "\n"

    def connect(self) -> None:
        """
        获取章节内容
        :return:
        """
        self.__req_res = self.__test_url()
        if self.__req_res is None:
            print('网页链接失败，可能原网页链接已变动或当前使用代理链接')
        else:
            if self.__parse_info():
                self.__get_chapter()
        # 翻页
        if self.__index >= self.page_count:
            print('爬取结束')
        else:
            self.__index += 1
            self.__input_url = f"{self.__base_url}/{self.__novel_type}/{self.__novel_id}_{self.__index}/"
            self.connect()
