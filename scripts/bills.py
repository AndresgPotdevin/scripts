def bills(electricity, gas, rent=1162, internet=50, insurance=400):

    andres_school = 300
    andres_car = 240
    andres_car_insurance = 250

    total = electricity + gas + rent + internet + insurance
    individual = (electricity + gas + rent + internet) / 2
    all_bills = individual + andres_school + andres_car
    andres = andres_car + andres_school

    print('''---Bills:---
------------''')
    print(f'House Total Bills: ${total}')
    print(f'Andres House Bills: ${individual}')
    print(f'Andres School & Car: ${andres}')
    print(f'Andres All Bills: ${all_bills}')

#------------------------------------------------------------------------------#
