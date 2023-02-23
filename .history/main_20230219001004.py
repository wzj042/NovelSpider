import cloudscraper
# from processor.text_processor import text_processor
from common import *

# target = 'http://www.2diyibanzhu.cc/32/32880/754225.html'
# scraper = cloudscraper.create_scraper()
# resp = scraper.get(target)
# print(resp.text)
# if resp.status_code == 403:
#     print('你可能使用了代理服务导致无法解析页面')
# # 输出文档
# with open('[case](32-32880-754225)无图正序.html', 'wt', encoding='utf-8') as f:
#     f.write(resp.text)

# with open('[case](32-32880-754225_2)乱序带图.html', 'rt', encoding='utf-8') as f:
#     data = f.read()
#     logger.info(text_processor(solve_text = data).img_process())



if __name__ == '__main__':
    # logger.debug('cnmd')
    const.NAME = '123'
    print(const.NAME)
    const.NAME = '13'
    logger.info(const.NAME)
    
    
