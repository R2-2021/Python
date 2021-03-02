import requests
res = requests.get('https://www.animatetimes.com/tag/details.php?id=6212')
with open('animatetimes.202101.html','w',encoding='utf8') as file:
    file.write(res.text)
