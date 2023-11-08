from urllib.request import urlopen
import time as t
while True:
    print("Fetching data...")
    page = urlopen("http://213.108.160.85:666/")
    print("Formatting data...")
    page = page.read()
    page = str(page)
    page = page.split(' ')
    page = page[50]
    page = str(page)
    print(page)
    print("Writting data...")
    soubor = "train-data.txt"   # Přidání textu na konec souboru
    text_k_pridani = page   # Text, který chcete přidat
    with open(soubor, "a") as soubor_objekt: # Otevření souboru v režimu "append" (přidávání)
        soubor_objekt.write(text_k_pridani + "\n")    # Přidání textu na konec souboru
    print("Waiting for 10 minutes...")
    t.sleep(600)