import datetime
import json
# from pathlib import Path

def tambah_game():
    path = "..\DATA\DATA_GAME.json"
    checkDup = 0
    with open(path, "r") as file :
        game = json.load(file)

    try :
     Nama_game = input("masukkan nama Game :")
     for key in game:
         if Nama_game in game[key]["judul_game"] :
            checkDup += 1
     if checkDup > 0 :
        raise ValueError("game sudah ada")
    except ValueError as err :
       print(err)
       return

    tanggal = input("tanggal rilis (yyyy-mm-dd) : ") 
    try :
     harga = int(input("masukkan harga : "))
    except ValueError :
       print("harga hanya perlu angka")
       return
       
    genre = input("masukkan genre : ")
    
    list_genre = genre.split(",")
    
    if len(list_genre[-1]) < 1 :
       del list_genre[-1]
    
    gameBaru = {
       "judul_game" : Nama_game,
       "tahun rilis" : tanggal,
       "harga" : harga,
       "genre" : list_genre
    }

    game[f"A00{len(game) + 1}"] = gameBaru

    with open(path, "w") as newValue :
       json.dump(game, newValue, indent=4)
    
    print(game)