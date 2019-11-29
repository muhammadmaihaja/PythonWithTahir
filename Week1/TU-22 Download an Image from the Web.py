import random #Set a random number string to serve as name of downloaded image
import urllib.request # Allows to get data from web pages

def download_Image(url): #function for image download
    image_name = random.randrange(1,1000) #select a random digit string for name of file
    image_name_and_extension = str(image_name) + ".jpg" #convert digit to string and add extension
    urllib.request.urlretrieve(url,image_name_and_extension) #calls method for image download
# Calls the function and input url as argument
download_Image("https://scontent.flos3-1.fna.fbcdn.net/v/t31.0-8/14524348_1623068177990687_5857572118016688551_o.jpg?_nc_cat=109&_nc_eui2=AeGTwt5mUUoKjXlN3EPC2trC3O0tCZQVjs9r5OIfyxhh9Ibt0TAZc6MCJ7tOJg2BFcWDrHkXMdlUBGIAM4MR18hO-hR2jAYcUzeFr-D_jWzgtg&_nc_ohc=D6THgfd4rr8AQmGkupLgvbb9FsICt3yjCSJsFydGHKPL1JwI-V8znoFTw&_nc_ht=scontent.flos3-1.fna&oh=bec7f4fa6ef28f5388f1f3cec1477b3d&oe=5E437666")