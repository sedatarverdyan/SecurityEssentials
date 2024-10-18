# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
import re

def load_users():
    users = {}
    try:
        with open('gaxtnabarer/nick_password.txt', 'r') as file:
            for line in file:
                nickname, email, password = line.strip().split(',')
                users[nickname] = {'email': email, 'password': password}
    except FileNotFoundError:
        pass  
    return users

users_data = load_users()

check = input('Sign in/Sign up: ')

def valid_mail(email):
    model = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(model, email) is not None

def valid_password():
    password = input("Write your password. Minimum 12 characters, at least one Upper Case, Lower Case, 1 number and 1 symbol: ")
    l, u, n, s = 0, 0, 0, 0
    upercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = r"[!@#$%^&*(),.?\":{}|<>]" 

    if len(password) >= 12:
        for i in password:
            if i in lowercase:
                l += 1
            if i in upercase:
                u += 1
            if i in numbers:
                n += 1
            if re.match(symbols, i):  
                s += 1

    return l >= 1 and u >= 1 and n >= 1 and s >= 1, password  

if check.lower() == 'sign in':
    nick_name = input('Input your nickname: ')
    password = input('Input your password: ')
    
    
    if nick_name in users_data and users_data[nick_name]['password'] == password:
        print(f'Welcome to your account, {nick_name}!')
    else:
        print('Nickname or password is incorrect.')

elif check.lower() == 'sign up':
    nick = input('Write your nickname: ')
    email = input('Write your email: ')
    
    if valid_mail(email):
        if nick not in users_data:  
            password_valid, password = valid_password()
            if password_valid:
               
                users_data[nick] = {'email': email, 'password': password}
                
                with open('gaxtnabarer/nick_password.txt', 'a') as file:
                    file.write(f"{nick},{email},{password}\n")
                    
                print(f'Welcome to your account, {nick}!')
            else:
                print('Password is not valid.')
        else:
            print('This nickname is already taken.')
    else:
        print('This email is not valid. Please try again.')
