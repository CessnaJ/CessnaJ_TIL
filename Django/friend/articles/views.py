from django.shortcuts import render
import random


# Create your views here.
def index(request):
    
    print('인덱스 대리..여기봐! 웹페이지에는 안보이는데 터미널 콘솔에는 찍힌다?')
    nums = [1,5,7,2,3,4,6]

    pick = random.choice(nums)
    
    
    context = {
        'name' : 'cessna',
        'foods': ['pizza','chicken','hamburger'],
        'address':{'city':'seoul'},
        'pick': pick
    }




    return render(request, 'index.html', context)


def throw(request):
    return render(request, 'throw.html')

def catch(request):
    print('catch에 도달했습니다.')
    print('=======================')

    print(request)
    print(type(request))
    print(request.GET)
    print(request.GET.get('message'))

    return render(request, 'catch.html')



def greeting(request, age, word):
    result = False
    
    if word == word[::-1]:
        result = True

    context= {
        'age': age,
        'result': result,
        'word': word
    }

    return render(request, 'greeting.html', context)




