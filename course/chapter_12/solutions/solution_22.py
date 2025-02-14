def check_analysis(**checks):
    amount = dict()
    for check in checks.values():
        for item in check:
            if item not in amount:
                amount[item] = 1
            else:
                amount[item] += 1
    hwmch = list()
    for kolvo in amount.values():
        hwmch.append(kolvo)
        mx = max(hwmch)
    print(amount)

check_analysis(
    id123={"яблоко": 100, "банан": 50},
    id124={"банан": 50, "апельсин": 70},
    id125={"яблоко": 100, "апельсин": 70}
)
# Ожидается:
# ("id125", "яблоко")