



from CRUD.CREATE import tambah_game
from CRUD.READ import tampilkan_game
from CRUD.UPDATE import ubah_data_game
from CRUD.DELETE import hapus_game

from MENU import menu_crud_admin,menu_multi_login,menu_user,menu_autentikasi_user
from AUTENTIKASI import admin_login,user_login,user_regist


# Program Utama

if __name__ == "__main__":
    while True:
        
        menu_dipilih = menu_multi_login()
        match menu_dipilih:
            case "1. Admin":
                admin_login()
                
            case "2. User":
                menu_dipilih = menu_autentikasi_user()
                match menu_dipilih:
                    case "1. Login":
                        user_login()
        
                    case "2. Buat Akun Baru":
                        user_regist()
        
                    case "3. Kembali":
                        break
            

            case "3. Keluar":
                break

        
        
        
    print("=========PROGRAM BERAKHIR=========")
            
        
    
    
