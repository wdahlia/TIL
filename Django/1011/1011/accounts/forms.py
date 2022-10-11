from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# AUTH_USER_MODEL의 default 값은 'auth.User' 기본적으로 장고가 제공하는 user값
# settings.py에서 디폴트 값을 바꾸고 AUTH_USER_MODEL = 'accounts.User' 어카운트 앱안의 내가 정의한 User class을 사용해줘라
# 이것의 사용은 get_user_model()로 하는 것


# usercreationform 에서는 사용자이름, 비밀번호1, 비밀번호2(비밀번호 1 대조 위한 값)
# 즉, 다시 말해서 상속 받아온 값 이외에도 email값을 추가해주어야한다.
class UserForm(UserCreationForm):
    # email = forms.EmailField(label="email")
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']