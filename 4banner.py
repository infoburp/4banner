import urllib, os
for x in range(0, 400):
        url="https://s.4cdn.org/image/title/"+str(x)+".gif"
        print url
        os.system('wget %s' % url)
        url="https://s.4cdn.org/image/title/"+str(x)+".jpg"
        print url
        os.system('wget %s' % url)
        url="https://s.4cdn.org/image/title/"+str(x)+".png"
        print url
        os.system('wget %s' % url)


