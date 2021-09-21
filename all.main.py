import requests
import json
import sys
from rich.console import Console
import asyncio

console = Console()
all_data = []

def cari(instansi):
    url = f"https://data-sscasn.bkn.go.id/ujian/list?draw=100&columns%5B0%5D%5Bdata%5D=instansi&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=jenis_pengadaan&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=titik_lokasi&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=alamat&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=mulai&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=selesai&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=0&length=10&search%5Bvalue%5D={instansi}&search%5Bregex%5D=false&_=1631980493298"
    res = requests.get(url)
    return res.json()

def getProvinsi():
	url = "https://emsifa.github.io/api-wilayah-indonesia/api/provinces.json"
	res = requests.get(url)
	for loc in res.json():		
		getKabupatenKota(loc['id'])

def getKabupatenKota(code):
	url = f"https://emsifa.github.io/api-wilayah-indonesia/api/regencies/{code}.json"
	res = requests.get(url)
	for instansi in res.json():
		data = cari(instansi['name'])
		if data['recordsFiltered'] > 0:
			console.print(data['data'])
			all_data.append(data['data'])

getProvinsi()

# saving
with open('data.txt', 'w') as outfile:
    json.dump(all_data, outfile)