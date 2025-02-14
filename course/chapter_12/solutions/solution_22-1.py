def check_analysis(**checks):
    items = list()
    for check in checks.values():
        for item in check:
            items.append(item)
    print(items)
check_analysis(
    id123={"яблоко": 100, "банан": 50},
    id124={"банан": 50, "апельсин": 70},
    id125={"яблоко": 100, "апельсин": 70}
)
# Ожидается:
# ("id125", "яблоко")