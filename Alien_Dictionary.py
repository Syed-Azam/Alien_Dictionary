# Project : Persistent Dictionary For Alien Civilization
# Author  : Syed Azam Hassan
import json # Alien Language JSON Datafile
def box(s):
    l = len(s)
    print("┌"+"─"*l+"┐")
    print("│"+s+"│")
    print("└"+"─"*l+"┘")
print("\a")
print(" ▄▄▄· ▄▄▌  ▪  ▄▄▄ . ▐ ▄     ·▄▄▄▄  ▪   ▄▄· ▄▄▄▄▄▪         ▐ ▄  ▄▄▄· ▄▄▄   ▄· ▄▌")
print("▐█ ▀█ ██•  ██ ▀▄.▀·•█▌▐█    ██▪ ██ ██ ▐█ ▌▪•██  ██ ▪     •█▌▐█▐█ ▀█ ▀▄ █·▐█▪██▌")
print("▄█▀▀█ ██▪  ▐█·▐▀▀▪▄▐█▐▐▌    ▐█· ▐█▌▐█·██ ▄▄ ▐█.▪▐█· ▄█▀▄ ▐█▐▐▌▄█▀▀█ ▐▀▀▄ ▐█▌▐█▪")
print("▐█ ▪▐▌▐█▌▐▌▐█▌▐█▄▄▌██▐█▌    ██. ██ ▐█▌▐███▌ ▐█▌·▐█▌▐█▌.▐▌██▐█▌▐█ ▪▐▌▐█•█▌ ▐█▀·.")
print(" ▀  ▀ .▀▀▀ ▀▀▀ ▀▀▀ ▀▀ █▪    ▀▀▀▀▀• ▀▀▀·▀▀▀  ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪ ▀  ▀ .▀  ▀  ▀ • ")
print("....ℭ𝔬𝔪𝔪𝔲𝔫𝔦𝔠𝔞𝔱𝔦𝔬𝔫 𝔴𝔦𝔱𝔥 𝔢𝔵𝔱𝔯𝔞𝔱𝔢𝔯𝔯𝔢𝔰𝔱𝔯𝔦𝔞𝔩 𝔦𝔫𝔱𝔢𝔩𝔩𝔦𝔤𝔢𝔫𝔠𝔢....")
while True:
    print("   ●───────┐            ┌───────●   ")
    print("           │            │           ")
    print("╔══════════╧════════════╧══════════╗")
    print("║   ◄██► M A I N    M E N U ◄██►   ║")
    print("╠══════════════════════════════════╣")
    print('║ [1] English to Alien Translation ║')
    print('║ [2] Alien to English Translation ║')
    print('║ [3] Display Dictionary           ║')
    print('║ [4] Edit Dictionary              ║')
    print('║ [5] Exit                         ║')
    print("╚══════════════(◄██►)══════════════╝")
    ch = input("      Enter Choice [1/5] : ")
    print()
    if ch == "5":
        box("What are you gonna do, talk the alien to death?")
        box("Good Bye")
        print("\a")
        break
    if ch == "1":
        box("English to Alien Translation")
        p = input("Type a phrase in English Language: ")
        p = p.lower()
        with open("alien_dict.json") as ad:
            d = json.load(ad)
            d = {k.lower():v.lower() for k,v in d.items()}
            ap = "Alien Phrase : "
            for w in p.split():
                if w in d:
                    ap = ap + " " + d[w]
                else:
                    ap = ap + " " + w
            box(ap.capitalize())
        input()
        continue
    elif ch == "2":
        box("Alien to English Translation")
        p = input("Type a phrase in Alien Language: ")
        p = p.lower()
        with open("alien_dict.json") as ad:
            d = json.load(ad)
            d = {k.lower():v.lower() for k,v in d.items()}
            ap = "English Phrase : "
            for w in p.split():
                if w in d.values():
                    l = [k  for (k, v) in d.items() if v == w]
                    ap = ap + " " + ' '.join(l)
                else:
                    ap = ap + " " + w
            box(ap.capitalize())
        input()
        continue
    elif ch == "3":
        box("Display Dictionary")
        with open("alien_dict.json") as ad:
            d = json.load(ad)
            print(json.dumps(d, indent = 4, sort_keys=True))
        input()
        continue
    elif ch == "4":
        box("Edit Alien Dictionary")
        try:
            with open("alien_dict.json") as ad:
                d = json.load(ad)
                e = input("Enter English Translation: ")
                a = input("Enter a Alien Word: ")
                if a.strip() == "" or e.strip() == "":
                    print("Blank Words Can't Add")
                else:
                    d[e] = a
                    with open("alien_dict.json", "w") as ad:
                        json.dump(d, ad)
                        print("Word added in Alien Dictioanry")
        except FileNotFoundError:
            with open("alien_dict.json", 'w') as ad:
                json.dump({}, ad)
                print("New Alien Dictionary Created")
        input()
        continue