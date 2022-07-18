import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Tabellen/bevoelkerung-staatsangehoerigkeitsgruppen.html;jsessionid=EA2CCAEFACA86E50B8C818E9208DED06.live732"
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
tags_tr = soup.tbody.find_all("tr")

def add_data(index, td, sub_data):
    string = td.text

    string = ''.join(string.split())
    if string.isdigit():
        string = string.replace(',', '.')
        if '.' in string:
            string = float(string)
        else:
            string = int(string)

    sub_data.append(string)

data = []
for tr in tags_tr:
    sub_data = []
    for index, td in enumerate(tr.find_all("td")):
        if index % 9 != 0 or index == 0:
            add_data(index, td, sub_data)
        else:
            add_data(index, td, sub_data)
            data.append(sub_data)
            sub_data = []

columns = ["Jahr", "insgesamt", "Deutschland", "Deutschland%", "EU", "EU%", "uebrigesEuropa", 'uebrigesEuropa%', 'Drittstaaten', 'Drittstaaten%']
df = pd.DataFrame(data, columns=columns)

for index, year in enumerate(df['Jahr']):
    if year // 3000 > 1:
        df.iloc[index, 0]= year // 10
print(df)

import matplotlib.pyplot as plt

plt.plot(df['Jahr'], df['insgesamt'])
plt.show()