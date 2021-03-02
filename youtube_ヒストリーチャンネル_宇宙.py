import requests
res = requests.get('https://www.youtube.com/results?search_query=%E3%83%92%E3%82%B9%E3%83%88%E3%83%AA%E3%83%BC%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB+%E5%AE%87%E5%AE%99')
with open('youtube.ヒストリーチャンネル_宇宙.html','w',encoding='utf8') as file:
    file.write(res.text)
