import json
from datetime import date

purchased = ""
payed_amount = ""
total = ""
ny_total = ""
updates = []
json_data = {}



def open_json():
    global json_data, updates, payed_amount, total, ny_total
    opened = open("summa.json", "r")
    data = json.load(opened)
    opened.close()
    for i in data['uppdateringar']:
        updates.append(i)
    index = len(data['uppdateringar']) - 1 
    total = data['uppdateringar'][index]['summa']
    ny_total = total - payed_amount

    json_data = {'summa': ny_total, 'utgift-typ': f'{purchased}', 'utgift-summa': payed_amount}
    data['uppdateringar'].append(json_data)

    write_json = open("summa.json", "w+")
    write_json.write(json.dumps(data, indent = 4, sort_keys = True))
    write_json.close()


def rakna():
    global purchased, payed_amount
    payed_amount = int(input("Enter the amount you payed: "))
    if payed_amount == 630:
        purchased = "Driving lesson"
    elif payed_amount == 1000:
        purchased = "Risk 1"
    elif payed_amount == 2600:
        purchased = "Risk 2"
    elif payed_amount == 800:
        purchased = "Driving test"
    elif payed_amount == 1200:
        purchased = "Theorylesson"
    elif payed_amount == 400:
        purchased = "Funktion & Kontroll"
    else:
        purchased = "Other expense"

    print("Files have been updated")


def write_to_txt():
    global purchased, payed_amount, ny_total
    f = open("korkort.txt", "a")
    f.write(
        f"Purchade type: {purchased}\nPurchase cost: {payed_amount}\nTotal left: {ny_total}\nDate: {date.today()}\n*********************\n"
    )
    f.close()


def run():
    rakna()
    open_json()
    write_to_txt()

run()