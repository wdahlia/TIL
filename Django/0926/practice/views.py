from django.shortcuts import render
import random

# Create your views here.

#main

def main(request):
    return render(request, 'main.html')

# number
def number(request, number):
    if number == 0:
        result = 0
    else:
        if number % 2 == 1:
            result = '홀수'
        elif number % 2 == 0:
            result = '짝수'

    context = {
        'num' : number,
        'result' : result,
    }
    return render(request, 'number.html', context)

# calculate
def calculate(request, firstnum, secondnum):
    plusnum = firstnum + secondnum
    minusnum = firstnum - secondnum
    multiplenum = firstnum * secondnum
    dividenum = firstnum // secondnum

    context = {
        'plusnum' : plusnum,
        'minusnum' : minusnum,
        'multiplenum' : multiplenum,
        'dividenum' : dividenum,
        'firstnum' : firstnum,
        'secondnum' : secondnum,
    }

    return render(request, 'calculate.html', context)

# hogwart
def hogwart(request):
    return render(request, 'hogwart.html')

def result(request):

    name = request.GET.get('p')

    # 기숙사 지정
    domitory_dict = {
        '그리핀도르' : ['https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/946397ca-37b3-4eed-9a27-6182d454e626/de0kjre-c20de09d-c0b8-4c67-b4b1-292217d2db93.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzk0NjM5N2NhLTM3YjMtNGVlZC05YTI3LTYxODJkNDU0ZTYyNlwvZGUwa2pyZS1jMjBkZTA5ZC1jMGI4LTRjNjctYjRiMS0yOTIyMTdkMmRiOTMucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.xC29ZjndzWaSPWaQaSvq3CDkICZkJ6M1a5OZ-QCuRoc', '#ae2012'],
        '슬리데린' : ['https://mblogthumb-phinf.pstatic.net/20150327_163/nyx0426_1427436480608W3VJk_PNG/1503HPPP_%2820%29.png?type=w420', '#84a98c'],
        '후플푸프' : ['https://mblogthumb-phinf.pstatic.net/20150327_265/nyx0426_1427436480960q8Nh5_PNG/1503HPPP_%2818%29.png?type=w420', '#fca311'],
        '래번클로' : ['https://mblogthumb-phinf.pstatic.net/20150327_139/nyx0426_14274364809686o18X_PNG/1503HPPP_%2816%29.png?type=w420', '#0466c8'],
        '덤스트랭' : ['https://mblogthumb-phinf.pstatic.net/20150728_300/jace0_1438087365172DhoPm_PNG/DurmstrangCrest.png?type=w2', '#da1e37'],
        '보바통' : ['https://vignette.wikia.nocookie.net/harrypotter/images/e/ea/BeauxbatonsCrestClearBg.png/revision/latest/scale-to-width-down/350?cb=20160630041801', '#9bb1ff'],
        '일버르모니' : ['https://file.namu.moe/file/8bc9e381797334eb33da66e3ba501be185dcdd0da33f657e698eea93d7de83e0dc5e34085ed3b73a523422c932934a6ed8a806d7b0c4432fe9f611f943fd000f7870dbf58c84f0260f346c289c43880f', '#59a5d8'],
        '죽음을먹는자들' : ['https://www.harrypotterpopvinyls.com/wp-content/uploads/2019/05/85-voldemort-with-nagini-pop-vinyl-400x0-c-center.png', '#a1a6b4'],
        '불사조기사단' : ['https://w.namu.la/s/116bf89f9fefad39f21d2885af75d3a01795852e20008c495a35ccfc81ff83b18393d28cb0b2dbe59f321e6e4e7d1b9970eef99e5c03ccbc26339a8d388051b00ea894e2635e1576ba80c75b3a65a51ddc023535d71cc1b2dd9a0d8bef304d6d', '#9b2915'],
    }

    domitory = random.choice(list(domitory_dict.items()))

    context = {
        'domitory' : domitory,
        'name' : name,
    }

    return render(request, 'result.html', context)

# lorem



def lorem(request):
    return render(request, 'lorem.html')



def loremresult(request):

    lorem_list = []
    
    # random 으로 단어의 수만큼 뽑아 저장하고 그걸 문단의 수만큼 출력

    lorem = ['꼬리별', '나봄', '늘솔길', '늘해랑', '다소니', '다온', '도담도담', '루리', '미리내', '보담', '새솔', '소예',
    '이플', '푸르내', '토리', '희나리']
    
    loremPara = request.GET.get('paran')
    loremNum = request.GET.get('wordn')

    for _ in range(int(loremPara)):
        lorems = []
        for _ in range(int(loremNum)):
            elements = random.choice(lorem)
            lorems.append(elements)
        lorem_list.append(lorems)

    context = {
        'loremlist' : lorem_list,
    }
    return render(request, 'loremresult.html', context)

