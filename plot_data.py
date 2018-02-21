import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/attendance.csv')
df.plot('local_date', 'yes_rsvp_count')
plt.title('PyData Meetup Attendance')
plt.gcf().savefig('figures/attendance.png')

