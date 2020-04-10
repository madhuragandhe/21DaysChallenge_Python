from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("ggplot")
data=pd.read_csv('data2.csv')
ages=data['Age']
dev_salary=data['All_Devs']
py_salary=data['Python']
# js_salary=data['Javascript']

plt.plot(ages,dev_salary,color='#444444',linestyle='--',label='All Devs')
plt.plot(ages,py_salary,color='#4af445',label='Python')
median=57287

plt.fill_between(ages,py_salary,dev_salary,where=(py_salary>dev_salary),
                 interpolate=True,alpha=0.25,label='Above avg')

plt.fill_between(ages,py_salary,dev_salary,where=(py_salary<dev_salary),
                 interpolate=True,color='black',alpha=0.25,label='Below avg')
plt.xlabel('ages')
plt.ylabel('salaries')
plt.legend()
plt.title("Line plot for median salary by age")
plt.tight_layout()
plt.savefig("Line plots")
plt.show()
