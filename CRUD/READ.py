import json 
from prettytable import PrettyTable
from pathlib import Path

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
      table.hrules = True

      for g,h in fileGame[i].items() :
         if "judul_game" in g :
            continue
          
         elif "harga" in g :
            continue
         
         table.add_row([g,h])
      
      stringTable = str(table)
      lebar = len(stringTable.split("\n")[0])
      print("=" * lebar)
      print(fileGame[i]["judul_game"].center(lebar))
      print("=" * lebar)
      print(table)
      print("\n")