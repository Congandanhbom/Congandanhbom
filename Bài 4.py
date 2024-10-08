from collections import Counter

def find_most_frequent_char(S):
    freq = Counter(S)
    max_freq = max(freq.values())
    most_frequent_chars = [char for char, count in freq.items() if count == max_freq]
    return min(most_frequent_chars)
S = input("Nhập chuỗi S: ")
result = find_most_frequent_char(S)
print(result)
