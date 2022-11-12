import requests

res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060")

# print(res.text["status"])
# print(type(res.json()["status"]))
print(res.json()["results"][0]["prefcode"])
