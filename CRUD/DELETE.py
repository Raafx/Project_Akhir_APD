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

    hapus_input = input("Masukkan nomor game yang ingin dihapus: ")
    try:
        nomor_tampil = int(hapus_input)
        if 1 <= nomor_tampil <= len(game_keys):
            key_asli = game_keys[nomor_tampil - 1]
            game = games[key_asli]

            print(f"\nKamu akan menghapus game: {game['judul_game']} ({game['tahun_rilis']} - {', '.join(game['genre'])})")
            konfirmasi = inquirer.prompt([
                inquirer.List("konfirmasi", message="Konfirmasi penghapusan", choices=["Ya", "Tidak"])
            ])["konfirmasi"]

            if konfirmasi == "Ya":
                del games[key_asli]

                games_baru = {}
                for i, data in enumerate(games.values(), start=1):
                    id_baru = f"A{str(i).zfill(3)}"
                    games_baru[id_baru] = data

                # Simpan ke JSON
                with open(path_json, "w") as file:
                    json.dump(games_baru, file, indent=4)

                sleep(1)
                os.system('cls')
                print("Game berhasil dihapus dan ID diurutkan ulang.")
                sleep(1)
            else:
                print("Penghapusan dibatalkan.")
        else:
            print("Nomor game tidak ditemukan.")
    except:
        print("Input tidak valid. Harus berupa angka.")
        return

    ulang = inquirer.prompt([
        inquirer.List("ulang", message="Hapus game lain?", choices=["Ya", "Tidak"])
    ])["ulang"]
    if ulang == "Ya":
        os.system('cls')
        hapus_game()
    else:
        os.system('cls')
        print("Kembali ke menu utama.")