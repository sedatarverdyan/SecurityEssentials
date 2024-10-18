# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
import random

def set_secret():
    while True:
        try:
            s = int(input("Secret (only number, 5-6 symbols): "))
            if 10000 <= s < 1000000:
                return s
            else:
                print("Please enter a number between 10000 and 999999.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def keys():
    rand = random.Random()
    s = set_secret()
    
    n = int(input("Choose keys count: "))
    keys = [0] * n
    
    for i in range(n - 1):
        keys[i] = rand.randint(100000, 999999)

    keys[n - 1] = keys[0]
    for i in range(1, n - 1):
        keys[n - 1] ^= keys[i]
    keys[n - 1] ^= s
    
    print("\nIt's your keys:")
    for key in keys:
        print(key)
    
    print("\nEnter recovery keys:")
    recover = 0
    for i in range(n):
        
        key = int(input(f"{i + 1} key: "))
        recover ^= key
    
    if recover == s:
        print(f"Secret recovered successfully: {recover}")
    else:
        print("Recovery failed. The keys do not match the secret.")

keys()
