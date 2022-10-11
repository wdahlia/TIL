# 221011 실습

`🔒 실습 목차`

<br>

<hr>


## ✔️ 가상환경 설정

### 가상환경 만들기

```python
# venv라는 가상환경 생성
python -m venv venv

# 1011 폴더안에 venv 생성
```

<br>

### 가상환경 진입

```python
# Mac의 경우
source venv/bin/activate # 가상환경 폴더 안에 bin폴더 안에 activate가 들어가있으므로
= . venv/bin/activate
# Window의 경우
soruce venv/Scripts/activate
= . venv/Scripts/activate

# (venv) 1011 Practice/1011
# 가상환경 진입 성공
```

<br>

### Django 설치

> 가상환경 내에서 Django를 설치하는 이유? **각 프로젝트마다 패키지 관리를 쉽게 하기 위하여**

```python
pip install django==3.2.13

'''WARNING: You are using pip version 20.2.3; however, version 22.2.2 is available.
You should consider upgrading via the '/Users/dahlia/Desktop/Django/1005 Practice/venv-1005/bin/python -m pip install --upgrade pip' command.'''
# 이런 오류 메시지 나는 경우, pip install --uprade pip만 간단하게 해주면 해결

pip list # pip 설치 목록 나옴
```

```python
# 패키지 목록을 생성
pip freeze > requirements.txt

# 다른 사람에게 받은 requirements.txt이 있을 경우
# requirements.txt를 venv와 같은 위치에 위치시키고
pip install -r requirements.txt
```



<br>

### 프로젝트 생성

```python
django-admin startproject [프로젝트 이름] .
# 현재 위치한 디렉토리 내에서 project를 생성하겠다는 것
# 1011 Practice/1011에 project를 만들겠다는 것

# 프로젝트를 생성하면,
> 1011 Practice
	> 1011
  	> pjt1011
      > __init__.py
      > asgi.py
      > settings.py
      > urls.py
      > wsgi.py
```

<br>

### 로컬 서버 실행하기

```python
# 로컬 서버 정상 작동을 진행 하기 위해서
python manage.py runserver

# 로켓 발사 확인 완!
```

<p align="center"><img src="https://user-images.githubusercontent.com/108653518/194748513-4352e4ae-a00c-4dd6-8512-4d30da77bdfd.png" alt="runserver"  /></p>

<br>

### 앱(App) 생성

> ***프로젝트***는 웹 사이트 자체라면 ***앱***은 그 웹 사이트의 기능을 담당

```python
# 앱 생성을 위해 runserver를 종료해주고 ctrl+c 종료 가능

python manage.py startapp [앱 이름]
# 앱 생성 완료
# 여기서는 accounts라는 앱을 생성
```



## ✔️ 앱 설정

### settings.py

```python
# 1011 Practice/1011/pjt1011(프로젝트)/settings.py

INSTALLED_APPS = [
  'accounts',					 # 앱 이름 추가
  'django_bootstrap5', # pip install로 다운
  'django_extensions', # pip install로 다운
]

# installed_apps 목록 최상단에 앱이름 추가
```

<br>

### urls.py

```python
# 프로젝트이름/urls.py는 프로젝트 안에 들어가는 앱들의 url을 관리해준다
# 즉, 앱의 각 url들의 경우 app안에서 따로 urls.py를 만들어 관리해주는 것이 좋다

# 1011 Practice/1011/pjt1011(프로젝트)/urls.py
'''
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''
# 참고

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
  	path('', include(accounts.urls)), # accounts라는 앱안의 urls.py
]
```

```python
# 앱에서 즉, accounts안에 urls.py를 생성
from django.urls import path
from . import views						# 현재의 디렉토리에서 views.py를 import 해온다

app_name = 'account'				# 앱 네임을 설정

urlpatterns = [
]
# urlpatterns = [ ] 까지만 정의 해주고 다음 단계인 모델 정의 makemigrations, migrate 단계로 넘어갈 것
```

<br>

#### app_name 활용

```python
# views.py에서

return redirect('account:index')	# app_name:path의 name
```

```html
<!-- templates에서 -->

{% url 'account:index' %}
```

<br>

## ✔️모델 생성

### 클래스 정의

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
    
# 모델에 필드 속성을 정의해준다
```

<br>

[참고 문서-1](https://velog.io/@mmy789/Django-AbstractUser%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C-%EC%9C%A0%EC%A0%80-%EB%AA%A8%EB%8D%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0) / [참고 문서-2](https://yonghyunlee.gitlab.io/python/user-extend/)

#### AbstractUser 

> **Django**의 로그인 기능을 사용하면서 **User Model**의 칼럼(데이터)들을 수정

- **Django**

  ```python
  class User(AbstractUser):
      """
      Users within the Django authentication system are represented by this
      model.
      Username and password are required. Other fields are optional.
      """
  
      class Meta(AbstractUser.Meta):
          swappable = "AUTH_USER_MODEL"
  ```

- User Model이 기본적으로 제공되어 자동으로 DB에 테이블을 만들기 때문에 Django가 이 테이블을 만들기 전 migrate 전에 작업을 해야 함

  - 물론, migrate이후에도 수정할 수 있는 방법 존재

- 기존 제공 필드 외에 더 추가할 필드가 없으면 `class User(AbstractUser): pass`를 한 후

- **`settings.py`**

  ```python
  AUTH_USER_MODEL = 'accounts.User'
  ```

- `accounts` 앱 안에 **`admin.py`** 

  - `localhost:8000/admin/` 페이지에서 확인 가능하도록 추가해줄 것

  ```python
  from django.contrib import admin
  from .models import User
  
  admin.site.register(User)
  ```

<br>

### makemigrations

```python
python manage.py makemigrations

'''
Migrations for 'accounts':
  accounts/migrations/0001_initial.py
    - Create model User
'''
```

- `accounts (앱 이름)/0001_initial.py`에 생성 된 파일을 확인 가능
- 테이블이 생성되지는 않음, 테이블 작업을 수행하기 위한 작업 파일을 생성하는 명령어

<br>

### migrate

```python
python manage.py migrate

# vscode안에서 db.sqlite3의 우측 마우스를 클릭하면, open database가 나오는데
# 이를 통해 user 데이터베이스가 생성된 것을 확인 할 수 있다
```

<br>

## ✔️ CRUD 구현 

<br>

### CREATE

<hr>

<br>

#### Static 생성

- `manage.py`와 같은 위치에 static을 생성하여 css 폴더와 image 폴더를 생성

  - 각각의 폴더에 정적파일들을 관리

- 프로젝트 폴더의 `settings.py`에 설정

  ```python
  STATICFILES_DIRS = [
    BASE_DIR / "static",
  ]
  ```

- ##### static 파일 활용방법

  ```html
  {% load static %}
  
  <link rel="stylesheet" href="{% static 'css/style.css'%}" type="text/css">
  ```

<br>

#### Templates 생성

- 상속을 받기 위하여 추가해준다

```python
# 상속을 하는 경우
# 프로젝트 폴더의 settings.py

TEMPLATES = [
  			...
        'DIRS': [ BASE_DIR / 'templates'], 
  			...
]
```

- `manage.py`와 같은 위치에 templates를 만들어 `base.html`을 생성하고

```html
<!-- Django/1011 Practice/1011/templates/base.html -->
{% load static %}
<!DOCTYPE html>
<html lang="en">

  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>movie</title>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <!-- style.css -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}" type="text/css">
    <!-- animate.css -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
  </head>

  <body>
    {% block nav %}
      <nav class="navbar navbar-expand-lg bg-light">
        <div class="container-fluid flex-column">
          <a class="me-0 navbar-brand" href="/">
            <img src="{% static 'image/logo.png' %}" class="img-size">
          </a>
          <div class="d-flex my-3 fw-light text-space">
            <a class="btn btn-outline-light nav-link border px-3 mx-3" aria-current="page" href="/">Home</a>
            <a class="btn btn-outline-light nav-link border px-3 mx-3" href="/accounts/index">Users</a>
            <a class="btn btn-outline-light nav-link border px-3 mx-3" href="{% url 'account:signup' %}">Sign Up</a>
          </div>
        </div>
      </div>
    </nav>
  {% endblock nav %}
  {% block content %}{% endblock content %}
  <!-- JavaScript Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
</body>

</html>
```

- `App`안에도 templates를 만들어 앱의 기능들을 담당할 html들을 생성해준다
  - `main.html` : 메인 페이지
  - `signup.html` : 회원가입 페이지
  - `index.html` : 회원 목록 페이지
  - `detail.html` : 회원 상세 페이지


```html
<!-- Django/1011 Practice/1011/accounts/templates/accounts/index.html -->
{% extends 'base.html' %}
{% load static %}
{% block nav %}{% endblock %}
{% block content %}
<!-- html 기록 -->
{% endblock %}
```

<br>

#### CREATE 구현

> **1. index.html 글 쓰기 버튼 클릭** 
>
> **2. 글 작성 Form이 나타남** 
>
> **3. 작성하기를 누르면 게시판에 표시**

<br>

#####  1️⃣ urls.py 

```python
path('create/', views.create, name='create'),
```

- `urlpatterns`에 create라는 경로를 추가해준다

<br>

##### 2️⃣ index.html

- 글 쓰기 버튼을 클릭하여야 하기 때문에, `index.html`을 구성해주어야함

```python
# community/urls.py

urlpatterns = [
  path('', views.index, name='index')
]

# community/views.py

def index(request):
    community = Community.objects.all()
    
    context = {
        'community' : community
    }
    return render(request, 'communities/index.html', context)
```

- `templates/communities`에 생성한 `index.html`의 `{% block content %}` `{% endblock %} ` 사이에

```python
{% extends 'base.html' %}
{% block content %}
			......
  
# 글 쓰기를 누르면 글 작성 form이 나타나는 페이지로 이동시킬 것
<a href="{% url 'community:create' %}" class="text-end text-dark fw-bolder">글 쓰기</a>

			......
{% endblock %}
```

- a 태그로 감싸주고 a태그의 hyper reference는 `community 앱`안의 `name이 create라는 path를 실행`시켜달라는 뜻

<br>

##### 3️⃣ forms.py

- 글 쓰기 버튼을 클릭하였을때 html안에 form을 보여주기 위해서 `장고 form`을 생성할 것
- html내에서 form태그 안에 input과 button을 이용하여 직접 만들 수도 있으나,
- **장고 form을 이용했을시 이점**
  - `form 태그` 내부에 `input 태그`들을 자동적으로 생성
  - `is_valid()`를 활용한 빠른 유효성 검사가 가능

```python
# community 앱 안에 forms.py 파일 생성

from django import forms	
from .models import Community
# 현재 디렉토리의 models.py에서 Community 클래스를 불러와준다.

class CommunityForm(forms.ModelForm):
  class Meta:
    model = Community
    fields = ['title', 'content']

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
    }

    labels = {
      'title': '제목',
      'content': '내용',
    }
```

- `from django import forms` : 장고가 제공해주는 form라이브러리
- `class Meta`  
  - '데이터에 대한 데이터' 혹은 '다른 데이터를 설명해주는 데이터'
  - 상위 클래스에 meta 데이터를 제공해주는 것
- `fields` :
  - form을 만들때 입력받을 fields를 선택해준다. 전부 다 입력 받고 싶다면 `'__all__'` 을 입력해주면 된다

<br>

##### 4️⃣ new.html

- 글 쓰기 버튼을 클릭하였을때, form을 보여줄 html을 생성해야함 여기서는 `new.html`이라고 정의하였음

```python
{% extends 'base.html' %}
{% block content %}
			.....
  
    <form action="" method="POST" class="fw-bolder">
      {% csrf_token %}
      {{ create_article.as_p }}
      <div class="d-flex justify-content-end">
        <button type="submit" class="btn btn-primary text-end">글 등록</button>
      </div>
    </form>
    
			.....
{% endblock %}
```

- `<form>`태그의 *action = "**URL**"*
  - 폼 데이터(form data)를 서버로 보낼 때 해당 데이터가 도착할 URL을 명시
- `<form>`태그의 *method = "**GET | POST**"*
  -  폼 데이터(form data)가 서버로 제출될 때 사용되는 HTTP 메소드를 명시
- `{% csrf_token %}`
  - ***CSRF*** - **C**ross **S**ite **R**equest **F**orgery
  - [CSRF 참고 사이트](https://chagokx2.tistory.com/49)
  - 장고에서 기본적으로 csrf_token을 이용하면 공격을 방어할 수 있음
- `{{ create_article.as_p }}`
  - `create_article` 은 변수명으로 views.py에 create 함수가 실행되고 new.html을 보여줄 때 context에 정의해준 변수명
    - 이 부분은 views.py에서 변수명을 지정한다음에 다시 수정해주어야한다
    - (참고) **밑의 views.py**
  - `as_p`
    - 각 필드가 단락(`<p>` 태그)으로 감싸져서 렌더링
  - `as_ul`
    - 각 필드가 목록 항목(`<li>` 태그)으로 감싸져서 렌더링
    - `<ul>` 태그는 직접 작성해야 한다
  - `as_table`
    - 각 필드가 테이블(`<tr>` 태그) 행으로 감싸져서 렌더링

<br>

> **GET** | **POST**
>
> - **GET**
>   - URL에 폼 데이터를 추가하여 서버로 전달하는 방식
>   - HTTP 요청은 브라우저에 의해 캐시되어(cached) 저장
>   - 보통 쿼리 문자열(query string)에 포함되어 전송, 길이의 제한 O
>   - 따라서 보안상 취약점이 존재, 중요한 데이터는 POST 방식을 사용하여 요청하는 것을 권장
> - **POST**
>   - 폼 데이터를 별도로 첨부하여 서버로 전달하는 방식
>   - HTTP 요청은 브라우저에 의해 캐시되지 않으므로, 브라우저 히스토리에도 남지 X
>   - POST 방식의 HTTP 요청에 의한 데이터는 쿼리 문자열과는 별도로 전송
>   - 따라서 데이터의 길이에 대한 제한 X, GET 방식보다 보안성이 높음

<br>

##### 5️⃣ views.py

- `urls.py`에 path안에 `views.create(views의 create 함수를 실행시켜 달라고하는 의미) ` 을 실행해야 하기에
- `views.py`에 `create 함수`를 정의해주어야함
- (참고) 만약 create함수를 정의해주지 않는다면,
  - **AttributeError: module 'community.views' has no attribute 'create'**
  - 이름이 잘못되거나 없는 속성을 가져오려면 나오는 에러
  - 모듈 community.views에는 create라는 속성이 없다는 뜻

```python
def create(request):
    if request.method == 'POST': # 요청받은 form의 메서드가 POST라면,
        create_article = CommunityForm(request.POST)
    # form 데이터를 처리하기 위해서 forms.py에 정의해준 CommunityForm 클래스 request.POST가 필요 
    # 이걸 create_article이라는 변수에 저장
        if create_article.is_valid():	# 유효성 검사에서 통과하면 (True 라면)
            create_article.save()	# create_article을 save
            return redirect('community:index') # community앱의 index라는 path로 redirect
          
            # 참고 views.index   
            '''
            def index(request):
            			community = Community.objects.all()	# 데이터베이스안의 모든 값을 불러와서

                  context = {
                      'community' : community				 
                  }
                  return render(request, 'communities/index.html', context)
                  # communities/index.html을 render해줘라
                  # context안의 값을 index.html에서 사용 가능
            '''
            
    else:	# 위의 if문을 충족하지 못하는 모든것
        create_article = CommunityForm() # 아무것도 받아오지 않은 상태를 create_article 변수에 저장
    
    # 모든 것과 별개로 context에 create_article을 저장
    context = {
        'create_article' : create_article,				
    }
    
    return render(request, 'communities/new.html', context) # new.html을 렌더 해준다
```

- 즉, 버튼을 눌러 submit이 되어질때 request가 일어나게 되는것인데 이때의 요청이 POST라면
  - 유효성 검사를 하여 통과하게 되면 그 결과를 데이터베이스에 저장해주고 index라는 함수를 실행시켜준다.
  - index라는 함수는 우리가 migrate한 데이터베이스의 모든 값을 받아 index.html에 렌더해주기 때문에
  - 우리는 우리가 새로 쓴 글을 입력하자마자 `localhost:8000` 로 이동하여 우리가 추가한 글을 바로 확인할 수 있게 된다

<br>

<p align="center"><img src="https://user-images.githubusercontent.com/108653518/194748505-0ce50dba-afc1-42c5-b335-f07e840dfd57.jpg" alt="create"  /></p>

- 만약, 유효성 검사에 실패한다면
  - 다시 new.html이 나오게 된다
  - 즉 `create_article`은 여기서  form 양식이라고 생각하면 된다 (우리가 forms.py에서 정의해주었던 그 폼)

<br>

### DELETE

<hr>


#### DELETE 구현

> **1. 각 글의 pk값을 받아와서**
>
> **2. 그 id값에 해당하는 row를 삭제**

- 전체 글을 삭제하는 것이 아니고 각 데이터베이스의 내가 지우고 싶은 row를 한줄 삭제한다는 개념으로 이해
- 즉, id(pk)값을 받아와야 한다.

<br>

##### 1️⃣ urls.py

```python
path('delete/<int:id>/', views.delete, name='delete'),
```

- `urlpatterns`에 delete라는 경로를 추가해준다
- 이 때, 다른점은 delete/ 뒤에 int:id 값을 받아오는것

<br>

##### 2️⃣ views.py

```python
def delete(request, id):
    Community.objects.get(pk=id).delete()
    return redirect('community:index')
```

- 요청과 id값 이때의 id값은 주소값 뒤에 받아온 int:id값이다
- `Community.objects.get(pk=id).delete()`
  - 데이터베이스에서 내가 받아온 id값과 일치하는 pk를 찾아 delete() 해달라
  - 이 때, delete()를 하게되면 바로 데이터베이스에서 그 pk값의 row가 삭제되므로 save()할 필요없다
- index 함수를 다시 실행시켜, 지운 결과를 index.html에 반영하게 함

<br>

##### 3️⃣ index.html

```python
{% for article in community %}
							.....
<a href="{% url 'community:delete' article.id %}">
	<i class="bi bi-trash3"></i>
</a>
							.....
{% endfor %}
```

- html의 href에 실행할 함수를 입력 `'community:delete'` 과 id값을 받아준다
  - for문을 돌면서 추가해주므로 `article.id`를 받아줘야함

<hr>


- 정리하자면, `localhost:8000`에서 휴지통 아이콘을 선택하게되면 href안에 정의한 `community:delete` 즉, delete함수가 실행 
  - 이때, article.id도 같이 받게됨 즉, 내가 지우고 싶은 글의 id값을 받아준다
- 그 이후, delete함수에 따라 데이터베이스의 pk값과 일치하는 받아온 id값을 찾아 그 행을 지우고
- index함수를 실행시키는 곳으로 redirect가 되어 삭제된 상태를 반영하게 됨

<br>

### UPDATE

<hr>


#### UPDATE 구현

> **1. 수정하기를 누르면 **
>
> **2. edit.html로 이동 **
>
> **3. edit.html에는 new와 같은 form이 존재, 이전에 작성했던 값이 들어있음**
>
> **4. 수정할 사항을 입력하고 제출하기를 누르면**
>
> **5. localhost:8000에 수정 내용이 반영되어 보임**

<br>

##### 1️⃣ urls.py

```python
path('update/<int:pk>/', views.update, name='update')
```

- `urlpatterns`에 update라는 경로를 추가해준다
- 이 때, 다른점은 update/ 뒤에 int:pk 값을 받아오는것
  - pk와 id는 같다

<br>

##### 2️⃣ views.py

```python
def update(request, pk):
    community = Community.objects.get(pk=pk)

    if request.method == "POST":
        edit_article = CommunityForm(request.POST, instance=community)
        if edit_article.is_valid():
            edit_article.save()
            return redirect('community:index')
    else:
        edit_article = CommunityForm(instance=community)
    context = {
        'edit_article' : edit_article,
    }

    return render(request, 'communities/edit.html', context)
```

- `create`와 비슷, 하지만 `create` 한 정보를 가져와서 form안에 넣어놔야하기 때문에
  - pk값과 일치하는 행의 정보를 가져와서 community라는 변수에 저장하고
  - instance=community로 form에 집어넣어놔야한다

##### 2️⃣ edit.html

```python
# community/templates/communities에 edit.html 생성

{% extends 'base.html' %}
{% block content %}
<div class="container my-5">
  <h3 class="text-primary">글 수정하기</h3>
  <hr>
  <form action="" method="POST" class="fw-bolder">
    {% csrf_token %}
    {{ edit_article.as_p }}
    <div class="d-flex justify-content-end">
    	<button type="submit" class="btn btn-primary text-end">수정</button>
    </div>
  </form>
</div>
{% endblock %}
```

- views에서 edit_article에 form정보를 저장해주었기때문에 `{{ edit_article.as_p }}` 설정

<hr>

<br>