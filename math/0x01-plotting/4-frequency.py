#%%

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
plt.hist(student_grades, bins = 10,edgecolor='black')
plt.xticks(np.arange(0, 100, 10))
plt.ylim(0, 30)
plt.xlim(0, 100)
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title("Project A")
plt.show()
