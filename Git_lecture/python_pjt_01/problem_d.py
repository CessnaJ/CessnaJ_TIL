import json


# movies라는 json에서 뽑아온 list로 감싸진 dict들을 input으로 받아서
# 가장 높은 revenue를 기록한 영화 이름을 뽑아보자!
# index 대응해서 list 뽑고 max씌우면 값나올테니 그 값에 해당하는 index 이름 return해보자!
# revenue는 영화 id코드에 대응하는 파일이름으로 따로 되어있는 json file에서 찾을 수 있다.
def max_revenue(movies):
    name_revenue_corresponding_dict = {}  # 빈 dict 선언

    for i in range(len(movies)):
        id_code = movies[i]['id']  # 세부데이터가 들어있는 파일명이 idcode로 입력되어있으니 for loop으로 열고 할일 마치면 닫아주는걸로 진행한다.
        with open(f'data/movies/{id_code}.json',
                  encoding='utf-8') as specific_movie_data:  # 이렇게 해야 메모리를 덜 쓴다. 할일을 마치면 파일을 닫아줌.
            specific_movie_dict = json.load(specific_movie_data)
            name_revenue_corresponding_dict[id_code] = specific_movie_dict[
                'revenue']  # idcode : revenue 대응되는 dict에 데이터를 넣어준다.
    revenues = list(name_revenue_corresponding_dict.keys())  # dict의 key인 revenue를 뽑아서 list로 만들고 싶다.
    max_value = max(name_revenue_corresponding_dict.keys())  # max값을 찾는다.
    max_revenue_index_order = revenues.index(max_value)  # 순서가 그대로 따라오기 때문에 max값의 index를 받아서 max rev의 idx순서 변수를 만들어준다.
    return movies[max_revenue_index_order]['title']  # 찾은 순서를 이용, 이름을 찾아서 반환해준다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(max_revenue(movies_list))
