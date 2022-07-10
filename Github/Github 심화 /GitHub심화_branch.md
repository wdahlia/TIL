# GitHub 심화 - Branch

[출처](#출처)

> **Branch란?**

- *독립적인 Working Directory*
- 현재의 버전으로 다른 버전(기존 코드를 clone해와 완전히 새로운 독립 공간을 만듦)을 만들어서 가지를 쳐보는 것
- 동일한 소스코드를 기반으로 서로 다른 버전을 만들거나, 서로 다른 작업을 할 수 있다.
- 작업의 용이성, 효율성 극대화

<br>

## Git-flow 전략

- `master` : 최종 배포 가능한 브랜치 (즉, 여기서 배포하는 것이 user의 눈에 보이게 되는 것)
- `Develop` : 다음 출시 버전을 개발하는 브랜치
- `(topic)feature` : 개발에 필요한 버그 수정 및 기능, 테스트버전을 가지치기하여 개발하는 브랜치, 팀원들이 각자 로컬로 작업하고 작업 완료되면 develop 브런치에 merge
- `release` : 이번 출시 버전을 준비하는 브랜치, develop 브랜치에서 merge한 후 배포 위한 최종적인 버그를 수정하는 작업 수행, 최종 배포 상태 완료되면 master 브랜치에 병합시켜 배포
- `hotfix` : 이미 1번 이상 배포한 버전에서 발생한 버그 유지 보수하는 브랜치

![git-flow_overall_graph](https://techblog.woowahan.com/wp-content/uploads/img/2017-10-30/git-flow_overall_graph.png)

<br>

## Branch 관련 용어, 명령어

| 용어                          |                                                              |
| ----------------------------- | ------------------------------------------------------------ |
| `Head`                        | 현재 작업 중인 branch를 가리키는 것 <br><img src="https://user-images.githubusercontent.com/108653518/178107660-82568d91-9fc0-4056-a4cd-74bbb567412e.png" alt="스크린샷 2022-07-09 오후 10.18.34" style="zoom: 67%;" /> |
| `master`                      | -`$ git init`할 때 자동으로 생성해주는 기본 브랜치<br>- 브랜치 따로 생성해주지 않으면 master안에서만 작업하는 것<br>- 보통 팀 프로젝트 시 각자 작업 코드를 하나로 합칠 때 사용하는 브랜치가 됨 |
| `$ git branch{branch}`        | 브랜치 생성 (***주의 : 생성했다고 해서 생성한 브랜치로 이동하는 것은 아님***) |
| `$ git checkout {}`           | 브랜치 이동                                                  |
| `$ git checkout -b {}`        | 브랜치를 생성하면서 그 브랜치로 이동                         |
| `$ git branch`                | 로컬 저장소의 브랜치 목록 ▶️ + -r : 원격 저장소 목록 , + -a : 모든 브랜치 목록 |
| `$ git branch -d {}`          | **로컬 저장소**에서 브랜치 **삭제** (필요하면 원격 브랜치에서 가져올 수 있음) |
| `$git branch -D {}`           | 로컬 브랜치 삭제 시 정상적으로 merge가 되어 있지 않거나, 충돌이 해결되지 않은 브랜치의 경우 강제 삭제 시 사용<br><img width="493" alt="스크린샷 2022-07-10 오후 1 05 57" src="https://user-images.githubusercontent.com/108653518/178130867-716ca619-ff52-4ac8-9f2b-ead0e4c3e7cb.png" style="zoom: 67%;" > |
| `git push origin --delete {}` | **원격저장소**에 올라가 있는 브랜치를 **삭제**할 수 있음     |
| `$ git push origin {}`        | <img src="https://user-images.githubusercontent.com/108653518/178108885-845fd19e-3d03-4bbd-a158-c2176844b1a8.png" alt="스크린샷 2022-07-09 오후 10.54.15" style="zoom:33%;" /><br>- 브랜치 이름을 넣으면 원격저장소에도 별도 관리가 됨<br>- 위의 사진은 이 브랜치는 생성될 때, 즉, 부모 브랜치로부터 복사 받았을 때 1개의 커밋 내역을 가진 상태로 복사를 받았고, 브랜치를 생성한 이후 1145번의 커밋을 했다는 것 |

<br>

## Branch Merge

> 각 branch에서 작업을 한 이후 커밋/버전과 같은 이력들을 합치기 위함

- 병합 진행시, 두 브랜치가 같은 파일의 같은 곳을 수정했다면 충돌(merge conflict)가 발생

  - 오류가 발생한 것이 아닌 작업을 수정하는 과정에서 충분히 생길 수 있는 상황. 수정만 하면 된다.

  ```zsh
  # master 브랜치로 develop 브랜치를 병합할때 (master <- develop)
  (develop) $ git check out master
  (master) $ git merge develop
  ```

<br>

____

### 1. Branch Merge - fast-forward 방식

<p align ="center"><img width="337" alt="스크린샷 2022-07-09 오후 11 11 05" src="https://user-images.githubusercontent.com/108653518/178109471-5af20b5c-21b5-4cc0-a0cf-3995c6d040f3.png" style="zoom: 67%;" >

- 그림의 **보라색**을 `master` 브랜치라고 **초록색**을 `example`이라고 하자

- 이 경우 `example`브랜치는 `master`의 커밋 내역을 전부 다 포함하고 있으며 

  - **`master`은 `example`브랜치가 생겨난 이후 아무 커밋도 하지 않았으므로**
  - `example` 브랜치가 `master` 브랜치보다 더 최신 버전이고 앞서 나간다고 볼 수 있음

- 따라서, `master` 브랜치를 가져와 `test` 브랜치에 병합

- 두 브랜치 병합 시 커밋 내역이 앞서나가고 있는 브랜치로 병합하는 것을 

  - ***fast-forward 방식***이라고 한다.(뒤쳐져 있는 `master`를 빨리감기하여 통합시킴)

  ```zsh
  (master) $ git checkout -b example
  (example) $ git add
  (example) $ git commit -m '커밋메세지'
  
  (example) $ git checkout master
  (master) $ git merge example
  ```

- 현재의 가지는 `master` 이고 두 브랜치는 똑같은 가지가 되었기 때문에 중복이 되므로
  -  `example` 로컬 브랜치는 삭제해주는 것이 좋다
  - (PUSH 한 후 삭제하면 원격 저장소에 `example` 커밋 내역 보존 가능하므로 로컬브랜치로서의 `example`만 삭제하면 된다.)

<br>

### 2. Branch Merge - merge commit

____

<p align ="center"><img width="1044" alt="git-merge" src="https://user-images.githubusercontent.com/108653518/178111421-f7464e92-25ae-4b35-9aae-aa2efb2f7682.png" style="zoom: 67%;" >

- 통합 하려는 두 브랜치가 서로 다른 커밋 내역을 가지고 있는 경우
- 서로 다른 커밋 내역을 가지고 있기 때문에, 동일한 부분을 다르게 코딩했을 가능성 때문에
  - 병합 시 충돌이 발생할 수 있다 (merge conflict)
- fast-foward 방식과 다르게 
  - 분기 후 부모 브랜치에서도 부보 브랜치 본인의 커밋 내역들이 진행되거나
  - 부모 브랜치에서 브랜치가 두개 이상 분기 한 경우 모두 포함
- 사진의 경우 `feat.multiply` , `feat/sum` 두개의 브랜치가 `master` 브랜치로부터 분기하였음
  - `feat/multiply`의 경우 3 커밋 내역 발생, `master` 의 브랜치는 이 경우 #4 커밋 결과물이 반영 되어 통합 되었을 것
  - `feat/sum`의 경우 1 커밋 내역 발생, `master`의 브랜치는 이 경우 #3 커밋 결과물이 반영되어 통합 되었을 것
- 각자 브랜치에서 커밋을 한 후 병합 기준이 될 브랜치로 (여기서는 `master`) 이동하여 merge

<br>

#### Merge Conflict

- 같은 파일의 같은 곳을 수정 했다면 충돌 발생

  - 한글판

    <p align = "center"><img width="456" alt="스크린샷 2022-07-10 오후 12 09 43" src="https://user-images.githubusercontent.com/108653518/178129737-746d2568-4eb6-4028-b406-39e285407047.png">

  - 영문판

    <p align = "center"><img width="635" alt="스크린샷 2022-07-10 오후 12 12 15" src="https://user-images.githubusercontent.com/108653518/178129812-3d359531-94f6-4a64-88a6-f9ac11aabf60.png" style="zoom: 67%;" >

- 충돌 발생 후 `$ git status` 를 하면 충돌 발생한 파일 찾을 수 있음

<p align = "center"><img width="535" alt="스크린샷 2022-07-10 오후 12 15 23" src="https://user-images.githubusercontent.com/108653518/178129903-6e66053f-230f-4098-8293-f558e25b7d09.png">

- 충돌한 파일을 수정

  <p align ="center"><img width="671" alt="스크린샷 2022-07-10 오후 12 19 04" src="https://user-images.githubusercontent.com/108653518/178129954-2dcac70b-d5a4-47de-8596-94229bcc70fe.png" style="zoom:67%;" >

  - < HEAD  부터 == 사이의 구간이 현재 checkout 되어진 (즉 현재 브랜치 위치)의 내용
  - == 부터 > exampe이 병합하려는 대상인 브랜치 코드 내용
  - 정보 참고 두개의 코드 병합 한 후에 특수기호를 전부 다 제거해 주면 됨 
  - 작업이 끝나면 파일 저장하고 add > commit

____

<br>

## Feature Branch Workflow / Forking Workflow

> 저장소의 소유권 유무 [👩🏻‍💻자세한 설명](https://github.com/gmlwjd9405/git-collaboration)

- **Feature Branch Workflow**

  - *원격 저장소의 소유권을 가진 상태* 에서 clone을 통해 저장소를 로컬에 복제
  - 각각의 branch를 생성하여 local에서 작업
  - 기능 구현 후 local에서 remote에 브랜치 반영
  - 풀 리퀘스트 통해 변경 코드 내용하고 마지막 팀원이(전부 소유권 지님) **merge 가능** 👌🏻
  - 그리고 병합된 master의 내용을 pull 한후 로컬 브랜치 삭제
  - 이 과정을 반복
  - [더 자세히 알고 싶다면 ▶️](https://gmlwjd9405.github.io/2017/10/27/how-to-collaborate-on-GitHub-1.html)

- **Forking Workflow**

  - 모든 프로젝트 참여자가 개인적인 로컬 저장소, 공개된 자신의 원격 저장소 = 2개의 Git 저장소 가짐

  - **모든 코드 기여자가 하나의 중앙 저장소에 push하는 것이 아닌, 각자 자신의 원격 저장소에 push 하고, 프로젝트 관리자만 다른 개발자들의 기여분을 중앙 원격 저장소에 병합할 수 있다는 점**

  - 오픈 소스 프로젝트에서 많이 사용하는 방식

  - **방법**

    - 중앙 원격 저장소를 fork해서 자신만의 원격 저장소를 만든다

    <p align ="center"><img width="1045" alt="스크린샷 2022-07-10 오후 12 43 27" src="https://user-images.githubusercontent.com/108653518/178130405-98f164f5-1758-4d91-ab16-0c61d2f8770d.png">

    - `$git clone` 명령으로 자신의 원격저장소에 복제하여 로컬 저장소를 생성 프로젝트 참여자는 이 로컬 저장소에서 작업을 수행한다

      ```zsh
      $ git clone [내 remote repository URL]
      ```

    - 일반적으로 포크한 원격 저장소는 origin(git clone할 때 자동으로 만들어짐),<br>프로젝트 중앙 원격 저장소는 upstream으로 붙이는 것이 일반적

    - 이렇게 해야지 로컬을 프로젝트 중앙 원격 저장소와 같은 상태로 유지가 됨

      ```zsh
      $ git remote add upstream [중앙 원격 저장소 URL]
      ```

    - 기능 추가를 위해 branch 생성하고 작업

    - 구현 후 내 원격 저장소에 브랜치에 push `git push origin [branch name]`

    - pull request해서 중앙 원격 저장소 소유권자가 merge하면 병합 완료된 branch 원격 삭제

    - 병합된 중앙원격 저장소의 내용을 `(master) $git pull upstream master`

    - 원격 저장소에서 병합 완료 된 로컬 브랜치 삭제

    - 위 과정의 반복

    - [더 자세히 알고 싶다면 ▶️](https://gmlwjd9405.github.io/2017/10/28/how-to-collaborate-on-GitHub-2.html)

<br>

<br>

<br>

<br>

<br>

<br>

<br>



## 출처

- <https://ansohxxn.github.io/git/branch/>
- <https://techblog.woowahan.com/2553/>
- <https://victorydntmd.tistory.com/78?category=682764>
- <https://velog.io/@kaitlin_k/branch>
- <https://ifuwanna.tistory.com/284>
- [merge commit 사진 출처](https://inmoonlight.github.io/2021/07/11/Git-merge-strategy/) 

- [fast-forward 방식 사진 출처](https://hyungjoon6876.github.io/jlog/2018/07/08/git-merge-rebase.html)
- [merge conflict 사진 출처](https://opentutorials.org/module/2676/15275)
