import requests
data = requests.get('https://h.wandouip.com/get/ip-list?pack=343&num=20&xy=1&type=1&lb=\r\n&mr=1&')
print(data.text)
with open('./files/proxy.txt', 'wb') as f:
  f.write(data.text)
