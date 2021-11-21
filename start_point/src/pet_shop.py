def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]

def add_or_remove_cash(total_cash, value_integer):
    total_cash["admin"]["total_cash"] += value_integer
    return total_cash["admin"]["total_cash"]
    
def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(pets_sold, amount):
    pets_sold["admin"]["pets_sold"] += amount
    return pets_sold["admin"]["pets_sold"]

def get_stock_count(stock_count):
    return len(stock_count["pets"])

def get_pets_by_breed(pets, breed):
    breed_amount = []
    for pet in pets["pets"]:
        if pet["breed"] == breed:
            breed_amount.append(pet["breed"])
    return breed_amount

def find_pet_by_name(pets, name):
    for pet in pets["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pets, name):
    delete_pet = None
    delete_pet = find_pet_by_name(pets, name)
    for pet in pets["pets"]:
        if pet["name"] == name:
            delete_pet = pet
    pets["pets"].remove(delete_pet)

def add_pet_to_stock(pets, new_pet):
    pets["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, remove_money):
    customer["cash"] -= remove_money
    return customer["cash"]

def get_customer_pet_count(num_pets):
    return len(num_pets["pets"])

def add_pet_to_customer(customers, new):
    return customers["pets"].append(new)

    












    















