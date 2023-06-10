import random
import secrets
import string

ran_char = ['@', '#', '&', '*']

letter = string.ascii_letters
digit = string.digits
special_Character = random.choice(ran_char)

alphabate = letter + digit + special_Character
password_length = 12

password = ''
for i in range(password_length):
  password += ''.join(secrets.choice(alphabate))

print("Password is ", password)
