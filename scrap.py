import requests
import re
from bs4 import BeautifulSoup

headers={
    "User-Agent":"Mozilla/5.0"
}
class Scrapmail:
    def __init__(self,url):
        self.url=url 

    def mails_found(self):
        url=self.url
        request=requests.get(url,timeout=100,headers=headers)
        if request.status_code==200:
            html=request.text
            bs=BeautifulSoup(html,"html.parser")
            texts=bs.get_text()
            regex_email= re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
            mails=regex_email.findall(texts)
            return mails
        else:
            error=request.raise_for_status()
            return error 
    
            