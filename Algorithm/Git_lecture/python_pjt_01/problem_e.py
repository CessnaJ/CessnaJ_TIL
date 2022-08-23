import json

# movies라는 json(list로 감싸진 dict 형식을 input으로 받는다.)
# 원하는 output은 해당월. 여기서는 그냥 12월이라고 정해놨음.개봉한 영화들의 제목 list
def dec_movies(movies):

    # 여기에 코드를 작성합니다. # 빈 month: title->list형 으로 나와 줄 수 있는 dict를 선언한다. 이렇게 안귀찮게 만드는 방법도 찾아보겠습니다.
    month_title_corresponding_dict = {'01': [],
                                      '02': [],
                                      '03': [],
                                      '04': [],
                                      '05': [],
                                      '06': [],
                                      '07': [],
                                      '08': [],
                                      '09': [],
                                      '10': [],
                                      '11': [],
                                      '12': [],
                                      }
    for i in range(len(movies)):
        id_code = movies[i]['id'] # 세부데이터가 들어있는 파일명이 idcode로 입력되어있으니 for loop으로 열고 할일 마치면 닫아주는걸로 진행한다.
        with open(f'data/movies/{id_code}.json', encoding='utf-8') as specific_movie_data: # 이렇게 해야 메모리를 덜 쓴다. 할 일을 마치면 파일을 닫아줌.
            specific_movie_dict = json.load(specific_movie_data)
            release_month = specific_movie_dict['release_date'][5:7] # datetime 쓰려고 했는데 오류가 나서 일단 데이터의 길이가 통일되어있으니 이렇게 진행.. 추후에 더 고민.
            month_title_corresponding_dict[release_month].append(specific_movie_dict['title']) # release_month : title 해당되는 dict에 loop 돌면서 하나하나 넣어줌.
    return month_title_corresponding_dict['12'] # 12월 해당하는 list value를 반환.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
