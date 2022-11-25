import sys

s = sys.stdin.readline().rstrip()
if '-' not in s:
    print(sum(list(map(int, s.split('+')))))
else:
    nums = s.split('-', 1)
    front = sum(
        list(map(int, nums[0].replace('+', ' ').replace('-', ' ').split(' '))))
    back = sum(
        list(map(int, nums[1].replace('+', ' ').replace('-', ' ').split(' '))))
    print(front - back)