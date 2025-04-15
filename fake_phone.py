import random

def phone_num():
    with open('./phone_mac.db','r') as file:
        read_db = file.readlines()

    rand_db = (random.choice(read_db)).replace("\n","")
    
    hlt_value = f"{random.randint(0000,9999):04d}"
    user_value = f"{random.randint(0000,9999):04d}"

    while True:
        if(hlt_value == user_value):
            user_value1 = f"{random.randint(0000,9999):04d}"
            user_value = user_value1
        break

    con_val = f"{rand_db}{hlt_value}{user_value}" + "\n"
    return con_val

def times_check():
    while True:
        try:
            num = int(input("Please enter the quantity to be ganerated： \n"))
            if num > 0:
                return num
            else:
                print("ERRPR: Quantity incorrect,please re-enter. \n")
        except ValueError:
            print("ERROR: Illegal numerical value,please enter a number. \n")


if __name__ == "__main__":
    i = 1
    num = times_check()

    with open ('./phones.txt','w') as file:
        for i in range(num):
            write_c=file.writelines(phone_num())