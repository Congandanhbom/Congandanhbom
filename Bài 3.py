def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Phần 1"
    elif x < 0 and y > 0:
        return "Phần 2"
    elif x < 0 and y < 0:
        return "Phần 3"
    elif x > 0 and y < 0:
        return "Phần 4"
    elif x == 0 and y == 0:
        return "Điểm nằm tại gốc O(0, 0)"
    elif x == 0:
        return "Điểm nằm trên trục tung (y-axis)"
    elif y == 0:
        return "Điểm nằm trên trục hoành (x-axis)"
x = float(input("Nhập hoành độ x: "))
y = float(input("Nhập tung độ y: "))
print(find_quadrant(x, y))
