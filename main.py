import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('uber-raw-data-sep14.csv')
#This data contains data about date and time, latitude and longitude, and a Base column that contains code affiliated with the uber pickup.
data['Date/Time']= data['Date/Time'].map(pd.to_datetime)
data.head()
# let’s have a look at each day to see on which day the Uber trips were highest:
sns.set(rc={'figure.figsize':(12, 10)})
sns.distplot(data["Day"])
# Analyze the Uber trips according to the hours:
sns.distplot(data["Hour"])
# Analyze the Uber trips according to the weekdays:
sns.distplot(data["Weekday"])

# correlation of hours and weekdays on the Uber trips:
df = data.groupby(["Weekday", "Hour"]).apply(lambda x: len(x))
df = df.unstack()
sns.heatmap(df, annot=False)

# ploting the density of Uber trips according to the regions of the New Your city:
data.plot(kind='scatter', x='Lon', y='Lat', alpha=0.4, s=data['Day'], label='Uber Trips',
figsize=(12, 8), cmap=plt.get_cmap('jet'))
plt.title("Uber Trips Analysis")
plt.legend()
plt.show()

