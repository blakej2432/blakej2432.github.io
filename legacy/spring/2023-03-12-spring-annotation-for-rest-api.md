---
title: "[Spring] REST API에서 사용되는 Spring 어노테이션 정리 (@RequestBody, @ModelAttribute, @RequestParam)"
date: 2023-03-12 21:01:28 +0900
excerpt: "REST API에서 사용되는 Spring 어노테이션에 대해서 알아보자."
tags:
  - network
  - http
categories:
  - spring
header:
  teaser: "../../img/cover/spring.png"

---


### REST API

업무를 하다보면 가장 많이 사용하는 것 중 하나가 바로 REST API일텐데요. 하지만 막상 설명을 하려고 하면 말문이 막히는 것 중에 하나가 또 REST API 라고 할 수 있습니다. (제가 아직 부족해서 그런걸 수도 있습니다ㅎㅎ) 

그래서 Java/Spring으로 API 작성시 많이 사용되는 어노테이션과 그 차이점을 짚고 넘어가고자 본 포스팅을 작성하게 되었습니다.

본문은 REST API에서 사용되는 어노테이션에 대해서 정리하고 있습니다. 
REST API에 대한 기본 개념 및 올바른 활용법은 아래 링크에 잘 정리되어 있습니다.

-  [[네트워크] REST API란? REST, RESTful이란?](https://khj93.tistory.com/entry/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-REST-API%EB%9E%80-REST-RESTful%EC%9D%B4%EB%9E%80)
-   [REST API 제대로 알고 사용하기](http://meetup.toast.com/posts/92)
-   [REST 아키텍처를 훌륭하게 적용하기 위한 몇 가지 디자인 팁](https://spoqa.github.io/2012/02/27/rest-introduction.html)


클라이언트에서 넘어오는 정보들을 바인딩하기 위해서 `@RequestBody`, `@ModelAttribute`, `@RequestParam` 를 사용할 수 있습니다. 



<br/>

### 1. @RequestBody

`@RequestBody`는 클라이언트에서 JSON(application/json) 이나 XML 포맷으로 요청한 HTTP Body에 담긴 정보를 매핑할 때 사용합니다. 저도 주로 POST에서 JSON으로 보내는 객체를 바인딩하기 위해서 `@RequestBody`를 사용하고 있습니다. 

**추가적인 이야기 1)**

현재 HTTP 스펙으로는 GET 방식에서도 Body를 사용할 수 있으므로 GET에서 Body를 매핑할 때 `@RequestBody` 를 사용할 수 있지만, 권장되는 방식은 아닌 것 같습니다. 
관련 내용이 궁금하시면 다음 [스택오버플로우](https://stackoverflow.com/questions/978061/http-get-with-request-body)의 답변들을 참고할 수 있을 것 같습니다.

**추가적인 이야기 2)**

참고로 `@RequestBody`로 받는 데이터는 MappingJackson2HttpMessageConverter를 통해 Java 객체로 변환됩니다. 해당 컨버터는 내부적으로 ObjectMapper를 사용해 JSON 값을 Java 객체로 역직렬화합니다. 따라서 @RequestBody를 사용하는 객체는 생성자나 setter가 필요하지 않습니다. 다만, 직렬화를 위한 기본 생성자는 필수이며, ObjectMapper가 getter 또는 setter를 참조하여 필드명을 알아내기 때문에 둘 중 1가지는 정의되어 있어야 합니다.
자세한 내용은 [여기](https://tecoble.techcourse.co.kr/post/2021-05-11-requestbody-modelattribute/) 를 참고하시면 좋을 것 같습니다.

```java
@PostMapping("/requestBody")
public ResponseEntity<User> requestBody(@RequestBody User user) { 
	return ResponseEntity.ok(board); 
}
```



<br/>

### 2. @ModelAttribute

`@ModelAttribute`는 클라이언트에서 폼(form) 형태의 HTTP Body와 쿼리스트링을 생성자나 Setter로 바인딩하기 위해 사용됩니다. 

스프링 MVC는 @ModelAttribute가 있는 경우 다음과 같은 과정을 거치게 됩니다.
1. User 객체를 생성합니다.
2. 요청 파라미터의 이름과 같은 User 객체의 프로퍼티를 찾습니다.
3. 해당 프로퍼티의 setter를 호출하여 파라미터의 값을 입력합니다.



@RequestBody와 @ModelAttribute는 클라이언트에서 요청한 데이터를 Java 객체로 변환시켜준다는 **공통점**이 있습니다. 그렇다면 어떤 **차이점**이 있는걸까요? **간단히 말하면 @ModelAttribute는 파라미터로 전달된 데이터를 처리하고, @RequestBody Body로 전달된 데이터를 처리합니다.** 다음은 정상 바인딩 되는 경우와 그렇지 않은 경우입니다.

 - `/modelAttribute1?userId=10&userName=jin` 처럼 쿼리스트링으로 보내는 경우  ✅
 - `x-www-form-url-encoded` 같이 Form 형식으로 보내는 경우  ✅
 - `application/json` 타입으로 보내는 경우 ❌


```java
@GetMapping("/modelAttribute1") 
public ResponseEntity<User> modelAttribute1(@ModelAttribute User user) { 
	return ResponseEntity.ok(board); 
}

@PostMapping("/modelAttribute2") 
public ResponseEntity<User> modelAttribute2(@ModelAttribute User user) { 
	return ResponseEntity.ok(board); 
}

@PostMapping("/modelAttribute2") 
public ResponseEntity<User> modelAttribute2(User user) { 
	// @ModelAttribute를 생략해도 바인딩됩니다.
	return ResponseEntity.ok(board); 
}
```



<br/>

### 3. @RequestParam

`@RequestParam`은 1개의 HTTP 요청 파라미터를 받기 위해서 사용합니다. `@RequestParam`은 필수 여부가 true이기 때문에 반드시 해당 파라미터가 전송되어야 하며, 파라미터가 전송되지 않으면 400 에러가 발생합니다. 반드시 필요한 값이 아니라면 required를 false로 설정해주면 되고, defaultValue 옵션을 사용하면 기본값 역시 지정할 수 있습니다. 
다음은 여러 형태로 사용한 `@RequestParam`의 예시입니다.
```java
@GetMapping("/requestParam1") 
public ResponseEntity<List<User>> requestParam1( @RequestParam String userId) { 
	// @RequestParam으로 1개의 요청 파라미터를 받을 수 있습니다.
	return ResponseEntity.ok(userService.getUsers(userId)); 
}

@GetMapping("/requestParam2") 
public ResponseEntity<List<User>> requestParam2(String userId) { 
	// @RequestParam을 생략해도 String, int 같은 타입의 경우 자동으로 @RequestParam으로 처리됩니다.
	return ResponseEntity.ok(userService.getUsers(userId)); 
}

@GetMapping("/requestParam2") 
public ResponseEntity<List<User>> requestParam2( @RequestParam(value = "userId", required = false, defaultValue = "user1") String searchKeyWord) { 
	// reuqired나 defaultValue 등 여러 옵션을 주고 싶은 경우 위와 같이 작성할 수 있습니다.
	return ResponseEntity.ok(userService.getUsers(userId)); 
}
```





<br/>

### 마무리하며
너무 기초적인 내용을 정리하는게 아닌가 싶었는데, 찾아보고 생각보다 동작원리를 뜯어보면서 몰랐던 내용들이 많았습니다.  흔히 스프링과 어노테이션을 사용하다보면 알아서 해줘서 정확히 알지 못하는 경우가 많은데, 이런 기초가 부실할수록 문제가 발생했을 때 찾아내기 어려운 지점들이 되는 것 같아 정확히 알고 사용하는게 중요하다고 다시금 느꼈습니다.

다음에는 어노테이션을 뜯어보면서 어떻게 자세히 동작하는지를 직접 실습해보는 것도 좋을 것 같습니다. 모르는 내용이나 틀린 내용들은 댓글을 통해 알려주세요! 



<br/>


### 참고한 문서
- [@RequestBody vs @ModelAttribute](https://tecoble.techcourse.co.kr/post/2021-05-11-requestbody-modelattribute/)
- [[Spring] @RequestBody, @ModelAttribute, @RequestParam의 차이](https://mangkyu.tistory.com/72)

