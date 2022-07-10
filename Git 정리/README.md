#  Git(분산버전관리시스템)

> [참고 링크](#참고-링크)

![baby-git-release](git.assets/baby-git-release.png)

> 리누스 토르발스가 개발한 도구로 코드의 버전을 관리, 컴퓨터 파일의 변경사항 추적, 여러 사용자들 간 해당 파일의 작업 조율



## 기본 흐름

![이름 없는 노트북 (61)-3](https://user-images.githubusercontent.com/108653518/177679105-c65e4434-838e-4368-90cb-a71f88998f3f.jpg)

____



![스크린샷 2022-07-07 오전 8.18.55](https://user-images.githubusercontent.com/108653518/177679265-cd1bdae9-101e-45a3-abed-c2036b57739f.png)

#### `$git status`로 확인할 수 있는 파일의 상태

- Tracted : 이전부터 버전으로 관리되고 있는 파일
  - Unmodified : git status에 나타나지 ❎
  - Modified : Changes not staged for commit 
  - Staged : Changes to be commited
- Untracked : 버전으로 관리된 적 없는 파일 (파일 새로 만드는 경우)

_____

<br>

## Git 명령어 정리

- `$ git init` :  **로컬 저장소 생성**

<br>

- `$ git add <파일명>` :  **특정 파일/폴더의 변경사항 추가**
  - `$ git add.`  : **수정한 전체파일 올림**

<br>

- `$ git commit -m '<커밋메시지>'` :  **커밋 (버전 기록)**

<br>

- `$ git status ` :  **상태 확인**

<br>

- `$ git log` :  **버전 확인**

<br>

- `$ git log --oneline` : **한 커밋 씩 출력**
- `$ git log --oneline --graph` : `한 줄 그래프 형태로 commit 히스토리 보기`

<br>

- `$ git config --global user.email "사용자 이메일"`  : **사용자 이메일 설정**
- `$ git config --global user.name "사용자 이름"`  :  **사용자 이름 설정**
- `$ git config --global --list`

<br>

- `$ git push origin 브랜치명` : **저장소에 commit 반영하기**
- `$ git push -u origin 브랜치명` 
  - **-u 옵션은 upstream repository 설정 즉, 한번 설정하면 git push, git pull만 간단하게 쓰면됨**
- `$ git pull origin 브랜치명` : **저장소에서 commit 가져오기**

<br>

- `$ git fetch --prune` : **remote에서 삭제된 branch를 local에서도 깔끔하게 삭제**

<br>

- reset 명령은 주의하여 사용
  - `$ git reset` - **Staged 상태의 파일을 Unstage로 변경**
  - `$ git reset --hard [commit]` 
    - **staging area가 초기화되고 working tree를 특정 커밋 시점으로 덮어쓰기**
  
  - `$ git reset --hard HEAD^`
    - **이전 Head 시점으로 초기화 working directory, 최근 commit 이력이 삭제된다.**
  

<br>

- `$ find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch` 

​		: **git add한 파일 status에 확인했을때 ds.store있는 경우 삭제하고 싶을 때 사용 가능**<br>		(단, 파일 위치 경로 확인 잘하고 입력해야함 경로 잘못 입력 시 전체 컴퓨터안의 ds.store 지워질 수 있음)

<br>

> **commit한 폴더이름을 바꾸고 싶을 때**

```zsh
# 내 컴퓨터 안의 깃허브 폴더 및 파일들 확인 할 수 있음
$ git ls-files
# commit한 폴더 이름 바꾸고 싶을 때
------------------------------------
$ git mv 현재폴더명 원하는폴더명
= $ git rm 현재폴더명
= $ git add 원하는 폴더명
------------------------------------
$ git add . 
$ git commit -m "commit 메세지 변경"
$ git push origin master
```
or `recommend` : 
파일, 폴더이름 바꾸고 싶을 때 새로운 폴더 파일 생성 후 다시 commit 후 push



<br>

> **방금 한 commit의 메세지 수정하고 싶을 때**

```zsh
# 방금 한 commit의 메세지 수정하고 싶은 경우
$ git commit --amend
# 보통은 vim으로 열림
# i를 입력후 원했던 commit 메세지로 메세지 수정
# :wq enter 누르고 종료
```

: **방금 한 commit의 메세지 수정하고 싶을 때**

<br>

> **이미 push한 파일 지우기**

```zsh
# local저장소 파일 삭제
$ git rm [File Name]

# remote한 원격저장소 파일 삭제
$ git rm --cached [File Name]

# 특정 파일 삭제
$ git rm --cached .폴더이름/파일이름

# 폴더 하위의 모든 파일 삭제
$ git rm --cached -r 폴더이름

# 이후 $git status로 파일 deleted 확인 이후 이 상태를 remote에 적용
$ git commit -m '커밋 메세지'
$ git push origin master
```

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>

## 참고 링크

- 멀티캠퍼스 실무 맞춤형 풀스택 과정
- <https://makemethink.tistory.com/163>
- https://wecandev.tistory.com/152