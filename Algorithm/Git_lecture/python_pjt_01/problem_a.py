import json
from pprint import pprint


def movie_info(movie):
    movie_info_key_list = ['id', 'title', 'poster_path',
                           'vote_average', 'overview', 'genre_ids'] # 뽑고싶은 순서대로 list를 만들면 for loop에서 순서대로 대응.
    movie_info_dict = {}
    for i in movie_info_key_list:
        movie_info_dict[i] = movie_dict[i] # keylist해당값 : movie_dict에서뽑아온 내가 원하는 키에 대한 value
    return movie_info_dict
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))


# print(movie_dict)