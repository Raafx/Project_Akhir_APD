import json
from pathlib import Path
from time import sleep
import os
import inquirer
from CRUD.READ import tampilkan_game

def ubah_data_game():
    # Path ke file JSON
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
        print("Belum ada game untuk diubah.")
        return

    tampilkan_game()

    id_game = input("Masukkan ID game yang ingin diubah (contoh: A001 DST.): ").upper()

    if id_game in games:
        game = games[id_game]
        print(f"\nKamu akan mengubah data game: {game['judul_game']} ({game['tahun_rilis']} - {', '.join(game['genre'])})")

        konfirmasi = inquirer.prompt([
            inquirer.List("konfirmasi", message="Lanjut ubah data?", choices=["Ya", "Tidak"])
        ])["konfirmasi"]

        if konfirmasi == "Ya":
            while True:
                pilihan_data = inquirer.prompt([
                inquirer.List("pilihan_data", message="Pilih bagian data yang ingin diubah", choices=[
                "Judul Game", "Tahun Rilis", "Harga", "Genre"])
                ])["pilihan_data"]

                if pilihan_data == "Judul Game":
                    game["judul_game"] = input("Masukkan judul game baru: ")
                elif pilihan_data == "Tahun Rilis":
                    game["tahun_rilis"] = input("Masukkan tahun rilis baru: ")
                elif pilihan_data == "Harga":
                    try:
                        game["harga"] = int(input("Masukkan harga baru: "))
                    except:
                        print("Input tidak valid. Harga harus berupa angka.")
                        continue
                    
                elif pilihan_data == "Genre":
                    genre_input = input("Masukkan genre baru (pisahkan dengan koma): ")
                    game["genre"] = [g.strip() for g in genre_input.split(",")]
                elif pilihan_data == "Total Terjual":
                    
                    lanjut = inquirer.prompt([
                        inquirer.List("lanjut", message="Ubah bagian lain dari game ini?", choices=["Ya", "Tidak"])
                ])["lanjut"]

                if lanjut == "Tidak":
                    break

            # Simpan perubahan
            games[id_game] = game
            with open(path_json, "w") as file:
                json.dump(games, file, indent=4)

            sleep(1)
            os.system('cls')
            print("Semua perubahan berhasil disimpan.")
            sleep(2)
            os.system('cls')
        else:
            print("Perubahan dibatalkan.")
    else:
        print("ID game tidak ditemukan.")