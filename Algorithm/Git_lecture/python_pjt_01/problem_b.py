import json
from pprint import pprint

def movie_info(movie, genres):
    genre =[] # 빈 리스트 genre를 만든다.
    for i in movie.get('genre_ids'): # movie.json에서 받아온 genre_ids는 iterable한 객체.id 하나씩 넣어준다!
        for j in genres: # genres_list에서 하나씩 대응해준다.
            if i == j['id']: # 대응되는 값 맞으면 append
                genre.append(j['name'])

    movie_info_list_order = ['id', 'title', 'poster_path',
                           'vote_average', 'overview'] # a번 문제꺼 가져옴. 이 순서대로 출력을 원한다.
    movie_info_dict = {}
    for k in movie_info_list_order:
        movie_info_dict[k] = movie.get(k)
    movie_info_dict['genre_names'] = genre # list순서 맞게 dict에 대응해서 뽑아줌.
    return movie_info_dict
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))

# print(genres_list)
# print(movie)

'''
{'genre_names': ['Drama', 'Crime'],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}

'''