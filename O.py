import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 30, 40]

fig, ax = plt.subplots()
ax.pie(values, labels=categories, autopct='%s: %.1f%%')
ax.set_title('Pie chart with string labels')
plt.show()