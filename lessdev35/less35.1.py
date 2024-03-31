#!/usr/bin/python3

import seaborn as sns
import matplotlib.pyplot as plt

# Загрузите набор данных "flights" из Seaborn
flights = sns.load_dataset("flights")

# Создайте сводную таблицу для корреляции между месяцами и пассажирскими перевозками
#flights_pivot = flights.pivot("month", "year", "passengers")

flights_pivot = flights.pivot(index="month", columns="year", values="passengers")



# Создайте тепловую карту корреляции
plt.figure(figsize=(10, 8))
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap='coolwarm')

# Настройте внешний вид графика
plt.title('Flights - Month vs Passengers Heatmap')
plt.xlabel('Year')
plt.ylabel('Month')

# Покажите график
plt.show()

