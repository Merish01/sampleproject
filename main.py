import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

plt.plot(x,y,color = 'red',marker = '*', linestyle = ':')
plt.title("Style line Graph")
plt.show()

Students = ['A','B','C','D','E']
Marks = [85,90,78,92,88]
plt.bar(Students, Marks, color = 'green')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Bar Graph')
plt.show()

labels = ["Python", "Java", "C++"]
sizes = [50, 30, 20]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Programming Language Usage")
plt.show()

plt.subplot(1,2,1)
plt.plot(x, y)
plt.title("Line")

plt.subplot(1,2,2)
plt.bar(Students, Marks)
plt.title("Bar")

plt.show()