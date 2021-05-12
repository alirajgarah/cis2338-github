#Ali Rajgarah 1586471

import csv
from datetime import datetime

class RequiredOutput:
    def __init__(self, items_listed):
        self.items_listed = items_listed
        ###creates list to simplify making new files###


    def fullinventorycsv(self):
        #csv output file###

        with open(r'.\Users\alira\Downloads\FullInventory.csv', 'w') as file:     #### opens full inventory file from my downloads folder#######
            inventoryitems = self.items_listed
#### alphabetically sorted by ####
            keys = sorted(inventoryitems.keys(), key=lambda x: inventoryitems[x]['manufacturer'])  #######items go into keys, which get sorted  by lambda and manufacturer######
            for item in keys:

                ### all keys listed##
                id = item
                manufacturer_name = inventoryitems[item]['manufacturer']
                typeof_item = inventoryitems[item]['typeof_item']
                price_ofitem = inventoryitems[item]['price_ofitem']
                date_ofservice = inventoryitems[item]['date_ofservice']
                list_ifdamaged = inventoryitems[item]['list_ifdamaged']
                #### writes file with id, name, type, price,  and damaged or not ####
                file.write('{},{},{},{},{},{}\n\n'.format(id, manufacturer_name, typeof_item, price_ofitem, date_ofservice, list_ifdamaged))


    def itemtypeinventorylistcsv(self):

        ## csv output file###
        inventoryitems = self.items_listed
        ## creates items based by type##
        types = []

        keys = sorted(inventoryitems.keys())
        for item in inventoryitems:
            typeof_item = inventoryitems[item]['typeof_item']
            if typeof_item not in types:
                types.append(typeof_item)
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open(r'.\Users\alira\Downloads\LaptopInventory.csv' + file_name, 'w') as file:
                for item in keys:

                    id = item
                    manufacturer_name = inventoryitems[item]['manufacturer']
                    price_ofitem = inventoryitems[item]['price_ofitem']
                    date_ofservice = inventoryitems[item]['date_ofservice']
                    list_ifdamaged = inventoryitems[item]['list_ifdamaged']
                    typeof_item = inventoryitems[item]['typeof_item']
                    if type == typeof_item:
                        #### writes file with id, name, type, price,  and damaged or not ####
                        file.write('{},{},{},{},{}\n'.format(id, manufacturer_name, price_ofitem, date_ofservice, list_ifdamaged))

    def pastservicedateinventorycsv(self):

        inventoryitems = self.items_listed
        keys = sorted(inventoryitems.keys(),
                      key=lambda x: datetime.strptime(inventoryitems[x]['service_date'], "%m/%d/%Y").date(),
                      reverse=True)
        with open(r'.C:\Users\alira\Downloads/PastServiceDateInventory.csv', 'w') as file:
            for item in keys:
                id = item
                manufacturer_name = inventoryitems[item]['manufacturer']
                typeof_item = inventoryitems[item]['typeof_item']
                price_ofitem = inventoryitems[item]['price_ofitem']
                date_ofservice = inventoryitems[item]['date_ofservice']
                list_ifdamaged = inventoryitems[item]['list_ifdamaged']
                ### only allows items that are past service date##
                current_date = datetime.now().date()
                past_servicedate = datetime.strptime(date_ofservice, "%m/%d/$Y").date()
                expired_items = past_servicedate < current_date
                ##if those items are expired, write the items to file##
                if expired_items:
                    file.write(
                        '{},{},{},{},{},{}\n'.format(id, manufacturer_name, typeof_item, price_ofitem, date_ofservice,
                                                     list_ifdamaged))


    def damagedinventorycsv(self):


        inventoryitems = self.items_listed
    #sort through keys##
        keys = sorted(inventoryitems.keys(), key=lambda x: inventoryitems[x]['price'], reverse=True)
        ##opens output file and closes it after getting data##
        with open(r'C:\Users\alira\Downloads\DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                manufacturer_name = inventoryitems[item]['manufacturer']
                typeof_item = inventoryitems[item]['typeof_item']
                price_ofitem = inventoryitems[item]['price_ofitem']
                date_ofservice = inventoryitems[item]['date_ofservice']
                list_ifdamaged = inventoryitems[item]['list_ifdamaged']
                #writes items to csv file if damaged##
                if list_ifdamaged:
                    file.write('{},{},{},{},{}\n'.format(id, manufacturer_name, typeof_item, price_ofitem, date_ofservice))


if __name__ == '__main__':
    inventoryitems = {}
    outputfiles = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in outputfiles:
        with open(file, 'r') as csv_file:
            ####opens and reads csv file#####
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                ##if file is manufacturerlist, list following##
                if file == outputfiles[0]:
                    inventoryitems[item_id] = {}

                        ### listed all attributes in output on lines###

                    manufacturer_name = line[1]
                    typeof_item = line[2]
                    list_ifdamaged = line[3]
                    ## cleans up output###
                    inventoryitems[item_id]['manufacturer'] = manufacturer_name.strip()
                    inventoryitems[item_id]['typeof_item'] = typeof_item.strip()
                    inventoryitems[item_id]['list_ifdamaged'] = list_ifdamaged

                    ##if file is pricelist, list following##
                elif file == outputfiles[1]:
                    price_ofitem = line[1]
                    inventoryitems[item_id]['price_ofitem'] = price_ofitem
                    ##if file is servicedateslist, list following##
                elif file == outputfiles[2]:
                    date_ofservice = line[1]
                    inventoryitems[item_id]['date_ofservice'] = date_ofservice


    inventory = RequiredOutput(inventoryitems)
### output file##
    inventory.fullinventorycsv()
    inventory.itemtypeinventorylistcsv()
    inventory.pastservicedateinventorycsv()
    inventory.damagedinventorycsv()

    types = []
    manufacturers = []
    for item in inventoryitems:
        first_man = inventoryitems[item]['manufacturer']
        first_type = inventoryitems[item]['typeof_item']
        if first_man not in types:
            manufacturers.append(first_man)
        if first_type not in types:
            types.append(first_type)

    user_input = None
    while user_input != 'q':
        user_input = input("\nEnter manufacturer and item type:\n")
        if user_input == 'q':

            ## goes through input and looks at any matching item type and manufacturer names
            break
        else:

            second_manname = None
            second_type = None
            user_input = user_input.split()
            error_input = False
            for word in user_input:
                if word in manufacturers:
                    if second_manname:

                        error_input = True
                    else:
                        second_manname = word
                elif word in types:
                    if second_type:

                        error_input = True
                    else:
                        second_type = word

                if not second_manname or not second_type or error_input:
                    print("No such item in inventory")
                else:

                    keys = sorted(inventoryitems.keys(), key=lambda x: inventoryitems[x]['price_ofitem'], reverse=True)

                    ## sees items with same item type and different manufacturer names
                    same_items = []

                    notsameitems = {}
                    for item in keys:
                        if inventoryitems[item]['item_type'] == second_type:

                            today = datetime.now().date()
                            service_date = inventoryitems[item]['service_date']
                            service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                            expired = service_expiration < today
                            if inventoryitems[item]['manufacturer'] == second_manname:
                                if not expired and not inventoryitems[item]['damaged']:
                                    same_items.append((item, inventoryitems[item]))

                                else:
                                    if not expired and not inventoryitems[item]['damaged']:
                                        notsameitems[item] = inventoryitems[item]

                    # output
                    if same_items:
                        item = same_items[0]
                        item_id = item[0]
                        man_name = item[1]['manufacturer']
                        item_type = item[1]['item_type']
                        price = item[1]['price']
                        print("Your item is {}, {}, {}, {}\n".format(item_id, manufacturer_name, typeof_item, price_ofitem))


                        if notsameitems:
                            price_matching = price

                            nearest_item = None
                            near_price = None

                            for item in notsameitems:
                                if near_price == None:
                                    nearest_item = notsameitems[item]
                                    near_price = abs(int(price_matching) - int(notsameitems[item]['price']))
                                    item_id = item
                                    manufacturer_name = notsameitems[item]['manufacturer']
                                    typeof_item = notsameitems[item]['item_type']
                                    price_ofitem = notsameitems[item]['price']

                                    continue

                                difference_inprice = abs(int(price_matching) - int(notsameitems[item]['price']))
                                if difference_inprice < near_price:
                                    nearest_item = item
                                    near_price = difference_inprice
                                    item_id = item
                                    manufacturer_name = notsameitems[item]['manufacturer_name']
                                    typeof_item = notsameitems[item]['typeof_item']
                                    price_ofitem = notsameitems[item]['price_ofitem']

                            print("You may, also consider: {}, {}, {}, {}\n".format(item_id, manufacturer_name, typeof_item, price_ofitem))

                        else:
                            print("No such item in inventory")