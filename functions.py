from tkinter import messagebox 
import string
import random


def generate_random_password(pwd_length, result):
    ''' Generating Password '''
    str = string.ascii_letters + string.digits + "@#$%*&-_"
    generated_password = ''.join(random.choices(str, k=pwd_length))
    update_password(generated_password, result)

def button_click(var, result):
    ''' Selecting type of Password '''
    user_choice = var.get()
    if user_choice == 1:
        pwd_length = random.randint(6, 8)
    elif user_choice == 2:
        pwd_length = random.randint(9, 12)
    elif user_choice == 3:
        pwd_length = random.randint(13,16)
    else:
        select_warning()
        return
    generated_password = generate_random_password(pwd_length, result)

def update_password(generated_password, result):
    ''' Displaying password on app '''
    result.delete('0','end')
    result.insert(0, generated_password)


def select_warning(): 
    messagebox.showwarning("Warning","Please select one of the option")  