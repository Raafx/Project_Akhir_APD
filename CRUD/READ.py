import json 
from prettytable import PrettyTable
from pathlib import Path
import math
import os
import datetime

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
      tanggal = datetime.date.fromisoformat(id['tahun_rilis'])

      table.add_row([i, id["judul_game"], tanggal, id["harga"], id["genre"], id["total_terjual"], id["total_pendapatan"] ])
      
   print(table)
   

def ambil_judul_game(koleksi_id, data_game):
    judul_game = []
    for id_game in koleksi_id:
        if id_game in data_game: 
            judul_game.append(data_game[id_game]["judul_game"])
        else:  # kalau ternyata masih ada judul langsung
            judul_game.append(id_game)
    return judul_game

def tampilkan_info_akun(akun_saat_ini):
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    folderUtama = folderSekarang.parent
    path_user = folderUtama / "DATA" / "DATA_USER.json"
    path_game = folderUtama / "DATA" / "DATA_GAME.json" 

    with open(path_user, "r") as file_user:
        data_user = json.load(file_user)
        akun = data_user[akun_saat_ini]

    with open(path_game, "r") as file_game:
        daftar_game = json.load(file_game)

    # Konversi ID ke judul
    koleksi_id = akun.get("koleksi_game", [])
    koleksi_judul = ambil_judul_game(koleksi_id, daftar_game)

    print("===== INFO AKUN =====")
    print(f"Username       : {akun['username']}")
    print(f"Saldo Anda     : Rp. {akun['saldo']}")
    print(f"PIN            : {akun['PIN']}")
    print(f"Game dimiliki  : {', '.join(koleksi_judul) if koleksi_judul else 'Belum ada game'}")
    print("================================\n")
    
    

def tampilkan_game_user():
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    folderUtama = folderSekarang.parent
    path_json = folderUtama / "DATA" / "DATA_GAME.json"

    with open(path_json, "r") as file:
        fileGame = json.load(file)

    table = PrettyTable()
    table.field_names = ["Nama game", "Tahun rilis", "Harga", "Genre"]

    for i in fileGame:
        game = fileGame[i]
        tanggal = datetime.date.fromisoformat(game['tahun_rilis'])
        table.add_row([
            game["judul_game"],
            tanggal,
            f"Rp {game['harga']}",
            ", ".join(game["genre"])
        ])

    print(table)