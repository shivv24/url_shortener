import pyshorteners
long_url=input("Enter the URL to shorten:")
#Create an instance of the Shortener class
type_tiny = pyshorteners.Shortener()
#Shorten the URL using the default shortener (TinyURL)
short_url = type_tiny.tinyurl.short(long_url)
print("Short URL:" + short_url)