import hashlib


def solve_puzzle(string: str, leading_zeroes: int):
    nonce = 0
    while True:
        nonce_str = str(nonce)
        data = string + nonce_str
        hash_string = hashlib.sha256(data.encode()).hexdigest()
        if hash_string.startswith("0" * leading_zeroes):
            return nonce, hash_value
        nonce += 1


input_string = input('Input some string: ')
input_leading_zeroes = int(input('Input number of leading zeroes:'))

nonce_value, hash_value = solve_puzzle(
    input_string,
    input_leading_zeroes
)

print("Input String:", input_string)
print("Nonce value for which the puzzle is solved:", nonce_value)
print("Generated Hash:", hash_value)
