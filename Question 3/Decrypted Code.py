global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]


    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

# Since sets expunge duplicate entries, I removed the duplicates from the set to make the code look cleaner
my_set = {1, 2, 3, 4, 5}
# Removed the argument passed into the function 'process-numbers() as it is redundant'
result = process_numbers()

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

# Removed 5 from the modify_dict function as it serves no purpose
modify_dict()


def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
# Removed i +=1 for clarity as it is another redundant line of code

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")
    
print(global_variable)
print(my_dict)
print(my_set)