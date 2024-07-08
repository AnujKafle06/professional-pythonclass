# fruits = []  # Initialize an empty fruits list

# print("\t\t Welcome, Welcome!")  # Double tab for better formatting

# limit = 10  # Maximum number of fruits (optional)

# while True:
#     print("Menu:")  # Clearer menu options
#     print("a) Add fruit")
#     print("q) Quit")

#     choice = input("Choose an option (a/q): ").lower()

#     if choice == 'a':
#         if len(fruits) < limit or limit == 0:  # Check limit (if set)
#             new_fruit = input("Enter the name of the fruit (lowercase): ").lower()
#             fruits.append(new_fruit)
#             print(f"Fruit added: {new_fruit}")
#         else:
#             print(f"Sorry, the list is full. You can add up to {limit} fruits.")

#     elif choice == 'q':
#         break  # Exit the loop

#     else:
#         print("Invalid choice. Please enter 'a' or 'q'.")

# print("Your fruits list:", ", ".join(fruits) or "No fruits added.")

limit = 2

fruits = []
while  True:
    print("Add the frit you wanna buy")
    print("Press A to Add item and Q to delete")
    choose = input("choose the option:")
    item = input("enter the fruit name")
    print("you have", limit, 'time limit')
    limit = limit - 1
    if limit == 0 :
        break
    if (choose) == 'A':
        fruits.append(item)
        print(fruits)
    elif (choose)== 'Q':
        fruits.remove(item)
        print(fruits)
