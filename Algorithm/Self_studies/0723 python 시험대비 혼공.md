# 0723 python 시험대비 혼공

- 다른 진법 10진법으로 return해주는 expression
  
  - 0bff →2진법 숫자
  - 0off → 8진법 숫자
  - 0xff →16진법. 10부터는 A~F 들어감. 소문자 써도 알아서 인식
  
  반대로 우리가 평소 사용하는 10진법 숫자를 다른진법 form으로 바꿀 수 있다.
  
  - bin(), oct(), hex() 함수를 써서. 근데 **str으로 바뀌는거** 알고 있어야 해!
    
    ```python
    i = 255
    print(bin(i)) -> 0b11111111
    print(oct(i)) -> 0o377
    print(hex(i)) -> 0xff
    
    print(type(bin(i))) -> <class 'str'>
    그러니까 변환된 숫자 자체만을 알고 싶으면 hex(i)[2:]를 해서 3번째 글자부터 뽑아내면 됨.
    ```
  
  - python 3.9부터 int이용해서도 다른진법을 또 바꿔 줄 수 있다.

```python
print(int('10')) ->10
print(int('10', 2)) -> 2
print(int('10', 16)) -> 16
```

- 함수 만들 때 default없는 param, defualt있는 param순서로 생성

- 사용할때는 kwargs를 뒤에 몰아서. 그래야 순서가 안꼬인다.

- 이 또한 두개의 개념이지만 사용할때는 똑같이 타이핑됨.

- default있는 param도 뒤로 모으기

- kwargs도 뒤로 모으기

- Arbitrary argument lists도 뒤로 모으기

- *args(arbitrary argument lists)는 몇개든 받을 수 있다는걸 말한다. tuple형태로 묶여서 iterable하게 쓰인다.

- **kwargs(keyword arbirtary argument list)는 우리가 대응시켜서 kwargs에 넣기 때문에 dict로 같이 들어가게 된다.
  
  - **2번파일 함수에 kwargs 어떻게 푸는지 이해가 안되었음.**

```python
callable이라는건 함수 선언하고 불러오는걸 말하는데, 변수로 지정해버리면 built-in함수로 가기전에
global scope에서 print이름 가진걸 찾아버려서 name탐색이 끝나니까.
변수로 지정된 print로 쓰게 되고 함수형식이 아니라서 not callable하다고 뜨게됨.

1. `print()` 코드가 실행되면
2. 함수에서 실행된 코드가 아니기 때문에 `L`, `E` 를 건너 뛰고,
3. `print`라는 식별자를 Global scope에서 찾아서 `print = ssafy`를 가져오고, 
4. 이는 함수가 아니라 변수이기 때문에 `not callable`하다라는 오류를 내뱉게 됩니다.
5. 우리가 원하는 `print()`은 Built-in scope에 있기 때문입니다.
```

- join method 다시 보자!
- 0723 2번 파일 map함수 약하다.
- Map object is iterable but not subscriptable.
- fileter(func, iterable) →iterable객체들에 function 씌워서 True를 뱉는 iterable객체만을 return.
- return은 그 자체로 statement.
  - list comprehension에 들어갈 수 있는건 expression.
  - list comprehension을 쓰면 → [i % ==0 for i in n]
    iterable한 객체 n의 각 객체 i를 왼쪽 expression에 돌려서 list를 return해준다.

**## lambda 함수**

- 표현식을 계산한 결과 값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불립니다.
- return 문을 가질 수 없고, 간단한 조건문 외의 구성이 어렵습니다. (이미 그 자체가 return이니)
- 함수를 정의해서 사용하는 것보다 간결하게 사용 가능합니다.

```python
기본형!
def triangle_area(b, h):
        return 0.5 * b * h

lambda b, h: 0.5 * b * h

람다함수 정의할 때 x = lambda var1, var2 : var1 * var2
이렇게 해서 람다 함수 자체를 변수로 지정할 수 있어. 
왜냐하면 결국 statement는 return값을 가지니까.

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
```

- 이렇게 생각하면 됨!
  lambda함수를 쓸거야! b,h를 args로 받을거야!
  : 로 구분해주고, 어떤 연산해서 return해줄건지 써!

```python
list(map(lambda n: n%2, [1, 2, 3]))
이게 뭐지!! 싶었다.
```

,가 있는 이유는 lambda가 아니라 map 때문!

map이 (원하는함수, iterable한 객체)인데 lambda를 통해서 내가 원하는 새로운 함수를 짧게 정의한거. map과 합쳐져서 1줄로 바로 돌려버리기가 가능하다!

- 패키지 활용도 좀 이상함. 하라는대로 **init**.py랑 디렉토리 다 만들었는데.
  my_package가 최상단 dir인데 그냥 무시하고

# any() 구현하다가 생긴 궁금증.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d4dabf0-1cd7-4b83-82a9-bee68306c6fc/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2e63ee96-a93b-4f00-af82-54f8728873d4/Untitled.png)

걍 i를 넣으면 true라서 제대로 작동하지만, i == True를 하면 False가 나온다?

그래서 bool([])을 넣으면 false가 나온다?

아래에 답안을 찾아놨다!

## Truth value testing

Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below.

By default, an object is considered true(implicit) unless its class defines either a **bool**() method that returns False or a **len**() method that returns zero, when called with the object. 1 Here are most of the built-in objects considered(not equal) false:

- constants defined to be false: None and False.
- zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
- empty sequences and collections: '', (), [], {}, set(), range(0)

Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true, unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)

- 이거랑 또 별개로 ==는 data type을 강제한다.
  - False == [] 해도 False
    False == 0 해도 False
    False == False 당연히 True
    [] == () False **0 == False 하면 True (이거 빼고는 걍 다 틀리다고 보면 됨)**
  - 다만 while something: 해서 T/F 들어가는 공간에 그대로 박아버리면 implicit하게 해석됨.

예시는 다음과 같다.

[](https://realpython.com/python-not-operator/)[Using the &quot;not&quot; Boolean Operator in Python – Real Python](https://realpython.com/python-not-operator/)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3bde1e1f-0f12-4e9a-82fd-5d972ac92048/Untitled.png)

explicit에서는 1만 “값”이 정확히 같고, data type도 boolean과 동일하게 0,1로 처리되는 것만 True로 반환. 그래서 [1]도 False다.

implicit에서는 0 아니면 그냥 다 True라고 봄. 그리고 bool안에 해당 객체를 넣으면 implicit으로 판단해서 T/F를 뱉어준다.

## Conditional Expression(조건표현식) = Ternary Operator(3항연산자)

- 코드블럭 자체에서 return을 해주는게 자동으로 들어가있다.

```python
num = int(input('숫자를 입력하세요 : '))
value = num if num >= 0 else -num

이렇게 되면 오른쪽 -num에도 value가 return되서 치환된 값이 들어가게 됨.
밑에
print(value)하면 return값이 출력되겠지.
```

- 그러니까 내가 return을 안써도 알아서 그 코드블럭이 if statement의 T/F를 판별해서 왼참우거 중 하나를 return해준다는거임.

- 위에서 value는 pointer를 말하겠지.

- 공부할것들 - subscriptable, immutable, iterable

- dict comprehension
  
  - dict 얘기가 나왔으니 말인데,

```python
기초예제 생성.
cubic = {i:i**3 for i in range(1,4)}
```

- .join(iterable, iterable객체사이에 넣고싶은거 default는 비어있음.)

## expression과 statement의 관계

## Expression

- expression이란, 수식.(하나이상의 값으로 표현(reduce)될 수 있는 코드.
- 사칙연산식이 곧 expression. 1+1, 2+5 [ 근데 여기에 더해 컴퓨터는 function call, var name등의 id, array등의 할당연산자 까지 포함한걸 다 expression이라고 봄.]
  Expression은 **평가(evaluate)가 가능해서 하나의 ‘값’으로 환원**됨. (그 코드블럭 덩어리채로 return값을 가진다는거임.)
- 리터럴의 형식은 달라도 그 “평가값(**evaluation**)”은 같을 수 있어.

```python
a, b, c = 1,2,3
list = [1,2,3]

1 + 2 + 3
a + b
list[2]
function(3)
10

0x10이랑 0b1010이랑 evaluation은 같다.

이것들 다 return 값이 있는 연산이니까 expression이다.
```

## Statement

- 진술, 서술을 말함. (**실행가능한(executable)** 최소 독립적 코드조각) compiler가 이해할 수 있는 모든 코드구문은 statement [그러니까 statement가 더 큰 범주고, 그 안에 expresstion이 들어간다.] → 그러니까, **모든 Expression은 statement다!**
- 보통 statement는 1개이상 expression + 프로그래밍 keyword(if, for, while, return 같은거.)를 포함.

```python
a = 3
a,b = 2, 3

if is_valid:
        return 4
```

- 3 + 2 이거는 평가가 가능한 expression이고, 실행가능한(python interpreter에 입려가면 정상적으로 실행 되니까) statement다.
- 반례로 statement인데 expression 아닌것 → return 3
  3을 반환한다. 라는 의미이지 evaluation해서 3이 나오는게 아니다.
  a = 3도 마찬가지! ⇒ 3을 a라는 var에 할당. evaluation 후 어떤 값으로 환원되지 않는다!

```python
증거.
eval()
exec()에서
exec('1+2')는 실행됨.
근데 eval('a = 3')은 실행안됨.
```

## Iterable, Ordered, Mutable, Hashable, Supscriptable 정리

[](https://towardsdatascience.com/iterable-ordered-mutable-and-hashable-python-objects-explained-1254c9b9e421)https://towardsdatascience.com/iterable-ordered-mutable-and-hashable-python-objects-explained-1254c9b9e421

이거 보고 내 언어로 정리해본다!

### 1. Iterable

집합으로 묶여있는 객체를 한개씩 뽑아서 loop돌릴 수 있다는 뜻이다.

Collection of items랑 **string**에 쓸 수 있음.

Collection of items→ (list, tuple, set, frozenset, dict, range, iterator)

- Dict를 iteration하면 key를 뽑아서 대응한다! (value를 대응한다고 착각하지마. value 뽑고 싶으면
  .values() method 쓰던가, dict를 for loop해서 나온 key값들에 dict[i]를 붙혀서 뽑아내자!

```python
for i in dict.values():
        print(i)

for i in dict:
        print(dict[i])

아니면 items method 이용해서 i, j 같이 뽑고 j만 쓴다.
for i, j in dict.itmes():
        print(j)
```

- 궁금증 → iter(list) 해서 <class ‘list_iterator’>를 뽑는다는게 뭐지?

### 2. Ordered / Unordered (순서가 있는/없는)

- 우리가 의도적으로 바꾸지 않는한, 기존의 순서가 유지되는걸 ordered라고 한다.

- **string, list, tuple, range, dict**는 순서가 있다! (이 순서나 element를 바꿀 수 있냐는거랑은 또 다른 개념)

- **set, frozenset, dict(3.7ver 이전)**은 순서가 없다.
  
  순서가 있다는거는 **slicing**을 통해서 접근이 가능하다는거다.
  tuple, range, dict의key는 immutable하고, 나머지 string, list는 iterable의 객체를 바꿀 수 있다.
  
  dict에서 특정 value 뽑기 위해서는 순서가 아니라 key를 이용해서 뽑는다.
  
  - 만약에 우리가 dict의 순서를 알고 있고, key를 모른다면 어떻게 할까?
    두번째 value를 뽑고 싶다면 어떻게 해야할까?# 0723 python 시험대비 혼공
    - 다른 진법 10진법으로 return해주는 expression
      
      - 0bff →2진법 숫자
      - 0off → 8진법 숫자
      - 0xff →16진법. 10부터는 A~F 들어감. 소문자 써도 알아서 인식
      
      반대로 우리가 평소 사용하는 10진법 숫자를 다른진법 form으로 바꿀 수 있다.
      
      - bin(), oct(), hex() 함수를 써서. 근데 **str으로 바뀌는거** 알고 있어야 해!
        
        ```python
        i = 255
        print(bin(i)) -> 0b11111111
        print(oct(i)) -> 0o377
        print(hex(i)) -> 0xff
        
        print(type(bin(i))) -> <class 'str'>
        그러니까 변환된 숫자 자체만을 알고 싶으면 hex(i)[2:]를 해서 3번째 글자부터 뽑아내면 됨.
        ```
      
      - python 3.9부터 int이용해서도 다른진법을 또 바꿔 줄 수 있다.
    
    ```python
    print(int('10')) ->10
    print(int('10', 2)) -> 2
    print(int('10', 16)) -> 16
    ```
    
    - 함수 만들 때 default없는 param, defualt있는 param순서로 생성
    
    - 사용할때는 kwargs를 뒤에 몰아서. 그래야 순서가 안꼬인다.
    
    - 이 또한 두개의 개념이지만 사용할때는 똑같이 타이핑됨.
    
    - default있는 param도 뒤로 모으기
    
    - kwargs도 뒤로 모으기
    
    - Arbitrary argument lists도 뒤로 모으기
    
    - *args(arbitrary argument lists)는 몇개든 받을 수 있다는걸 말한다. tuple형태로 묶여서 iterable하게 쓰인다.
    
    - **kwargs(keyword arbirtary argument list)는 우리가 대응시켜서 kwargs에 넣기 때문에 dict로 같이 들어가게 된다.
      
      - **2번파일 함수에 kwargs 어떻게 푸는지 이해가 안되었음.**
    
    ```python
    callable이라는건 함수 선언하고 불러오는걸 말하는데, 변수로 지정해버리면 built-in함수로 가기전에
    global scope에서 print이름 가진걸 찾아버려서 name탐색이 끝나니까.
    변수로 지정된 print로 쓰게 되고 함수형식이 아니라서 not callable하다고 뜨게됨.
    
    1. `print()` 코드가 실행되면
    2. 함수에서 실행된 코드가 아니기 때문에 `L`, `E` 를 건너 뛰고,
    3. `print`라는 식별자를 Global scope에서 찾아서 `print = ssafy`를 가져오고, 
    4. 이는 함수가 아니라 변수이기 때문에 `not callable`하다라는 오류를 내뱉게 됩니다.
    5. 우리가 원하는 `print()`은 Built-in scope에 있기 때문입니다.
    ```
    
    - join method 다시 보자!
    - 0723 2번 파일 map함수 약하다.
    - Map object is iterable but not subscriptable.
    - fileter(func, iterable) →iterable객체들에 function 씌워서 True를 뱉는 iterable객체만을 return.
    - return은 그 자체로 statement.
      - list comprehension에 들어갈 수 있는건 expression.
      - list comprehension을 쓰면 → [i % ==0 for i in n]
        iterable한 객체 n의 각 객체 i를 왼쪽 expression에 돌려서 list를 return해준다.
    
    **## lambda 함수**
    
    - 표현식을 계산한 결과 값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불립니다.
    - return 문을 가질 수 없고, 간단한 조건문 외의 구성이 어렵습니다. (이미 그 자체가 return이니)
    - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능합니다.
    
    ```python
    기본형!
    def triangle_area(b, h):
            return 0.5 * b * h
    
    lambda b, h: 0.5 * b * h
    
    람다함수 정의할 때 x = lambda var1, var2 : var1 * var2
    이렇게 해서 람다 함수 자체를 변수로 지정할 수 있어. 
    왜냐하면 결국 statement는 return값을 가지니까.
    
    x = lambda a, b, c: a + b + c
    print(x(5, 6, 2))
    ```
    
    - 이렇게 생각하면 됨!
      lambda함수를 쓸거야! b,h를 args로 받을거야!
      : 로 구분해주고, 어떤 연산해서 return해줄건지 써!
    
    ```python
    list(map(lambda n: n%2, [1, 2, 3]))
    이게 뭐지!! 싶었다.
    ```
    
    ,가 있는 이유는 lambda가 아니라 map 때문!
    
    map이 (원하는함수, iterable한 객체)인데 lambda를 통해서 내가 원하는 새로운 함수를 짧게 정의한거. map과 합쳐져서 1줄로 바로 돌려버리기가 가능하다!
    
    - 패키지 활용도 좀 이상함. 하라는대로 **init**.py랑 디렉토리 다 만들었는데.
      my_package가 최상단 dir인데 그냥 무시하고
    
    # any() 구현하다가 생긴 궁금증.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d4dabf0-1cd7-4b83-82a9-bee68306c6fc/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2e63ee96-a93b-4f00-af82-54f8728873d4/Untitled.png)
    
    걍 i를 넣으면 true라서 제대로 작동하지만, i == True를 하면 False가 나온다?
    
    그래서 bool([])을 넣으면 false가 나온다?
    
    아래에 답안을 찾아놨다!
    
    ## Truth value testing
    
    Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below.
    
    By default, an object is considered true(implicit) unless its class defines either a **bool**() method that returns False or a **len**() method that returns zero, when called with the object. 1 Here are most of the built-in objects considered(not equal) false:
    
    - constants defined to be false: None and False.
    - zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
    - empty sequences and collections: '', (), [], {}, set(), range(0)
    
    Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true, unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)
    
    - 이거랑 또 별개로 ==는 data type을 강제한다.
      - False == [] 해도 False
        False == 0 해도 False
        False == False 당연히 True
        [] == () False **0 == False 하면 True (이거 빼고는 걍 다 틀리다고 보면 됨)**
      - 다만 while something: 해서 T/F 들어가는 공간에 그대로 박아버리면 implicit하게 해석됨.
    
    예시는 다음과 같다.
    
    [](https://realpython.com/python-not-operator/)[Using the &quot;not&quot; Boolean Operator in Python – Real Python](https://realpython.com/python-not-operator/)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3bde1e1f-0f12-4e9a-82fd-5d972ac92048/Untitled.png)
    
    explicit에서는 1만 “값”이 정확히 같고, data type도 boolean과 동일하게 0,1로 처리되는 것만 True로 반환. 그래서 [1]도 False다.
    
    implicit에서는 0 아니면 그냥 다 True라고 봄. 그리고 bool안에 해당 객체를 넣으면 implicit으로 판단해서 T/F를 뱉어준다.
    
    ## Conditional Expression(조건표현식) = Ternary Operator(3항연산자)
    
    - 코드블럭 자체에서 return을 해주는게 자동으로 들어가있다.
    
    ```python
    num = int(input('숫자를 입력하세요 : '))
    value = num if num >= 0 else -num
    
    이렇게 되면 오른쪽 -num에도 value가 return되서 치환된 값이 들어가게 됨.
    밑에
    print(value)하면 return값이 출력되겠지.
    ```
    
    - 그러니까 내가 return을 안써도 알아서 그 코드블럭이 if statement의 T/F를 판별해서 왼참우거 중 하나를 return해준다는거임.
    
    - 위에서 value는 pointer를 말하겠지.
    
    - 공부할것들 - subscriptable, immutable, iterable
    
    - dict comprehension
      
      - dict 얘기가 나왔으니 말인데,
    
    ```python
    기초예제 생성.
    cubic = {i:i**3 for i in range(1,4)}
    ```
    
    - .join(iterable, iterable객체사이에 넣고싶은거 default는 비어있음.)
    
    ## expression과 statement의 관계
    
    ## Expression
    
    - expression이란, 수식.(하나이상의 값으로 표현(reduce)될 수 있는 코드.
    - 사칙연산식이 곧 expression. 1+1, 2+5 [ 근데 여기에 더해 컴퓨터는 function call, var name등의 id, array등의 할당연산자 까지 포함한걸 다 expression이라고 봄.]
      Expression은 **평가(evaluate)가 가능해서 하나의 ‘값’으로 환원**됨. (그 코드블럭 덩어리채로 return값을 가진다는거임.)
    - 리터럴의 형식은 달라도 그 “평가값(**evaluation**)”은 같을 수 있어.
    
    ```python
    a, b, c = 1,2,3
    list = [1,2,3]
    
    1 + 2 + 3
    a + b
    list[2]
    function(3)
    10
    
    0x10이랑 0b1010이랑 evaluation은 같다.
    
    이것들 다 return 값이 있는 연산이니까 expression이다.
    ```
    
    ## Statement
    
    - 진술, 서술을 말함. (**실행가능한(executable)** 최소 독립적 코드조각) compiler가 이해할 수 있는 모든 코드구문은 statement [그러니까 statement가 더 큰 범주고, 그 안에 expresstion이 들어간다.] → 그러니까, **모든 Expression은 statement다!**
    - 보통 statement는 1개이상 expression + 프로그래밍 keyword(if, for, while, return 같은거.)를 포함.
    
    ```python
    a = 3
    a,b = 2, 3
    
    if is_valid:
            return 4
    ```
    
    - 3 + 2 이거는 평가가 가능한 expression이고, 실행가능한(python interpreter에 입려가면 정상적으로 실행 되니까) statement다.
    - 반례로 statement인데 expression 아닌것 → return 3
      3을 반환한다. 라는 의미이지 evaluation해서 3이 나오는게 아니다.
      a = 3도 마찬가지! ⇒ 3을 a라는 var에 할당. evaluation 후 어떤 값으로 환원되지 않는다!
    
    ```python
    증거.
    eval()
    exec()에서
    exec('1+2')는 실행됨.
    근데 eval('a = 3')은 실행안됨.
    ```
    
    ## Iterable, Ordered, Mutable, Hashable, Supscriptable 정리
    
    [](https://towardsdatascience.com/iterable-ordered-mutable-and-hashable-python-objects-explained-1254c9b9e421)https://towardsdatascience.com/iterable-ordered-mutable-and-hashable-python-objects-explained-1254c9b9e421
    
    이거 보고 내 언어로 정리해본다!
    
    ### 1. Iterable
    
    집합으로 묶여있는 객체를 한개씩 뽑아서 loop돌릴 수 있다는 뜻이다.
    
    Collection of items랑 **string**에 쓸 수 있음.
    
    Collection of items→ (list, tuple, set, frozenset, dict, range, iterator)
    
    - Dict를 iteration하면 key를 뽑아서 대응한다! (value를 대응한다고 착각하지마. value 뽑고 싶으면
      .values() method 쓰던가, dict를 for loop해서 나온 key값들에 dict[i]를 붙혀서 뽑아내자!
    
    ```python
    for i in dict.values():
            print(i)
    
    for i in dict:
            print(dict[i])
    
    아니면 items method 이용해서 i, j 같이 뽑고 j만 쓴다.
    for i, j in dict.itmes():
            print(j)
    ```
    
    - 궁금증 → iter(list) 해서 <class ‘list_iterator’>를 뽑는다는게 뭐지?
    
    ### 2. Ordered / Unordered (순서가 있는/없는)
    
    - 우리가 의도적으로 바꾸지 않는한, 기존의 순서가 유지되는걸 ordered라고 한다.
    
    - **string, list, tuple, range, dict**는 순서가 있다! (이 순서나 element를 바꿀 수 있냐는거랑은 또 다른 개념)
    
    - **set, frozenset, dict(3.7ver 이전)**은 순서가 없다.
      
      순서가 있다는거는 **slicing**을 통해서 접근이 가능하다는거다.
      tuple, range, dict의key는 immutable하고, 나머지 string, list는 iterable의 객체를 바꿀 수 있다.
      
      dict에서 특정 value 뽑기 위해서는 순서가 아니라 key를 이용해서 뽑는다.
      
      - 만약에 우리가 dict의 순서를 알고 있고, key를 모른다면 어떻게 할까?
        두번째 value를 뽑고 싶다면 어떻게 해야할까?
