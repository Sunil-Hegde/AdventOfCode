import hashlib

def calculate_md5(input_str):
    md5_hash = hashlib.md5(input_str.encode()).hexdigest()
    return md5_hash

def mine_adventcoin(secret_key):
    number = 1
    while True:
        input_str = secret_key + str(number)
        md5_hash = calculate_md5(input_str)
        
        # Check if the hash starts with at least five zeroes
        if md5_hash.startswith('000000'):
            return number
        
        number += 1

# Replace 'your_secret_key' with your actual secret key
secret_key = 'iwrupvqb'
result = mine_adventcoin(secret_key)

print(f'The lowest number is: {result}')
