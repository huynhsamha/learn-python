import requests

word = 'country'

r = requests.get('http://dog.ceo/api/breeds/list/all')

print('Status', r.status_code)
print('encoding', r.encoding)
print('cookie', r.cookies)
print('headers', r.headers)
print('url', r.url)
print('json', r.json())