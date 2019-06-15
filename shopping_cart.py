# shopping_cart.py

import datetime
import os
import json

'''
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
'''
products = [
    {"id":1, "price_per": "item", "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "price_per": "item", "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "price_per": "item", "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "price_per": "item", "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "price_per": "item", "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "price_per": "item", "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "price_per": "item", "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "price_per": "item", "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "price_per": "item", "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "price_per": "item", "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "price_per": "item", "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "price_per": "item", "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "price_per": "item", "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "price_per": "item", "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "price_per": "item", "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "price_per": "item", "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "price_per": "item", "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "price_per": "item", "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "price_per": "item", "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "price_per": "item", "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25},
    {"id":21, "price_per": "pound", "name": "Bananas", "department": "Organic", "aisle": "fruits", "price": 0.79},
    {"id":'7C04L6E8QG', "price_per": "item", "name": "Google Home Mini", "department": "Electronics", "aisle": "Home Automation", "price": 30.00},
    {"id":'052800488625', "price_per": "item", "name": "Lubriderm", "department": "Personal Care", "aisle": "Moisturizer", "price": 4.56},
    {"id":'049022769922', "price_per": "item", "name": "Wexford Notebook", "department": "Stationary", "aisle": "Notebook", "price": 0.56}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


# prompt the checkout clerk to input the identifier of each shopping cart item, one at a time. 
# When the clerk enters DONE, process payment
# If product id is not found, ask the user to add a correct entry

###########################
# CODE
'''
c_var = os.path.join(os.path.dirname(__file__), "..", "data", "common_variable.json")

#with open(c_var) as json_file:  
 #   data = json.load(json_file)

breakpoint()
'''
# rounds the number to 2 decimal digits and adds $ sign to indicate currency
def to_usd(dollar_amt):
    return "${0:,.2f}".format(dollar_amt)

# calculates the tax amount
def calc_tax(product_total):
    tax_percent = 8.73                     # TODO: This is in main script. Can i put it in a different script?
    tax_amt = product_total * tax_percent/100
    return tax_amt

# calculates the grand total
def calc_total_bill_amt(product_total, tax_percent = 8.73):    #TODO:This is in main script. Can i put in in a different script?
    return product_total + (product_total * tax_percent/100)

# Current date logic to print current date and time based on 12 hour scale
def def_date():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d:%I:%M:%S %p")

def def_date_text():
    now = datetime.datetime.now()
    #return now
    return now.strftime("%Y-%m-%d-%I-%M-%S-%f %p")

def validate_prod(prod, available_products = []):
    #available_products = [p["id"] for p in products]
    
    if str(prod) in str(available_products) or prod.lower() == "done":
        return str(prod).lower()


#
#
#    else:
#        error_msg = "You have entered an invalid product id. Enter again or contact the store manager"
#        return error_msg
#         #print("You have entered an invalid product id. Enter again or contact the store manager")


'''
    mapped_prod = [p["id"] for p in products if str(p["id"]) == str(prod)]
    return mapped_prod
'''

# execute the code only when the program is invoked from CLI.
if __name__ == "__main__":
    #breakpoint()
    
    # STEP 1: TAKE INPUTS AND PRINT THEM
    selected_products_item = []
    selected_products_pound = []
    total_price = 0
    #product_ids = [i["id"] for i in products]    # type : LIST, INT. list of all products available. Useful for validation purposes
    product_ids_item = [str(i["id"]) for i in products if i["price_per"] == 'item']
    product_ids_pound = [str(i["id"]) for i in products if i["price_per"] == "pound"]
    consolidate_products_ids = product_ids_item + product_ids_pound
    #breakpoint()


    while True:
        input_id = input("Please input a product identifier:")   #type : STR

        #mapped_prod = validate_prod(input_id, product_ids)
        
        #breakpoint()
        mapped_prod = validate_prod(input_id, consolidate_products_ids)
        #breakpoint()

        #mapped_prod = [list_prod]
        #breakpoint()

        # If the input is valid, do further processing until user enters Done
        # Done signal is case agnostic
        if mapped_prod != None:

            if mapped_prod == "done":
                break
            else:
                if mapped_prod in product_ids_pound:
                    #breakpoint()
                    input_pound = input("Please input the quantity in pounds:")

                    # checks whether the input pound is a valid number
                    try:
                        ip = int(input_pound)
                        prod_dict = {'id' : mapped_prod, 'qty' : int(input_pound)}
                        #prod_dict = {'id' : int(mapped_prod), 'qty' : int(input_pound)}
                        # this step will create list of dictionaties when product requires a qty
                        selected_products_pound.append(prod_dict)
                    except:
                        print("Invalid quantity. Please try again")
                    
                else:
                    selected_products_item.append(mapped_prod)        

            
            #if mapped_prod == "done":
            #    break
            #else:
            #    selected_products.append(mapped_prod)
        
        else:
            print("You have entered an invalid product id. Enter again or contact the store manager")
        
    #breakpoint()
  
    ## this code is working. if function fails, restore this code
    #while True:
    #    input_id = input("Please input a product identifier:")
#
    #    # Validate user input
    #    if str(input_id) in str(product_ids) or input_id.lower() == "done":
#
    #        # If the input is valid, do further processing until user enters Done
    #        # Done signal is case agnostic
    #        if input_id.lower() == "done":
    #            break
    #        else:
    #            selected_products.append(input_id)
    #    else:
    #        print("You have entered an invalid product id. Enter again or contact the store manager")


    print("-------------------------------------------------")
    print("GREEN FOODS GROCERY STORE")       #TODO: This is in main script. Can i put it in a different script
    print("WWW.GREEN-FOODS-GROCERY.COM")     #TODO: This is in main script. Can i put it in a different script. Can i make this a hyperlink
    print("-------------------------------------------------")
    print(f"CHECK OUT AT: {def_date()}")
    print("-------------------------------------------------")
    print("SELECTED PRODUCTS")


    
    # filters empty strings from the list
    #selected_products = selected_products.strip()

    selected_products_item = [p for p in selected_products_item if p.strip() != '']  # type : LIST, STR
    #selected_products_item = list(map(int, selected_products_item))

    #selected_products_pound = [p for p in selected_products_pound if p.strip() != '']  # type : LIST, STR
    #selected_products_pound = list(map(int, selected_products_pound))
    #breakpoint()

    # HANDLE ITEMS
    product_list = []

    for selected_product in selected_products_item:
        product_match = [p for p in products if str(p["id"]).lower() == selected_product]
        #breakpoint()     
        total_price = total_price + product_match[0]['price']
        product_price = to_usd(product_match[0]['price'])
        item = {'name' : product_match[0]['name'], 'price' : product_price}
        product_list.append(item)
        print(f"... {product_match[0]['name']} ({product_price})")
            


    ## HANDLE POUNDS

    for selected_product in selected_products_pound:
        p_id = selected_product["id"]
        p_qty = selected_product["qty"]
        product_match = [p for p in products if str(p["id"]).lower() == p_id]
        #breakpoint()     
        total_price = total_price + product_match[0]['price'] * p_qty
        product_price = to_usd(product_match[0]['price'] * p_qty)
        item = {'name' : product_match[0]['name'], 'price' : product_price}
        product_list.append(item)
        print(f"... {product_match[0]['name']} ({product_price})")


            
    print("-------------------------------------------------")


    #STEP 2: PRINT SUBTOTAL AND GRAND TOTAL

        
    product_tot_amt = to_usd(total_price)
    product_tot_tax = to_usd(calc_tax(total_price))
    product_grand_tot = to_usd(calc_total_bill_amt(total_price))
    print(f"SUBTOTAL = {product_tot_amt}")
    print(f"TAX = {product_tot_tax}")
    print(f"TOTAL = {product_grand_tot}")
    print("-------------------------------------------------")
    print("Thanks, SEE YOU AGAIN SOON!")
    print("-------------------------------------------------")


    file_name = os.path.join(os.getcwd(), "receipts", f"{def_date_text()}.txt")

    with open(file_name, 'w') as file:

        #file.write(print_header())

        file.write("-------------------------------------------------\n")
        file.write("GREEN FOODS GROCERY STORE\n")       #TODO: This is in main script. Can i put it in a different script
        file.write("WWW.GREEN-FOODS-GROCERY.COM\n")     #TODO: This is in main script. Can i put it in a different script. Can i make this a hyperlink
        file.write("-------------------------------------------------\n")
        file.write(f"CHECK OUT AT: {def_date()}\n")
        file.write("-------------------------------------------------\n")
        file.write("SELECTED PRODUCTS\n")    

        for product in product_list:
            file.write(f"... {product['name']} ({product['price']})")
            file.write("\n")
            
        file.write("\n")
        file.write(f"SUBTOTAL = {product_tot_amt}\n")
        file.write(f"TAX = {product_tot_tax}\n")
        file.write(f"TOTAL = {product_grand_tot}\n")
        file.write("-------------------------------------------------\n")
        file.write("Thanks, SEE YOU AGAIN SOON!\n")
        file.write("-------------------------------------------------\n")

        #file.write(print_footer())
    
    #file_name = os.path.join(os.path.dirname(__file__), "..", "receipts", "tt.txt")


''' 
    "my_message.txt" # a relative filepath

    with open(file_name, 'w') as file: # "w" means "open the file for writing" 
        file.write("Hello World")
        file.write("\n")
        file.write("\n")
        file.write("...")
        file.write("\n")
        file.write("\n")
        file.write("Hello Again")

       # gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", "test.txt")
'''

















#TODO: Send email receipt, write email receipt in folder, google sheets input, price and header automation, pound