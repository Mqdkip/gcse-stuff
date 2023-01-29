def currency_converter(inCur,outCur):
    if inCur == "euros":
        euros = int(input("How many euros will you be converting?"))
        if outCur == "pounds":
             e2p = euros * 0.86
             print(f"{euros} euros convert to {e2p} pounds")
        elif outCur == "dollars":
            e2d = euros * 1.08
        print(f"{euros} euros convert to {e2d} dollars")
    if inCur == "dollars":
        dollars = int(input("How many dollars will you be converting?"))
        if outCur == "pounds":
            d2p = dollars * 0.79
            print(f"{dollars} dollars convert to {d2p} pounds")
        elif outCur == "euros":
            d2e = dollars * 0.9
            print(f"{dollars} pounds convert to {d2e} euros")
    if inCur == "pounds":
        pounds = int(input("How many pounds will you be converting?"))
        if outCur == "dollars":
            p2d = pounds * 1.233
            print(f"{pounds} pounds convert to {p2d} dollars")
        elif outCur == "euros":
            p2e = pounds * 1.123
        print(f"{pounds} pounds convert to {p2e} euros")

inCur = input("What currency are you inputting? (euros,pounds,dollars)")
outCur = input("What currency are you outputting? (euros,pounds,dollars)")

currency_converter(inCur,outCur)
