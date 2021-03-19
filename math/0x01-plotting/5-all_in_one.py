#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

figure = plt.figure(figsize=(9, 9))
figure.suptitle("All in one")
grid = plt.GridSpec(3, 2, wspace=0.3, hspace=0.5)

rows1 = figure.add_subplot(grid[0,0])
plt.xlim(0, 10)
plt.plot(y0,color="RED")

rows2 = figure.add_subplot(grid[0,1])
plt.xlabel('Height (in)', size="x-small")
plt.ylabel('Weight (lbs)', size="x-small")
plt.title("Men's Height vs Weight",size="small")
plt.plot(x1,y1,'mo', markersize=3)

rows3 = figure.add_subplot(grid[1,0])
plt.xlabel('Time (years)',size="x-small")
plt.ylabel('Fraction Remaining',size="x-small")
plt.title("Exponential Decay of C-14t",size="small")
plt.yscale("log")
plt.xlim(0, 28650)
plt.plot(x2,y2)

rows4 = figure.add_subplot(grid[1,1])
plt.xlim(0, 20000)
plt.ylim(0, 1)
plt.plot(x3,y31,color='red',dashes=[4, 3], label='C-14')
plt.plot(x3,y32, color='green', label='Ra-226')
plt.xlabel('Time (years)',size="x-small")
plt.ylabel('Fraction Remaining',size="x-small")
plt.title("Exponential Decay of Radioactive Elements",size="small")
plt.legend(loc='upper right', shadow=True, fontsize='large')

rows5 = figure.add_subplot(grid[2, :2])
bins=[10,20,30,40,50,60,70,80,90,100]
plt.ylim(0, 30)
plt.xlim(0, 100)
plt.xticks(np.arange(0, 110, 10))
plt.xlabel('Grades',size="x-small")
plt.ylabel('Number of Students',size="x-small")
plt.title("Project A")
plt.hist(student_grades, bins ,edgecolor='black')

plt.show()
