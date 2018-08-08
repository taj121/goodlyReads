import requests
import os
GOODREADS_KEY = os.environ['GOODREADS_KEY']
GOODREADS_BASE_URL = "https://www.goodreads.com/"

payload={ "v" : 2, "id" : 7552901, "shelf" : "to-read", "sort" : "date_added", "key" : GOODREADS_KEY }
response = requests.get('https://www.goodreads.com/review/list', params=payload) 

print( response.content )
