from django.shortcuts import render
import random

# Create your views here.

def index(request):

    dinner = [
        ('치폴레','https://mblogthumb-phinf.pstatic.net/MjAxODAxMTJfMjEx/MDAxNTE1NzE2NzgzODI3.dHJpUMnxQxhEOSUGZ3R_45AGLdm9TZFYgAWSDwP6SDYg.N8MjTLanHuJsCQMLe0F3IazGz5sKqPl-fN2upDXoGYwg.JPEG.ddubabi/IMG_0833.JPG?type=w800'),
        ('초밥', 'https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/00/a0000881/img/basic/a0000881_main.jpg'),
        ('매운탕', 'http://img.research-paper.co.kr/resources/2018/08/10/Xh4qxMUofbc8kEqz.jpg'),
        ('떡볶이', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Tteokbokki.JPG/1200px-Tteokbokki.JPG')
    ]

    menu = random.choice(dinner)

    context = {
        'menu' : menu[0],
        'img' : menu[1],
    }
    
    return render(request, 'today_dinners/index.html', context)