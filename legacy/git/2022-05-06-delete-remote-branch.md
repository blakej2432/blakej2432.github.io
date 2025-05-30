---
title: "[Git] remote branch 삭제하기"
date: 2022-05-06 13:01:28 +0900
excerpt: "원격저장소에 있는 branch를 삭제해보자."
tags:
  - git
  - branch
categories:
  - git
header:
  teaser: "../../img/cover/git.jpg"
---



###  문제상황

브랜치를 삭제해야한다. 그리고 원격 저장소에 있는 브랜치도 같이 삭제하고 싶다. 



<br/>

### 해결

먼저 원격브랜치를 삭제하고, 로컬에 있는 브랜치를 삭제해준다. 

```bash
$ git push -d <remote_name> <branchname> 	# 원격 브랜치 삭제
$ git branch -d <branchname>			# 로컬 브랜치 삭제
```



<br/>

즉, 원격저장소가 `origin`이고 삭제하고자 하는 브랜치가 `issue1`이라면 이렇게 사용할 수 있다.

```bash
$ git push -d origin issue1
$ git branch -d issue1
```



혹시 로컬 브랜치가 삭제가 되지 않는다면 d를 대문자 D로 바꿔보자

```bash
$ git branch -D issue1
```



<br/>

### References

- [How do I delete a Git branch locally and remotely?](https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely)