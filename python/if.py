Price = []
AgeGroup = []
AgeGroupName = []
dict_list = {}

itertime = int(input("How many agegroup you want to add:"))
count = 0
if itertime <= 4:
    while count <= itertime:
        AgeGroupName.append(int(input(f"AgeGroupName{count}")))
        AgeGroup.append(int(input(f"AgeGroup{count}:")))
        Price.append(int(input(f"Price{count}:")))
        dict_list.update({AgeGroup[count]:Price[count]:AgeGroupName[count]})
        count = count + 1
    else:
        print("we can only add upto 4.")
    print(dict_list)

# glass1 = "milk"
# glass2 = "pacola"
# tempglass =""

# tempglass = glass1
# glass1 = glass2 
# glass2 = tempglass

# print(tempglass)

