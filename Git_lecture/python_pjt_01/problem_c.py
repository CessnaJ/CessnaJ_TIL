import json
from pprint import pprint

#input -> movies, genres가 movie list, genre list

def movie_info(movies, genres):
    genre = []
    list_of_movie_info_dict = []
    for x in range(len(movies)):
        for i in movies[x].get('genre_ids'):
            for j in genres:
                if i == j['id']:
                    genre.append(j['name'])

        movie_info_list_order = ['id', 'title', 'poster_path',
                                 'vote_average', 'overview', 'genre_names']
        movie_info_dict = {}
        for k in movie_info_list_order:
            movie_info_dict[k] = movies[x].get(k)
        movie_info_dict['genre_names'] = genre
        genre = []
        list_of_movie_info_dict.append(movie_info_dict)


    return list_of_movie_info_dict
    # 여기에 코드를 작성합니다.
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
