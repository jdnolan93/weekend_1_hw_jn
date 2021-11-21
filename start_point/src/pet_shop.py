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




    















