import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if not args.payment:
    a_i = float(args.interest)
    i = a_i / (100 * 12)
    principal = float(args.principal)
    periods = float(args.periods)

    monthly_pay = principal * ((i * math.pow(i + 1, periods)) / (math.pow(1 + i, periods) - 1))
    print(f'Your monthly payment = {math.ceil(monthly_pay)}!')
elif not args.principal:
    a_i = float(args.interest)
    i = a_i / (100 * 12)
    payment = float(args.payment)
    periods = float(args.periods)

    principal = payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
    print(f'Your loan principal = {round(principal)}!')
elif not args.periods:
    a_i = float(args.interest)
    i = a_i / (100 * 12)
    principal = float(args.principal)
    payment = float(args.payment)

    periods = math.log(payment / (payment - i * principal), 1 + i)
    periods = math.ceil(periods)
    time_str = ''

    if periods < 12:
        if periods == 1:
            time_str = f'{periods} month'
        else:
            time_str = f'{periods} months'
    else:
        years = periods // 12
        rem_months = periods % 12
        if years == 1:
            if rem_months == 0:
                time_str = f'{years} year'
            elif rem_months == 1:
                time_str = f'{years} year {rem_months} month'
            else:
                time_str = f'{years} year {rem_months} months'
        else:
            if rem_months == 0:
                time_str = f'{years} years'
            elif rem_months == 1:
                time_str = f'{years} years {rem_months} month'
            else:
                time_str = f'{years} years {rem_months} months'

    print(f'It will take {time_str} to repay this loan!')
