# David Gonzalez
# 1630338

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_description = item_description
        self.item_quantity = item_quantity

    def print_item_cost(self):
        s = "{} {} @ ${} = ${}" .format(self.item_name, self.item_price,
                                        self.item_quantity, (self.item_price * self.item_quantity))
        c = self.item_price * self.item_quantity
        return s, c

    def print_item_description(self):
        s = "{}: {}, %d oz." .format(self.item_name, self.item_description, self.item_quantity)
        print(s)
        return s


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self):
        print("ADD ITEM TO CART")
        item_name = str(input("Enter the item name:\n"))
        item_description = str(input("Enter the item description:\n"))
        item_price = int(input("Enter the item price:\n"))
        item_quantity = int(input("Enter the item quantity:\n"))

        self.cart_items.append(ItemToPurchase(item_name, item_quantity, item_price, item_description))

    def remove_item(self):
        print("REMOVE ITEM FROM CART")
        s = str(input("Enter name of item to remove:\n"))
        i = 0
        for item in self.cart_items:
            if item.item_name == s:
                del self.cart_items[i]
                f = True
                break
            else:
                f = False
            i += 1
        if f is False:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self):
        print("CHANGE ITEM QUANTITY")
        n = str(input("Enter the item name:\n"))
        for item in self.cart_items:
            if item.item_name == n:
                q = int(input("Enter the new quantity:\n"))
                item.item_quantity = q
                f = True
                break
            else:
                f = False
        if f is False:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total = 0
        cost = 0
        for item in self.cart_items:
            cost = item.item_quantity * item.item_price
            total += cost
        return total

    def print_total(self):
        total = self.get_cost_of_cart()
        if total == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            self.output()

    def print_description(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print("{}\'s Shopping Cart - {}" .format(self.customer_name, self.current_date), end="\n")
        print()
        print("Item Descriptions", end="\n")
        for item in self.cart_items:
            print("{}: {}" .format(item.item_name, item.item_description))

    def output(self):
        print("OUTPUT SHOPPING CART")
        print("{}\'s Shopping Cart - {}" .format(self.customer_name, self.current_date))
        print("Number of Items:", self.get_num_items_in_cart(), end="\n")
        print()
        total_c = 0
        for item in self.cart_items:
            print("{} {} @ ${} = ${}" .format(item.item_name, item.item_price, item.item_quantity,
                                              (item.item_quantity * item.item_price)), end="\n")
            total_c += item.item_price * item.item_quantity
        if total_c == 0:
            print("SHOPPING CART IS EMPTY\n")

            print("Total: ${}" .format(total_c), end="\n")


def print_menu(c_cart):
    m = ("\nMENU\n"
         "a - Add item to cart\n"
         "r - Remove item from cart\n"
         "c - Change item quantity\n"
         "i - Output items\' descriptions\n"
         "o - Output shopping cart\n"
         "q - Quit\n")

    com = ''
    while com != 'q':
        print(m)
        com = input("Choose an option:\n")

        while (com != 'a' and com != 'o' and com != 'i' and com != 'r'
               and com != 'c' and com != 'q'):
            com = input("Choose an option:\n")

        if com == "a":
            c_cart.add_item()

        elif com == "o":
            c_cart.output()

        elif com == "i":
            c_cart.print_description()

        elif com == "c":
            c_cart.modify_item()

        elif com == "r":
            c_cart.remove_item()


if __name__ == '__main__':
    customer_name = str(input("Enter customer's name:\n"))
    current_date = str(input("Enter today's date:\n"))
    print("\nCustomer name:", customer_name, end="\n")
    print("Today's date:", current_date, end="\n")
    n_cart = ShoppingCart(customer_name, current_date)
    print_menu(n_cart)
