import math

print('Enter the loan principal:')
principal = int(input())

print('''
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
''')
choice = input()

if choice == 'm':
    print('Enter the monthly payment:')
    monthly_pay = int(input())

    print()
    time = math.ceil(principal / monthly_pay)
    if time > 1:
        print('It will take ' + str(time)
              + ' months to repay the loan')
    else:
        print('It will take 1 month to repay the loan')

elif choice == 'p':
    print('Enter the number of months:')
    months_num = int(input())
    monthly_pay = principal / months_num
    remainder = principal % months_num

    print()
    if remainder > 0:
        monthly_pay = math.ceil(monthly_pay)
        last_pay = principal - (months_num - 1) * monthly_pay
        print('Your monthly payment = ', monthly_pay,
              ' and the last payment = ', last_pay, '.',
              sep='')
    else:
        print('Your monthly payment = ', int(monthly_pay))
