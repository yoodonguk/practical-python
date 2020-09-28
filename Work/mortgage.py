# mortgage.py
#
# Exercise 1.7

principal = 500_000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    months += 1

    principal = principal * (1 + rate/12) - payment
    total_paid += payment

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    

  
    print(f'{months:3d}, {round(total_paid, 2):9.2f}, {round(principal, 2):9.2f}')

if principal < 0:
    total_paid += principal
    print('Last payment', round(payment + principal, 2))

print(f'Total paid {round(total_paid,2)}')
print(f'Months     {months}')