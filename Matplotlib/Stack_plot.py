from matplotlib import pyplot as plt
plt.style.use("ggplot")

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

colors=['#008fd5','#fc4f30','#e5ae37']
labels=['Player1','Player2','Player3']

plt.stackplot(minutes,player1,player2,player3,labels=labels,colors=colors)
plt.xlabel('Minutes')
plt.ylabel('Players')
plt.legend(loc=(0.07,0.05))
plt.title("Stack plot")
plt.tight_layout()
# plt.savefig("Stack plots")
plt.show()