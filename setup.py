from scrap import Scrapmail
import requests 

url="https://www.andrewng.org/contact/"
mails=Scrapmail(url)
results=mails.mails_found()
print(results)