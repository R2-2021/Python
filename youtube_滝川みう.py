import requests
res = requests.get('https://www.youtube.com/results?search_query=%E6%BB%9D%E5%B7%9D%E3%81%BF%E3%81%86')
with open('youtube.滝川みう.html','w',encoding='utf8') as file:
    file.write(res.text)
