import datetime
import random

def create_id(num):
    valid_id=[]
    num=int(num)
    while num != 0:
        generated_id = [
        random.randint(1, 6),
        *create_fixed_digits(random.randint(0, 99), 2),
        *create_fixed_digits(random.randint(0, 12), 2),
        *create_fixed_digits(random.randint(0, 31), 2),
        *create_fixed_digits(random.randint(0, 999), 3),]
        generated_id.append(check_number(generated_id))
        if is_date_valid(generated_id):
            generated_id = (''.join([str(foo) for foo in generated_id]))
            valid_id.append(generated_id)
            num -= 1
    return valid_id

def find_ids(text):
    possible_ids = []
    for s in text.split(' '):
        if s.isdigit():
            possible_ids.append(s)
    return possible_ids
def validate_ids(possible_ids):
    real_ids=[]
    for i in possible_ids:
        if len(i) == 11:
            id_numbers = [int(foo) for foo in i]
            if is_date_valid(id_numbers) and id_numbers[-1] == check_number(id_numbers):
                real_ids.append(i)
    return real_ids

def create_fixed_digits(number, digits):
    return [int(i) for i in '{0:0{1}d}'.format(number, digits)]


def checksum_calculator(personnal_id, coeficients):
    ss = 0
    for i in range(len(coeficients)):
        ss += coeficients[i] * personnal_id[i]
    return ss


def check_number(id):
    s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    s2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    ss = checksum_calculator(id, s1)
    if ss % 11 < 10:
        return ss % 11
    else:
        ss = checksum_calculator(id, s2)
        if ss % 11 < 10:
            return ss % 11
        else:
            return 0


def connect_ints(int_list):
    return 10 * int_list[0] + int_list[1]


def is_date_valid(personal_id):
    if personal_id[0] == 1 or personal_id[0] == 2:
        year = 1800
    elif personal_id[0] == 3 or personal_id[0] == 4:
        year = 1900
    elif personal_id[0] == 5 or personal_id[0] == 6:
        year = 2000
    else:
        return False

    year += connect_ints(personal_id[1:3])
    month = connect_ints(personal_id[3:5])
    day = connect_ints(personal_id[5:7])
    try:
        datetime.datetime(int(year), int(month), int(day))
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    while True:
        print("""
    1 - Check if ID(s) are valid 
    2 - Generate a valid ID
    0 - Exit
            """)
        menu = int(input())
        if menu == 1:
            id = input("Enter ID(s) : ")
            possible_ids=find_ids(id)
            real_ids=validate_ids(possible_ids)
            if not real_ids:
                print("No valid IDs entered")
            else:
                print(real_ids,' - are valid ids')
        if menu == 2:
            print("How many IDs do you wish to generate: ")
            num = int(input())
            num2=num
            print('Valid ids: ')
            print(create_id(num2))
        if menu == 0:
            print("Exiting program")
            break
        if menu < 0 or menu > 2:
            print("invalid option")
