"""
Write a Python programming to create a below chart of the popularity of programming Languages.
2. Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
"""
import matplotlib.pyplot as plt

# Programming languages
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']

# Popularity percentages
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create pie chart
plt.pie(popularity, labels=languages, autopct='%1.1f%%')

# Set aspect ratio to be equal so that pie is drawn as a circle
plt.axis('equal')

# Add a title
plt.title('Popularity of Programming Languages')

# Display the chart
plt.show()
