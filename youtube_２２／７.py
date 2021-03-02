import requests
res = requests.get('https://www.youtube.com/results?search_query=%EF%BC%92%EF%BC%92%EF%BC%8F%EF%BC%97')
with open('youtube.２２／７.html','w',encoding='utf8') as file:
    file.write(res.text)
