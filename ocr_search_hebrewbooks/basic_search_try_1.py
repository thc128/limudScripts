# -*- coding: utf-8 -*-
import requests
hebrew_books='http://hebrewbooks.org/'
search_string='as'
#r= requests.get(hebrew_books)
#print r.text
#payload = {'ctl00$cpMstr$ocrRequest': search_string}
payload = {'ctl00$cpMstr$txtsefer': search_string}
r2 = requests.post(hebrew_books+'home.aspx', data=payload)
print r2.text


