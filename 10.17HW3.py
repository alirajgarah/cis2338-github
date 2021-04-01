#Ali Rajgarah 1586471

class ItemToPurchase:

## default constructor values and atttributes ##
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

## method ##

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" +
              str(self.item_price * self.item_quantity))

if __name__ == '__main__':
    print("Item 1")
    first_item = ItemToPurchase()
    first_item.item_name = input('Enter the item name:\n')
    first_item.item_price = int(input('Enter the item price:\n'))
    first_item.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nItem 2")
    second_item = ItemToPurchase()
    second_item.item_name = input('Enter the item name:\n')
    second_item.item_price = int(input('Enter the item price:\n'))
    second_item.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nTOTAL COST")
    first_item.print_item_cost()
    second_item.print_item_cost()

    total_cost = (first_item.item_price * first_item.item_quantity) + (second_item.item_price * second_item.item_quantity)

    print("\nTotal: $" + str(total_cost))
