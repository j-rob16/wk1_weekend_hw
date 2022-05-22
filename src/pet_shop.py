def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, price):
    pet_shop["admin"]["total_cash"] += price
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold_pets):
    pet_shop["admin"]["pets_sold"] += sold_pets
    
def get_stock_count(pet_shop):
    stock_count = 0
    for pet in pet_shop["pets"]:
        stock_count += 1
    return stock_count

def get_pets_by_breed(pet_shop, breed):
    found_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_breed.append(pet)
    return found_breed

def find_pet_by_name(pet_shop, name):
    found_pet = []
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            found_pet.append(pet)
    if found_pet:
        return found_pet[0]
    else:
        return None

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    pet_count = []
    for pet in customer["pets"]:
        pet_count.append(pet)
    return len(pet_count)

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    customer_money = get_customer_cash(customer)
    pet_price = new_pet["price"]
    if customer_money >= pet_price:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None:
        if customer_can_afford_pet(customer, pet) == True:
            remove_customer_cash(customer, pet["price"])
            add_or_remove_cash(pet_shop, pet["price"])
            add_pet_to_customer(customer, pet)
            increase_pets_sold(pet_shop, 1)