# # # import Shifting_Items.Books
# # # # import Shifting_Items.Cloths.Jeans
# # # # Shifting_Items.Cloths.Jeans.display()
# # # #! To acces a class (MyClass) from books module we have to create a object of it.
# # # b = Shifting_Items.Books.MyClass()
# # # b.bookType()
# # # Shifting_Items.Books.display()
# # from Shifting_Items import Books
# # Books.display()
# from Shifting_Items.Footwears import Flats,Heels
# Flats.display()
# Heels.display()
'''
# To import all the fucntions:
from Shifting_Items.Footwears.Flats import*
'''
from Shifting_Items.Footwears.Flats import display, flat_color,a
display()
flat_color()
print(a)
