
# Complete the function calc_discounted price so that it returns the discounted price.
def calc_discounted_price(start_price):
    if start_price >= 1000 :
        price = start_price*0.8
    elif start_price >= 500 :
        price = start_price*0.9
    else:
        price = start_price
    return(price)


original_prices = [400, 600, 1200, 2400, 1000]

discounted_prices = []
for i in original_prices :
    discounted_prices.append(calc_discounted_price(i))


# Write a loop that goes through all of the prices in the original_prices list
# and prints out a message with the original price and the discount price.
original_prices = [400, 600, 1200, 2400, 1000]
for i in original_prices :
    print(f"The original price was £{i}, the discounted price is £{calc_discounted_price(i)}.")
