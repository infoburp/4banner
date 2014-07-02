import urllib.request, urllib.parse, urllib.error, os
for x in range(0, 400):
        url="https://s.4cdn.org/image/title/"+str(x)+".gif"
        print(url)
        try:
                urllib.request.urlretrieve(url,str(x)+".gif")
        except urllib.error.HTTPError as err:
                print(err.code)
        url="https://s.4cdn.org/image/title/"+str(x)+".jpg"
        print(url)
        try:
                urllib.request.urlretrieve(url,str(x)+".jpg")
        except urllib.error.HTTPError as err:
                print(err.code)
        url="https://s.4cdn.org/image/title/"+str(x)+".png"
        print(url)
        try:
                urllib.request.urlretrieve(url,str(x)+".png")
        except urllib.error.HTTPError as err:
                print(err.code)

