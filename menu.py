class Menu:
    def __init__(self):
        self.data=[]

    def create_menu(self, menu_id, menu_name, items):
        new_menu = {
            "menu_id" : menu_id,
            "menu_name" : menu_name,
            "items" : items
        }    

        self.data.append(new_menu)
        print("New menu is created")

    def read_menu(self, menu_id):
        for menu in self.data:
            if menu["menu_id"] == menu_id:
                print(menu)
        return None

    def update_menu(self, menu_id, menu_name=None, items=None):
        for menu in self.data:
            if menu["menu_id"] == menu_id:
                if menu_name is not None:
                    menu["menu_name"] = menu_name
                if items is not None:
                    menu[:"items"] = items
                print(menu)
            return None

    def delete_menu(self, menu_id):
        for menu in self.data:
            if menu["menu_id"] == menu_id:
                self.data.remove(menu)
                return True
            return False

    def get_all_menus(self):
        for menu in self.data:
            print(menu)


menus = Menu()

