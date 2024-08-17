"""
All programming language syntax contains:
1. Sequential: a linear order without parallel processing
2. Branch: an optional algorithm and creating parallel processing
3. Iteration: a repeating order as long as/until the condition is met
"""

# Sequential
print('Mom said, "Go to the store"')
print('Budi answered, "Ok, what should I buy at the store?"')
print('Mom said, "Buy a bottle of milk. If they had eggs, buy six eggs too"')
print("Budi walk to the store")
print("Budi arrives at the store and start to shop")

# Branch
milk_count = 10
egg_count = 10

print("Is there any milk?")
print(f"There are {milk_count} bottles")

if milk_count > 0:
    print("Budi buys a bottle of milk")
else:
    print("Budi do not buy a bottle of milk")

print("Is there any eggs?")
print(f"There are {egg_count} eggs")

if egg_count > 0:
    print("Budi buys 6 eggs")
else:
    print("Budi do not buy eggs")

print("Budi heads home")
print("Budi hands over the shopping items to mom")
