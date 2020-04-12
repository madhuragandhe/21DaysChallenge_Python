from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("ggplot")

data=pd.read_csv('data3.csv')
ids=data['Responder_id']
age=data['Age']
bins=[10,20,30,40,50,60,70,80,90]
plt.hist(age,bins=bins,edgecolor='black',color='#12fa7b')
median=29
plt.axvline(median,color='#fc4f30',label='Age median',linewidth=1)
plt.legend()

plt.title("No. of responders")
plt.xlabel("Ages")
plt.ylabel("Responders")
plt.tight_layout()
plt.savefig("Histograms")
plt.show()