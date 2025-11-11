import json 
from prettytable import PrettyTable
from pathlib import Path
import math

def tampilkan_game():
   lokasiFile = Path(__file__).resolve()
   folderSekarang = lokasiFile.parent
   folderUtama = folderSekarang.parent
   path_json = folderUtama / "DATA" / "DATA_GAME.json"

   with open(path_json, "r") as file :
      fileGame = json.load(file)

   for i in fileGame :
      table = PrettyTable()
      table.field_names = ["Harga", f"Rp {fileGame[i]["harga"]}"]

      for g,h in fileGame[i].items() :
         if "judul_game" in g :
            continue
          
         elif "harga" in g :
            continue
         
         table.add_row([g,h])
      
      stringTable = str(table)
      lebar = len(stringTable.split("\n")[0])
      setengahLebar = ((lebar - len(fileGame[i]["judul_game"]))/2)
      print("=" * math.floor(setengahLebar), end="")
      print(fileGame[i]["judul_game"], end="") 
      print("=" * math.ceil(setengahLebar))
      print(table)

tampilkan_game()