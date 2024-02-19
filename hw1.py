name1 = ''

def hello_name(user_name):
    name1 = input('input your user name\n')
    print('Hello' + ' ' + name1)

hello_name(name1)
    

NumList = list(range(1,101)) 

def first_odds(num):
    for num in NumList:
        if num % 2 != 0:
            print(num, end=' ')

first_odds(NumList)

print('\n')

def max_num_in_list(a_list):
    print('The max number is: ')
    print(max(a_list))

max_num_in_list(NumList)

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print('this is a leap year')
        return True
    elif a_year % 100 == 0 and a_year % 400 == 0:
        print('this is a leap year')
        return True
    else:
        print('this is not a leap year')
        return False

year1 = 2024
year2 = 2000
year3 = 1900
year4 = 2023

is_leap_year(year1)
is_leap_year(year2)
is_leap_year(year3)
is_leap_year(year4)

def is_consecutive(a_list):
    return a_list == list(range(min(a_list),max(a_list)+1))

list1 = [1,2,3,4,5]
list2 = [1,2,4,3,6,5]
list3 = [2,6,5,4,7]
list4 = [4,5,6,7,8]

print(is_consecutive(list1))
print(is_consecutive(list2))
print(is_consecutive(list3))
print(is_consecutive(list4))