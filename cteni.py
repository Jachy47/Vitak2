soubor = "karlikjara.txt"

with open(soubor, "r", encoding="utf-8") as f: 
    text = f.read()

slova = text.split()
txt = text.replace(" ", "").replace("\n", "")
pocty_slov = {}

for slovo in slova:
    if slovo in pocty_slov:
        pocty_slov[slovo] += 1
    else:
        pocty_slov[slovo] = 1

seradit = sorted(pocty_slov.items(), key=lambda x: x[1], reverse=True)

for slovo, pocet in seradit:
    print(f"'{slovo}': {pocet}")