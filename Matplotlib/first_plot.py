from matplotlib import pyplot as plt

# print(plt.style.available)
plt.style.use('ggplot')
dev_x=[25,26,27,28,29,30,31,32,33,34]

py_dev_y=[37485,41789,43788,52789,57134,59784,64123,66127,77134,79146]
plt.plot(dev_x,py_dev_y,color='#444444',linestyle='--',marker='o',linewidth=2,label='Python Devs')

dev_y=[35987,41657,45789,46135,52789,55678,62137,65894,67124,78942]
plt.plot(dev_x,dev_y,color='#5a7d9a',linestyle='--',marker='o',linewidth=2,label=' All Devs')

plt.ylabel('Salary')
plt.xlabel('Age')
plt.title('Salary by Age')
plt.legend()

plt.grid(True)
plt.tight_layout()

plt.savefig('first_plot.png')
plt.show()