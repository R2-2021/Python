import requests
res = requests.get('https://www.youtube.com/results?search_query=%E6%98%A0%E7%94%BB%E9%9F%B3%E6%A5%BD+%E5%90%8D%E6%9B%B2')
with open('youtube.映画音楽名曲.html','w',encoding='utf8') as file:
    file.write(res.text)
