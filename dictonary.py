# user_info = {
#     'model' : '2008',
#     'color' : 'black',
#     'make_model' :'2007'
# }
# for i, j in user_info.items():
#     print(i, j)

# user_info.update({
#     'price' : '250,000'
# })
# print(len(user_info))
# # model = user_info.get('model')
# print(user_info)

# print("Welcome to online Car buying we also accept exchange")
# user = input("Enter Attribute of Car that you like")
# car_info={
    
# }

# key = input("Enter desire key")
# value = input("Enter desire value")

# while True:
#      print("Menu:")  # Clearer menu options
#      print("a) Add")
#      print("q) Quit")

#      choose = input("Choose an option (a/q): ").lower()
#      if choose =='a':
#           print(car_info.update())
          

#      elif choose =='q':
#           ("Thanks for the info have a nice day!")
#           break
#      else:
#           ("Invaild please try again later!")
          


# car_info.update(key, value)
# print(car_info)

car_info=[

]
time = int(input("Enter the number"))
for i in range (1, time+1):
    key =input("Enter key")
    val =input("Enter value")
    
    car_info.update({
        key:val
     })
print(car_info)