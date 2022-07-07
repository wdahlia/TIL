#  Git(분산버전관리시스템)

![baby-git-release](git.assets/baby-git-release.png)

> 리누스 토르발스가 개발한 도구로 코드의 버전을 관리, 컴퓨터 파일의 변경사항 추적, 여러 사용자들 간 해당 파일의 작업 조율'



## 기본 흐름

![이름 없는 노트북 (61)-3](git.assets/이름 없는 노트북 (61)-3.jpg)

____



![스크린샷 2022-07-07 오전 8.18.55](git.assets/스크린샷 2022-07-07 오전 8.18.55.png)

#### `$git status`로 확인할 수 있는 파일의 상태

- Tracted : 이전부터 버전으로 관리되고 있는 파일
  - Unmodified : git status에 나타나지 ❎
  - Modified : Changes not staged for commit 
  - Staged : Changes to be commited
- Untracked : 버전으로 관리된 적 없는 파일 (파일 새로 만드는 경우)

_____

## Git 명령어 정리

- `$ git init` :  **로컬 저장소 생성**

____

- `$ git add <파일명>` :  **특정 파일/폴더의 변경사항 추가**
  - `$ git add.`  : **수정한 전체파일 올림**

____

- `$ git commit -m '<커밋메시지>'` :  **커밋 (버전 기록)**

____

- `$ git status ` :  **상태 확인**

____

- `$ git log` :  **버전 확인**

____

- `$ git log --oneline` : **한 커밋 씩 출력**

____

- `$ git config --global user.email "사용자 이메일"`  : **사용자 이메일 설정**

- `$  git config --global user.name "사용자 이름"`  :  **사용자 이름 설정**

____

- `$ git reset HEAD <FILE>` :  **git add한 후 파일 취소**
  - 파일 전부다 취소하고 싶은 경우는 `$ git reset HEAD` 만 입력

____

- `$ find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch` 

  : **git add한 파일 status에 확인했을때 ds.store있는 경우 삭제하고 싶을 때 사용 가능**(단, 파일 위치 경로 확인 잘하고 입력해야함 경로 잘못 입력 시 전체 컴퓨터안의 ds.store 지워질 수 있음)

____

- ```zsh
  # 내 컴퓨터 안의 깃허브 폴더 및 파일들 확인 할 수 있음
  $ git ls-files
  # commit한 폴더 이름 바꾸고 싶을 때
  $ git mv 현재폴더명 원하는폴더명
  $ git add . 
  $ git commit -am "commit 메세지 변경"
  $ git push origin master
  ```

  : **commit한 폴더이름 바꾸고 싶을 때**

____

- ```zsh
  # 방금 한 commit의 메세지 수정하고 싶은 경우
  $ git commit --amend
  # 보통은 vim으로 열림
  # i를 입력후 원했던 commit 메세지로 메세지 수정
  # :wq enter 누르고 종료
  ```

  : **방금 한 commit의 메세지 수정하고 싶을 때**