income_clear = 0
tax_count = 0
tax_ration = 0.13
income_count = 0

def tax_calculator(income_count):
    tax_count = (income_count*tax_ration)
    income_clear = (income_count-tax_count)
    print(f"Доход, до вычета налогов: {income_count:.2f} Налоговый вычет:{tax_count:.2f} Чистый доход:{income_clear:.2f}")
    return 

tax_calculator(float(input("Введите свой доход")))