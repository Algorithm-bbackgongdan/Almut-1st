n = int(input())
arr = list(map(int,input().split()))

arr.sort()

start = 0
end = n-1
result = abs(arr[start] + arr[end])
left = start
right = end
while (start < end):
  temp = arr[start] + arr[end]
  if abs(temp) < result:
    result = abs(temp)
    left = start
    right = end
    if result == 0:
      break
  elif temp > 0:
    end -= 1
  elif temp < 0:
    start += 1

print(arr[left],arr[right])