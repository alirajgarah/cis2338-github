import csv

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
                if_damaged = inventoryitems[item]['list_ifdamaged']
                #### writes file with id, name, type, price,  and damaged or not ####
                file.write('{},{},{},{},{},{}\n\n'.format(id, manufacturer_name, typeof_item, price_ofitem, date_ofservice, if_damaged))




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


