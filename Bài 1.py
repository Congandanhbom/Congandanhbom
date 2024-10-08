
def find_second_largest(a, b, c):
    if (a > b and a > c):
        return max(b, c)
    elif (b > a and b > c):
        return max(a, c)
    else:
        return max(a, b)
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

print("Số lớn thứ hai là:", find_second_largest(a, b, c))
