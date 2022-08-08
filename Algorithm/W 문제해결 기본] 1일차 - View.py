# 10 번 try. 2칸 옆으로 뚫려있으면 조망권 확보된 집이라고 보는거임. 7 8 10 5 5 이런식이면 옆 2개씩 봐서 가장 크면서,
# 가장 difference 작은 숫자가 들어가게 됨. 그리고, 만약에 가장 큰 뭔가가 나왔다고 치자 그러면 굳이 그 뒤 2개를 셀 필요가 없음.
# list로 일단 변수 N번째 숫자 봤을때 N-2 N-1 N+1 N+2 비교해서 max차이나는거 (list slicing 통해서 해결하면 될듯)

for _ in range(10):
    num_of_house = 0
    min_height_difference = 256
    skip = 0
    view_checking = [-2, -1, 1, 2]
    N = int(input())
    buildings_height_list = list(map(int, input().split()))
    for i in range(N)[2:-2]:

        if min_height_difference != 256:
            skip = 2
            min_height_difference = 256
        if skip != 0:
            skip -= 1
            continue

        height_difference_list =[]
        for j in view_checking:
            height_difference_list += [buildings_height_list[i] - buildings_height_list[i + j]]

        for k in height_difference_list:
            if k < 0:
                min_height_difference = 256
                break
            elif min_height_difference > k:
                min_height_difference = k
        else:
            if min_height_difference != 256:
                num_of_house += min_height_difference

    print(f'#{_ + 1} {num_of_house}')




