import matplotlib.pyplot as plt

labels = ('Python', 'Java', 'Scala', 'C#')
sizes = [45.0, 30.0, 15.0, 10.0]
# autopct: takes a string (or function) to be used to format the numeric values
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.f%%',
    counterclock=False,
    startangle=90
)

plt.show()
