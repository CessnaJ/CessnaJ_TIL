# 0720 PYTHON. IF/function/env

## 제어문 (control statement)

- 중첩 조건문.
  
  - if 안에 if를 또 넣어줌.
  - and 라고 생각하면 됨.
  - 윤년계산 예제.

- 조건표현식(Conditional Expression) = 삼항연산자(Ternary Operator)
  
  ```jsx
  (true인 경우 값) if (조건) else (false인 경우 값)
  
  왼참 오거/ 좌참 우거       맞아 조건 틀려
  
  ex)
  value = num if num >= 0 else -num
  ```
  
  - 아래 두 코드는 같은 효과를 지닌다.
  
  ```jsx
  num = 2
  if num % 2:
      result = '홀수'
  else:
      result = '짝수'
  print(result)
  # 어차피 계산의 return값이 0/1로 나뉘니까 그냥 식 그대로 박아버렸음.
  ```
  
  ```jsx
  num = 2
  result = '홀수입니다.' if num % 2 else '짝수입니다.'
  print(result)
  ```
  
  - 이런거 만들때 지난시간에 배웠던 성질 잘 이용해보자
    - Truthy, Falsy한 값들.. () [] {} 0 1

- 반복문
  
  - while loop
    
    - 종료조건에 해당하는 코드를 통해 종료지점을 **반드시** 정해야함. 책에서 배운 recursion의 base case와도 일맥상통
    - 안그러면 무한루프. (base case 설정)
  
  - for loop
    
    - iterable요소를 loop. (**string**, tuple, list, range …)
    
    ```python
    for loop 돌려줄 대상에 list, range만 넣지 말고
    창의적으로 쓸 수 있다는걸 생각해보자.
    
    chars = 'abcdefg'
    for i in chars[2:5]:
        print(i)
    
    for j in my_list[::-1]:
        print(j)
    ```
    
    - 추가 method를 이용한 dict에 for loop
      - keys() →key로 구성된 결과
      - values() →value로 구성된 결과
      - items() → (Key, value)의 튜플로 구성된 결과
    
    ```python
    ex)
    grades = {'john':80, 'eric':90}
    
    for student, grade in grades.items():
            print(student, grade)
    
    결과.
    john, 80
    eric, 90
    ```
    
    - for loop using **enumerate**
      - index와 객체를 쌍으로 담은 **enumerate(열거) tuple**객체를 반환.
  
  ```python
  members = ['민수', '영희', '철수']
  
  for idx, number in enumerate(members):
          print(idx, number)
  
  0, 민수
  1, 영희
  INDEX가 없는 LIST를 받았을 때, INDEX를 넣어서
  뭔가를 표현하고 싶으면 enumerate를 쓴다.
  
  enumerate 자체는 Tuple을 주지만, idx, number 값을 따로 받아서
  print를 해주니까 출력 자체에는 튜플이 안나온다.
  
  enumerate(members, start=1)
  이런식으로 start라는 kwargs에 1을 주면 index가 1부터 시작함.
  ```
  
  - List Comprehension
    
    - iterable에 가공을 한번 더 해줘서 값을 list로 받는 기능.
    
    ```python
    [code for 변수 in iterable]
    [code for 변수 in iterable if 조건식]
    
    # 예시1. 1~3의 3제곱 리스트
    cubic_list =[]
    for number in range(1,4):
            cubic_list.append(number ** 3)
    print(cubic_list)
    
    # 예시2. 이 긴걸 list comprehension을 써서 만들 수 있다.
    cubic_list = [number **3 for number in range(1,4)]
    print(cubic_list)
    ```
  
  - Dictionary Comprehension

```python
cubic_dict ={}

for number in range(1,4):
        cubic_dict[number] = number ** 3
print(cubic_dict)
{1:1, 2:8, 3:27}

cubic_dict = {number: number ** 3 for number in range(1,4)}
원리는 똑같음. 연산하고 싶은거/형식 for 나열할변수 in iterable객체   
```

- 반복문 제어
  
  - break, continue, for-else
  
  - break 반복문 종료.
    
    - for/ while loop 탈출해버림. (여러겹이면 그 겹만 깸)
  
  - continue
    
    - continue **이후 코드는 안읽고, 다음 반복**을 수행.
  
  - **for - else (이거는 다시 공부)**
    
    - 끝까지 반복문을 실행한 이후에 else문 ‘1번’ 실행.
    - **break를 통해 중간에 종료되는경우 else문은 실행 X**
    
    ```python
    for char in 'apple':
            if char == 'b':
                    print('b!')
                    break
    else:
            print('b가 없습니다.')
    # b가 없습니다.
    # if문 조건 만족하는 b가 없으니까 
    # 아래의 print('b'), break는 읽지도 않았으니 else가 마지막에.
    
    for char in 'banana:
            if char == 'b':
                    print('b!')
                    break
    else:
            print('b가 없습니다.')
    # break를 만나게 되면 이 for문 자체가 전체 종료되니까
    # else도 실행이 안됨.
    # break로 중단되었는지 여부를 파악하기 위함.
    ```
  
  - pass
    
    - 아무기능없음. if문이나 밑에 아무것도 안쓰면 에러날까봐 만듬.
    
    ```python
    for i in range(4):
            if i ==2:
                    pass
            print(i)
    0
    1
    2
    3
    
    for i in range(4):
            if i == 2:
                    continue
            print(i)
    0
    1
    3
    ```

  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6556c46a-3de3-4658-9230-9268cc6b4d24/Untitled.png)

- In-Place Operator(복합연산자)
  
  - 연산 + 할당 합쳐둔거.
  - +=, *=, **=, //=, 이런거 다 됨.
  
  Indentation할때 PEP8에서 권장하는 4SPACE 사용하자
  
  찾아보다가 발견한 좋은 선배님 블로그
  
  [](https://yongku.tistory.com/entry/SSAFYcial-%EC%97%AC%EB%8D%9F-%EB%B2%88%EC%A7%B8-%EC%9D%B4%EC%95%BC%EA%B8%B0-SSAFY-1%ED%95%99%EA%B8%B0%EB%A5%BC-%EB%A7%88%EC%B9%98%EB%A9%B0)[https://yongku.tistory.com/entry/SSAFYcial-여덟-번째-이야기-SSAFY-1학기를-마치며](https://yongku.tistory.com/entry/SSAFYcial-%EC%97%AC%EB%8D%9F-%EB%B2%88%EC%A7%B8-%EC%9D%B4%EC%95%BC%EA%B8%B0-SSAFY-1%ED%95%99%EA%B8%B0%EB%A5%BC-%EB%A7%88%EC%B9%98%EB%A9%B0)

# 함수

## 함수 왜 쓰나?

- Decomposition (분해)
  
  - 기능을 분해하고, 재사용을 가능하게 만듬.
  
  ```python
  len([1,2,3])
  이거 어떻게 만들까?
  
  numbers = [1,2,3]
  count = 0
  
  for i in [1,2,3]:
          count += 1
  print(count) # 3
  
  sum([1,2,3])
  이건 어떻게?
  numbers = [1,2,3]
  result = 0
  
  for i in [1,2,3]:
          result += i
  print(result) # 6
  
  평균구하기
  numbers = [1,2,3]
  result = 0
  count = 0
  
  for num in numbers:
          result += num
          count += 1
  print(result/count) # 2.0
  ```

- Abstraction (추상화) - 변수 할당도 추상화의 종류 중 하나다!
  
  - 복잡한 내용을 모르더라도 사용할 수 있도록 (스마트폰처럼!)
  - 재사용성. 가독성. 생산성

## 함수 종류 3개

### 함수란 - 특정한 기능을 하는 코드의 묶음

- 내장함수
  
  - 기본 함수 (python개발자가 만듬)

- 외장함수
  
  - import문을 이용. 외부 라이브러리에서 제공

- 사용자 정의 함수
  
  - 내가 잠깐 쓰려고 만드는거.

## 함수 기본 구조

- 선언, 호출(define & call) - 생성, 사용 관계로으로 생각하면 됨.
- 입력 (input)
- 문서화(Docstring) - 이게 뭐하는건지 설명을 적어둔다.
- 범위(Scope)
- 결과값(Output)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ea23ca03-8156-41aa-9551-e4f085e3974a/Untitled.png)

## 함수의 output

값에 따른 함수의 종류

- Void function
  
  - return값이 없는경우. **None**을 Return하고 종료.

- Value returning function
  
  - 함수 실행 후, return문 통해 값 반환.
  - return을 하게 되면, 값 반환 후 함수가 바로 종료.

### print vs return

- print → 테스트를 위해서 사용. 사용할때마다 값이 출력
  - 출력이 되지만 그 블럭에 “반환”되지는 않는다. None.
- data처리 위해서 return 사용.

```python
#Void function 예시
def void_product(x, y):
        print(f'{x} x {y} = {x * y})

void_product(4,5) ->print 찍어주긴 하지만 함수에 print를 씌우면 None
ans = void_product(4,5)
print(ans) ->None
```

```python
Value returning function 예시
def value_returning_product(x, y):
        return x * y

value_returning_product(4, 5)
ans = value_returning_product(4, 5)
print(ans) # 20 ->return을 했기 때문에 print씌워서 찍어보면 나옴.
```

- 두 개 이상 반환 받고 싶어!

```python
# wrong code
def minus_and_product(x,y):
        return x - y
        return x * y
첫번째 return에서 값 반환하고 func 끝나버림.

# right code
def minus_and_product(x,y):
        return x - y, x * y
# 두개가 tuple형으로 반환된다.
```

- 원론적으로 return은 None 혹은 1개의 값만 반환 가능하다.
  - 그럼 어떻게 해? → container(list, tuple …)에 넣어서 1 덩어리로!

## 함수의 input

- Parameter → 함수 정의(**선언call**)시. 함수 내부에서 사용되는 변수.(만들때)

- Argument → 함수를 **호출def**할 때, 넣어주는 값(쓸 때)
  
  - 필수 args → 필수 변수. 없으면 오류.
  
  - optional args →없어도 됨. 부가기능 위해. (안쓰면 default)
  
  - Positional Arguments →위치에 따라서(순서) 함수 내 전달
  
  - Keyword Arguments →변수이름 특정.(args가 너무 많으면 kw가 낫다.)
    
    - 주의사항⇒ **기본이 Positional argument.**
    
    ```python
    def add(x,y):
            return x + y
    
    add(2, y=5) ->괜찮음.
    add(x=2, 5) error -> 맨 처음에 kwargs쓰면 positional 어긋남. 
    kwargs는 모아서 맨 뒤에 몰아서 쓰자.
    ```
  
  - Default Arguments Values

```python
정의 할 때, default값 넣어준다.
def add(x, y=0):
        return x + y
```

- 정해지지 않은 여러 args 처리.
  
  ```python
  print('hello')
  print('여러개도', '출력이', '될까??')
  
  *(asterisk, Unpacking 연산자를 사용하니까!
  여러개를 받을 수 있게 해놨음.)
  
  몇개를 받을지 모를때 이렇게 정의함.
  def add(*args):
          for arg in args:
                  print(arg)
  ```

- Packing / Unpacking
  
  가변인자 이해 위해서 이해해야함.
  
  - 패킹
    여러개 데이터 묶어서 변수에 할당하는것.
    numbers = (1,2,3,4,5)
    print(numbers) → (1,2,3,4,5)
  
  - 언패킹
    시퀀스 속 요소들을 여러 변수에 나눠 할당하는것.
    numbers = (1,2,3,4,5)
    a, b, c, d, e = numbers # 언패킹
    print(a, b, c, d, e) → 1 2 3 4 5
  
  - 언패킹시 “변수개수” / “할당 요소” 개수 안맞으면 error
  
  - 언패킹시 왼쪽 변수에 asterisk를 붙이면 할당하고 남은 요소를 리스트에 담을 수 있음.

    ```python
    numbers = (1,2,3,4,5) # 패킹
    a, b, *rest = numbers # 1, 2는 a,b에 넣고, 나머지*rest에 넣어
    
    print(a,b, rest) -> 1 2 [3, 4, 5]
    
    a, *rest, e = numbers
    print(rest) -> [2,3,4] 앞에 몇개, 뒤에 몇개 이렇게 할당하고
    가운데만 쫙 해서 rest라는 변수로 묶을 수 있다.
    
    ```

- asterisk와 **가변인자** *는 sequence Unpacking 연산자라고 불리며, 말 그대로 sequence를 풀어헤치는 연산자.

```python
def func(*args):
        print(args)
        print(type(args))

# func(1, 2, 3, 'a', 'b')
# (1, 2, 3, 'a', 'b')
# <class 'tuple'>

def func(a, *args):
        해서 받으면 a에 첫 arg 받아지고 나머지가 튜플로 처리.
```

- **튜플로 받네? 여러개를 한번에 받으면 튜플로 처리하는게 기본.**
  
  ```python
  가변인자 예시2
  
  def sum_all(*numbers):
        result = 0
        for number in numbers:
                result += number
        return result
  
  print(sum_all(1,2,3)) #6 ->numbers라는 튜플로 합쳐져서 for loop
  print(sum_all(1,2,3,4,5,6)) #21
  -> numbers = (1,2,3,4,5,6)이라는 tuple로 합쳐져서 for loop
  
  가변인자 예시3 - 반드시 받아야하는 인자, 추가적인 인자 구분.
  def print_family_name(father, mother, *pets):
        print(f'아버지 : {father}')
        print(f'어머니 : {mother}')
        print('반려동물들..')
        for name in pets:
                print(f'반려동물: {name}')
  ```

- 가변 키워드 인자 (**kwargs)
  
  - 몇개의 kwargs를 받을지 모르는 함수를 정의
  - **kwargs는 dict로 묶여처리됨. 호출 parameter에 **붙여 표현
  
  ```python
  def family(**kwargs):
          for key, value in kwargs.items():
                  print(key, ':', value)
  
  family(father='아버지', mother='어머니', baby='아기')
  # 문자열로 쓰면 안됨.
  
  예시2
  def print_family_name(father, mother, **pets):
          print("아버지 :", father)
          print("어머니 :", mother)
          if pets:
                  print("반려동물들..")
                  for species, name in pets.item():
                          print(f'{species} : {name}')
  print_family_name('아버지', '어머니', dog='멍멍이', cat='냥')
  ```

  가변인자(*args)

  가변키워드인자(**kwargs)

  당연히 동시에 사용 가능하다!!!

```python
def print_family_name(*parents, **pets):
        print("아버지 :", parents[0])
        print("어머니 :", parents[1])
        if pets:
                print("반려동물들..")
                for title, name in pets.items():
                        for title, name in pets.items():
                                print('{} : {}'.format(title, name))
```

### Python의 범위 (Scope)

- Scope는 공간을 말한다.

- 함수”**function**”는 code 내부에 local scope를 생성
  그 외 공간인 global scope로 구분

- scope
  
  - global scope: 코드 어디에서든 참조할 수 있는 공간
  - local scope: 함수가 만든 scope. 함수 내부에서만 참조 가능함.

- variable
  
  - global variable: global scope 범위의 var
  - local variable: local scope 범위의 var

- 변수 수명주기(lifecycle)
  
  - 변수는 각자의 수명주기(lifecycle)이 존재
  1. built-in scope
     파이썬이 실행된 이후부터 영원히 유지되는 scope
  2. global scope
     모듈 호출~ interpreter가 끝날때까지 유지.
  3. local scope
     func CALL시 생성, 종료시 사라짐.(보통 Return만나거나..)

- Python의 이름검색규칙 (Name Resolution)
  
  - 파이썬에서 사용되는 **이름(식별자)들은 이름공간(namespace)에 저장되어있음.**
  
  - 아래같은 순서로 이름을 찾아나가며, LEGB Rule이라 함.
    
    - **L**ocal scope →현재작업
    - **E**nclosed scope (더 상단의 계층을 말함.)
    - **G**lobal scope → 최상단
    - **B**uilt-in scope →모든걸 담고있는 범위 (정의안하고 사용가능한것들..) ⇒print()
    
    내 이해→ 변수 찾아서 처리할때, 점점 1계층씩 밖으로 나가면서 탐색. (코드를 읽어나갈때 위에서 읽는게 아니라 점점 밖계층으로 나간다)
    
    좋은 예시.
    
    ```python
    print(sum) -> <bulit-in function sum>
    print(sum(range(2))) # 1 출력
    
    sum = 5 이렇게 변수할당
    print(sum) ->5 출력
    print(sum(range(2))) 
    # TypeError: 'int' object is not collable
    
    밖 계층으로 점점 찾아나가니까, 위에 sum = 5 가 global로 정의.
    Built-in scope인 sum 내장함수를 찾기전에 그 안에서 정의된거 써버림.
    ```
    
    ```python
    연습문제 ->실행결과는?
    
    a = 0
    b = 1
    def enclosed ():
            a = 10
            c = 3
            def local(C):
                    print(a,b,c) # 10 1 300
            local(300)
            print(a,b,c) # 10 1 3
    encloed()
    print(a,b) # 0 1
    
    '''
    1번째 -> local(C)가 300을 변수로 아예 넣어주니까.
    2번째 -> 이 floor보고, 없으면 한 층 낮게 가서 탐색해보자
    ```
    
    - 궁금증 global a 하면 해당 계층 이하에서 쓸 수 있는건지?
      아니면 모든 계층에서 쓸 수 있는건지?
  
  - global a

```python
주의점
1. 쓰기 전에 global 써서 선언해주고 써야함.
2. parameter에 global사용 불가

a = 10
def func1(a):
        global a # parameter에 global 사용 불가
        a = 3

print(a)
func1(3)
print(a)
```

- nonlocal
  
  - global은 다같이 쓰는거고, global을 하면서 최초로 변수 선언이 가능한데,
  - nonlocal은 이미 존재하는 이름과의 연결만 가능, 1겹만 밖으로 나가서 연결.
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/87c76f78-c7f3-4fe7-94dc-648d30898296/Untitled.png)
  
  ```python
  에러나는거 보여줌.
  def func1():
          global out
          out = 3
  
  func1()
  print(out) # 3 ->얘는 global 이니까 잘됨.
  
  def func1():
          def func2():
                  nonlocal y
                  y = 2
          func2()
          print(y)
  func1()
  
  # SyntaxError: no binding for nonlocal 'y'
  ```

- 함수의 Scope 정리~
  
  - 기본적으로 local scope 함수종료시 사라짐
  - 해당 scope에 변수가 없으면 LEGB 룰 따라 검색
    - 접근(read)는 되지만 더 윗계층에서 수정불가
    - 값을 할당하는 경우 해당 scope의 **이름공간에 새롭게 생성되니까!**
    - **단, 함수 내에서 필요한 상위 scope변수는 arg로 넘겨서 활용할것.**
    - global, nonlocal은 안쓰는거 권장함. 복잡하니까!
      내가 만든적 없는 변수가 쭈루룩 하면서 실행되버림
      왜냐하면 프로그램이 커지면(코드 수천줄) 변수가 한두개가 아니니까
    - 함수로 값 바꾸고 싶으면 argument로 넘기고 return값 쓰는걸 추천함

## 함수 응용! (기본함수들)

- map(function, iterable)
  
  - iterable 개체를 쭉 돌려가면서 fuction에 적용하고 결과를 map object로 반환.
  - 결과 확인은 list() 씌워서 확인해준다.
  - print(map(~~~~~))해버리면 <map object>로만 나오니까!
  
  **다시보기**
  
  ```python
  n, m = map(int, input().split()) # 3 5 입력하면
  # tuple을 활용한 UNPACKING 이용해서 넣어준다!!!!
  ```

- filter(function, iterable)
  
  map이랑 비슷한데, fuction 적용해서 값이 True나오는것들을 filter object로 반환.
  
  ```python
  def odd(n):
          return n % 2
  numbers = [1, 2, 3]
  result = filter(odd, numbers)
  print(result, type(result)) # <filter object at 0x0001313212>
  <class 'filter'>
  print(list(result)) # [1,3]
  
  # number가 filter통해 odd함수를 거쳐서 iterable 객체중 Truthy
  # 값을 반환
  ```

- zip(*iterables)
  
  - iterable 여러개 모아서 tuple을 원소로 하는 zip object 반환.
  
  ```python
  girls = ['jane', 'ashley']
  boys = ['justin', 'eric']
  pair = zip(girls, boys) -># zip object 생성
  
  print(list(pair))
  # [('jane', 'justin'), ('ashley', 'eric')]
  # 이렇게 나옴.
  
  # list로 묶는다고 생각해보면
  # [ ['jane', 'ashley'],
  #        ['justin', 'eric']] 이렇게 2차원 배열이 되서 행렬처럼.
  
  # 근데 zip은 첫번째 항목끼리 묶어서 tuple로 묶어주고,
  # 2번째 항목끼리 묶어서 tuple로 묶어주고.... 이런식으로 변환.
  # 그래서 이렇게 나온다.
  # [('jane', 'justin'), ('ashley', 'eric')]
  ```

- lambda 함수
  lambda [parameter들(list씌우는거 아님. 그냥 변수 나열)] : 표현식
  
  - 표현식(statement)를 계산한 결과를 return하는 함수.
  
  - 이름이 없는 함수여서 ‘익명함수’라고 불림
  
  - 특징
    
    - return문을 가질 수 없음.
    - 간편조건문 외 조건문이나 반복문을 가질 수 없음.
  
  - 장점
    
    - 함수를 정의해서 쓰는거보다 간결
    - def 사용할 수 없는곳에서도 사용가능.
    
    ```python
    # 삼각형 넓이구하기 - def
    def triangle_area(b, h):
            return 0.5 * b * h
    print(triangle_area(5, 6)) ->15.0
    
    # 삼각형 넓이 -람다 lambda
    triangle_area = lambda b, h : 0.5 * b * h
    # 간단한 함수 정의할 때, 1줄로 return 해버린다.
    # 왜? -> 함수 정의하는 이유는 재사용성인데 한번 쓰고 버릴거.
    print(triangle_area(5,6)
    ```

### Recursive function(재귀)

- 자기자신을 호출

- 무한 안되게 설계. 알고리즘 설계/구현에서 유용
  
  - recursive funct로 표현하기 쉬운경우 →점화식
  - 변수사용 줄고 가독성 UP

- 1개 이상의 Base case(자기자신 호출 안하는 경우)가 존재.
  base case로 수렴하도록 작성

- 메모리스택 넘치면(stack overflow) 프로그램 동작X

- 파이썬 최대 재귀깊이(max recursion depth) 1000번.→넘으면 Recursion Error

- 왜 쓰나?
  
  - 재귀가 자연스러울 때 있음. (의식의 흐름으로 코드 짤 때) →번지고 번지고 하는 문제
  - 변수사용 줄여줌
  - 기본적으로 while문을 쓸 수 있다는게 recursion을 쓸 수 있다는 뜻임. (while도 반복조건을 달거고, recursion도 base case제외하면 반복이니..)
    - but, 입력값 커질수록 연산속도 오래걸림( stack처럼 완전히 끝날때까지 함수가 중첩되서 계속 동작하고 있으니까. 메모리 엄청 먹음.)
  - FACTORIAL WHILE문으로 재정의해보는게 과제!

### Module(모듈)

- 다양한 기능을 하나의 파일로 모은것!

### Package(패키지)

- 다양한 파일을 하나의 폴더로!

### Library(라이브러리)

- 다양한 패키지를 하나의 묶음으로!
- **VS Framework ?? buzzword다. 딱 자르기 애매한거.**
  - 주도권이 누구한테 있나?→ 내가 자유롭게 가져다가 여기저기 쓰는게 라이브러리
    Framework는 규칙을 정해서 내가 거기에 맞추는 느낌이 강함.
  - 이것을 관리하는 관리자 → pip

### 가상환경

- 패키지의 활용 공간 (Django가면 쓴다.)

이런 흐름으로 기억해두고 다시 자세하게 설명 들어감.

### 모듈,패키지

- 모듈 →특정기능하는 코드를 .py단위로 자름.
- 패키지 →특정기능 관련 여러 **모듈 집합**.
  패키지 안에는 sub- package를 포함.

```python
import module
from module import var, function, Class
from module import * # 다가져온다는 뜻.

from package import module
from package.module import var, function, Class
```

### 파이썬 패키지 관리자 (pip)

- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

- 그래서 주피터 노트북 깔때, pip install jupyternotebook 이렇게 했음.
  
  - 최신버전깔려면 그냥 pip install PackageName (최신/ 특정버전/ 최소버전 명시해서 설치가능)
  - pip install PackageName==1.0.5
  - pip install PackageName==1.0.4’
    모두 bash, cmd환경에서 쓰임.

- 삭제 pip uninstall PackageName

- 패키지목록 pip list

- 특정 패키지 정보pip show SomePackage

- pip 명령어로 패키지목록 관리, 설치 가능하다.
  
  - pip freeze>requirements.txt →requirements.txt라는 txt파일에 설치된 pip list를 박제해줌. 이거를 패키지 깔려있는 컴퓨터에서 해줘서 뭐뭐 깔았나 txt로 가져옴
  - pip install -r requirements.txt 를 집에 가서 해주면 됨. 그러면 txt file로 박제했던 목록을 가져와서 설치함.

### 모듈/패키지 활용

- 패키지는 여러 모듈, 하위 패키지로 구조화 (패키지가 모듈이 모여서 만들어지니까.)
  package.module
- 모든 폴더에는 **init**.py를 만들어 패키지로 인식한다.
  python 3.3부터는 파일이 없어도 되지만 하위버전, 프레임워크 호환위해 만듬.

```python
말이 어려운데 실제로는 간단해!

폴더안에 __init__.py를 넣어주면 그 폴더를 패키지로 인식한다.
그리고 그 안에 들어가는 다른이름을가진.py파일들이 모듈이 되는 것!

__init__.py이 있는 폴더 안에 또 폴더를 만들어서 
__init__.py를 넣어주면 하부폴더 자체도 패키지로 인식하니까, 
패키지 안에 있는 하위패키지가 되는것. 어렵게 생각 NO NO

요즘 파이썬 버전에는 이거 없어도 됨. 
```

### 가상환경(venv - virtual environment)

왜 쓰나?

- Python 표준 lib가 아닌 외부 package, module사용하는경우 모두 pip통해 설치

- 복수의 프로젝트하는경우 버전이 상이할 수 있음.
  
  - 과거 외주 프로젝트 - django 버전 2.x
  - 신규 회사 프로젝트 - django 버전 3.x

- 이럴때 가상환경 만들어(한 컴퓨터로 호환성 문제안되게 관리) 프로젝트별로 독립적 패키지 관리 가능

- 가상환경 만들고 관리하는 모듈이 python 3.5부터 생김

- 특정 dir에 가상환경 만들고, 고유한 python package 집합 가질 수 있음.
  
  - 예시- 어떤 폴더에 가상환경(package 집합폴더)있고
    실행환경(git bash)에서 가상환경을 (불러와서)활성화 시켜
    해당 폴더에 있는 패키지를 관리, 사용
  - 예를 들어서 python 3.8에서는 삭제되거나 코드가 바뀌어서 변한 기능.
    python 3.5 가상환경 폴더를 만들어서 그걸 bash로 켜면 편리하게 이용 가능.
