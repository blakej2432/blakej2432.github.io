---
title: "[TIL] 넥사크로 SpringBoot 연동"
date: 2021-02-15 18:40:28 +0900
categories: til
tags: nexacro
header:
  teaser: "../../img/cover/til.png"
---

### 오늘 한 일

#### nexacro 연동 frame과 Base 폴더의 경로를 못찾는 문제 발생

nexacro 예제파일을 Generate해서 Spring boot 프로젝트와 연동하는 작업을 진행하였다. 그런데 resources > static > sample > Base 와 frame 폴더를 찾지 못해서 브라우저에서 에러가 발생하였다. 분명 FrameBase는 잘 찾았는데. 에러는 다음과 같다.

```
Access to XMLHttpRequest at 'frame::rfmLeft.xfdl.js' from origin 'http://localhost' has index.html.1 been blocked by CORS policy...
```

투비소프트에 한팀장님과 반나절 이상 고민했는데 해결법이 너무 간단해서 헛웃음만 나왔다...해결방법은 강력한 새로고침이다.

하는 방법은  `F12` 를 눌러서 개발자도구를 연 후, 크롬창 왼쪽 상단에 새로고침 버튼을 우클릭 후 <u>캐시 비우기 및 강력한 새로고침</u> 을 눌러주면 된다. 아니면 `ctrl+shift+R` 이라는 단축키를 사용하면 된다.



### 오늘 느꼈던 점

- 뻘짓도 경험이지만 너무 뻘짓이었다.
- 이제부터 넥사크로와 병합해서 문제도 많겠지만, 빠르게 끝내자! 화이팅!



### References

https://chocoball3.tistory.com/202
