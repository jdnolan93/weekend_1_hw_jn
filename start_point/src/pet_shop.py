def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]

def add_or_remove_cash(total_cash, value_integer):
    total_cash["admin"]["total_cash"] += value_integer
    return total_cash["admin"]["total_cash"]
    

    















