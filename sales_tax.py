import re
from Item import *


#inputitemlist     
itemlist1 = ['1 book at 12.49','1 music CD at 14.99', '1 chocolate bar at 0.85'] 
itemlist2 = ['1 imported box of chocolates at 10.00', '1 imported bottle of perfume at 47.50'] 
itemlist3 = ['1 imported bottle of perfume at 27.99', '1 bottle of perfume at 18.99',
             '1 packet of headache pills at 9.75', '1 box of imported chocolates at 11.25']

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

objslist = parser(itemlist1)
print(objslist)