import requests
res = requests.get("https://picsum.photos/v2/list")
print(res.status_code)
pic=res.json()
print(pic[10]['url'])