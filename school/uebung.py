import random
import string

def blockwoche_3 ():
    
    def generate_password():
    
        allowed_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(allowed_characters) for _ in range(7))
        password += random.choice(string.punctuation)
        return password

    generated_password = generate_password()
    print(generate_password())

print(blockwoche_3())