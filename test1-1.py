# Yongdong Xi
import random

def name_a_clone():
    while True:
        decision = input("Name a clone? ")
        name = []
        if decision == "Y":
            clone_num = random.randint(0, 9999)
            while (len(str(clone_num)) + len(str(name))) < 4:
                name.append('0')
                clone_name = name.append(clone_num)
                print('New clone trooper name: CT-{0}'.format(clone_name))
            continue
        if decision == "N":
            break


name_a_clone()
