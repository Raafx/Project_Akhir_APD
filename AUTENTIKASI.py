from MENU import menu_crud_admin

list_akun_admin = [
    {
    "username":"Rafi",
    "password":"admin034"
    },
    {
    "username":"Bakil",
    "password":"admin044"
    },
    {
    "username":"Ozora",
    "password":"admin034"
    }
                   ]



def admin_login():
    max_percobaan = 5 

    percobaan = 0 

    while percobaan < max_percobaan:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        for akun in list_akun_admin:
            if username == akun["username"] and password == akun["password"]:
                print(f"Selamat datang yang mulia, {username} , Anda berhasil login sebagai admin.")
                menu_crud_admin()
                percobaan = max_percobaan 
                break
        
                
        else:
            percobaan += 1
            print(f"Username atau password salah. Sisa percobaan: {max_percobaan - percobaan}")
            if percobaan == max_percobaan:
                print("Sudah sampai max percobaan. coba lagi nanti.")
                break
                
            

def user_regist():
    pass

def user_login():
    pass