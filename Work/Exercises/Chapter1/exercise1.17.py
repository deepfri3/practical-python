# exercise 1.17 - Dave's mortgage

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 1

while principal > 0:
    if months <= 12:
        total_paid = total_paid + (payment+1000.0)
        principal = principal * (1+rate/12) - (payment+1000.0)
    else:
        if principal > payment:
            total_paid = total_paid + payment
            principal = principal * (1+rate/12) - payment
        else:
            principal = 0
    if principal > 0:
        months = months + 1
    print(f'{months} ${total_paid:0.2f} ${principal:0.2f}')

print(f'\nTotal paid: ${total_paid:0.2f}\nMonths: {months}')

