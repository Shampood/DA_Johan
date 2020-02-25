import requests
url = 'http://172.17.50.43/halice'
r = requests.get(url)
print(r.text)
#Getting Status Code
print("Status Code:")
print("\t*",r.status_code)
#headers time
h = requests.head(url)
print("Header:")
print("**********")
# for line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
# Modifying the User-Agent
headers = {
    'User-Agent': 'Mobile'
}
# Testing on another site
url2 = 'http://172.17.50.53/halice'
rh = requests.get(url2, headers=headers)
print(rh.text)
