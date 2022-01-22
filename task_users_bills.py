user_data_table = { 1: ['"Maria"', '"+35987111111"'],
                    2: ['"Ivan"', '"+35987222222"'],
                    3: ['"Asen"', '"+35987333333"']
}

users_bills_table = {1: 25.50, 
                     2: 30.48, 
                     3:  5.98
}

# print table user_data_table
print ('{:>2}|{:>7}|{:>14}'.format('id', 'name', 'number'))
for id, x in user_data_table.items():
    name, number = x
    print('{:>2}|{:>7}|{:>14}'.format(id, name, number))

# print table users_bills_table
print ('{:>2}|{:>7}'.format('id', 'bill'))
for id, z in users_bills_table.items():
    bill = z
    print('{:>2}|{:>7}'.format(id, bill))

#max
bill_val = users_bills_table.values()
bill_max = max(bill_val)
for id, bill in users_bills_table.items():
    if bill == bill_max:
        print("The user with highest bill - {} is {}".format(bill, name))
#min
bill_min = min(bill_val)
for id, bill in users_bills_table.items():
    if bill == bill_min:
        print("The user with lowest bill - {} is {}".format(bill, name))
