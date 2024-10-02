g = int(input())

if g > 100:
    print()
elif g >= 90:
    print("Отлично")
elif g >= 75 and g < 90:
    print("Хорошо")
elif g >= 50 and g < 75:
    print("Удовлетворительно")
elif g >= 0 and g < 50:
    print("Неудовлетворительно")
elif g < 0:
    print()