class MenuItems:
    def __init__(self):
        self.items_menu = {}

    def create(self, item, price):
        if item not in self.items_menu:
            self.items_menu[item] = price
            print(f"Item {item} added to the menu")
        else:
            print(f"Item {item} is already in the list") 

    def update(self, item, new_price):
        if item in self.items_menu:
            self.items_menu[item] = new_price
            print(f"Item {item} new price is updated")
        else:
            print(f"Item {item} you are trying to update is not available in the menu")

    def read(self):
        if not self.items_menu:
            print("The menu is empty")
        else:
            print("Menu")
            for item,price in self.items_menu.items():
                print(f"Item {item} : {price}")

    def delete(self, item):
        if item in self.items_menu:
            del self.items_menu[item]
            print(f"{item} is deleted")
        else:
            print(f"{item} is not present to delete")    

menu = MenuItems()
menu.create("Idly" , 15)
menu.create("Dosa" , 12)

menu.read()

menu.delete("Dosa")