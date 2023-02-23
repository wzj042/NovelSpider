from core.diyibanzhu import diyibanzhu




if __name__ == '__main__':
    main = diyibanzhu()
    # chapter = main.get_chpater('http://www.2diyibanzhu.cc/32/32880/754225_4.html')
    # main.save_chapter(chapter = chapter)
    
    while True:
        inp = input('输入第一版主小说链接爬取:')
        novel = main.get_novel(inp)
        if novel:
            main.save_novel(novel)
        print('理论上保存完了, 看看当前exe的文件夹罢')
        input('按下回车Enter继续')
    

    
    
