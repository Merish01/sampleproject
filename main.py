import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentData.csv")

plt.scatter(df['Hours'],df['Scores'],marker = 'o',linestyle = '--')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.title('Student Scores vs Hours Studied')
plt.show()

plt.bar(df['Hours'],df['Scores'], color = 'green')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.title('Bar Graph')
plt.show()

labels = df['Hours'].head(5)
sizes = df['Scores'].head(5)
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Top 5 Scores")
plt.show()
plt.hist(df['Scores'],bins =10 )

plt.title("Distribution of Scores")
plt.show()
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)   
plt.scatter(df['Hours'], df['Scores'])
plt.title("Scatter Plot")

plt.subplot(1,2,2)  
plt.hist(df['Scores'])
plt.title("Histogram")

plt.tight_layout()
plt.show()