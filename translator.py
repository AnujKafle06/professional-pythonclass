# Nepali={
#     'school': '',
#     'home': '',
#     'flower':'',
#     'bucket':'',
#     'flag':'',

# }

# print("\t\t\t Nepali translator")
# search= input("Enter the word").lower()
# print(search)
# print("The nepali translator of", search, "is")
# print(Nepali.get(search))

Nepali={
    'school': '',
    'home': '',
    'flower':'',
    'bucket':'',
    'flag':'',

}

print("\t\t\t Nepali bananatranslator")
search= input("Enter the word").lower()
print(search)
print("The nepali bananatranslator of", search, "is")
try:
    print(Nepali(search))
except:
    print("Not found there is not such word that exist",search,"in our bananatranslator")
