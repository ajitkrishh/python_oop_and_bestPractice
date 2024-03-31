class Item:
    discount = 0.2 # 20% off
    all = []

    def __init__(self,name:str ,price :float,quantity : int =0):
        #  Run validation to the received arguments

        assert type(name) == str, "name should be string"
        assert price >= 0 , "price should be greater than 0"
        assert quantity >= 0 ,"quantity should be greater than 0"
       
        #  Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        self.total_price = 0

        self.all.append(self)

    @property
    # Property Decorator : Read-Only Attribute
    def name(self):
        return self.__name

    @property
    # Property Decorator : Read-Only Attribute
    def price(self):
        return self.__price
    
    @name.setter
    def name(self,value):
        if len(value) < 1:
            raise Exception("name length should be grater than 0")
        else:
            self.__name = value

    @price.setter
    def price(self,value):
        if float(value) < 1:
            raise Exception("price should be grater than 0")
        else:
            self.__name = value

    def get_total_price(self):
        self.total_price = self.price * self.quantity

        return self.total_price

    def apply_discount(self):
        self.price = self.price*(1-self.discount)

    @classmethod
    def instantiate_class(cls,filename):
        print(cls,filename)
        with open(filename , 'r') as f:
            # opening file for reading data 
            itemlist = f.readlines()
            
            # reading line by line 
            for itemline in itemlist: 
                # striping "\n" from the line
                itemline = itemline[:-1] 
                # spliting the data string using ',' to get "name" ,"price", "quantity" from string like 
                #  " 'item1',100,12 "
                itemline = itemline.split(",") 

                #  Creating object from the data 
                cls(itemline[0], float(itemline[1]),int(itemline[2]))
                

    @staticmethod
    def get_total_items():
        return len(Item.all)

    def __repr__(self): 
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"



    

# i1=Item("item1", 5,4)
Item.instantiate_class("items.txt")
# print(Item.instantiate_class("items.txt"))
# print(Item.get_total_items())
# print(dir(Item.get_total_items))