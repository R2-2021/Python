import requests
res = requests.get('https://www.youtube.com/results?search_query=%E3%82%86%E3%81%84%E3%81%8B%E3%81%8A%E3%82%8A')
with open('youtube.ゆいかおり.html','w',encoding='utf8') as file:
    file.write(res.text)
