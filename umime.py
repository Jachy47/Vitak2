def najdi_unikatni_osmipismenna(nazev_souboru):
    try:
        with open(nazev_souboru, 'r', encoding='utf-8') as f:
            obsah = f.read().lower()
        cisty_text = ""
        for znak in obsah:
            if 'a' <= znak <= 'z':
                cisty_text += znak
            else:
                cisty_text += " "


        vsechna_slova = cisty_text.split()


        seznam_osmi = []
        for slovo in vsechna_slova:
            if len(slovo) == 8:
                seznam_osmi.append(slovo)


        unikatni_slova = sorted(list(set(seznam_osmi)))

        return unikatni_slova

    except FileNotFoundError:
        print(f"Chyba: Soubor {nazev_souboru} nebyl nalezen.")
        return []

# Spuštění
vysledek = najdi_unikatni_osmipismenna('s.txt')

print(f"Nalezeno {len(vysledek)}")