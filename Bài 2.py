def count_numbers_with_last_digit(n, d):
    count = 0
    for i in range(d, n, 10):
        count += 1
    return count
n = int(input("Nhập số nguyên dương n: "))
d = int(input("Nhập chữ số cuối cùng d (0 <= d <= 9): "))
result = count_numbers_with_last_digit(n, d)
print(f"Số lượng các số nguyên dương nhỏ hơn {n} và có tận cùng là chữ số {d} là: {result}")
