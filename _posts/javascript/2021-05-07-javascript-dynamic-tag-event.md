---
title: "[Javascript] 동적으로 생성된 태그에 이벤트 걸기"
date: 2021-05-07 23:58:28 +0900
categories: javascript
---

이벤트를 먼저 선언을 해준 후에, ajax로 데이터를 받아서 화면에 뿌려주는 경우를 생각해보자.
그러면 앞서 이벤트에 있는 태그들이 선언 당시에는 태그들이 존재하지 않았기 때문에, 태그들이 동적으로 생성된 후에도 제대로 동작하지 않는 경우들이 생긴다.



예를 들어 다음과 같은 경우이다.

```javascript
$('#tablist02').on("click", function(e){
 	// 원하는 코드   
}
```



그럴 때는 다음과 같이 `off` 한 후 다시 `on`하는 식의 방법으로 해결할 수 있다.

```javascript
$('body').off("click", '#tablist02').on("click", '#tablist02', function(e){
 	// 원하는 코드   
}
```



### 👻 느낀점 

아직도 javascript 공부가 부족하다고 느낀다. 처음엔 hoisting 문제인지, garbage collection 문제인지를 고민했는데...ㅎㅎ 물어보니 금방해결이 되었다.



### References

- [악덕고용주의 개발 일기 - 동적으로 생성된 태그에 이벤트 걸기]( https://rongscodinghistory.tistory.com/41)

