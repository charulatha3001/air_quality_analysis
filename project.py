import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('clean.xlsx')


data['FullDate'] = pd.to_datetime({
    'year': data['Year'],
    'month': data['Month'],
    'day': data['Date']
})


data = data.sort_values('FullDate')

plt.plot(data['FullDate'], data['AQI'])
plt.title('AQI Over Time')
plt.xlabel('Date')
plt.ylabel('AQI')
plt.show()


print(data[['AQI', 'NO2', 'SO2', 'CO', 'Ozone']].corr())