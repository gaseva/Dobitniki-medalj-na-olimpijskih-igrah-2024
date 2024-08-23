import csv
import os
import requests
import re

medalists_url = 'https://olympics.com/en/paris-2024/medals/medallists'
medalists_mapa = 'podatki'
medalists_filename = 'dobitniki_medalje.html'
csv_filename = 'dobitniki_medalje.csv'

def pridobi_html(url):
    headers = {'User-agent': 'Chrome/124.0.6367.201'}
    html = requests.get(url, headers=headers)
    return html.text

def shrani_v_mapo(vsebina, mapa, filename):
    os.makedirs(mapa, exist_ok=True)
    path = os.path.join(mapa, filename)
    with open(path, 'w', encoding='utf-8') as dat:
        dat.write(vsebina)
    return None

def shrani_html(url, mapa, filename):
    text = pridobi_html(url)
    shrani_v_mapo(text, mapa, filename)
    return None

#shrani_html(medalists_url, medalists_mapa, medalists_filename)

def preberi_vsebino(mapa, filename):
    path = os.path.join(mapa, filename)
    with open(path, 'r', encoding='UTF-8') as dat:
        vsebina = dat.read()
    return vsebina

def razbitje_na_bloke(vsebina):
    return re.findall(r'\{"organisation".*?\}\}\]', vsebina, flags=re.DOTALL)

def izlusci_info_iz_bloka(blok):
    vzorec_ime = r'"fullName":"(.*?)",'
    vzorec_država = r'"organisationName":"(.*?)",'
    vzorec_spol = r'"gender":"(.)",'
    vzorec_zlate = r'"medalsGold":(.),'
    vzorec_srebrne = r'"medalsSilver":(.),'
    vzorec_bronaste = r'"medalsBronze":(.),'
    vzorec_skupaj = r'"medalsTotal":(.),'
    vzorec_disciplina = r'"disciplineName":"(.*?)",.*?\}\}\]'

    ime = re.search(vzorec_ime, blok)
    država = re.search(vzorec_država, blok)
    spol = re.search(vzorec_spol, blok)
    zlate = re.search(vzorec_zlate, blok)
    srebrne = re.search(vzorec_srebrne, blok)
    bronaste = re.search(vzorec_bronaste, blok)
    skupaj = re.search(vzorec_skupaj, blok)
    disciplina = re.search(vzorec_disciplina, blok)
    
    return{'ime': ime.group(1), 'država': država.group(1), 'spol': spol.group(1), 
        'disciplina': disciplina.group(1), 'zlate': zlate.group(1), 'srebrne': srebrne.group(1),
        'bronaste': bronaste.group(1), 'skupaj': skupaj.group(1)}
    
def izlusci_iz_dat(mapa, filename):
    vsebina = preberi_vsebino(mapa, filename)
    bloki = razbitje_na_bloke(vsebina)
    podatki = []
    for blok in bloki:
        tekmovalec = izlusci_info_iz_bloka(blok)
        podatki.append(tekmovalec)
    return podatki

def ustvari_cvs(mapa, filename, podatki = list):
    os.makedirs(mapa, exist_ok=True)
    path = os.path.join(mapa, filename)
    fieldnames = podatki[0].keys()
    with open(path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(podatki)
    return

def izlusci_in_shrani_csv(mapa, filename, csv_mapa, csv_filename):
    podatki = izlusci_iz_dat(mapa, filename)
    ustvari_cvs(csv_mapa, csv_filename, podatki)
    return None

#izlusci_in_shrani_csv(medalists_mapa, medalists_filename, medalists_mapa, csv_filename)

def main(url, mapa, filename, csv_filename):
    shrani_html(url, mapa, filename)
    izlusci_in_shrani_csv(mapa, filename, mapa, csv_filename)
    return None
