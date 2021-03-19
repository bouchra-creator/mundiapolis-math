#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

labels1 = ['Farrah', 'Fred', 'Felicia']
labels2 = ['apples', 'bananas', 'oranges', 'peaches']
labels3 = ['red', 'yellow', '#ff8000', '#ffe5b4']
plt.title("Number of Fruit per Person")
plt.ylabel("Quantity of Fruit")


for i in range(len(fruit)):
    plt.bar(labels1, fruit[i], bottom=np.sum(fruit[:i], axis=0),
            color=colors[i], label=fruits[i], width=0.5)
    
plt.yticks(np.arange(0, 90, 10))
plt.legend()

plt.show()
