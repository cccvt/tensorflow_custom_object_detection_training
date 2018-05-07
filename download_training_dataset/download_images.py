import urllib
import os

count = 0
file_object = open("imagenet.synset.txt", 'r')
image_urls = file_object.read()
urls = image_urls.split("\n")


for url in urls:
	if count == 750:   # Stop after 750 images downloaded
		break
	try:
		urllib.urlretrieve(url, "images/" + str(count)+ ".jpg")
		count += 1
		print 'Download Complete ', (float(count)*100.0/750.0), '%'
	except:
		print 'Failed!'

print
print 'Download Complete!'
