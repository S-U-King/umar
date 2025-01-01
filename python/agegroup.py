price = []
agegroup = []
dict_list = {}

itertime = int(input("how many agegroup you want to add:"))
count = 0
if itertime <= 4:
    while count <= itertime:
        agegroup.append(input(f"agegroup{count}:"))
        price.append(input(f"price{count}:"))
        dict_list.update({agegroup[count]:price[count]})
        count = count + 1

    else:
        print("we can only add upto 4.")
    print(dict_list)