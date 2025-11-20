# Python Conditions (if, elif, else)
# a = int(input("A: "))
# b = int(input("B: "))
# c = int(input("C: "))

# largest = a
# smallest = a

# # largest check
# if b > largest:  
#     largest = b
# if c > largest:
#     largest = c

# # smallest check
# if b < smallest:
#     smallest = b
# if c < smallest:
#     smallest = c

# print("Largest =", largest)
# print("Smallest =", smallest)

# username = input("Enter username: ")

# valid = True

# # 1. Length must be exactly 12
# if len(username) == 12:
#     print("Invalid: Length must be exactly 12")
#     valid = False

# # 2. Must contain at least one special character
# specials = "@#$%&"
# has_special = False

# for ch in username:
#     if ch in specials:
#         has_special = True

# if has_special == False:
#     print("Invalid: No special character found (@#$%&)")
#     valid = False

# # Final Output
# if valid == True:
#     print("VALID Username")


# items = {
#     "pizza": 120,
#     "coffee": 60,
#     "burger": 90,
#     "tea": 20,
#     "pasta": 3,
#     "momos": 80,
#     "sandwich": 70,
#     "juice": 50,
#     "fries": 40,
#     "icecream": 30
# }

# user_item = input("Enter item name: ").lower()

# available = False

# # checking only with IF
# if user_item in items:
#     available = True

# if available == True:
#     print("Available")
# if available == False:
#     print("Not Available")


# items = {
#     "pizza": 120,
#     "coffee": 60,
#     "burger": 90,
#     "tea": 0,
#     "pasta": 110,
#     "momos": 80,
#     "sandwich": 70,
#     "juice": 50,
#     "fries": 40,
#     "icecream": 30
# }

# user_item = input("Enter item name: ").lower()

# found = False

# # check item available
# if user_item in items:
#     found = True

# # available
# if found == True:
#     print("Available")

# # not available + add item
# if found == False:
#     print("Not Available")
#     items[user_item] = 20
#     print("Added Item:", user_item)


tags = ["@gmail.com"]
name = input("Enter your name: ")
email = name + tags[0]
print("Your Email:", email)
