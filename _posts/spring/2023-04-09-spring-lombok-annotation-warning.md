---
title: "[Spring] Lombok 어노테이션 주의사항"
date: 2023-04-09 23:54:28 +0900
excerpt: "Lombok 어노테이션 주의사항 대해서 알아보자."
tags:
  - lombok
categories:
  - spring
header:
  teaser: "../../img/cover/spring.png"

---

제가 작성한 코드를 동료 개발자가 보더니, `@AllArgsConstructor` 를 사용하여 추후 발생할 수 있는 문제에 대해 말해주셨습니다. 그리고 다음 링크를 읽어보면 좋을 것 같다고 추천했습니다. 잘 모르면서 어노테이션을 남발해서 사용했던 것 같아서 반성하는 시간을 가졌습니다.

- [Lombok 사용상 주의점(Pitfall)](https://kwonnam.pe.kr/wiki/java/lombok/pitfall)


위 글에서는 많은 것들을 금지하고 있는데, 여기서는  `@AllArgsConstructor` 어노테이션에 대해서만 설명하고, 추후 글을 보충하도록 하겠습니다.


## @AllArgsConstructor, @RequiredArgsConstructor 사용금지

```java
@AllArgsConstructor
public static class User {
    private String id;
    private String name;
}
```

다음과 같이 DTO를 생성하는 경우, 두 필드에 대해 순서를 바꾸게 되면 개발자가 인식하지 못한사이에 name 에 id 가, id에 name이 들어갈 수 있습니다. 심지어 둘이 동일한 타입이라면 더더욱 인식하기 힘듭니다. 개발자와 IDE 모두 감지 하기 힘들기 때문에 아예 사용을 금지하는 것이 좋습니다. 

이것은 @AllArgsConstructor 와 @RequiredArgsConstructor 모두에 해당될 수 있는 문제입니다. 대신 위 코드의 경우 직접 생성자를 만들고 다음과 같이 [@Builder](https://projectlombok.org/features/Builder "https://projectlombok.org/features/Builder") 애노테이션을 붙여서 사용하는 것이 좋습니다.

```java
public static class User {
    private String id;
    private String name;
 
    @Builder
    private User(String id, String name) {
        this.id = id;
        this.name = name;
    }
}
```



### 결론

결론은 실무 프로젝트에서라면 [@Getter, @Setter](https://projectlombok.org/features/GetterSetter "https://projectlombok.org/features/GetterSetter"), [@ToString](https://projectlombok.org/features/ToString "https://projectlombok.org/features/ToString") 정도만 사용하는 것이 좋을 것 같습니다. 

잘 알지 못하면서 어노테이션을 남발하지 맙시다!