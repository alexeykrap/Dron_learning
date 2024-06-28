import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# numpy as np

# ID БПЛА | Время полёта (минуты) | Расстояние (километры) | Средняя скорость (км/ч) | Высота полёта (метры)
drones_data = np.array([
    [1, 30, 10, 20, 500],
    [2, 45, 15, 20, 600],
    [3, 25, 8, 19.2, 550],
    [4, 60, 25, 25, 700],
    [5, 35, 12, 20.6, 580],
])
print('Данные о полётах БПЛА:')
print(drones_data)

flight_time = drones_data[:, 1]
average_flight_time = np.mean(flight_time)
print(f'Среднее время полёта: {average_flight_time} минут')

# pandas as pd:

drones_data2 = {
    'ID БПЛА': [1, 2, 3, 4, 5],
    'Время полёта': [30, 45, 25, 60, 35],
    'Расстояние': [10, 15, 8, 25, 12],
    'Средняя скорость': [20, 20, 19.2, 25, 20.6],
    'Высота полёта': [500, 600, 550, 700, 580],
}

drones_df = pd.DataFrame(drones_data2)
print('\n______________\n')
print('Данные о полётах БПЛА:')
print(drones_df)

average_flight_time = drones_df['Время полёта'].mean()
print(f'Среднее значение полёта: {average_flight_time} минут')

# matplotlib.pyplot as plt:

drones_df.plot(x='ID БПЛА', y='Время полёта', kind='bar')
plt.xlabel('ID БПЛА')
plt.ylabel('Время полёта (минуты)')
plt.title('Время полёта БПЛА')
plt.show()



