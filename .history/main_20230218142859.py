import requests

r = requests.get('http://www.2diyibanzhu.cc/32/32880/754225.html')
print(r.status_code)
print(r.text)
if __name__ == '__main__':
    print('test')
