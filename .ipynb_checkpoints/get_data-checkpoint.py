import requests
import pandas as pd


url = 'https://api.meetup.com/PyData-Munchen/events?&status=past'
r = requests.get(url)

print(r.status_code)

print(r.json())

# Put into a Pandas dataframe
df = pd.DataFrame(r.json())
df = df[['name', 'local_date', 'yes_rsvp_count']]
print(df)

df.to_csv('data/attendance.csv')