import requests

url = 'https://api.meetup.com/PyData-Munchen/events?&status=past'
r = requests.get(url)

print(r.status_code)

print(r.json())
