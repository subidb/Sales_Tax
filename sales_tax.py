import re
from Item import *


def parser(itemlist): #parses the input of the goods and converts the items into python objects with properties/attributes/values
    item_objs_list = [] 
    excempt_prods = ["chocolate","book", "tablets", "pills"]     #list of products that are except from basic sales tax

    for item in itemlist: #parsing the input goods and creating object with properties with the help of Item class
        try: 
            quantity = int(re.match(r"\d+",item).group()) 
            price = float(re.findall(r'\d+\.\d+', item)[-1])
            item_name = re.search(r'\d+(.*?).\d+ *', item).group(1)[:-2]
        
            item1 = Item(item_name, quantity, price) #item class
            if any(word in item for word in excempt_prods):
                item1.excempt = True
            if "imported" in item:        
                item1.imported = True
            item_objs_list.append(item1)
            
        except: 
            return "invalid input" #if the input doesn't match the assumed standard format
            
        
    return item_objs_list #returns the list of item objects after parsing

#inputitemlist     
itemlist1 = ['1 book at 12.49','1 music CD at 14.99', '1 chocolate bar at 0.85'] 
itemlist2 = ['1 imported box of chocolates at 10.00', '1 imported bottle of perfume at 47.50'] 
itemlist3 = ['1 imported bottle of perfume at 27.99', '1 bottle of perfume at 18.99',
             '1 packet of headache pills at 9.75', '1 box of imported chocolates at 11.25']

inputlist = [itemlist1, itemlist2, itemlist3] 

output_receipt = []          
        
for count, itemlist in enumerate(inputlist): 
    
    output_receipt.append("\nOutput {}:\n".format(count+1))
    item_objs_list = parser(itemlist) 

    if type(item_objs_list) is list: #item_objs_list is a list only if the input is valid
        for item in item_objs_list:
            item.sales_tax() 
            item.tax_calc() #member functions of the Item Class to calculate sales tax
            sales_taxes_sum = 0
            total = 0
            
        for item in item_objs_list: #adding up the sales tax sum and total for each item list, adding them to the output list
            
            sales_taxes_sum+=item.tax
            total+= item.price_after_tax
            output_receipt.append(("{}{}: {:.2f}".format(item.quantity, item.name, item.price_after_tax)))
        
        output_receipt.append(("Sales Taxes:{:.2f}".format(sales_taxes_sum)))
        output_receipt.append(("Total:{:.2f}".format(total)))
        output_receipt.append("_______________________________________")
            
        
    else:
        output_receipt.append("\nInput error, could not process")
        output_receipt.append("_______________________________________")

for receipt in output_receipt:
    print(receipt)