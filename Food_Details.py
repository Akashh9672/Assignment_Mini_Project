


class Food:
    def __init__(self,Food_ID,Food_name,Food_quantity,Food_price,Food_discount,Food_stock):
        self.Food_ID=Food_ID
        self.Food_name=Food_name
        self.Food_quantity=Food_quantity
        self.Food_price=Food_price
        self.Food_discount=Food_discount
        self.Food_stock=Food_stock
    def __str__(self):
        return f"Food ID : {self.Food_ID} \n Food Name : {self.Food_name} \n Food Quantity : {self.Food_quantity} \n Food Price : {self.Food_price} \n Food Discount : {self.Food_discount} \n Food Stock : {self.Food_stock}"

    def set_Food_ID(self,Food_ID):
        self.Food_ID=Food_ID

    def get_Food_ID(self):
        return self.Food_ID

    def set_Food_name(self,Food_name):
            self.Food_name=Food_name

    def get_Food_name(self):
        return self.Food_name

    def set_Food_quantity(self,Food_quantity):
            self.Food_quantity=Food_quantity

    def get_Food_quantity(self):
        return self.Food_quantity

    def set_Food_price(self,Food_price):
        self.Food_price=Food_price

    def get_Food_price(self):
        return self.Food_price 

    def set_Food_discount(self,Food_discount):
        self.Food_discount=Food_discount

    def get_Food_discount(self):
        return self.Food_discount

    def set_Food_stock(self,Food_stock):
        self.Food_stock=Food_stock

    def get_Food_stock(self):
        return self.Food_stock   

                
            