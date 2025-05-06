---
title: "[Error] Plugin [id 'org.springframework.boot' version '2.1.8.RELEASE'] was not found in any of the following sources"

date: 2022-04-06 11:00:28 +0900
published: false
categories:
  - error
tags:
  - gradle
  - spring
---



대리님 컴퓨터에서만 빌드가 안돼서 에러메세지를 확인해보니 이런 것이었다.

```
Plugin [id 'org.springframework.boot' version '2.1.8.RELEASE'] was not found in any of the following sources:
```

<br/>

다른 블로그 글들을 찾아보니 buildscript를 추가해주고 어쩌고 `build.gradle` 파일을 변경해줘야 한다는 얘기가 쓰여져 있었다. 하지만 대리님 자리에서만 안되는 거라면 다른 오류라고 생각했다.

그래서 찾아보니 터미널에서 직접 gradle build를 실행해주면 IDE에서 간혹 발생하는 문제를 잡아줄 수 있다는 글을 보고 해보니 해결되었다.

```bash
C:git>wg_xxx>.gradlew build
```

그 전에 다른 방법들을 시도하고 있었어서 이게 직접적인 해결방법은 아니었을 수도 있다.



<br/>

### References

- [Plugin id: 'org.springframework.boot', version: '2.2.4.RELEASE' was not found in any of the following sources:](https://stackoverflow.com/questions/60017092/plugin-id-org-springframework-boot-version-2-2-4-release-was-not-found)

