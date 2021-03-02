import requests
res = requests.get('https://www.youtube.com/results?search_query=%E5%A2%97%E7%94%B0%E6%9C%AA%E4%BA%9C')
with open('youtube.増田未亜.html','w',encoding='utf8') as file:
    file.write(res.text)
