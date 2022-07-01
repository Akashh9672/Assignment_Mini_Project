class user:
    def __init__(self,User_Name,User_Number,User_Email,User_Adress,User_Password ):
        self.User_Name=User_Name
        self.User_Number=User_Number
        self.User_Email=User_Email
        self.User_Address=User_Adress
        self.User_Password=User_Password
    def __str__(self):
        return f"User Profile Details: \n Name: {self.User_Name} \n Phone Number:  {self.User_Number} \n Email: {self.User_Email} \n Address: {self.User_Address} "

    def set_User_Name(self,User_Name):
        self.User_Name=User_Name
    def get_User_Name(self):
        return self.User_Name
    def set_User_Number(self,User_Number):
            self.User_Number=User_Number
    def get_User_Number(self):
        return self.User_Number 
    def set_User_Email(self,User_Email):
            self.User_Email=User_Email
    def get_User_Email(self):
        return self.User_Email

    def set_User_Address(self,User_Address):
            self.User_Address=User_Address
    def get_User_Address(self):
        return self.User_Address

    def set_User_Password(self,User_Password):
            self.User_Password=User_Password
    def get_User_Password(self):
        return self.User_Password
        