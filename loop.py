# num = int(input("Enter the number:"))
# if num %2 == 0:
#     if num <100:
#         print("Given number is not vaild, check again!")
#     print(f"The number is even{num}")
# else:
#     print(f"The number is odd{num}")

#Extra 
# Get a number from the user
# num = int(input("Enter a number: "))

# # Even numbers have a 0 in the least significant bit position
# even_indicator = num & 1

# # Use string formatting to print result
# print(f"{num} is {'Even' if not even_indicator else 'Odd'}")

#loop 
# for i in range(1,6):
#     for j in range(i):
#         print("*", end="")
#     print("")

#Array in python
# friuts =["apple", "banana", "orange"]

# friuts.append("Mango")
# friuts.insert(3, "grapes")
# print("your list of fruits are:", friuts)
# friuts.remove("apple")
# print("say remove apple no one likes it", friuts)
# print("I likes that more",friuts[0])

#Online shopping
# print("Welcome to fruit store")
# Customer_name = input("Your name")
# print("Choose the fruit you like")
# fruits=["apple", "banana", "orange","grapes","mango"]

# for i in fruits:
#     print("Remove the fruits you don't like")
#     if fruits == i:
#         fruits.remove(i)

# print("Welcome to the fruit store!")
# customer_name = input("What is your name? ")
# print(f"Hello, {customer_name.capitalize()}! Here are our fruits:")

# fruits = ["apple", "banana", "orange", "grapes", "mango"]

# # List all fruits with a single print statement
# print(", ".join(fruits))

# remove_choice = input("\nWould you like to remove any fruits? (y/n) ").lower()

# if remove_choice == 'y':
#     # Use a loop to ask about each fruit
#     for fruit in fruits:
#         remove_fruit = input(f"Do you want to remove {fruit}? (y/n) ").lower()
#         if remove_fruit == 'y':
#             fruits.remove(fruit)  # Remove directly from the list

# print(f"\nOkay, {customer_name.capitalize()}, here's your final selection:")
# print(", ".join(fruits) or "No fruits selected.")
friuts =["apple", "banana", "orange"]

# while True:
#     new_fruits = input("Enter new fruits")
#     new_fruits.append(friuts)
#     print("The fruits you don't like")
#     print(new_fruits)
        
fruits = ["apple", "banana", "orange"]  # Corrected spelling (fruits)

while True:
    new_fruit = input("Enter a new fruit (or 'q' to quit): ").lower()  # Lowercase for case-insensitive input

    if new_fruit == 'q':
        break  # Exit the loop when 'q' is entered

    # Append the new fruit (avoiding the error of appending the entire list)
    fruits.append(new_fruit)
    

    # Enhanced output with a clear message
    print(f"The fruits you have selected so far: {', '.join(fruits)}")

print("Thanks for adding fruits!")


