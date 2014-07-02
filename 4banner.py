#deprecated, no error handler
import urllib, os
for x in range(0, 400):
        url="https://s.4cdn.org/image/title/"+str(x)+".gif"
        print url
        urllib.urlretrieve(url,str(x)+".gif")
        url="https://s.4cdn.org/image/title/"+str(x)+".jpg"
        print url
        urllib.urlretrieve(url,str(x)+".jpg")
        url="https://s.4cdn.org/image/title/"+str(x)+".png"
        print url
        urllib.urlretrieve(url,str(x)+".png")



