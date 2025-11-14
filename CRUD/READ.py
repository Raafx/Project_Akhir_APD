import json 
from prettytable import PrettyTable
from pathlib import Path
import math
import os

def tampilkan_game():
   
   lokasiFile = Path(__file__).resolve()
   folderSekarang = lokasiFile.parent
   folderUtama = folderSekarang.parent
   path_json = folderUtama / "DATA" / "DATA_GAME.json"

   with open(path_json, "r") as file :
      fileGame = json.load(file)

   table = PrettyTable()
   table.field_names = ["Id", "Nama game", "tahun rilis", "harga game", "genre", "total terjual", "total pendapatan"]
   
   for i in fileGame :
      id = fileGame[i]

      table.add_row([i, id["judul_game"], id["tahun_rilis"], id["harga"], id["genre"], id["total_terjual"], id["total_pendapatan"] ])
      
   print(table)
   
   kembali = input("Tekan Enter Untuk Kembali: ")
   