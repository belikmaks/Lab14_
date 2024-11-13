import pandas as pd
import matplotlib.pyplot as plt

# Try to load the CSV file
try:
    data = pd.read_csv('lab11_1.csv')
except FileNotFoundError:
    print("Не вдалося знайти файл csv.")
    exit()  # Exit if the file is not found

# Define the years for the plot
years = [str(year) for year in range(2015, 2023)]

# Extract relevant columns
data = data[['Country Name', 'Country Code'] + years]

# Data for specific countries
country1 = "Aruba"
country2 = "Armenia"

# Filter data for each country
country_data1 = data[data['Country Name'] == country1]
country_data2 = data[data['Country Name'] == country2]

# Extract the population data for the years and convert to float
country_data1_years = country_data1[years].T.astype(float)
country_data2_years = country_data2[years].T.astype(float)

# Plot population dynamics for both countries
plt.figure(figsize=(10,6))
plt.plot(years, country_data1_years, label=country1, marker='o', color='blue')
plt.plot(years, country_data2_years, label=country2, marker='o', color='red')

# Add titles and labels
plt.title('Динаміка показника населення для обраних країн за 2015-2023 роки')
plt.xlabel('Рік')
plt.ylabel('Значення показника(млн)')
plt.legend()
plt.grid(True)
plt.show()

# Ask the user for a country to plot a bar chart
country_bar = input("Введіть назву країни для побудови стовпчастої діаграми:")

# Check if the country exists in the dataset
if country_bar not in data['Country Name'].values:
    print(f"Країна {country_bar} не знайдена в даних.")
else:
    # Filter data for the selected country
    country_data_bar = data[data['Country Name'] == country_bar]
    country_data_bar_years = country_data_bar[years].T.astype(float)

    # Plot the bar chart for the selected country
    plt.figure(figsize=(10, 6))
    plt.bar(years, country_data_bar_years[0], color='orange')
    plt.title(f'Стовпчаста діаграма для країни: {country_bar}')
    plt.xlabel('Рік')
    plt.ylabel('Значення показника (млн)')ґ
    plt.xticks(rotation=45)
    plt.show()
