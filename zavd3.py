import matplotlib.pyplot as plt

# Дані
data = [
    {"name": "School 1", "type": "school", "students": 450},
    {"name": "Technical College 1", "type": "college", "students": 300},
    {"name": "Vocational School 1", "type": "vocational", "students": 200},
    {"name": "Technical College 2", "type": "college", "students": 350},
    {"name": "Vocational School 2", "type": "vocational", "students": 180},
    {"name": "School 23", "type": "school", "students": 304}
]

school_students = sum(item['students'] for item in data if item['type'] == 'school')
college_students = sum(item['students'] for item in data if item['type'] == 'college')
vocational_students = sum(item['students'] for item in data if item['type'] == 'vocational')

labels = ['School', 'College', 'Vocational']
sizes = [school_students, college_students, vocational_students]
colors = ['blue', 'green', 'red']

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})

# Налаштування заголовку
plt.title('Розподіл кількості учнів за типом навчального закладу', fontsize=15)

# Показати діаграму
plt.show()
