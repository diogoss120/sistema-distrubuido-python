import sqlite3
import requests
import random
from datetime import datetime
import time

url = 'https://api.thingspeak.com/update?api_key=AEGFG6YV26QD4F50&'
campo01 = '&field1='
campo02 = '&field2='
campo03 = '&field3='

conexao = sqlite3.connect('D:\\temperatura.db')
cursor = conexao.cursor()

def escreverNoThinkSpeak(id, umi, temp):
    req = requests.get(url+campo01+str(id)+campo02+str(umi)+campo03+str(temp))

def escreverNoBd(temp, umi):
    insert = "insert into sensores (temperatura, umidade, data) values ('"+str(umi)+"', '"+str(temp)+"', strftime('%Y %m %d','now'))"
    cursor.execute(insert)
 
while True:
    temp = random.randrange(10, 40)
    umid = random.randrange(1, 100)

    escreverNoBd(umid , temp)

    cursor.execute('select max(id) from sensores')
    id = ''
    for row in cursor.fetchall():
        id = str(row[0])
    print('Id do ultimo registro: '+str(id))
        
    escreverNoThinkSpeak(id, umid , temp)

    conexao.commit()
    time.sleep(20)

cursor.close()