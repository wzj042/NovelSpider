from core.diyibanzhu import diyibanzhu




if __name__ == '__main__':
    """每次加载时设置baseurl"""
    main = diyibanzhu()
    chapter = main.get_chpater('http://www.2diyibanzhu.cc/32/32880/754225_4.html')
    # novel = main.get_novel('http://www.2diyibanzhu.cc/32/32986/')
    main.save_chapter(chapter)
    # print(chapter)

    

    
    
