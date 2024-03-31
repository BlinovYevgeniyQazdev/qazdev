#!/usr/bin/python3

import seaborn as sns
import matplotlib.pyplot as plt

# Загружаем набор данных "diamonds" из Seaborn
diamonds = sns.load_dataset("diamonds")

# Группируем данные по качеству огранки и суммируем цену
diamonds_grouped = diamonds.groupby('cut')['price'].sum().reset_index()

# Создаем круговую диаграмму (pie chart) с суммами цен по категориям качества огранки
plt.figure(figsize=(8, 8))
plt.pie(diamonds_grouped['price'], labels=diamonds_grouped['cut'], autopct='%1.1f%%', startangle=140)
plt.title('Diamond Prices by Cut Quality')

# Показываем график
plt.show()

