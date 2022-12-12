from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re,time,os
from bs4 import BeautifulSoup
import requests
import hashlib
from ujson import getJson, saveJson
from adsolver import banText
"""
    使用selenim实现的爬取章节内容
    单独获取内容其实不难，但是因为其中他加载了一个使用sojson.v5加密的js
    来替换原本加载完之后乱序的内容，这个加密方式会将原本的信息丢失
    我js水平实在不大行，就没有继续逆向，直接用浏览器模拟获取加载之后的结果
"""
driverUrl = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

class Chapter:
    __chapterUrl = None
    __chapterTitle = None
    __baseUrl = None
    __parseUrl = None
    __index = 1
    __chapterContent = None
    author = None
    novelTitle = None
    __novelFile = None
    # 定义多个参数并赋值None实现伪重载
    def __init__(self, inputUrl=None, href = None) -> None:
        # 匹配一下baseUrl
        if not inputUrl is None:
            self.setBaseUrl(inputUrl)
            
        if not href is None:
            self.__chapterUrl = href

    
    def setBaseUrl(self, inputUrl='http://www.bz1111.xyz/'):

        if inputUrl is None or len(inputUrl) == 0:
            print('baseUrl为空')
            return

        pattern = re.compile(r'(http://|https://)?([^/]*)').search(inputUrl)
        baseUrl = pattern.group()
        self.__baseUrl = baseUrl
        
        if not self.__chapterUrl is None:
            urlSuffix = self.__chapterUrl
        else:
            urlSuffix = '/'+inputUrl[pattern.span()[1] + 1:]

        if '.' in urlSuffix:
            urlSuffix = urlSuffix[:urlSuffix.index('.')]
        if '_' in urlSuffix:
            urlSuffix = urlSuffix[:urlSuffix.index('_')]
        
        print('author:', self.author)
        print('urlSuffix:', urlSuffix)
        self.__parseUrl = baseUrl + urlSuffix

        
    def __solveImg(self) -> None:
        imgSoup = BeautifulSoup(self.__chapterContent,'lxml')
        imgs = imgSoup.find_all('img')
        urls = set()
        # 去重
        for img in imgs:
            urls.add(img['src'])
        # 处理图片，
        folder = 'img//original'

        files = os.listdir(folder)
        updateCnt = 0
        allCnt = len(files)
        for imgUrl in urls:
            imgName = imgUrl[imgUrl.index('a/') + 2:]
            if not imgName in files:
                updateCnt+=1
                print(imgName)
                imgUrl = self.__baseUrl + imgUrl
                response = requests.get(imgUrl)
                with open(f'{folder}//{imgName}','wb') as file_obj:
                    file_obj.write(response.content)

        print(f'原有{allCnt}张图片,更新了{updateCnt}张图片，现有{allCnt+updateCnt}张')
        
        pass
    
    def __get_md5(self, url) -> str:
        imgUrl = self.__baseUrl + '/toimg/data/' +imgUrl
        response = requests.get(imgUrl)
        with open('temp.png','wb') as file_obj:
            file_obj.write(response.content)
        file = open("temp.jpg", "rb")
        return hashlib.md5(file.read()).hexdigest()
    
    # 替换标签和广告文本
    def solveContext(self, content) -> str:
        try:
            content = content.replace('<br/>', '\n')
            ouput_json = r'output\text.json'

            # 获取json 查重
            tmpJson = getJson(ouput_json)
            textImgList = []
            textList = []
            textMd5 = []

            if not tmpJson is None:
                for text in tmpJson['texts']:
                    textList.append(text['text'])
                    textImgList.append(text['imgName'])
                    textMd5.append(text['md5'])
            else:
                print('没有映射json')
                return content
            
            pattern = re.compile('\w*?\.png')
            imgList = pattern.findall(content)
            imgs = set()
            for img in imgList:
                imgs.add(img)
            
            for img in imgs:
                text = None
                
                index = textImgList.index(img) if img in textImgList else -1
                if index == -1:
                    print('可能图片名修改了或者图片未扫描过')
                    md5 = self.__get_md5(img)
                    index = textMd5.index(md5) if md5 in textMd5 else -1
                
                if index == -1:
                    text = ''
                    print('图片未扫描过')
                else:
                    text = textList[index]
                
                content = content.replace(f'<img src="/toimg/data/{img}"/>',text)
            pass
        
        except (Exception) as e:
            print('替换内容时发生错误:', e)
        
        return content
    # 注意获取图片不需要等待页面加载
    def getImgList(self):
        print('parseImgUrl:',f'{self.__parseUrl}_{self.__index}.html')
        soup = BeautifulSoup(requests.get(f'{self.__parseUrl}_{self.__index}.html').text,'lxml')
        print(soup.h1.get_text())
        allPage = soup.find('center', class_='chapterPages')
        if allPage is None:
            allPage = 1
        else :
            allPage=allPage.get_text().split('】【')
            allPage=int(allPage[len(allPage)-1][:-1])
        print(allPage,"页")

        # 获取章节内容
        chapterText = soup.find('div', id='ad')
        if chapterText is None:
            chapterText = BeautifulSoup(str(soup.find('div', class_='neirong')),'lxml')
            chapterText = chapterText.find_all('div')[1]
    
        self.__chapterContent = str(chapterText)

        # 处理图片
        self.__solveImg()

        # 翻页
        if self.__index >= allPage:
            print('爬取结束')
            return
        else:
            self.__index += 1
            self.getImgList()
        pass
    def getChapter(self, url):
        self.__parseUrl = url[:url.index('.html')]
        self.connect()
    """
        通过驱动打开网页解析数据
    """
    def connect(self):
        print('parseUrl:',f'{self.__parseUrl}_{self.__index}.html')
        if self.__baseUrl is None:
            print('未设置baseUrl')
            return
        
        driver = None
        try:
            service = Service(driverUrl)
            driver = webdriver.Chrome(service=service)
            driver.get(f'{self.__parseUrl}_{self.__index}.html')
            print(f'第{self.__index}页\n',f'{self.__parseUrl}_{self.__index}.html')
        except:
            print("""加载chromdriver.exe驱动失败，可以尝试下载与chrome浏览器匹配版本
            chrome浏览器输入chrome://version查看版本的chromedriver.exe
            https://registry.npmmirror.com/binary.html?path=chromedriver/
            放在chrome安装目录下,如
            C:\Program Files\Google\Chrome\Application\
            """)
        
        if not driver is None:
            print('加载驱动成功')
            try:
                # 保证加载完成
                time.sleep(0.5)
                soup = BeautifulSoup(driver.page_source,'lxml')
                novel_title =  soup.h1.get_text()
                # 需要分章节的时候可以用，但我懒得分
                self.__chapterTitle = novel_title

                allPage = soup.find('center', class_='chapterPages')

                if allPage is None:
                    allPage = 1
                else :
                    allPage=allPage.get_text().split('】【')
                    allPage=int(allPage[len(allPage)-1][:-1])
                # print(allPage,"页")

                # 获取章节内容
                chapterText = soup.find('div', id='ad')
                if chapterText is None:
                    chapterText = str(soup.find('div', class_='neirong'))
                
                # if chapterText is None:
                #     print("该章节内容不存在，已丢失或页面结构已更新")
                #     return
            
                self.__chapterContent = str(chapterText)
                content = str(chapterText)
                # print(content)
                content = self.solveContext(content)
                resSoup = BeautifulSoup(content,'lxml')
                content = resSoup.get_text()
                 
                for ban in banText:
                    if ban in content:
                        print('发现广告*1')
                        content = content.replace(ban, '')
                
                print(content)

                path = 'novel\\'+self.author+'\\'

                if not os.path.exists(path):
                    os.makedirs(path)
                # 文件路径
                if self.novelTitle is None or len(self.novelTitle) == 0:
                    self.novelTitle = self.__chapterTitle

                path = path+self.novelTitle+'.txt'

                file = open(path, 'a+', encoding='utf-8', newline='')
                file.writelines(content)
                file.flush()
                file.close()
                file = None


                # 翻页
                if self.__index >= allPage:
                    print('爬取结束')
                    driver.close()
                    return
                else:
                    self.__index += 1
                    driver.close()
                    self.connect()
            except (Exception) as e:
                print('爬取内容解析错误:',e)

        


