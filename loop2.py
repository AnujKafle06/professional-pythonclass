for num in range(100, 301):
    aternative_num =0
    while num > 0:
        digit = num % 10
        aternative_num += digit if num % 2 ==0 else -digit
        num //= 10
        if aternative_num ==0:
            print(num)