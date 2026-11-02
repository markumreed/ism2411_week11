# customers.py
# Author: [Your Name]
# Module 11 Lab: Customer Dictionary & Lookup

print("--- Exercise 1 ---")
customer = {
    "name": "Alice", # Key : Value ,
    "Name": "Not-Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
    
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])


print("--- Exercise 2 ---")
customer['phone'] = '555-5555' # Adding a new key-value pair to the dictionary
print(customer)
customer['tier']    = 'platinum' # Updating the value of an existing key
print(customer)
del customer['Name'] # Deleting a key-value pair from the dictionary
print(customer)



# Reflection 1: When I would use .get() and when I would use bracket notation:
#   [2-3 sentences]
#
# Reflection 2: What the Exercise 8 summary reminds me of in Excel, and why
# Python is more useful for large datasets:
#   [2-3 sentences]
