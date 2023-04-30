import random
import string

password_length = 8

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_characters = lowercase + uppercase + digits + symbols

password = ''.join(random.sample(all_characters, password_length))

print(" Your Randomly generated password: ", password)