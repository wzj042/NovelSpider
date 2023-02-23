import cloudscraper

target = 'http://www.2diyibanzhu.cc/32/32880/754225.html'
scraper = cloudscraper.create_scraper()
resp = scraper.get(target)
print(resp.text)

if __name__ == '__main__':
    print('test')
