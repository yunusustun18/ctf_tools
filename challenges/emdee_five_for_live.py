import requests
import re
import hashlib

url = "http://docker.hackthebox.eu:40180/"

session = requests.Session()
r = session.get(url=url).content

word = re.findall("'>....................<",str(r))
word = word[0]

blacklist = "'><"
for i in blacklist:
    if i in word:
        word = word.replace(i,"")

hash = hashlib.md5(word.encode()).hexdigest()
req = session.post(url=url,data={"hash":hash})
print(req.text)