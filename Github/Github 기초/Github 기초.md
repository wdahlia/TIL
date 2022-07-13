# GitHub 기초

> Git과 마찬가지로 Github도 버전(커밋)을 관리

```
원격 저장소를 만들고, 로컬 저장소의 커밋을 PUSH해서 원격저장소로 보낸다.
원격 저장소에서 PULL하여 로컬 저장소로도 가져올 수 있다.
```

<br>

## GitHub에서 원격 저장소 생성

<p align="center"><img width="1552" alt="스크린샷 2022-07-10 오후 10 46 22" src="https://user-images.githubusercontent.com/108653518/178147734-477c850b-19c4-4638-9a7d-b703ea01b8ee.png"></p>

- `New repository 생성`

<img width="1508" alt="스크린샷 2022-07-10 오후 10 53 49" src="https://user-images.githubusercontent.com/108653518/178147988-e47da500-fe07-4c23-884d-96b1298905f4.png">

- `저장소 설정하기`

<img width="1552" alt="스크린샷 2022-07-10 오후 10 59 18" src="https://user-images.githubusercontent.com/108653518/178148055-61a293df-2589-4668-b874-f03359ff08a7.png">

- `확인하기` 

  ```diff
  http://github.com/GitHub Username/저장소이름.git
  ```

- `원격저장소 경로 설정`

  ```zsh
  $ git remote(원격저장소) add(추가해) origin(origin으로) {위의 링크} 
  ```

<br>

## Push 실패

<p align=center><img width="456" alt="스크린샷 2022-07-10 오후 11 21 15" src="https://user-images.githubusercontent.com/108653518/178148897-a3e48d29-bade-43be-b8bc-6ca1dea739ae.png"></p>

- 로컬과 원격 저장소의 커밋 이력이 다른 경우 발생하는 것

- **해결방법**

  - 원격저장소의 커밋을 로컬로 가져와서 (PULL)

  - 로컬에서 두 커밋을 병합(추가 커밋 발생) 

  - 다시 GitHub로 PUSH

<br>

## Git Ignore

> 버전관리와 상관 없는 파일 어떻게 관리해야할까?

- 일반적인 개발 프로젝트에 버전 관리를 별도로 하지 않는 파일/디렉토리가 발생
- Git 저장소에 .gitignore 파일을 생성하고 해당 내용을 관리
- 작성 예시
  - 특정 파일 : a.txt (모든 a.txt), test/a.txt (테스트 폴더의 a.txt)
  - 특정 디렉토리 : /my_directory
  - 특정 확장자 : *.exe
  - 예외 처리 : !b.exe

- **주의** : 이미 커밋된 파일은 반드시 삭제를 하여야 .gitignore로 적용
  - 따라서, 프로젝트 시작전에 미리 설정할 것

