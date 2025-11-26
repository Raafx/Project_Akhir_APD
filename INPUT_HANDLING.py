import datetime
def input_string_handling(input_user):
    while True :
      try :
          input_string = input(f"{input_user} : ")
          if input_string == "" or input_string.isspace() :
            raise ValueError("input tidak boleh kosong atau spasi saja")
            
          elif input_string.isdigit() :
            raise ValueError("input tidak boleh nomor saja")
          
      except ValueError as e :
          print(f"input error : {e}")
      else :
          return input_string

      
def input_number_handling(input_user):
   while True :
      try :
         input_integer = int(input(f"{input_user} : "))
         if input_integer < 0 :
           raise ValueError("input nomor harus lebih dari 0")
         
      except ValueError as e :
         print(f"input error : {e}")
         
      else :
         return input_integer

def input_date_handling(input_user) :
 while True :
   tanggal = input(f"{input_user} : ")

   try :
      convert_data = datetime.datetime.strptime(tanggal, "%Y-%m-%d")
      tanggal = convert_data.date()

      if tanggal >= datetime.date.today() :
         raise ValueError("tanggal lebih atau sama dengan hari ini")
      
   except ValueError as e :
      print(f"error : {e}")

   else :
      return tanggal

