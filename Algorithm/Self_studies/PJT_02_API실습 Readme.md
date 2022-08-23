# PJT_02_API실습 Readme





## 1. 단계별로 구현과정 중 학습한 내용

- 내가 뭔가를 쓰고싶다면, 그걸 변수 설정하는 '추상화 방식'으로 문제를 해결하는게 더 쉽다. 
  
  

## 2. 어려웠던 부분

- 점수의 order에 맞춰서 다시 영화이름을 순서대로 뽑아내려고 dictionary comprehension, enumerate를 사용하고 key, value의 대응을 서로 바꿔보는 방식을 시도. 하지만 중복값이 있어서 dict가 내 의도대로 만들어지지 않았음.  value가 중복되는 상황에 key, value를 서로 바꾸는걸 시도하면 이전에 선언해준 name error가 뜨면서 dict가 아예 형성이 안되는 문제가 발생했음.

- 그냥 list로 다시 풀어서 해결. 중복되는 vote의 영화는 원 list의 order를 따르기로 했음.

- parameter로 들어가는 dict, url을 맨 위에 몰아서 깔끔하게 정리하려고 했는데, name scaping 규칙 때문에 꼬여서 고치는 방법을 못찾고 결국 싹 지웠습니다.

- 로직은 간단하게 풀어쓰는게 지금 단계에서는 맞는거같습니다.



## 3. 새로 배운 부분

- query 타입을 이용해서 parameter를 받을 수 있다는것.

- try except 사용방법








