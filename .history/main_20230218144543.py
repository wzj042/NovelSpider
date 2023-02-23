import requests
import cloudscraper

headers = {
    'User-Agent':
    'Mozilla/5.0 (Linux; Android 10; LYA-AL00 Build/HUAWEILYA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/12.5 SP-engine/2.26.0 baiduboxapp/12.5.0.11 (Baidu; P1 10) NABar/1.0'
}
target = 'http://www.2diyibanzhu.cc/32/32880/754225.html'
scraper = cloudscraper.create_scraper()
resp = scraper.get(target)
print(resp.text)
if __name__ == '__main__':
    print('test')
