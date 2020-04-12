from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("seaborn")

data=pd.read_csv("2019-05-31-data.csv")
view=data['view_count']
likes=data['likes']
ratio=data['ratio']

plt.scatter(view,likes,c=ratio,cmap='cool',
            edgecolors='black',linewidths=1,alpha=0.75)
plt.xscale('log')
plt.yscale('log')
cbar=plt.colorbar()
cbar.set_label("Like - Dislike ratio")
plt.tight_layout()
plt.title("Trending videos ")
plt.xlabel("View counts")
plt.ylabel("Likes")
plt.savefig("Scatter plots")
plt.show()