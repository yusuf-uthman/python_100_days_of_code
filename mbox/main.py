import pandas as pd

with open("mbox/data/mbox.txt", "r") as file:
     raw_data = file.read()

data_list = []
for i in raw_data.lower().split(' '):
    if i.find('@') != -1:
        i = i.split(sep=">")[0]
        i = i.split(sep="\n")[0]
        i = i.replace("\\","")
        i = i.replace("<","")
        i = i.replace(";","")        
        data_list.append(i)

exclude_list =[]
for item in data_list:
    if item.find('localhost') != -1:
        exclude_list.append(item)

# remove emails with no username before @ symbol
for i in data_list:
    if i.find('@') != -1:
        at_loc = i.find('@')
        left_at  = i[:at_loc]
        if left_at in "" or left_at in " ":
            exclude_list.append(i)

# remove emails with no string after @ symbol
for i in data_list:
    if i.find('@') != -1:
        at_loc = i.find('@')
        right_at  = i[at_loc:]
        if right_at in "" or right_at in " ":
            exclude_list.append(i)

def clean(my_list, exclusion_list):
    clean_list = []
    for i in my_list:
        if i in exclusion_list:
            continue
        elif i in clean_list:
            continue
        elif len(i) <5:
            continue
        elif '@' not in i:
            continue
        else:
            clean_list.append(i)
    return clean_list

#call the clean function
clean_email = clean(data_list,exclude_list)

df  = pd.DataFrame(clean_email, columns=['email'])
print(df.head(10))

df.to_excel('mbox/data/clean_email.xlsx',index=False)