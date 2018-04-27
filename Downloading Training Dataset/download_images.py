import urllib
import os

count = 0
file_object = open("C:\Users\Prasad\Desktop\image_downloader\imagenet.synset.txt", 'r')
image_urls = file_object.read()
urls = image_urls.split("\n")


for url in urls:
	if count == 500:
		break
	try:
		urllib.urlretrieve(url, "images/" + str(count)+ ".jpg")
		count += 1
		print 'Download Complete ', (float(count)*100.0/500.0), '%'
	except:
		print 'Failed!'

print
print 'Download Complete!'