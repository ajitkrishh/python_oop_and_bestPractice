from item import Item

class Phone(Item):

	def __init__(self, name:str ,price :float,quantity : int =0,phone_type:str = "smartphone"):
		super().__init__(
			name,price,quantity
		)

		#  Run validation to the received arguments
		assert phone_type in ("smartphone","telephone","basicphone") , f"{phone_type} type is not defined"

		 #  Assign to self object
		self.phone_type = phone_type

	def __repr__(self):
		return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity},{self.phone_type})"



Phone.instantiate_class("phones.txt")
