import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpldat
from datetime import datetime,timedelta

plt.style.use("seaborn")
data=pd.read_csv("real-time-data.csv")
data['Date']=pd.to_datetime(data['Date'])
data.sort_values('Date',inplace=True)

price_date=data['Date']
price_close=data['Close']
plt.plot_date(price_date,price_close,linestyle='solid')

plt.xlabel("Date")
plt.ylabel("Closing file")
plt.tight_layout()
plt.title("Bitcoin prices")
plt.savefig("Time series")
plt.show()