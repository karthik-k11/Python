arr = [10, 23, 12, 17]
target = 22

seen = {}

for i in range(len(arr)-1):
    needed = target - arr[i]

    if needed in seen:
        print(seen[needed], i)
        break
    seen[arr[i]] = i