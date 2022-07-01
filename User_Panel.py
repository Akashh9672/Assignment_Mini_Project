from User_Details import user
from Food_Details import *
from Admin_panel import *
from Food_Details import *
class User_Login:
    User_Name_list=[]
    User_Password_list=[]
    User_list=[]
    Order_list=[]
    Order_History_list=[]

    def user_regestration(self,User_Name,User_Number,User_Email,User_Adress,User_Password):
        user_obj=user(User_Name,User_Number,User_Email,User_Adress,User_Password)
        User_Login.User_list.append(user_obj)
        User_Login.User_Name_list.append(User_Name)
        User_Login.User_Password_list.append(User_Password)
    def User_login(self,username,password):
        flag=False
        for i in User_Login.User_Name_list:
            if i==username:
                flag=True
            else:
                flag=False
        for b in User_Login.User_Password_list:
            if b==password:
                flag=True
            else:
                flag=False
        if flag==True:
            return True
        else:
            return False
    def User_Update(self,User_Name):
        for user in User_Login.User_list:
            print(user)
            if user.User_Name==User_Name:
                user.set_User_Number(int(input("User Number:")))
                user.set_User_Email(input("User Email:"))
                user.set_User_Address(input("Address:"))
                print("updated User",user)

    def Place_Order(self):
        xy=True
        while xy==True:
       
            choice=int(input("Enter \n1. For view Food Menu: \n2. Place Order \n3. View Order Basket\n4.Confirm Order \n5.Back to main menu \n"))
            if choice==1:

                for Foods in Admin_Panel.Food_list:
                    Food_ID=Foods.get_Food_ID()
                    Food_Name=Foods.get_Food_name()
                    Food_Quantity=Foods.get_Food_quantity()
                    Food_Price=Foods.get_Food_price()
                    print(f"{Food_ID}. {Food_Name} ({Food_Quantity} [{Food_Price}])")
            elif choice==2:

                Food_ID=int(input("Enter Your Choice Food:"))
                for Foods in Admin_Panel.Food_list:
                    if Foods.Food_ID==Food_ID:
                        User_Login.Order_list.append(Foods)
            elif choice==3:
                print("************Order List****************")
                for i in User_Login.Order_list:
                    print(i)            
            elif choice==4:
                print("Order Placed Successfully")
                for i in User_Login.Order_list:
                    User_Login.Order_History_list.append(i)
            elif choice==5:
                xy=False
            else:
                print("Invalid Choice")



    def Order_History(self):
        print("******************Your Order History****************")
        for order in User_Login.Order_History_list:
            print(order)
        

