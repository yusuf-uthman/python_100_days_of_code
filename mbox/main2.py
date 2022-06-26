import pandas as pd

with open('data/mbox.txt', 'r') as file:
    raw_data = file.read()

print(dir(raw_data))

email_list = raw_data.split('\n\n\n\n')

# print(email_list)

print(len(email_list))

new_file = []
for i in email_list:
    print(i)
    print("""
    
        Another line Inserted
    
    """)
    new_file.append(i)

print(new_file[:100])    