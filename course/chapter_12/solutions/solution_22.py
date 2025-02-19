def check_analysis(**checks):

    goods = list()
    amount = list()
    sum = 0
    ids = list()
    prices = list()
    for id, check in checks.items():
        for item, price in check.items():
            goods.append(item)
            sum += price
        ids.append(id)
        prices.append(sum)
        sum = 0
    mx = max(prices)
    place_id = prices.index(mx)
            
    for check in checks.values():
        for item in check:
            amount.append(goods.count(item))
    mx = max(amount)
    place_item = amount.index(mx)
    
    return (ids[place_id], goods[place_item])
    
    
check_analysis(
    id123={"яблоко": 100, "банан": 50},
    id124={"банан": 50, "апельсин": 70},
    id125={"яблоко": 100, "апельсин": 70}
)
# Ожидается:
# ("id125", "яблоко")