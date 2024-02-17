from urllib.request import urlopen
import time as t
while True:
    print("Fetching data...")
    page = urlopen("http://sampleadr.ess:port")
    print("Formatting data...")
    #uprava html, tak aby nam zbyla jen teplota na kotli
    page = page.read()
    page = str(page)
    page = page.split(' ')
    page = page[50]
    page = str(page)
    print(page)
    print("Writting data...")
    soubor = "train-data.txt" 
    text_k_pridani = page 
    with open(soubor, "a") as soubor_objekt: # Otevření souboru v režimu "append" (přidávání)
        soubor_objekt.write(text_k_pridani + "\n")    # Přidání textu na konec souboru
    print("Waiting for 10 minutes...")
    t.sleep(600)
