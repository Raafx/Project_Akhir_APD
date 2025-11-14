import json
from pathlib import Path
from time import sleep
import os
import inquirer
from CRUD.READ import tampilkan_game

def hapus_game():
    
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    folderUtama = folderSekarang.parent
    path_json = folderUtama / "DATA" / "DATA_GAME.json"

    # Load data
    try:
        with open(path_json, "r") as file:
            games = json.load(file)
    except FileNotFoundError:
        print("File DATA_GAME.json tidak ditemukan.")
        return

    if len(games) == 0:
        print("Belum ada game untuk dihapus.")
        return

    game_keys = list(games.keys())

    tampilkan_game()


    id_hapus = input("Masukkan ID game yang ingin dihapus (contoh: A001 DST.): ").upper()

    if id_hapus in games:
        game = games[id_hapus]
        print(f"\nKamu akan menghapus game: {game['judul_game']} ({game['tahun_rilis']} - {', '.join(game['genre'])})")
        konfirmasi = inquirer.prompt([
            inquirer.List("konfirmasi", message="Konfirmasi penghapusan", choices=["Ya", "Tidak"])
        ])["konfirmasi"]

        if konfirmasi == "Ya":
            del games[id_hapus]

            games_baru = {}
            for i, data in enumerate(games.values(), start=1):
                id_baru = f"A{str(i).zfill(3)}"
                games_baru[id_baru] = data

            with open(path_json, "w") as file:
                json.dump(games_baru, file, indent=4)

            sleep(1)
            os.system('cls')
            print("Game berhasil dihapus.")
            sleep(1)
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("ID game tidak ditemukan.")