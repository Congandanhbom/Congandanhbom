def count_subarrays_with_sum_at_most_k(A, k):
    n = len(A)
    count = 0
    start = 0
    current_sum = 0
    
    for end in range(n):
        current_sum += A[end]
        while current_sum > k and start <= end:
            current_sum -= A[start]
            start += 1
        count += (end - start + 1)
    
    return count
A = list(map(int, input("Nhập dãy số A: ").split()))
k = int(input("Nhập giá trị k: "))
result = count_subarrays_with_sum_at_most_k(A, k)
print("Số lượng dãy con có tổng không quá k là:", result)
