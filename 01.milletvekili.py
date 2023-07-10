#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:36:47 2023

@author: yasin
"""

import requests
import json
import pandas as pd
import time, random

response = requests.get("https://acikveri.ysk.gov.tr/api/getSecimDetayList")
election_list = json.loads(response.text)



target_name = "2CUMHURBAŞKANI VE 28.DÖNEM MİLLETVEKİLİ GENEL SEÇİMİ"
target_election_id = 20230

for election in election_list:
    for elec in election["secimList"]:
        if elec["secim_ADI"] == target_name:
            target_election_id = elec["secim_ID"]
            
            
response = requests.get("https://acikveri.ysk.gov.tr/api/getSandikSecimSonucBaslikList", params={
  "secimId": target_election_id,
  "secimCevresiId": "",
  "ilId": "",
  "bagimsiz": "1",
  "secimTuru": "8",
  "yurtIciDisi": "1"
})
party_list = json.loads(response.content.decode("utf-8"))



parti01	=	None
parti02	=	None
parti03	=	None
parti04	=	None
parti05	=	None
parti06	=	None
parti07	=	None
parti08	=	None
parti09	=	None
parti10	=	None
parti11	=	None
parti12	=	None
parti13	=	None
parti14	=	None
parti15	=	None
parti16	=	None
parti17	=	None
parti18	=	None
parti19	=	None
parti20	=	None
parti21	=	None
parti22	=	None
parti23	=	None
parti24	=	None
parti25	=	None
parti26	=	None
parti27	=	None
parti28	=	None
parti29	=	None
parti30	=	None

for party in party_list:
    if party['ad'] == 'MİLLET':
        parti01 = party['column_NAME']
    elif party['ad'] == 'HAK-PAR':
        parti02 = party['column_NAME']
    elif party['ad'] == 'TKP':
        parti03 = party['column_NAME']
    elif party['ad'] == 'TKH':
        parti04 = party['column_NAME']
    elif party['ad'] == 'SOL PARTİ':
        parti05 = party['column_NAME']
    elif party['ad'] == 'GENÇPARTİ':
        parti06 = party['column_NAME']
    elif party['ad'] == 'MEMLEKET':
        parti07 = party['column_NAME']
    elif party['ad'] == 'BBP':
        parti08 = party['column_NAME']
    elif party['ad'] == 'AK PARTİ':
        parti09 = party['column_NAME']
    elif party['ad'] == 'YENİDEN REFAH':
        parti10 = party['column_NAME']
    elif party['ad'] == 'MHP':
        parti11 = party['column_NAME']
    elif party['ad'] == 'YEŞİL SOL PARTİ':
        parti12 = party['column_NAME']
    elif party['ad'] == 'TİP':
        parti13 = party['column_NAME']
    elif party['ad'] == 'AB':
        parti14 = party['column_NAME']
    elif party['ad'] == 'ANAP':
        parti15 = party['column_NAME']
    elif party['ad'] == 'YP':
        parti16 = party['column_NAME']
    elif party['ad'] == 'HKP':
        parti17 = party['column_NAME']
    elif party['ad'] == 'MİLLİ YOL':
        parti18 = party['column_NAME']
    elif party['ad'] == 'VATAN PARTİSİ':
        parti19 = party['column_NAME']
    elif party['ad'] == 'GBP':
        parti20 = party['column_NAME']
    elif party['ad'] == 'CHP':
        parti21 = party['column_NAME']
    elif party['ad'] == 'İYİ PARTİ':
        parti22 = party['column_NAME']
    elif party['ad'] == 'AP':
        parti23 = party['column_NAME']
    elif party['ad'] == 'ZAFER PARTİSİ':
        parti24 = party['column_NAME']
    elif party['ad'] == 'SOSYALİST GÜÇ BİRLİĞİ İTTİFAKI':
        parti25 = party['column_NAME']
    elif party['ad'] == 'CUMHUR İTTİFAKI':
        parti26 = party['column_NAME']
    elif party['ad'] == 'EMEK VE ÖZGÜRLÜK İTTİFAKI':
        parti27 = party['column_NAME']
    elif party['ad'] == 'MİLLET İTTİFAKI':
        parti28 = party['column_NAME']
    elif party['ad'] == 'ATA İTTİFAKI':
        parti29 = party['column_NAME']
    elif party['ad'] == 'BAĞIMSIZ TOPLAM OY':
        parti30 = party['column_NAME']


















        
        
urls = []
for province_id in range(1, 82):
    url = "https://acikveri.ysk.gov.tr/api/getSecimSandikSonucList?secimId={}&secimTuru=8&ilId={}&ilceId=&beldeId=&birimId=&muhtarlikId=&cezaeviId=&sandikTuru=&sandikNoIlk=&sandikNoSon=&ulkeId=&disTemsilcilikId=&gumrukId=&yurtIciDisi=1&sandikRumuzIlk=&sandikRumuzSon=&secimCevresiId=&sandikId=&sorguTuru=2".format(target_election_id,province_id)
    urls.append(url)       
    
    
    
district_ids = pd.DataFrame()

for url in urls:
    response = requests.get(url)
    data = json.loads(response.text)
    df = pd.DataFrame(data).loc[:, ["il_ADI", "ilce_ADI", "il_ID", "ilce_ID"]]
    district_ids = pd.concat([district_ids, df], ignore_index=True)


district_ids["URLs"] = district_ids.apply(lambda x: "https://acikveri.ysk.gov.tr/api/getSecimSandikSonucList?secimId=" + str(target_election_id) + "&secimTuru=8&ilId=" + str(x["il_ID"]) + "&ilceId=" + str(x["ilce_ID"]) + "&beldeId=&birimId=&muhtarlikId=&cezaeviId=&sandikTuru=&sandikNoIlk=&sandikNoSon=&ulkeId=&disTemsilcilikId=&gumrukId=&yurtIciDisi=1&sandikRumuzIlk=&sandikRumuzSon=&secimCevresiId=&sandikId=&sorguTuru=2", axis=1)



province_votes = pd.DataFrame()

for j in range(district_ids.shape[0]):
    time.sleep(random.randint(1,5))
    url = district_ids["URLs"][j]
    df = pd.read_json(url)
    part01=list(df.columns).index(parti01)
    part02=list(df.columns).index(parti02)
    part03=list(df.columns).index(parti03)
    part04=list(df.columns).index(parti04)
    part05=list(df.columns).index(parti05)
    part06=list(df.columns).index(parti06)
    part07=list(df.columns).index(parti07)
    part08=list(df.columns).index(parti08)
    part09=list(df.columns).index(parti09)
    part10=list(df.columns).index(parti10)
    part11=list(df.columns).index(parti11)
    part12=list(df.columns).index(parti12)
    part13=list(df.columns).index(parti13)
    part14=list(df.columns).index(parti14)
    part15=list(df.columns).index(parti15)
    part16=list(df.columns).index(parti16)
    part17=list(df.columns).index(parti17)
    part18=list(df.columns).index(parti18)
    part19=list(df.columns).index(parti19)
    part20=list(df.columns).index(parti20)
    part21=list(df.columns).index(parti21)
    part22=list(df.columns).index(parti22)
    part23=list(df.columns).index(parti23)
    part24=list(df.columns).index(parti24)
    part25=list(df.columns).index(parti25)
    part26=list(df.columns).index(parti26)
    part27=list(df.columns).index(parti27)
    part28=list(df.columns).index(parti28)
    part29=list(df.columns).index(parti29)
    part30=list(df.columns).index(parti30)

    df = df[["il_ADI", "ilce_ADI",     parti01	, parti02	,parti03	,
    parti04	,
    parti05	,
    parti06	,
    parti07	,
    parti08	,
    parti09	,
    parti10	,
    parti11	,
    parti12	,
    parti13	,
    parti14	,
    parti15	,
    parti16	,
    parti17	,
    parti18	,
    parti19	,
    parti20	,
    parti21	,
    parti22	,
    parti23	,
    parti24	,
    parti25	,
    parti26	,
    parti27	,
    parti28	,
    parti29	,
    parti30	,]]
    
    province_votes = pd.concat([province_votes, df])
    print(j)


province_votes.columns = ['il',
'ilce',
'MİLLET',
'HAK-PAR',
'TKP',
'TKH',
'SOL PARTİ',
'GENÇPARTİ',
'MEMLEKET',
'BBP',
'AK PARTİ',
'YENİDEN REFAH',
'MHP',
'YEŞİL SOL PARTİ',
'TİP',
'AB',
'ANAP',
'YP',
'HKP',
'MİLLİ YOL',
'VATAN PARTİSİ',
'GBP',
'CHP',
'İYİ PARTİ',
'AP',
'ZAFER PARTİSİ',
'SOSYALİST GÜÇ BİRLİĞİ İTTİFAKI',
'CUMHUR İTTİFAKI',
'EMEK VE ÖZGÜRLÜK İTTİFAKI',
'MİLLET İTTİFAKI',
'ATA İTTİFAKI',
'BAĞIMSIZ TOPLAM OY']


province_votes.to_excel("/media/DRIVE/Dropbox/_My_Research/UmitHocaSecim/02.milletvekili.xlsx")  
















'''



[{'sira_NO': 1, 'ad': 'MİLLET', 'column_NAME': 'parti1_ALDIGI_OY'},
 {'sira_NO': 2, 'ad': 'HAK-PAR', 'column_NAME': 'parti2_ALDIGI_OY'},
 {'sira_NO': 3, 'ad': 'TKP', 'column_NAME': 'parti3_ALDIGI_OY'},
 {'sira_NO': 4, 'ad': 'TKH', 'column_NAME': 'parti4_ALDIGI_OY'},
 {'sira_NO': 5, 'ad': 'SOL PARTİ', 'column_NAME': 'parti5_ALDIGI_OY'},
 {'sira_NO': 6, 'ad': 'GENÇPARTİ', 'column_NAME': 'parti6_ALDIGI_OY'},
 {'sira_NO': 7, 'ad': 'MEMLEKET', 'column_NAME': 'parti7_ALDIGI_OY'},
 {'sira_NO': 8, 'ad': 'BBP', 'column_NAME': 'parti8_ALDIGI_OY'},
 {'sira_NO': 9, 'ad': 'AK PARTİ', 'column_NAME': 'parti9_ALDIGI_OY'},
 {'sira_NO': 10, 'ad': 'YENİDEN REFAH', 'column_NAME': 'parti10_ALDIGI_OY'},
 {'sira_NO': 11, 'ad': 'MHP', 'column_NAME': 'parti11_ALDIGI_OY'},
 {'sira_NO': 12, 'ad': 'YEŞİL SOL PARTİ', 'column_NAME': 'parti12_ALDIGI_OY'},
 {'sira_NO': 13, 'ad': 'TİP', 'column_NAME': 'parti13_ALDIGI_OY'},
 {'sira_NO': 14, 'ad': 'AB', 'column_NAME': 'parti14_ALDIGI_OY'},
 {'sira_NO': 15, 'ad': 'ANAP', 'column_NAME': 'parti15_ALDIGI_OY'},
 {'sira_NO': 16, 'ad': 'YP', 'column_NAME': 'parti16_ALDIGI_OY'},
 {'sira_NO': 17, 'ad': 'HKP', 'column_NAME': 'parti17_ALDIGI_OY'},
 {'sira_NO': 18, 'ad': 'MİLLİ YOL', 'column_NAME': 'parti18_ALDIGI_OY'},
 {'sira_NO': 19, 'ad': 'VATAN PARTİSİ', 'column_NAME': 'parti19_ALDIGI_OY'},
 {'sira_NO': 20, 'ad': 'GBP', 'column_NAME': 'parti20_ALDIGI_OY'},
 {'sira_NO': 21, 'ad': 'CHP', 'column_NAME': 'parti21_ALDIGI_OY'},
 {'sira_NO': 22, 'ad': 'İYİ PARTİ', 'column_NAME': 'parti22_ALDIGI_OY'},
 {'sira_NO': 23, 'ad': 'AP', 'column_NAME': 'parti23_ALDIGI_OY'},
 {'sira_NO': 24, 'ad': 'ZAFER PARTİSİ', 'column_NAME': 'parti24_ALDIGI_OY'},
 {'sira_NO': 1,
  'ad': 'SOSYALİST GÜÇ BİRLİĞİ İTTİFAKI',
  'column_NAME': 'ittifak1_ALDIGI_OY'},
 {'sira_NO': 2, 'ad': 'CUMHUR İTTİFAKI', 'column_NAME': 'ittifak2_ALDIGI_OY'},
 {'sira_NO': 3,
  'ad': 'EMEK VE ÖZGÜRLÜK İTTİFAKI',
  'column_NAME': 'ittifak3_ALDIGI_OY'},
 {'sira_NO': 4, 'ad': 'MİLLET İTTİFAKI', 'column_NAME': 'ittifak4_ALDIGI_OY'},
 {'sira_NO': 5, 'ad': 'ATA İTTİFAKI', 'column_NAME': 'ittifak5_ALDIGI_OY'},
 {'sira_NO': 999,
  'ad': 'BAĞIMSIZ TOPLAM OY',
  'column_NAME': 'bagimsiz_TOPLAM_OY'}]
'''