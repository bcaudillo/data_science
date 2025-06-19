# Libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Data
fruits = ['Apple', 'Banana', 'Orange', 'Grape']
counts = [25, 20, 15, 10]

# Create a bar chart
sns.set(style="whitegrid")
ax = sns.barplot(x=fruits, y=counts)

# Add labels and title
ax.set(xlabel='Fruit', ylabel='Count', title='Favorite Fruits')

# Display the chart
plt.show()