from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
url = 'https://boe2.github.io/bsus.html?l=jp'
driver.get(url)
sleep(5)

#表示中のページのポケモンの名前を取得,使用率も
pokename = driver.find_element_by_id('monsinfo2').text.replace('-', '').replace('推定使用率：', '').replace(' ', '').strip('123456789.%#')
pokesiyou_tmp = driver.find_element_by_id('monsinfo2').text
pokesiyou = float(pokesiyou_tmp[-7:-1])
pokesiyou = round(pokesiyou,1)

#技使用率の取得
#ここから 取得用のcssid作成
wazaid = []
wazasiyouid = []
for q in range(1,19):
    if (q + 1) % 3 == 0:
        tmp = str(q)
        wazaid.append('td' + tmp)
    if q % 3 == 0:
        tmp1 = str(q)
        wazasiyouid.append('td' + tmp1)
#ここまで

waza = [] #ここに技が入る
waza_siyouritu = [] #技の使用率が入る
for i in wazaid:
    tmp = driver.find_element_by_id(i).text
    waza.append(tmp)
for i in wazasiyouid:
    tmp = float(driver.find_element_by_id(i).text.replace('%', ''))
    tmp = round(tmp,1)
    waza_siyouritu.append(tmp)

#csv用の前処理
write = []
write.append(pokename)
write.append(pokesiyou)
write = write + waza + waza_siyouritu

#csvへの処理
header = ['pokename', 'pokerate', 'waza1', 'waza2', 'waza3', 'waza4', 'waza5', 'waza6', 'waza1r','waza2r', 'waza3r', 'waza4r', 'waza5r', 'waza6r']
with open('some.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerow(header)
    writer.writerow(write)     # list（1次元配列）の場合
f.close()
####################################################
#print(pokename)
#print(str(pokesiyou) + '%')
#for i, j in zip(waza,waza_siyouritu):
#    print(i,str(j)+'%')
for i in write:
    print(i)


driver.quit()
