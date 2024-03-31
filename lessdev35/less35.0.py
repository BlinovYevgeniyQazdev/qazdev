#!/usr/bin/python3

import seaborn as sns
import matplotlib.pyplot as plt

# Загрузите набор данных "tips" из Seaborn
tips = sns.load_dataset("tips")

# Создайте совмещенные гистограммы для 'total_bill' и 'tip' на одном графике
# Используйте прозрачность, чтобы улучшить видимость данных
sns.histplot(data=tips, x="total_bill", color="blue", alpha=0.5, label='Total Bill')
sns.histplot(data=tips, x="tip", color="orange", alpha=0.5, label='Tip')

# Добавьте легенду
plt.legend()

# Настройте внешний вид графика
plt.title('Overlayed Histograms of Total Bill and Tip')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Показать график
plt.show()

