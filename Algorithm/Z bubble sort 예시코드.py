unsorted_list = [4,3,5246,36,36,854,634,6,73,623,
                 34,35,236,2,37,685,9,696,95,745,999]

def bubble_sort(given_list):
    for j in range(len(given_list)):
        for i in range(len(given_list)-1-j):
            if given_list[i] > given_list[i+1]:
                given_list[i], given_list[i+1] = given_list[i+1], given_list[i]
    return given_list


print(bubble_sort(unsorted_list))

# 1사이클 흘러갈때마다 idx 왼쪽에서 오른쪽으로 탐색해나가면서, 두개씩 비교해서 왼쪽게 더 크면 자리를 swap하는 메커니즘을 사용할것.(len에다가 -1 해주는 이유는 i+1이 idx error가 나오니까)
# 2번째 사이클부터는 가장 큰게 1개씩 오른쪽에 쌓이기 때문에 사이클 반복되면서 최대 idx를 하나씩 감소시켜야한다.

def bubble_sort_internet(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 그냥 처음을 역순으로 꽂아줘서 한계를 두는건 어떨까? 이렇게 됨. 내꺼는 한계를 밑에서 정해주는거고, 찾은 코드는 한계를 위에서 정하고, 밑에서는 idx 따라서 실행만 해주는식.

#clone coding

def mimicing_bubble_sort(given_list):
    for i in range(len(given_list) -1, 0, -1):
        for j in range(i):
            if given_list[i] > given_list[i+1]:
                given_list[i], given_list[i+1] = given_list[i+1], given_list[i]

# 얘는 복원정렬이에요~ O(n^2)