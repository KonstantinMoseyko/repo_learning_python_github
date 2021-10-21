# 6_6

from sys import argv
# file append script
with open("bakery.csv", "a", encoding="utf-8") as bakery_sales_append:
    with open("bakery.csv", "r", encoding="utf-8") as bakery_sales_read:
        if str(argv[1:]).strip("[']").replace(".", "").isdigit():
            if "." in str(argv[1:]).strip("[']") and len(str(argv[1:]).strip("[']")) == 6:
                print(str(argv[1:]).strip("[']"), file=bakery_sales_append)
            else:
                print("Введите значение суммы продаж в формате ХХХХ.Х")
        else:
            print(bakery_sales_read.read())
