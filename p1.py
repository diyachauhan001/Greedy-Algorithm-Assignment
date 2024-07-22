def max_sum_k_elements(arr, k):
  arr.sort(reverse=True)
  return sum(arr[:k])

arr = [10, 5, 20, 15, 8]
k = 3
max_sum = max_sum_k_elements(arr, k)
print(f"The maximum sum of {k} elements is: {max_sum}")