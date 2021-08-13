from urllib3 import PoolManager

https = PoolManager()

req = https.request('GET', 'https://www.google.com')





