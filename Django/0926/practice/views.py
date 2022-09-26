from django.shortcuts import render

# Create your views here.

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


def pastlife(request):
    return render(request, 'pastlife.html')
