import urllib.request, urllib.parse, urllib.error, os
extensions = {".gif",".jpg",".png"}
for filenumber in range(0, 400):
	for extension in extensions:
		url="https://s.4cdn.org/image/title/"+str(filenumber)+extension
		try:
			urllib.request.urlretrieve(url,str(filenumber)+extension)
			print(url)
		except urllib.error.HTTPError as err:
			print(err.code)

