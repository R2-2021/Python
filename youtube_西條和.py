import requests
res = requests.get('https://www.youtube.com/results?search_query=%E8%A5%BF%E6%A2%9D%E5%92%8C')
with open('youtube.西條和.html','w',encoding='utf8') as file:
    file.write(res.text)
