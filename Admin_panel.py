import random
from Food_Details import Food
class Admin_Panel:
    Food_list = []
    def __init__(self):
        pass
    def Admin_login(self,username,password):
            if username == "admin" and password == "admin":
                return True
            return False
          
    def Add_Food(self,Food_ID,Food_name,Food_quantity,Food_price,Food_discount,Food_stock):
        
       
        
        Food_obj=Food(Food_ID,Food_name,Food_quantity,Food_price,Food_discount,Food_stock)
        Admin_Panel.Food_list.append(Food_obj)

    def Edit_Food(self,Food_ID):
         
        for Foods in Admin_Panel.Food_list:
            if Foods.Food_ID==Food_ID:
                    Foods.set_Food_name(input("Food Name:"))
                    Foods.set_Food_quantity(input("Food Quantity:"))
                    Foods.set_Food_price(input("Food Price:"))
                    Foods.set_Food_discount(input("Food Discount:"))
                    Foods.set_Food_stock(input("Food Stock:"))
    
    def View_Food(self):
        print("*****************All Food Details******************")
        for i in range(len(Admin_Panel.Food_list)):
                print(Admin_Panel.Food_list[i])

    def Remove_Food(self,Food_ID):
        found= False
        
        for Foods in Admin_Panel.Food_list:
            if Foods.Food_ID== Food_ID:
                Admin_Panel.Food_list.remove(Foods)
                found= True
        if found==False:
            print("Food Not Found")



