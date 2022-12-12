import os
banText = [
    '记住地阯發布頁 ４Ｖ４Ｖ４Ｖ点ＣＯＭ ',
    '**********************************************',
    '【01bz 官方 QQ群（1）】：６５１９９２２９７（满）',
    '【 https://m.diyibanzhu.in 】',
    '用浏览器打开下列地址阅读171',
    'http://dwz.cn/syrj171',
    '上面信息看不到 看不全的自己找原因',
    '第壹版主小説站官網　——',
    '"请识别正版网站！"',
    '"01bz.net"',
    '"01bz.com"',
    '最新地址发布页:',
    '最^新^地^址:^',
    '最-新-地-址-发-布-页:',
    '１Ｋ２Ｋ３Ｋ４Ｋ、ｃ〇㎡',
    '1k2k3k4k.com',
    '1m2m3m4m.com',
    '１Q２Q３Q４Q．Ｃ*〇*Ｍ',
    ' （苹`果`手`机`使用Safari自带浏览器，安`卓`手`机`使用chrome谷歌浏览器）',
    '1q2q3q4q.com',
    '（苹果手机使用Safari自带浏览器，安卓手机使用chrome谷歌浏览器）',
    '= м.ｄīｙīｂāńｚｈū.īń =——',
    '= 第壹版主小説站官網 =——',
    'んττρs://м.dìγìЪаηzんú.ìη-',
    'んττρs://ωωω.dìγìЪаηzんú.ìη',
    'んττρs://м.dǐγǐЪáηzんυ.ǐη-',
    '= щщщ.ｄīｙīｂāńｚｈū.ìň =-',
    '发送邮件 ｄīｙīｂāńｚｈū ⊙ ｑｑ.ｃōｍ',
    'DI 阯發布頁 ⒋Ⅴ⒋Ⅴ⒋Ⅴ.с○Μ',
    '⒋v⒋v⒋v.с○Μ',
    '记住地阯發布頁 ④∨④∨④∨.с☉Μ',
    '记住地阯發布頁 ４Ｖ４Ｖ４Ｖ点ＣＯＭ ',
    '哋址发咘頁 4Ｖ4ｖ4v.ｃōｍ',
    '地阯發鈽頁 4ν4ν4ν.cом',
    'んττρs://ωωω.dΙyΙьáиzんú.Ιи',
    'んττρs://м.dΙyΙьáиzんú.Ιи-',
    'ＹＹＤＳＴxＴ．ｏRｇ',
    'ＹyＤsＴxＴ．ORG',
    '（苹`果`手`机`使用Safari自带浏览器，安`卓`手`机`使用chrome谷歌浏览器）',
    '本站地址随时可能失效，记住发布邮箱：diyibanzhu＠gmail．ｃｏｍ',
    """

    んττρs://щщщ.dǐγǐЪáηzんυ.ǐη""",
    """

    = 第壹版主小説站官網 =——""",
    """

    = м.ｄīｙīｂāńｚｈū.īń =——""",
    """

    = щщщ.ｄīｙīｂāńｚｈū.ìň =-""",
    """
    んττρs://м.di yΙьáиzんú.Ιи-""",
    """

    哋址发咘頁 4Ｖ4ｖ4v.ｃōｍ""",
    """
    最新找回４Ｆ４Ｆ４Ｆ．ＣＯＭ""",
    """
    最新找回4F4F4F,C0M""",
    '最^.^新^.^地^.^址;',
    '５ｓ６ｓ７ｓ８ｓ．Ｃ０Ｍ',
    '－－－－－－',
    '============================'
]

# 处理匹配一下小说中的广告文本
def solveAdText(content) -> str:
    for ban in banText:
        if ban in content:
            print('发现广告*1')
            content = content.replace(ban, '')
    return content
    pass
def solveAd():
    # 遍历小说列表替换广告, 这里不打算考虑加载上mb的文件，就不分块加载了
    for root, dirs, files in os.walk("novel", topdown=False):
        for name in files:
            print(files)
            content = ''
            with open(f'{root}\{name}','r', encoding='utf-8') as f:
                for line in f.readlines():
                    content += line
                f.close()
            content = solveAdText(content)
            with open(f'{root}\{name}','w', encoding='utf-8') as f:
                f.write(content)
                f.close()

    pass

if __name__ == '__main__':
    solveAd()
    