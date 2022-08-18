# 미완성. 다시.

# 문제에서 주어진 방식은 정점의 max 개수가 100개. 각 정점에서 길이 max 2개
# input은 출발node, 목적지 node 순의 경로를
case, routes = map(int, input().split())
input_start_destination_list = list(map(int, input().split()))
start_destination_list = [[]*100]
print(start_destination_list)
stack = []
visited = []
for i in range(len(input_start_destination_list)):
    if not i%2:
        start_destination_list[input_start_destination_list[i]].append(input_start_destination_list[i+1])


print(start_destination_list)
