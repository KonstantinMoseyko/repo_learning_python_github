# 6_6

from sys import argv
# file read script
with open("bakery.csv", "r", encoding="utf-8") as bakery_sales_read:
    if 1 < len(argv) < 4 and [ind for ind in argv[1:] if ind.isdigit()]:
        if len(argv) == 3:
            start_val, end_val = map(int, argv[1:])
            result_double_digit = (val for ind, val in enumerate(bakery_sales_read) if start_val - 1 <= ind < end_val)
            print(*result_double_digit)
        else:
            result_single_digit = (val for ind, val in enumerate(bakery_sales_read) if ind >= int(argv[1]) - 1)
            print(*result_single_digit)
    else:
        print(bakery_sales_read.read())

