import json

data = None



def simpan():
    global data

    with open('data/data.json','r') as file:
        cot = json.load(file)
        data = cot
def simpan_barcode():
    global data_barcode
    with open('data/barcode_data.txt','r') as outfile :
        isi = outfile.read()
        data_barcode = isi

