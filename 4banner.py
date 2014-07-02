import urllib.request, urllib.parse, urllib.error, os
for x in range(0, 400):
	url="https://s.4cdn.org/image/title/"+str(x)+".gif"
	try:
		urllib.request.urlretrieve(url,str(x)+".gif")
		print(url)
	except urllib.error.HTTPError as err:
		print(err.code)
	url="https://s.4cdn.org/image/title/"+str(x)+".jpg"
	try:
		urllib.request.urlretrieve(url,str(x)+".jpg")
		print(url)
	except urllib.error.HTTPError as err:
		print(err.code)
	url="https://s.4cdn.org/image/title/"+str(x)+".png"
	try:
		urllib.request.urlretrieve(url,str(x)+".png")
		print(url)
	except urllib.error.HTTPError as err:
		print(err.code)

