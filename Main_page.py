from Food_Details import Food
import random
from Admin_panel import Admin_Panel
from User_Panel import User_Login
class main:
    def __init__(self,Admin,User):
        self.User=User
        self.Admin=Admin
    
    def execute(self,choice):

        if choice == 1:
            print("******************Admin Login******************")
            username = input("Enter your username : ")
            password = input("Enter your password : ")
            flag = self.Admin.Admin_login(username,password)
            if flag:
                print("Logged In Successfully!")
                xy=True
                while xy==True:
            

                        choice = int(input("Enter \n1.Add Food \n2.View Food \n3. Edit Food \n4. Remove Food \n5. Back to main menu \n"))
                        if choice==1:
                            print("---------------Add Food------------------")
                            Food_ID=random.randint(1,100)
                            Food_name=input("Food Name:")
                            Food_quantity=input("Food Quantity:")
                            Food_price=int(input("Food Price:"))
                            Food_discount=int(input("Discount:"))
                            Food_stock=input("stock in Hotel:")
                        
                            self.Admin.Add_Food(Food_ID,Food_name,Food_quantity,Food_price,Food_discount,Food_stock)
                        elif choice==2:
                                self.Admin.View_Food()
                        elif choice==3:
                                print("******************Edit Food*****************")
                                Food_ID=int(input("Enter Food ID you want to change: "))
                                self.Admin.Edit_Food(Food_ID)
                        elif choice==4:
                                Food_ID=int(input("Enter Food ID you want Remove:"))
                                self.Admin.Remove_Food(Food_ID)
                        elif choice==5:
                                xy=False
                        else:
                                print("Invalid Choice")
                else:
                        print("Invalid Credintionals")                
        elif choice==2:
                print("*************************User Login******************")
                
                username = input("Enter your username : ")
                password = input("Enter your password : ")
                flag = self.User.User_login(username,password)
                if flag:
                        print("User Login Successful")
                        xy=True
                        while xy==True:

                                n=int(input("Enter \n 1.Place New Order \n 2.Order History \n 3. Update Profile \n 4. Back to main menu \n"))
                                if n==1:
                                        print("**************Place New Order****************")
                                       
                                        User.Place_Order()
                                elif n==2:
                                
                                        User.Order_History()
                                elif n==3:
                                        print("***************Update Profile**************")
                                        User_Name=input("Enter your User Name:")
                                        User.User_Update(User_Name)
                                elif n==4:
                                        xy=False
                                else:
                                        print("Invalid Choice")
                else:
                        print("Invalid Credintionals")
                                                

                                        


        elif choice==3:
                print("***************New User Regestration****************")
                User_Name=input("Enter User Name:")
                User_Number=int(input("Enter Phone Number:"))
                User_Email=input("Enter Email ID:")
                User_Adress=input("Enter Address:")
                User_Password=input("Enter Passwod:")
                self.User.user_regestration(User_Name,User_Number,User_Email,User_Adress,User_Password)

if __name__ == "__main__":
    Admin = Admin_Panel()
    User=User_Login()
    Main = main(Admin,User)
    while True:
        choice = int(input("Login as : \n1.Admin Login \n2.User Login \n3.New User Registration \n"))
        Main.execute(choice=choice)