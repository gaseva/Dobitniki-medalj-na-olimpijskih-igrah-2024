# Analiza dobitnikov medalj na Olimpijskih igrah 2024 v Parizu
Za projektno nalogo pri predmetu *Uvod v programiranje* *(UVP)* v študijskem letu *2023/2024* sem 
se odločila zajeti in analizirati podatke o dobitnikih medalj na [**Olimpijskih igrah 2024 v Parizu**](https://olympics.com/en/paris-2024).

## Uporaba programa
Za uporabo mora imeti uporabnik naložene knjižnice `os`, `requests`, `re`, `csv`, `pandas` in `matplotlib.pyplot`, ter nameščen `Jupyter Notebook`.

## 1. del - zajem podatkov
V datoteki zajem_podatkov.py so funkcije, ki s spletne strani shranijo njeno vsebino kot html kodo (datoteka
dobitniki_medalje.html), v njej poiščejo potrebne podatke in jih na koncu shranijo v csv datoteki
(dobitniki_medalje.csv)

Za vsakega dobitnika medalj izluščila naslednje podatke:
- ime in priimek
- državo
- spol
- disciplino
- število zlatih/srebrnih/bronastih medalj
- skupno število medalj

## 2. del - analiza podatkov
Za analizo sem uporabila knjižnico pandas, za risanje grafov pa matplotlib. Analiza je narejena v Jupyter
Notebook (datoteka analiza.ipynb). Pri analizi sem se osredotočila na razlike glede na spol, število dobljenih medalj ter državo tekmovalca. Na koncu sem še izluščila podatke o slovenskih dobitnikih medalj ter o plezalcih, ki so dobili medaljo.
