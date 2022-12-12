from novel import Novel
from chapter import Chapter
import os
novelList = [
    'http://www.bz1111.xyz/14/14735/',
    'http://www.bz1111.xyz/14/14292/',
    'http://www.bz1111.xyz/6/6548/',
    'http://www.bz1111.xyz/7/7650/',
    'http://www.bz1111.xyz/19/19998/',
    'http://www.bz1111.xyz/19/19946/',
    'http://www.bz1111.xyz/14/14233/',
    'http://www.bz1111.xyz/10/10492/',
    'http://www.bz1111.xyz/9/9149/',
    'http://www.bz1111.xyz/8/8349/',
    'http://www.bz1111.xyz/4/4409/',
    'http://www.bz1111.xyz/2/2197/',
    'http://www.bz1111.xyz/14/14884/',
    'http://www.bz1111.xyz/1/1033/',
    'http://www.bz1111.xyz/18/18337/',
    'http://www.bz1111.xyz/4/4154/',
]

def getNovel(url, overwride=False):
    novel = Novel(url)
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
        path = 'novel\\'+novelAuthor+'\\'+novelTilte+'.txt'
        if os.path.exists(path):
            print('文件已存在')
            return
    for url in novel.chapterList.split('\n'):
        print('chapterUrl:', url)
        chapter = Chapter(url)
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
        # 根据层数打印空格
        print("   " * depth,end="")
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

if __name__ == '__main__':

    for url in novelList:
        getNovel(url)
    



    


