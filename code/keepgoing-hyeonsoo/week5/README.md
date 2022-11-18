# week5

## 16401. 과자나눠주기

결과 : 성공  

무난한 이분탐색 문제였다
조건문의 조건이 맞는 경우에 답을 미리 저장시키는게 포인트였던 것 같다.

```python
# 나눠주는 길이 이분탐색
while start <= end:
    mid = (start + end) // 2
    if cookie_count(mid) >= m:  # 길이 더 키울 수 있음
        res = mid  # 되는 경우에 답 미리 저장
        start = mid + 1
    else:  # 나눠주는 길이 줄여야함
        end = mid - 1

print(res)
```

## 2470. 두 용액

결과 : 실패 후 구글링

너무 어렵게 생각했던 것 같다.
처음에는 combination 을 썼는데 시간초과가 떴고 투포인터로 풀어야 하는 건 감을 잡았는데 결과적으론 못 풀었다.
왼쪽 끝과 오른쪽 끝에 각각 포인터를 잡고 가운데로 수렴하는 방식으로 풀었어야 했다.

```python
while start < end: # 등호 들어가면 안 됨!
    cur_sum = lst[start] + lst[end]

    if abs(cur_sum) < minn:
        cur = [lst[start], lst[end]]
        minn = abs(cur_sum)
        if minn == 0:
            break

    if cur_sum < 0:
        start += 1
    else:
        end -= 1
```

그리고 이 문제는 while 조건절에서 등호가 들어가면 안 된다.
등호를 넣을 시, start 와 end 가 같아질 수 있는데 문제 조건 상 그러면 안 되기 때문이다.

## 1561. 놀이공원

결과 : 실패 후 구글링

개인적으로 너무 어려웠다. 풀이를 봐도 이해를 못 하다가 그림을 그려보고 코드를 따라쳐보니까 이해가 됐다. 그런데 다시 풀라하면 또 틀릴 것 같다.
이분탐색을 통해서 아이들이 모두 한 번씩 타게 되는 최적의 시간 까지는 잘 구했는데 그 다음 처리를 못 했다.
마지막에 아이가 탑승한 놀이기구의 번호를 얻어내는 과정이 꽤나 까다로웠다.

```python
  # (optimal_time - 1) 까지 탑승한 아이들의 숫자 계산
  cur_children = count_children(optimal_time - 1)

  # optimal_time 에 탑승한 아이 계산
  for i in range(m):
      if optimal_time % times[i] == 0:  # optimal_time 에 탑승한 아이
          cur_children += 1
      if cur_children == n:
          print(i + 1)
          break
```

위 부분이 마지막 처리 부분인데 최적의 시간에서 1 을 빼서 그 때까지 탑승한 아이들 수를 구하는 아이디어가 어렵기도 하면서 참신했다.