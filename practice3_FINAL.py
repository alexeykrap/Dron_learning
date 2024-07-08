import pandas as pd
import matplotlib.pyplot as plt

months_temparature = pd.read_csv('months_temparature_Tver.csv')

months = months_temparature['Месяцы']
temp_days = months_temparature['Днём']
temp_nights = months_temparature['Ночью']

print(months)
print(temp_days)
print(temp_nights)

plt.figure(figsize=(10, 5))
plt.plot(months, temp_days, label='Температура днём')
plt.plot(months, temp_nights, label='Температура ночью')
plt.xlabel('Месяцы')
plt.ylabel('Температура')
plt.title('Среднемесячная температура в Твери')
plt.legend()
plt.grid()
plt.show()

