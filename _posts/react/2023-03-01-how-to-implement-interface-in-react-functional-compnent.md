---
title: "[React] 함수형 컴포넌트에서 인터페이스 구현하기"
date: 2023-03-01 12:00:28 +0900
categories: react
excerpt: "React 함수형, 클래스형 컴포넌트에서 인터페이스 구현하는 방식의 차이를 알아봅시다."
header:
  teaser: "../../img/cover/react.png"
---


### 인터페이스란?

인터페이스(interface)란 다른 클래스를 작성할 때 기본이 되는 틀을 제공하면서, 다른 클래스 사이의 중간 매개 역할까지 담당하는 일종의 추상 클래스를 의미합니다. 해당 포스팅은 Java와 React에서 인터페이스를 구현하는 방법을 정리한 문서입니다. 인터페이스에 대한 자세한 설명은 다음 링크를 참고해주세요.

- [자바의 인터페이스(interface)란?](http://www.tcpschool.com/java/java_polymorphism_interface)



<br/>

### 1. Java에서 인터페이스 구현하기

먼저 `cry()` 라는 메서드를 가지는 `Animal`이라는 인터페이스를 선언합니다.

```java
interface Animal { 
	public abstract void cry(); 
}
```

`Animal` 을 구현한 `Cat`과 `Dog` Class를 작성합니다. 고양이는 야옹야옹, 강아지는 멍멍하고 짖겠죠?

```java
class Cat implements Animal {
    public void cry() {
        System.out.println("냐옹냐옹!");
    }
}

class Dog implements Animal {
    public void cry() {
        System.out.println("멍멍!");
    }
}
```



<br/>

### 2. React 클래스형 컴포넌트에서 인터페이스 구현하기

클래스형 컴포넌트는 자바와 유사하게 인터페이스를 선언하고 그 인터페이스를 구현해주면 됩니다.

2.1. 컴포넌트 밖에 원하는 인터페이스를 선언합니다.
여기서는 `myMethod` 라는 메서드가 필요한 `MyInterface` 라는 인터페이스를 선언합니다.

```typescript
interface MyInterface {
  myMethod: () => void;
}
```

<br/>

2.2. 해당 인터페이스를 구현한 리액트 컴포넌트를 상속해서 만들고 싶은 클래스 컴포넌트를 선언합니다.
여기서 `MyProps`와 `MyState`는 생략이 가능하며, 컴포넌트에서 사용되는 props와 state로 대체되어야 합니다.

```typescript
class MyComponent extends React.Component<MyProps, MyState> implements MyInterface {
  // ...
}
```

<br/>

2.3. 그리고 인터페이스의 메서드를 구현해주면 완성!

```typescript
class MyComponent extends React.Component<MyProps, MyState> implements MyInterface {
  myMethod() {
    // implementation here
  }
}
```

<br/>

2.4. 자바의 예시와 동일하게 작성해 봅시다

```typescript
interface Animal {
  cry: () => void;
}

class Cat extends React.Component<> implements Animal {
  cry() {
    console.log('야옹야옹!')
  }
}

class Dog extends React.Component<> implements Animal {
  cry() {
    console.log('멍멍!')
  }
}

```



<br/>

### 3. React 함수형 컴포넌트에서 인터페이스 구현하기

함수형 컴포넌트는 클래스형 컴포넌트와 구현방식이 다릅니다. 컴포넌트를 인터페이스로 선언하는게 아니라, props나 state의 구조를 정의함으로써 인터페이스를 정의할 수 있습니다.
즉, props나 state를 인터페이스로 만들고 상속하는 방법으로 인터페이스를 구현합니다.

3.1. Props를 인터페이스로 정의하기
`Props` 라는 인터페이스를 정의했고, 이는 컴포넌트 props의 구조를 잡아줍니다. 

```jsx
interface Props {
  name: string;
  age: number;
}

const MyComponent: React.FC<Props> = ({ name, age }) => {
  return (
    <div>
      <p>Name: {name}</p>
      <p>Age: {age}</p>
    </div>
  );
};

```

<br/>

3.2. State를 인터페이스로 정의하기
아래 예시는 state를 interface로 선언하여 사용하는 방법입니다.

```jsx
interface State { 
	count: number; 
}

const MyComponent: React.FC<{}, State> = () => { 
	const [state, setState] = useState<State>({ count: 0 }); 
	const incrementCount = () => { 
		setState({ count: state.count + 1 }); 
	}; 
	
	return ( 
		<div> 
			<p>Count: {state.count}</p> 
			<button onClick={incrementCount}>Increment</button> 
		</div> 
	); 
};
```

<br/>

3.3. 자바의 예시와 동일하게 작성해 봅시다

```jsx
interface Props {
    cry: () => void;
}

const cat: Props = {
    cry: () => {
	    console.log('야옹야옹!')
    }
}

const dog: Props = {
    cry: () => {
	    console.log('멍멍!')
    }
}

const Animal: React.FC<Props> = ({ cry }) => {
	useEffect(() => {
		cry()
	}, [])
	
  return (
    <div>
      <p>Animal class</p>
    </div>
  );
};
```



<br/>

### 글을 마치며

간단한 예시로 자바와 리액트에서의 인터페이스 구현에 대해서 알아보았습니다. 백엔드하면서 프론트를 겸하다보니 Java처럼 생각하다가 구현방식이 다르면 당황하게 되는 경우가 있는 것 같습니다.

혹시 잘못된 내용이 있다면 댓글로 알려주세요!

번외) 구글을 찾아보는데 딱 원하는 답변이 없어서 ChatGpt에 물어본 답변을 참고해서 적었습니다. 근데 예상보다 진짜 대답을 잘해줘서 놀랬고, 신기하면서도 조금 무서울 정도였습니다. 잘 활용하면 좋을 것 같습니다(?)

