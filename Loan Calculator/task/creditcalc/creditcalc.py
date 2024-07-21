import argparse
import math
import sys


class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print("Incorrect parameters")
        sys.exit(2)


def restricted_range(value):
    if value:
        value = float(value)
        if value < 0:
            print("Incorrect parameters")
            sys.exit(2)
    return value


parser = CustomArgumentParser(description="Advanced interest calculator")

parser.add_argument("--type",
                    choices=["annuity", "diff"],
                    required=True,
                    help="select 'annuity' or 'diff' to calculate")
parser.add_argument("--payment",
                    type=restricted_range,
                    help="specify amount to be paid monthly if "
                         "'annuity' is chosen")
parser.add_argument("--principal",
                    type=restricted_range,
                    help='specify initial loan amount')
parser.add_argument("--periods",
                    type=restricted_range,
                    help="specify the amount of months to be used to "
                         "pay back the loan")
parser.add_argument("--interest",
                    type=restricted_range,
                    help="specify the annual interest rate")

args = parser.parse_args()

if args.interest is None:
    print('Incorrect parameters')
    sys.exit(2)

if args.type == "annuity":
    if not args.payment:
        if args.principal is None or args.periods is None:
            print('Incorrect parameters')
        else:
            a_i = float(args.interest)
            i = a_i / (100 * 12)
            principal = float(args.principal)
            periods = float(args.periods)

            monthly_pay = principal * ((i * math.pow(i + 1, periods)) /
                                       (math.pow(1 + i, periods) - 1))
            monthly_pay = math.ceil(monthly_pay)
            print(f'Your annuity payment = {monthly_pay}!')
            print(f'Overpayment = {int((monthly_pay * periods) - principal)}')
    elif not args.principal:
        if args.payment is None or args.periods is None:
            print('Incorrect parameters')
        else:
            a_i = float(args.interest)
            i = a_i / (100 * 12)
            payment = float(args.payment)
            periods = float(args.periods)

            principal = payment / ((i * math.pow(1 + i, periods)) /
                                   (math.pow(1 + i, periods) - 1))
            principal = math.floor(principal)
            print(f'Your loan principal = {principal}!')
            print(f'Overpayment = {int((payment * periods) - principal)}')
    elif not args.periods:
        if args.principal is None or args.payment is None:
            print('Incorrect parameters')
        else:
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
            print(f'Overpayment = {int((periods * payment) - principal)}')
elif args.type == 'diff':
    if args.payment is not None:
        print('Incorrect parameters')
    elif args.principal is None or args.periods is None:
        print('Incorrect parameters')
    else:
        total = 0
        P = args.principal
        m = 1
        i = args.interest / (100 * 12)
        n = args.periods

        while m <= n:
            current_pay = (P / n) + i * (P - ((P * (m - 1)) / n))
            current_pay = math.ceil(current_pay)
            total += current_pay
            print(f'Month {m}: payment is {current_pay}')
            m += 1

        print()
        print(f'Overpayment = {int(total - P)}')
