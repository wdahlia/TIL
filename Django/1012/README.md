# 221012 실습

`🔒 실습 목차`

<br>

<hr>
## ✔️ 가상환경 설정

### 가상환경 만들기

```python
# venv라는 가상환경 생성
python -m venv venv

# 1012 폴더안에 venv 생성
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

# (venv) 1012 Practice/1012
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

<p align="center"><img width="200" alt="pip_list" src="https://user-images.githubusercontent.com/108653518/195528526-a8f3e729-caf5-4709-9583-b6b5362323c8.png"></p>

<br>

### 프로젝트 생성

```python
django-admin startproject [프로젝트 이름] .
# 현재 위치한 디렉토리 내에서 project를 생성하겠다는 것
# 1012 Practice/1012에 project를 만들겠다는 것

# 프로젝트를 생성하면,
> 1012 Practice
	> 1012
  	> pjt1012
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

```python
'''
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
'''
```

- `runserver` 를 하게 되면 위의 문구가 보이게 되는데

- 이것은 **admin**, **auth**, **contenttypes**, **sessions** 앱들과 관련된 내용이고 이것을 적용하려면 migrate를 실행해야 한다는 내용

  - 이 앱들은 장고 프로젝트 생성시 기본적으로 설치되는 앱

  - `settings.py` 에서 확인 가능

    ```python
    INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
    ]
    ```

  - `'django.contrib.messages'` , `'django.contrib.staticfiles'` 의 경우 데이터베이스와 상관없기에 위의 메시지에는 포함되어있지 않음

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
# 1012 Practice/1012/pjt1012(프로젝트)/settings.py

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

# 1012 Practice/1012/pjt1012(프로젝트)/urls.py
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
>
> 원래 기본 User모델을 사용해도 되지만, 나중에 커스텀 할 가능성을 생각하여 상속받아올 것 장고에서도 적극 권장

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

## ✔️ 구현 

<br>

### Static 생성

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
<!-- Django/1012 Practice/1012/templates/base.html -->
{% load static %}
<!DOCTYPE html>
<html lang="en">

  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>login/logout</title>
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
  - `main.html` : 메인 페이지, 로그인 폼
  - `signup.html` : 회원가입 페이지
  - `index.html` : 회원 목록 페이지
  - `detail.html` : 회원 상세 페이지


```html
<!-- Django/1012 Practice/1012/accounts/templates/accounts/index.html -->
{% extends 'base.html' %}
{% load static %}
{% block nav %}{% endblock %}
{% block content %}
<!-- html 기록 -->
{% endblock %}
```

<br>

### 회원 가입 구현 

<hr>

> **1. 회원 가입 버튼을 클릭**
>
> **2. 회원가입 페이지로 이동하면서 회원가입 Form이 나타남** 
>
> **3. 가입하기를 누르면 메인 페이지로 이동, 회원 목록을 누르면 회원 목록 확인 가능**

<br>

#### 1️⃣ urls.py 

```python
path('', views.login, name="login"),
path('signup/', views.signup, name="signup"),
```

- `urlpatterns`에 회원 가입 버튼이 위치할 path인 `main`과 회원가입 Form을 보여줄 `signup`을 추가

<br>

#### 2️⃣ forms.py

- **UserCreationForm**

  ```python
  # 생성한 가상환경 폴더/lib/python3.9/site-packages/django/contrib/auth/forms.py
  
  from django import forms
  
  class UserCreationForm(forms.ModelForm):
      """
      A form that creates a user, with no privileges, from the given username and
      password.
      """
      error_messages = {
          'password_mismatch': _('The two password fields didn’t match.'),
      }
      password1 = forms.CharField(
          label=_("Password"),
          strip=False,
          widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
          help_text=password_validation.password_validators_help_text_html(),
      )
      password2 = forms.CharField(
          label=_("Password confirmation"),
          widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
          strip=False,
          help_text=_("Enter the same password as before, for verification."),
      )
  
      class Meta:
          model = User
          fields = ("username",)
          field_classes = {'username': UsernameField}
  
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          if self._meta.model.USERNAME_FIELD in self.fields:
              self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True
  
      def clean_password2(self):
          password1 = self.cleaned_data.get("password1")
          password2 = self.cleaned_data.get("password2")
          if password1 and password2 and password1 != password2:
              raise ValidationError(
                  self.error_messages['password_mismatch'],
                  code='password_mismatch',
              )
          return password2
  
      def _post_clean(self):
          super()._post_clean()
          # Validate the password after self.instance is updated with form data
          # by super().
          password = self.cleaned_data.get('password2')
          if password:
              try:
                  password_validation.validate_password(password, self.instance)
              except ValidationError as error:
                  self.add_error('password2', error)
  
      def save(self, commit=True):
          user = super().save(commit=False)
          user.set_password(self.cleaned_data["password1"])
          if commit:
              user.save()
          return user
  ```

- **UserCreationForm은 forms의 ModelForm을 상속 받고 있다**

  ```python
  class UserCreationForm(forms.ModelForm):
  ```

  - password1과 password2 input을 2가지 받아서 2개가 같은지 검증하기 위해 2개의 필드를 추가하기 위하여 상속받아 커스텀한 것

- **내부적으로 User를 받는다**

  ```python
  class Meta:
          model = User
  ```

  - 이 부분에서 Model을 User로 받게 되는데 **이때의 User은 auth.User**로 이미 **장고 내부적으로 설정**이 되어있기에
  - migrate 전에 models.py 설정에서 AbstractUser을 import해서 내가 만든 User로 모델을 설정 후 
  - settings.py에서 경로 설정을 마친다음 migrate를 해야한다

<br>

```python
# accounts 앱 안에 forms.py 파일 생성

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# 현재 디렉토리의 models.py에서 Community 클래스를 불러와준다.

class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
```

- `from django.contrib.auth import get_user_model`
  - **`venv/lib/python3.9/site-packages/django/contrib/auth/__init_.py/get_user_model`**
  - *Return the User model that is active in this project.*
  - 즉, 말하자면 내가 AUTH_USER_MODEL에 정해준 model을 불러오는 것
  - 내가 정의한 user model을 변수화 한 것
- `class Meta`  
  - '데이터에 대한 데이터' 혹은 '다른 데이터를 설명해주는 데이터'
  - 상위 클래스에 meta 데이터를 제공해주는 것
- `fields` :
  - form을 만들때 입력받을 fields를 선택해준다. 전부 다 입력 받고 싶다면 `'__all__'` 을 입력해주면 된다

<br>

#### 3️⃣ main.html

- 회원 가입 버튼을 클릭하여야 하기 때문에, `main.html`을 구성해주어야함

```python
# accounts/views.py

def login(request):
    return render(request, 'accounts/main.html')
```

- `templates/accounts`에 생성한 `main.html`의 `{% block content %}` `{% endblock %} ` 사이에

```python
{% extends 'base.html' %}
{% load static %}

{% block nav %}{% endblock nav %}
{% block content %}

  <div class="container site-size d-flex flex-column justify-content-center align-items-center mt-5">
    <img src="{% static 'image/logo.png' %}" class="img-size mb-5">
    <a href="{% url 'account:signup' %}" class="me-5 text-decoration-none text-center">
      <div class="btn btn-light">회원 가입</div>
    </a>
  </div>

{% endblock content %}
```

- a 태그로 감싸주고 a태그의 hyper reference는 `accounts 앱`안의 `name이 signup인 path를 실행`시켜달라는 뜻

<br>

#### 4️⃣ signup.html

- 회원가입 버튼을 클릭하였을때, form을 보여줄 html을 생성해야함 여기서는 `signup.html`이라고 정의하였음

```python
{% extends 'base.html' %}
{% load static %}
{% load django_bootstrap5 %}

{% block nav %}{% endblock nav %}
{% block content %}

  <div class="container-size d-flex justify-content-center align-items-center">
    <form action="" method="POST" class="mx-4 fw-semibold border border-3 rounded-2 form-size p-5">
      {% csrf_token %}
      {% bootstrap_form signup_list %}
      <div class="text-end">
        <input type="submit" class="btn btn-dark" value="회원가입">
      </div>
    </form>
  </div>

{% endblock content %}
```

- `<form>`태그의 *action = "**URL**"*
  - 폼 데이터(form data)를 서버로 보낼 때 해당 데이터가 도착할 URL을 명시
- `<form>`태그의 *method = "**GET | POST**"*
  -  폼 데이터(form data)가 서버로 제출될 때 사용되는 HTTP 메소드를 명시
- `{% csrf_token %}`
  - ***CSRF*** - **C**ross **S**ite **R**equest **F**orgery
  - [CSRF 참고 사이트](https://chagokx2.tistory.com/49)
  - 장고에서 기본적으로 csrf_token을 이용하면 공격을 방어할 수 있음
- `{% bootstrap_form signup_list %}`
  - 부트스트랩 form을 적용, 이때 signup_list는 views.py의 signup함수에서 받아온 값
  

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

#### 5️⃣ views.py

- `urls.py`에 path안에 `views.signup(views의 signup 함수를 실행시켜 달라고하는 의미) ` 을 실행해야 하기에
- `views.py`에 `signup 함수`를 정의해주어야함
- (참고) 만약 signup함수를 정의해주지 않는다면,
  - **AttributeError: module 'accounts.views' has no attribute 'signup'**
  - 이름이 잘못되거나 없는 속성을 가져오려면 나오는 에러
  - 모듈 accounts.views에는 signup 속성이 없다는 뜻

```python
def signup(request):
    if request.method == "POST":
      # 요청받은 method가 post라면
        signup_list = CustomUserCreationForm(request.POST)
        # forms.py에서 정의해준 CustomUserCreationForm에 받아온 값들을 signup_list에 할당
        if signup_list.is_valid():
          # 유효성 검사에 통과하면
            signup_list.save()
            # db에 저장
            return redirect('account:login')
          # app_name을 account로 정의 account의 name이 login인 path를 실행
          	'''
          	def main(request):
          	return render(request, 'accounts/main.html')
          	'''

    else:
        signup_list = CustomUserCreationForm()
    
    context = {
        'signup_list' : signup_list,
    }

    return render(request, 'accounts/signup.html', context)
```

- 즉, 버튼을 눌러 submit이 되어질때 request가 일어나게 되는것인데 이때의 요청이 POST라면
  - 유효성 검사를 하여 통과하게 되면 그 결과를 데이터베이스에 저장해주고 main이라는 함수를 실행시켜준다.
  - main이라는 함수는 accounts/main.html을 렌더해주는 역할
  - 회원가입을 하게되고 유효성 검사를 통과하게 되면, 우리는 메인 창으로 돌아가서 로그인을 할 수 있도록 해준다

- 만약, **유효성 검사에 실패**한다면
  - 다시 signup.html을 렌더해준다
  - 즉 `signup_list`은 여기서  form 양식이라고 생각하면 된다 (우리가 forms.py에서 정의해주었던 그 폼)

<p align="center"><img src="https://user-images.githubusercontent.com/108653518/195528550-e49b4e2a-2af2-4e16-9d71-f4dabfed1f4f.png" alt="signup"  /></p>

<br>

### 로그인 / 로그아웃 구현

<hr>

>**1. main.html에 로그인 form 생성**
>
>**2. 로그인 상태일 경우 로그인 한 사용자의 username을 출력**
>
>**3. username을 클릭하면 해당 회원 조회 페이지로 이동**
>
>**4. 회원 조회 페이지에 로그아웃 버튼**
>
>**5. 네비게이션 바에도 로그아웃 버튼**

<br>

#### 로그인

#### 1️⃣ urls.py

- `main`에 로그인 form을 보여줄 것이기 때문에 추가할 필요 없음

<br>

#### 2️⃣ views.py

```python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login # 로그인 함수와 이름이 겹치기 때문

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) # data는 forms.form의 두번째 인자로 생략 가능
        if form.is_valid(): # form이 유효성 검사에서 통과하면
            auth_login(request, form.get_user())
            return redirect('account:main')
    else:
        form = AuthenticationForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/main.html', context)
```

- AuthenticationForm으로 등록된 회원인지를 확인후
- 유효성 검사에서 통과하게 되면 login을 한다음 main으로 redirect

> **참고**

- **AuthenticationForm**

  - 로그인을 위한 built-in form

  - 로그인 하고자 하는 사용자 정보를 입력 받음(username, password)

  - ModelForm이 아닌 일반 Form을 상속 받고 있으며, request를 첫번째 인자로 취함

  - **유저가 존재하는지를 검증할 뿐, 세션과는 무관함**

    ```python
    class AuthenticationForm(forms.Form):
        """
        Base class for authenticating users. Extend this to get a form that accepts
        username/password logins.
        """
        username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
        password = forms.CharField(
            label=_("Password"),
            strip=False,
            widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        )
    
        error_messages = {
            'invalid_login': _(
                "Please enter a correct %(username)s and password. Note that both "
                "fields may be case-sensitive."
            ),
            'inactive': _("This account is inactive."),
        }
    
        def __init__(self, request=None, *args, **kwargs):
            """
            The 'request' parameter is set for custom auth use by subclasses.
            The form data comes in via the standard 'data' kwarg.
            """
            self.request = request
            self.user_cache = None
            super().__init__(*args, **kwargs)
    
            # Set the max length and label for the "username" field.
            self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
            username_max_length = self.username_field.max_length or 254
            self.fields['username'].max_length = username_max_length
            self.fields['username'].widget.attrs['maxlength'] = username_max_length
            if self.fields['username'].label is None:
                self.fields['username'].label = capfirst(self.username_field.verbose_name)
    
        def clean(self):
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
    
            if username is not None and password:
                self.user_cache = authenticate(self.request, username=username, password=password)
                if self.user_cache is None:
                    raise self.get_invalid_login_error()
                else:
                    self.confirm_login_allowed(self.user_cache)
    
            return self.cleaned_data
    
        def confirm_login_allowed(self, user):
            """
            Controls whether the given User may log in. This is a policy setting,
            independent of end-user authentication. This default behavior is to
            allow login by active users, and reject login by inactive users.
    
            If the given user cannot log in, this method should raise a
            ``ValidationError``.
    
            If the given user may log in, this method should return None.
            """
            if not user.is_active:
                raise ValidationError(
                    self.error_messages['inactive'],
                    code='inactive',
                )
    
        def get_user(self):
            return self.user_cache
    
        def get_invalid_login_error(self):
            return ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name},
            )
    ```


- **get_user(request)**

  ```python
  def get_user(request):
      """
      Return the user model instance associated with the given request session.
      If no user is retrieved, return an instance of `AnonymousUser`.
      """
      from .models import AnonymousUser
      user = None
      try:
          user_id = _get_user_session_key(request)
          backend_path = request.session[BACKEND_SESSION_KEY]
      except KeyError:
          pass
      else:
          if backend_path in settings.AUTHENTICATION_BACKENDS:
              backend = load_backend(backend_path)
              user = backend.get_user(user_id)
              # Verify the session
              if hasattr(user, 'get_session_auth_hash'):
                  session_hash = request.session.get(HASH_SESSION_KEY)
                  session_hash_verified = session_hash and constant_time_compare(
                      session_hash,
                      user.get_session_auth_hash()
                  )
                  if not session_hash_verified:
                      if not (
                          session_hash and
                          hasattr(user, '_legacy_get_session_auth_hash') and
                          constant_time_compare(session_hash, user._legacy_get_session_auth_hash())
                      ):
                          request.session.flush()
                          user = None
  
      return user or AnonymousUser()
  ```

<br>

#### 3️⃣ main.html

```html
{% extends 'base.html' %}
{% load static %}
{% load django_bootstrap5 %}

{% block nav %}{% endblock nav %}
{% block content %}
  <div class="container site-size d-flex flex-column justify-content-center align-items-center mt-5">
    <img src="{% static 'image/logo.png' %}" class="img-size mb-5">
    
    <!-- 로그인 상태일 때-->
    {% if request.user.is_authenticated %}
      <div class="p-4 border border-2 border-dark border-style rounded-3 animate__animated animate__fadeIn">
        <p class="text-center">
          <span class="text-decoration-underline fw-bolder">{{ user }}</span>
          님 안녕하세요!
        </p>
        <!-- 로그인 상태이면 (user 이름)님 안녕하세요 보여줌 -->
        <div class="text-center"><img src="{% static 'image/user.png' %}"></div>
        <h3 class="mt-2 text-center text-space">{{ user }}</h3>
       	<div class="d-flex justify-content-between mt-3">
          <form action="{% url 'account:logout' %}" method="POST">
            {% csrf_token %}
            <input class="btn btn-danger" type="submit" value="로그아웃">
          </form>
          <a href="" class="ms-2 text-decoration-none btn btn-warning">내 정보</a>
        </div>
      </div>
    
    <!-- 비로그인 상태일 때-->
    {% else %}
      <div class="p-4 border border-1 border-dark border-style rounded-3">
        <p class="text-center">
          <span class="text-decoration-underline fw-bolder">비회원</span>
          님 안녕하세요!
        </p>
        <!-- 비로그인 상태이면 비회원님 안녕하세요 보여줌 -->
        <form action="" method="POST">
          {% csrf_token %}
          {% bootstrap_form form %}
          <div class="d-flex justify-content-end">
            <input class="btn btn-dark" type="submit" value="로그인">
            <a href="{% url 'account:signup' %}" class="text-decoration-none ms-3">
              <div class="btn btn-light">회원 가입</div>
            </a>
          </div>
        </form>
      </div>
      
    {% endif %}
  </div>

{% endblock content %}
```

- `request.user.is_authenticated` 
  - 즉, 로그인과 비그로인 상태에서 출력되는 링크를 다르게 설정
  - `로그인 시` : user 이름과 함께 프로필 창이 나타나고 로그아웃(logout)과 회원정보(detail) 버튼 표시
  - `로그아웃/비로그인 상태` : 로그인창과 회원가입창이 나타남

- `is_authenticated` :
  - User Model의 속성 중 하나
  - **사용자가 인증 되었는지 여부**를 알 수 있음
  - User 인스턴스에 대해 항상 True
    - AnoymousUser에 대해서는 항상 False

  - 권한, 유효한 세션인지 활성화 상태인지는 확인하지 않음


<p align="center"><img src="https://user-images.githubusercontent.com/108653518/195528540-96567335-4569-4562-8b23-6511f6146d63.gif" alt="login"  /></p>

<br>

#### 로그아웃

#### 1️⃣ urls.py

```python
path('logout/', views.logout, name="logout"),
```

- `logout` 함수를 실행시키는 `logout`이라는 이름의 url을 urlpatterns에 추가

<br>

#### 2️⃣ main.html

```python
{% if request.user.is_authenticated %}
								.....
<div class="d-flex justify-content-between mt-3">
	<form action="{% url 'account:logout' %}" method="POST">
		{% csrf_token %}
	 	<input class="btn btn-danger" type="submit" value="로그아웃">
	</form>
	<a href="" class="ms-2 text-decoration-none btn btn-warning">내 정보</a>
</div>
								.....
```

- 로그인 했을 때, main 페이지에 회원 정보 페이지를 보여주고 로그아웃과 상세 정보 버튼을 보여주므로
- 로그아웃 버튼을 눌렀을때 logout함수를 실행시켜주도록 form action에 url을 추가해준다

#### 3️⃣ views.py

```python
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('account:login')
```

- **logout**

  ```python
  def logout(request):
      """
      Remove the authenticated user's ID from the request and flush their session
      data.
      """
      # Dispatch the signal before the user is logged out so the receivers have a
      # chance to find out *who* logged out.
      user = getattr(request, 'user', None)
      if not getattr(user, 'is_authenticated', True):
          user = None
      user_logged_out.send(sender=user.__class__, request=request, user=user)
      request.session.flush()
      if hasattr(request, 'user'):
          from django.contrib.auth.models import AnonymousUser
          request.user = AnonymousUser()
  ```

<br>

<p align="center"><img src="https://user-images.githubusercontent.com/108653518/195528531-e20f7c61-e06c-4619-bb34-1c72700deb49.gif" alt="logout"  /></p>

### user의 상세 정보 페이지

<hr>
#### DETAIL 구현

> **1. 로그인 이후 내 정보를 클릭하면**
>
> **2. Detail 페이지로 이동하면서 내 정보와 관련된 상세 항목들이 나온다**

<br>

#### 1️⃣ urls.py

```python
path('<int:user_pk>/detail/', views.detail, name="detail"),
```

- `urlpatterns`에 `<int:user_pk>/detail/` 이라는 경로를 추가해준다
- 이 때, 다른점은 pk 값을 받아오는것
  - pk와 id는 같다

<br>

#### 2️⃣ views.py

```python
from django.contrib.auth.decorators import login_required
# 로그인 했을 때만, 내 정보 조회 가능하게 만들기
@login_required
def detail(request, user_pk):
    user_detail = get_user_model().objects.get(pk=user_pk)
    # id값과 user_pk 받아온 값이 같은 db안의 row를 user_detail이라는 변수에 할당

    context = {
        'user_detail' : user_detail,
    }

    return render(request, 'accounts/detail.html', context)

```

- `from django.contrib.auth.decorators import login_required` 를  import하고

- **@login_required를 주석처리 했을때, 실행결과**

  ![required_before](https://user-images.githubusercontent.com/108653518/195528583-a9f37e2c-6194-41fb-9aac-7c13a71b0456.png)

  - `localhost:8000/2/detail/`을 입력하면 로그인이 안되어있는 상태에서도 창을 띄우게 된다

- **@login_required를 써주었을때, 실행결과**

  ![required_after](https://user-images.githubusercontent.com/108653518/195528578-780516f0-c3d6-4fdd-b22e-8510a5075c41.png)

  - `localhost:8000/2/detail/`를 입력하면 `http://localhost:8000/accounts/login/?next=/2/detail/` 이런식으로 보여주면서 Page not found를 보여준다

<br>

#### 3️⃣ detail.html

```python
# accounts/templates/accounts에 detail.html 생성

{% extends 'base.html' %}
{% load static %}

{% block content %}

  <div class="container my-5 text-space">
    <div class="border border-secondary rounded-3 p-4 bg-light">
      <h1>{{ user_detail.username }}</h1>
      <h6 class="fw-lighter">{{ user_detail.last_name }}{{ user_detail.first_name }}</h6>
      <hr>
      <h4 class="text-primary fw-light">
        <i>{{ user_detail.email }}</i>
      </h4>
      <br>
      {% if user_detail.last_login == NULL %}
        <div class="list-group">
          <a href="" class="list-group-item list-group-item-action fw-bolder">{{ user_detail.username }}의 정보
          </a>
          <a href="" class="list-group-item list-group-item-primary">최근 로그인 :
          </a>
          <a href="" class="list-group-item list-group-item-success">회원가입 :
            {{ user_detail.date_joined }}</a>
        </div>
      {% else %}
        <div class="list-group">
          <a href="" class="list-group-item list-group-item-action">{{ user_detail.username }}의 정보
          </a>
          <a href="" class="list-group-item list-group-item-primary">최근 로그인 :
            {{ user_detail.last_login }}</a>
          <a href="" class="list-group-item list-group-item-success">회원가입 :
            {{ user_detail.date_joined }}</a>
        </div>
      {% endif %}
    </div>
  </div>

{% endblock content %}

```

<p align="center"><img src="https://user-images.githubusercontent.com/108653518/195528573-7609cd99-4607-4c3b-b6bc-9798a38b1bd5.png" alt="detail"  /></p>

<hr>

<br>