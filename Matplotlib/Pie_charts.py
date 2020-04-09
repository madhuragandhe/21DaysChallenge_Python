from matplotlib import pyplot as plt

plt.style.use('ggplot')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode=[0,0,0,0.1,0]
colors=['#008fd5','#fc4f30','#e5ae37','#6d904f','#653891']

plt.pie(slices,labels=labels,explode=explode,shadow=True,startangle=90,
        autopct='%1.1f%%',colors=colors,wedgeprops={'edgecolor':'black'})
plt.title("Fav Languages")
plt.tight_layout()
plt.savefig("Pie chart")
plt.show()