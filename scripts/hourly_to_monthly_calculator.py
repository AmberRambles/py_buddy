'''This program is designed to take an hourly pay rate and convert it to an approximate monthly amount.
Uses hourly_pay * 40 hours per week * 4 weeks per month'''
print('This program takes an hourly pay rate and converts it to an approximate monthly amount for a full time job.')
hourly_rate = float(input('Please enter the hourly rate of pay: $'))
monthly_rate = hourly_rate * 40 * 4
print(f'${hourly_rate:.2f} per hour is approximately ${monthly_rate:.2f} per month.')
