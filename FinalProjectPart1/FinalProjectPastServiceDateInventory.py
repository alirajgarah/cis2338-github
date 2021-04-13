import csv
from datetime import datetime
#importing datetime module for current date##

class RequiredOutput:
    def __init__(self, items_listed):
        self.items_listed = items_listed
        ###creates list to simplify making new files###



    def pastservicedateinventorycsv(self):


        inventoryitems = self.items_listed
        keys = sorted(inventoryitems.keys(), key=lambda x: datetime.strptime(inventoryitems[x]['service_date'], "%m/%d/%Y").date(), reverse=True)
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
                    file.write('{},{},{},{},{},{}\n'.format(id, manufacturer_name, typeof_item, price_ofitem, date_ofservice, list_ifdamaged))


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
    inventory.pastservicedateinventorycsv()


