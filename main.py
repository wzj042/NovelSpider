from core.diyibanzhu import diyibanzhu




if __name__ == '__main__':
    main = diyibanzhu()
    """@TODO: 不同分流处理的unit test, 获取章节"""
    
    chapter = main.get_chpater('https://8yydstxt178.com/27/27103/')
    main.save_chapter(chapter)
    
    """获取小说的unit test"""
    # novel = main.get_novel('http://www.2diyibanzhu.cc/27/27103/')
    # main.save_novel(novel)

    # while True:
    #     inp = input('输入第一版主小说链接爬取:')
    #     novel = main.get_novel(inp)
    #     if novel:
    #         main.save_novel(novel)
    #         print('理论上保存完了, 看看当前exe的文件夹罢')
    #     else:
    #         print('保存失败')
    #     input('按下回车Enter继续')
    

    
    
