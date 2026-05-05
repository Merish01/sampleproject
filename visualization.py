import matplotlib.pyplot as plt

def plot_scatter(df):
    plt.scatter(df['Hours'], df['Scores'])
    plt.title("Hours vs Scores")
    plt.xlabel("Hours")
    plt.ylabel("Scores")
    plt.show()


def plot_histogram(df):
    plt.hist(df['Scores'], bins=10)
    plt.title("Score Distribution")
    plt.xlabel("Scores")
    plt.ylabel("Frequency")
    plt.show()


def plot_bar(grouped):
    grouped.plot(kind='bar')
    plt.title("Average Score by Study Hours Group")
    plt.xlabel("Hours Group")
    plt.ylabel("Average Score")
    plt.show()


def plot_pie(df):
    sizes = df['Scores'].head(5)
    labels = df['Hours'].head(5)

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Top 5 Scores Distribution")
    plt.show()


def plot_subplot(df):
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.scatter(df['Hours'], df['Scores'])
    plt.title("Scatter")

    plt.subplot(1,2,2)
    plt.hist(df['Scores'], bins=10)
    plt.title("Histogram")

    plt.tight_layout()
    plt.show()