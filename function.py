def calculate_discount(amount, price, rate):
    discount_amount= price * rate / 100
    discount_price = price - discount_amount
    return discount_price

default_price = 100
discount_price = calculate_discount(default_price, 10)
print(f"discount price with 10%:${discount_price}")

another_price = 150
specific_discount_price = calculate_discount(another_price, 20)
print(f"Discount price with 20%: ${specific_discount_price}")