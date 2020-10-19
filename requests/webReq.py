import requests
url='https://icanhadadjoke.com/'

r=requests.get(url)
print(r.text)

