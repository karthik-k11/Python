arr = [-1, 0, 1, 2, -1, -4]

arr.sort()

result = []

n = len(arr)

for i in range(n - 2):

    left = i + 1
    right = n - 1

    while left < right:

        total = arr[i] + arr[left] + arr[right]

        if total == 0:

            result.append(
                [arr[i], arr[left], arr[right]]
            )

            left += 1
            right -= 1

        elif total < 0:

            left += 1

        else:

            right -= 1

print(result)