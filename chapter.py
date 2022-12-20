import hashlib
import os
import re
import time

import requests
from bs4 import BeautifulSoup

import adsolver
from ujson import load_json


class Chapter:
    __chapterUrl = None
    __chapterTitle = None
    __base_url = None
    __parseUrl = None
    __index = 1
    __chapterContent = None
    __driver = None
    author = None
    novelTitle = None
    BAN_TEXT_LIST = []

    def __init__(self, input_url=None, href=None) -> None:
        """
        定义多个参数并赋值None实现伪重载
        :param input_url:
        :param href:
        """
        # 匹配一下baseUrl
        if input_url:
            self.set_base_url(input_url)

        if href:
            self.__chapterUrl = href

    def set_driver(self, driver=None):
        self.__driver = driver

    def set_base_url(self, input_url: str):

        if not input_url:
            print('baseUrl为空')
            return

        pattern = re.compile(r'(http://|https://)?([^/]*)').search(input_url)
        base_url = pattern.group()
        self.__base_url = base_url

        if self.__chapterUrl:
            url_suffix = self.__chapterUrl
        else:
            url_suffix = '/' + input_url[pattern.span()[1] + 1:]

        if '.' in url_suffix:
            url_suffix = url_suffix[:url_suffix.index('.')]
        if '_' in url_suffix:
            url_suffix = url_suffix[:url_suffix.index('_')]

        print('author:', self.author)
        print('url_suffix:', url_suffix)
        self.__parseUrl = base_url + url_suffix

    def __solve_img(self) -> None:
        img_soup = BeautifulSoup(self.__chapterContent, 'lxml')
        img_arr = img_soup.find_all('img')
        urls = set()
        # 去重
        for img in img_arr:
            urls.add(img['src'])
        # 处理图片，
        folder = 'img//original'

        files = os.listdir(folder)
        update_cnt = 0
        all_cnt = len(files)
        for img_url in urls:
            img_name = img_url[img_url.index('a/') + 2:]
            if img_name not in files:
                update_cnt += 1
                print(img_name)
                img_url = self.__base_url + img_url
                response = requests.get(img_url)
                with open(f'{folder}//{img_name}', 'wb') as file_obj:
                    file_obj.write(response.content)

        print(f'原有{all_cnt}张图片,更新了{update_cnt}张图片，现有{all_cnt + update_cnt}张')

        pass

    def __get_md5(self, url) -> str:
        img_url = self.__base_url + '/toimg/data/' + url
        response = requests.get(img_url)
        with open('temp.png', 'wb') as file_obj:
            file_obj.write(response.content)
        file = open("temp.jpg", "rb")
        return hashlib.md5(file.read()).hexdigest()

    # 替换标签和广告文本
    def solve_context(self, content) -> str:
        try:
            content = content.replace('<br/>', '\n')
            output_json = r'output\text.json'

            # 获取json 查重
            tmp_json = load_json(output_json)
            text_img_list = []
            text_list = []
            text_md5 = []

            if tmp_json:
                for text in tmp_json['texts']:
                    text_list.append(text['text'])
                    text_img_list.append(text['imgName'])
                    text_md5.append(text['md5'])
            else:
                print('没有映射json')
                return content

            pattern = re.compile('\\w*?\\.png')
            img_list = pattern.findall(content)
            img_set = set()
            for img in img_list:
                img_set.add(img)

            for img in img_set:
                text = None

                index = text_img_list.index(img) if img in text_img_list else -1
                if index == -1:
                    print('可能图片名修改了或者图片未扫描过')
                    md5 = self.__get_md5(img)
                    index = text_md5.index(md5) if md5 in text_md5 else -1

                if index == -1:
                    text = ''
                    print('图片未扫描过')
                else:
                    text = text_list[index]

                content = content.replace(f'<img src="/toimg/data/{img}"/>', text)
            pass

        except Exception as e:
            print('替换内容时发生错误:', e)

        return content

    # 注意获取图片不需要等待页面加载
    def get_img_list(self):
        print('parseImgUrl:', f'{self.__parseUrl}_{self.__index}.html')
        soup = BeautifulSoup(
            requests.get(f'{self.__parseUrl}_{self.__index}.html').text,
            'lxml')
        print(soup.h1.get_text())
        all_page = soup.find('center', class_='chapterPages')
        if all_page is None:
            all_page = 1
        else:
            all_page = all_page.get_text().split('】【')
            all_page = int(all_page[len(all_page) - 1][:-1])
        print(all_page, "页")

        # 获取章节内容
        chapter_text = soup.find('div', id='ad')
        if chapter_text is None:
            chapter_text = BeautifulSoup(
                str(soup.find('div', class_='neirong')), 'lxml')
            chapter_text = chapter_text.find_all('div')[1]

        self.__chapterContent = str(chapter_text)

        # 处理图片
        self.__solve_img()

        # 翻页
        if self.__index >= all_page:
            print('爬取结束')
            return
        else:
            self.__index += 1
            self.get_img_list()
        pass

    def get_chapter(self, url):
        self.__parseUrl = url[:url.index('.html')]
        self.connect()

    def connect(self):
        """
        通过驱动打开网页解析数据
        :return:
        """
        print('parseUrl:', f'{self.__parseUrl}_{self.__index}.html')
        if self.__base_url is None:
            print('未设置baseUrl')
            return
        if self.__driver is None:
            print('未设置driver')
            return

        if self.__driver:
            self.__driver.get(f'{self.__parseUrl}_{self.__index}.html')
            print(f'第{self.__index}页\n',
                  f'{self.__parseUrl}_{self.__index}.html')
            try:
                # 保证加载完成
                time.sleep(0.3)
                soup = BeautifulSoup(self.__driver.page_source, 'lxml')
                novel_title = soup.h1.get_text()
                print(novel_title)
                # 需要分章节的时候可以用，但我懒得分
                self.__chapterTitle = novel_title

                all_page = soup.find('center', class_='chapterPages')

                if all_page is None:
                    all_page = 1
                else:
                    all_page = all_page.get_text().split('】【')
                    all_page = int(all_page[len(all_page) - 1][:-1])
                # print(all_page,"页")

                # 获取章节内容
                chapter_text = soup.find('div', id='ad')
                if chapter_text is None:
                    chapter_text = str(soup.find('div', class_='neirong'))

                # if chapter_text is None:
                #     print("该章节内容不存在，已丢失或页面结构已更新")
                #     return

                self.__chapterContent = str(chapter_text)
                content = str(chapter_text)
                # print(content)
                content = self.solve_context(content)
                res_soup = BeautifulSoup(content, 'lxml')
                content = res_soup.get_text()
                # 访问太快还是怎么样，反正资源妹拿到
                if "Notice: Undefined index:" in content:
                    self.connect()
                    return

                print(content)

                if self.__index == 1:
                    if self.__chapterTitle is None or len(self.__chapterTitle) == 0:
                        self.__chapterTitle = '分卷阅读'
                    content = f'\n【{self.__chapterTitle}】\n' + content

                self.author = self.author.replace('\t', '')
                self.author = self.author.replace('\r', '')
                novel_file = adsolver.NOVEL_NAME_FORMAT.format(author=self.author, title=self.novelTitle)
                novel_path = os.path.dirname(novel_file)
                if not os.path.exists(novel_path):
                    os.makedirs(novel_path)
                # 文件路径
                if not self.novelTitle:
                    self.novelTitle = self.__chapterTitle

                with open(novel_file, 'a+', encoding='utf-8', newline='') as file:
                    file.write(content)
                    file.flush()

                # 翻页
                if self.__index >= all_page:
                    print('爬取结束')
                    return
                else:
                    self.__index += 1
                    self.connect()
            except Exception as e:
                print('爬取内容解析错误:', e)
