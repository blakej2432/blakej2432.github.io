---
title: "[javascript] Bootstrap에서 Flex로 div 가운데 정렬하기"
date: "2021-02-26 18:30:30 +0900"
categories: javascript
tags: bootstrap
---



아직도 부트스트랩을 잘 쓰지를 못해서...ㅠㅜ정렬할 때마다 너무 힘들다. 그래서 오늘 한 내용만 간단히 정리하고 내용을 모아서 하나의 포스팅으로 작성해볼 예정이다.

- `d-flex`
- `justify-content-center`

  - 가로중에서 가운데에 정렬하는 속성
  - `<div class="d-flex justify-content-end>` 로 썼다면 하위에 있는 요소들이 가운데로 정렬된다.
  - `center` 외에도 `start`, `end` ,`between` 등으로 바꿔서 쓸 수 있다.
- `align-self-center`
  - 자기 자신을 부모요소를 기준으로 세로중에서 가운데에 정렬하는 속성


```html
<div class="d-flex justify-content-center">
    <div class="p-2">A</div>
    <div class="p-2">B</div>
    <div class="p-2">C</div>
</div>

<div class="d-flex">
    <div class="align-self-center">
        Good!
    </div>
    <div class="align-self-center">
        Better!
    </div>
</div>
```



### 오늘 한 일

강사님에게 채팅 페이지가 마치 i7성능의 컴퓨터에 486의 바디를 입힌 것 같다고 한소리를 들은 후에, 미루고 미루던 디자인을 수정했다. 나름 깔끔하게 나온 것 같아서 만족 중 :)
그렇지만 프론트는 너무 어렵다...흐어...

<img src="/img/210226_chat.png" alt="210226_chat" style="zoom: 50%;"/>

### References

[Bootstrap Flex 공식문서](https://getbootstrap.com/docs/4.0/utilities/flex/)

[css로 svg 색상 제어하기](https://blogpack.tistory.com/812)

[스크롤바 js](https://bit.ly/3pYpca9)
