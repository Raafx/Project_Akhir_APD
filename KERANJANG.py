import inquirer


def menu_keranjang(id_game,id_akun,data_user):
    user = data_user[id_akun]
    username = user["username"]
    keranjang_user = user["keranjang"]
    
    print(f"================= Keranjang {username} =================")
    
    tampilkan_keranjang(keranjang_user)
    pilih_menu = [inquirer.List(
                "Menu",
                message="Pilih Menu",
                choices=[
                    "1. Lanjutkan Pembayaran",
                    "2. Belanja Game"
                    "3. Hapus Game dari Keranjang",
                    "4. Kembali"]
                )
            ]
    menu_dipilih = inquirer.prompt(pilih_menu)["Menu"]
    
    match menu_dipilih:
        case "1. Lanjutkan Pembayaran":
            pass
        case "2. Belanja Game":
            pass
        case "3. Hapus Game dari Keranjang":
            pass
        case "4. Kembali":
            pass
            
            
    
    
    
    

    
    


def masuk_keranjang(id_game,id_akun,data_user):
    user = data_user[id_akun]
    keranjang_user = user["keranjang"]
    
    keranjang_user.append(id_game)
    user.update({"keranjang":keranjang_user})
    data_user.update({id_akun:user})
    
    print("\n===================== Game Telah Berhasil Ditambahkan di Keranjangmu! =====================\n")
    
def tampilkan_keranjang(keranajang_user):
   
   table = PrettyTable()
   table.field_names = ["Nama game", "tahun rilis", "harga game", "genre"]
   
   for i in keranajang_user :
      id = keranajang_user[i]
      tanggal = datetime.date.fromisoformat(id['tahun_rilis'])

      table.add_row([id["judul_game"], tanggal, id["harga"], id["genre"]])

    
