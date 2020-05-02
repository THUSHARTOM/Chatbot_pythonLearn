class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{self.name} menu available from {self.start_time} to {self.end_time}".format(self=self)

    def calculate_bill(self, purchased_items):
        total_price = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                total_price += self.items[purchased_item]
        return total_price


class Franchise():

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        available_menu = []
        for menu in self.menus:
            if time in range(menu.start_time, menu.end_time):
                available_menu.append(menu.name)
        return available_menu


class Business():
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# arepas_menu
arepas_menu_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a’ Arepa", arepas_menu_items, 10, 20)

# Brunch Menu
items_brunch = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch = Menu("Brunch", items_brunch, 11, 16)
# print(brunch.calculate_bill(['pancakes','home fries', 'coffee']))

# Early_Bird Menu
items_early_bird = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("Early-bird Dinner", items_early_bird, 15, 18)
# print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

# Dinner Menu
items_dinner = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
                'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00, }
dinner = Menu("Dinner", items_dinner, 17, 23)

# Kids Menu
items_kids = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("Kids", items_kids, 11, 21)

menu = [brunch, early_bird, dinner, kids]

take_a_arepa = Franchise("189 Fitzgerald Avenue", [arepas_menu])

flagship_store = Franchise("1232 West End Road", menu)
new_installment = Franchise("12 East Mulberry Street", menu)
list_franchises = [flagship_store, new_installment]

new_business = Business("Basta Fazoolin' with my Heart", list_franchises)

arepa_business = Business("Take a' Arepa", [take_a_arepa])

print(arepa_business.franchises[0].menus[0])
print(flagship_store)
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))