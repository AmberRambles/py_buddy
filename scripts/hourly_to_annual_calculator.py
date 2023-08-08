'''This program is designed to take an hourly pay rate and convert it to an approximate annual amount.
Uses hourly_pay * 40 hours per week * 52 weeks per year'''
print('This program takes an hourly pay rate and converts it to an approximate annual amount for a full time job.')
hourly_rate = float(input('Please enter the hourly rate of pay: $'))
annual_rate = hourly_rate * 40 * 52
print(f'${hourly_rate:.2f} per hour is approximately ${annual_rate:.2f} per year.')
