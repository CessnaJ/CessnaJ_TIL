# 이거 chain식으로 풀어야된다. 이전숫자 base로 그 뒤의 dice의 방향을 맞춰나가는 식.
# 결국 각 dice의 아래쪽이 1번으로 오게 숫자를 정렬시키고,
# 근데 위아래를 정했다고 해서 측면이 정렬되는건 아니다. 4방향 모두 돌아갈 수 있다.
# 다 맞추고 나서 최대 합을 구하는것보다는, 일단 쌓아나가면서 최대가 되는 나머지 숫자를 점점 더해주면 될거같다.
# 그게 계산을 덜한다.
# list의 idx와 value를 한방에 잘 써버리면 예술적으로 가능하겠지만, 나는 enumerate를 써서 좀 더 인간편의성이 높게 풀것이다.
def find_max_num(dice, top_index, bottom_index):
    left_nums = []
    for i, j in enumerate(dice):
        if i in [top_index, bottom_index]:
            pass
        else:
            left_nums.append(j)
    return max(left_nums)



dices = int(input())
dices_in_list = [list(enumerate(map(int, input().split()))) for _ in range(dices)]
top_bottom_idx_corresponding_dict = {0: 5,
                                 1: 3,
                                 2: 4,
                                 3: 1,
                                 4: 2,
                                 5: 0}
dices = int(input())
dices_in_list = [list(map(int, input().split())) for _ in range(dices)]
max_side_sum = 0
top = 0
for i in dices_in_list[0]: # 일단 첫째 dice의 bottom이 뭔지 모르니까 하나씩 넣는것.
    bottom_idx = dices_in_list[0].index(i)
    top_idx = top_bottom_idx_corresponding_dict[bottom_idx]
    while dices:
    if i ==
    for j in dices_in_list[1:]:
        dices -= 1 # 이번 dice에 대한 작업을 마쳤으니까 1개 제거. 0이 되면 while문이 끝난다.
