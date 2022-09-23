
from multiprocessing import context
from django.shortcuts import render
import random
# Create your views here.



def index(request):
    lottoNumber = []

    bonus, *whoIsWinner = random.sample(range(1, 46), 7)

    for _ in range(5):
        cnt = 0
        result = 0
        randomBalls = random.sample(range(1, 46), 6)
        for randomBall in randomBalls:
            if randomBall in whoIsWinner:
                cnt += 1

        if cnt == 3:
            result = 5
        elif cnt == 4:
            result = 4
        elif cnt == 5:
            if bonus in randomBalls:
                result = 2
            else:
                result = 3
        elif cnt == 6:
            result = 1
        
        lottoNumber.append((randomBalls, result))
        
            
    context = {
        'whoIsWinner' : whoIsWinner,
        'bonus' : bonus,
        'randomBall' : lottoNumber,

    }
    
    return render(request, 'lottos/index.html', context)