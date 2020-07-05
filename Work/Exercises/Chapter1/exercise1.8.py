# exercise 1.8 - Dave's mortgage

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
        total_paid = total_paid + payment
        principal = principal * (1+rate/12) - payment
    print('Principal:',principal)
    print('Total paid:',total_paid)
    months = months + 1

print('\nTotal paid:',round(total_paid,2),'Months:',months)

