# 오늘도 굉장히 의미없는가정 ( 첫번째줄이 가로줄이면 어떻게 하지?)를 생각하며 이상한 뻘짓을 했습니다. 문제를 잘 읽어야합니다. 근데 어차피 이렇게 해도 문제는 풀리니까 그냥 갑니다.
# 상태 / 이동 두가지 상태로 separation. 저는 아예 layer를 하나 더 만들어서 직전 위치를 스탬프로 기록하는 tracer를 만듭니다.
# 우선순위는 옆으로 가는것. 다만, 다시 위로 가야하는 상황에서는 위로 가야하는데 옆으로 가는 우선순위를 무시할 수 있는 로직 (모멘텀이 없다 + 좌우에 뭔가가 있다 + 위에 뭔가가 있다)
# 상황파악을한다 -> 옆으로 움직이던 중이었는지? 위로 가던 중이었는지?
# 옆을 움직이던 중이었으면 계속 갈지, 가던걸 멈추고 위로 가야할지.
# given_ladder = [list(map(int, input().split())) for _ in range(100)]

# 사다리 게임 역순으로 가서, 시작점의 col 좌표 return
# 매 실행마다 좌우 있는지 탐색(좌우를 봤을때 list의 edge를 벗어나면 그쪽은 탐색하지 않는다.)
# 있다면 좌,우로간다.
for _ in range(10):
    case = int(input())
    given_ladder = [list(map(int, input().split())) for _ in range(100)]
    trace_marking = [[0]*100 for _ in range(100)]
    col_count_at_first = 0
    idx_for_first_position = 0
    once_proceed_to_left = False
    once_proceed_to_right = False
    for i in given_ladder[99]: # for loop으로 start 위치 찾기.
        if i == 2:
            row, col = 99, idx_for_first_position
        else:
            idx_for_first_position +=1

    while row != 0: # new_position의 trace를 계속 marking하게 됨. marking한 postion이 row 0가 되면 위치 출력하고 종료할것임.
        if once_proceed_to_left: #왼쪽으로 가던 중이었는지 체크하고 왼쪽이 끝날때까지 계속 이동. (사다리의 가로줄을 탄다는 의미)
            if col!=0 and (given_ladder[row][col - 1] == 1): # 모멘텀 있음 + 옆으로 갈 수 있음.
                col = col - 1
                trace_marking[row][col] = 1 # trace_marking해주는 다른 layer에 기록해줌.
            else: # 모멘텀 있음. 막힘.
                once_proceed_to_left = False # 한번 옆으로 진행이 불가능하게 되면 계속 진행하려는 모멘텀도 없애주기 위함.
        elif once_proceed_to_right: #오른쪽으로 가던 중이었는지 체크하고 왼쪽이 끝날때까지 계속 이동. (사다리의 가로줄을 탄다는 의미)
            if col != 99 and (given_ladder[row][col + 1] == 1): # 모멘텀 있음. + 오른쪽으로 감. col!=99를 and 연산자 왼쪽에 넣어줘야 뒤를 안봐서 index error를 막는다.
                col = col + 1
                trace_marking[row][col] = 1
            else: # 모멘텀 있음 + 막힘
                once_proceed_to_right = False
        else: #가로줄 타던중이 아니었으니.. # 모멘텀 없음. 이걸 처음에 2로 시작하니까 일단 1칸 올려주는 로직 추가해주고, 내가 방금 막! 모멘텀을 없앤건지? 아니면 위로 올라가는거밖에 없어서 모멘텀이 없는건지 구분해줄 필요가 있음.
            if given_ladder[row][col] == 2: # 추적을 해주고 있었으니 그걸 확인해서 1이 있으면 위로 무조건 올리고, 흔적이 없으면 좌우를 탐색해서 움직인다음에 모멘텀을 새로 만들어주면 되지 않을까?
                row = row - 1
                trace_marking[row][col] = 1
            elif col!=0 and col!=99 and ((trace_marking[row][col-1] == 1) or (trace_marking[row][col+1] == 1)): # 기존에 다른 layer에 흔적을 marking하고 있었기때문에 양 옆에 흔적이 있으면 (위 조건문에서 모멘텀이 사라지고, 흔적이 있다면 이제는 위로 올라가야한다는뜻.)
                row = row -1
                trace_marking[row][col] = 1
            elif col!=0 and given_ladder[row][col-1] == 1 and trace_marking[row][col-1] != 1: # 여기서 문제가 발생. 모멘텀없고, col99, 왼쪽에 뭔가 있으면(이미 trace한것.) 다시 왼쪽으로 가는 문제.
                col = col - 1
                trace_marking[row][col] = 1
                once_proceed_to_left = True
            elif col != 99 and given_ladder[row][col+1] == 1 and trace_marking[row][col+1] != 1:
                col = col + 1
                trace_marking[row][col] = 1
                once_proceed_to_right = True
            else:
                row = row - 1
                trace_marking[row][col] = 1
        if row == 0:
            print(f'#{case} {col}')












'''
내 로직.
좌우가 제일 우선이다. (좌우가 있다면 일단 간다!) 그 다음 스텝으로(once moved to left/right direction -> proceed until encountered 0 block. (탐색, 이동))
상/하 중에서는 위로 가는게 우선이다.

current_position
new_position
을 만들어서 끼워넣고 둘을 비교하는 과정을 거친다. 좌우가 없을시 상으로 움직인다.
'''
