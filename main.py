from core.diyibanzhu import diyibanzhu




if __name__ == '__main__':
    main = diyibanzhu()
    # chapter = main.get_chpater('http://www.2diyibanzhu.cc/32/32880/754225_4.html')
    # main.save_chapter(chapter = chapter)

    """其实可以更精简一点是吧"""
    novel = main.get_novel('http://www.2diyibanzhu.cc/23/23044/')
    main.save_novel(novel)

    
    
