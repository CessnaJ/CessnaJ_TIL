import requests
from pprint import pprint

MY_API_KEY = 'c45ff232f6fbb4731afd07f09e5b072b'
URL = f'https://api.themoviedb.org/3/movie/popular?api_key={MY_API_KEY}&language=en-US&page=1'
params = {'url': 'https://api.themoviedb.org/3/movie/popular',
          'api_key': MY_API_KEY,
          'language': 'en-US',
          'page': 1,
          }


#
# def vote_average_movies():
#     page1_result_list = requests.get(url=URL, params=params).json()['results']
#     average_vote_list = []
#     for i in range(len(page1_result_list)):
#         average_vote_list.append(page1_result_list[i])
#     return average_vote_list


# 어떻게 풀것인가? -> page1_result_list는 가지고 있다. 얘네는 그냥 섞여있는 data.
# 이 리스트에서 평점을 뽑아낼 수 있다. 그러면 그거끼리 비교해서 인덱스를 추출할 수 있다. 여기까지 완료!
# 랭킹을 낸다음에 탑 5의 index를 뽑아낸다. .sort() 이용
# 그 인덱스 순서(list에 필요한 index를 넣어준다)를 리스트로 넣어준다. enumerate이용 (make iterable into idx tupled list)
# print하고싶은건 모든걸 다 뽑고 싶은거니까 그 인덱스 순서대로 들어가는 결과리스트를 만든다. 그리고 그걸 return

def ranking():
    page1_result_list = requests.get(url=URL, params=params).json()['results']  # 여러가지로 싸여있는 data를 list로 보여줘야함.
    average_vote_list = []
    sorted_index_vote_corresponding_dict = {}
    for i in range(len(page1_result_list)):
        average_vote_list.append(page1_result_list[i]['vote_average'])

    index_vote_corresponding_dict = {i: j for i, j in enumerate(average_vote_list)}
    sorted_index_vote_corresponding_dict = {k: v for k, v in
                                            sorted(index_vote_corresponding_dict.items(), key=lambda item: item[1])}
    return sorted_index_vote_corresponding_dict


# print(sorted_index_vote_corresponding_dict)

# for i,j in enumerate(average_vote_list):
#     average_vote_list.append([i, j])
# average_vote_list.sort(reverse= True)
# return average_vote_list


# for i in range(len(page1_result_list)):
#     average_vote_list.append(page1_result_list[i]['vote_average'])
# average_vote_list.sort(reverse= True)
# return average_vote_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
