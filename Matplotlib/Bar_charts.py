from matplotlib import pyplot as plt
import numpy as np

# Vertical Bar plots
'''
plt.style.use('fivethirtyeight')
dev_x=[25,26,27,28,29,30,31,32,33,34]
x_indexes=np.arange(len(dev_x))
width=0.25

py_dev_y=[37485,41789,43788,52789,57134,59784,64123,66127,77134,79146]
plt.bar( x_indexes+width,py_dev_y,width=width,color='#ff0000',label='Python Devs')


js_dev_y=[31374,42107,43789,49789,59176,59794,64003,67334,75122,79999]
plt.bar( x_indexes-width,js_dev_y,width=width,color='#00ff00',label='Javascript Devs')

dev_y=[35987,41657,45789,46135,52789,55678,62137,65894,67124,78942]
plt.bar(x_indexes,dev_y,width=width,color='#0000ff',label='All Devs')

plt.ylabel('Salary')
plt.xlabel('Age')
plt.title('Salary by Age')
plt.legend()
plt.xticks(ticks=x_indexes,labels=dev_x)

plt.grid(True)
plt.tight_layout()

plt.savefig('Horizontal_bars.png')
plt.show()
'''
import csv
from collections import Counter
# Plotting top 15 most used languages

plt.style.use('fivethirtyeight')
with open('data.csv') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    language_counter = Counter()
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

language=[]
popularity=[]

for item in language_counter.most_common(15):
    language.append(item[0])
    popularity.append(item[1])

language.reverse()
popularity.reverse()

plt.barh(language,popularity)
plt.title("Most popular languages")
plt.xlabel("No of people using")
plt.tight_layout()
plt.plot()
plt.savefig("Horizontal_bar")
plt.show()
