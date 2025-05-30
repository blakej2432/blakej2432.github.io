---
title: "[토비의 스프링] 1.1 초난감 DAO ~ 1.2 DAO의 분리"
date: 2022-01-09 07:00:28 +0900
categories:
  - book
tags:
  - 토비의 스프링
  - spring
header:
  teaser: "../../img/book/tobi-spring.jpg"
---



<div class="notice--info" markdown="1">

💡 객체지향 기술의 진정한 가치 회복

- 스프링이 가장 관심을 많이 두는 대상은 오브젝트다. 애플리케이션에서 오브젝트가 생성되고 다른 오브젝트와 관계를 맺고, 사용되고, 소멸되기까지의 전과정을 진지하게 생각해볼 필요가 있다.
- 오브젝트의 설계와 구현, 동작원리에 집중

</div>

<div class="notice--info" markdown="1">

💡 자바빈(JavaBean) : 다음 두 가지 관례를 따라 만들어진 오브젝트를 가리킨다.

- 디폴트 생성자 : 리플렉션을 이용해 오브젝트를 생성하기 때문에 필요

- 프로퍼티 : 자바빈이 노출하는 이름을 가진 속성을 프로퍼티라고 한다. (getter, setter)

</div>



<br/>


# 1.1 초난감 DAO

## 1.1.1 User

User 클래스와 테이블 생성

```java
package springbook.user.domain;

public class User {
	String id;
	String name;
	String password;

	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
}
```



<img src="../../img/tobi-spring/1-1/DB837426-687D-42C6-943D-BE9A0241408D.jpeg" alt="DB837426-687D-42C6-943D-BE9A0241408D.jpeg" style="zoom:50%;" />

<br/>

## 1.1.2 UserDao

사용자 정보를 DB에 넣고 관리할 수 있는 DAO

DB연결은 JDBC 이용

```java
package springbook.user.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import springbook.user.domain.User;

public class UserDao {

	public void add(User user) throws ClassNotFoundException, SQLException {
		Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection c = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:xe", "springbook", "springbook");

		PreparedStatement ps = c.prepareStatement(
					"insert into users(id,name,password) values(?,?,?)");
		ps.setString(1, user.getId());
		ps.setString(2, user.getName());
		ps.setString(3, user.getPassword());

		ps.executeUpdate();

		ps.close();
		c.close();

	}

	public User get(String id) throws ClassNotFoundException, SQLException {
		Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection c = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:xe", "springbook", "springbook");

		PreparedStatement ps = c.prepareStatement(
					"select * from users where id = ?");
		ps.setString(1, id);

		ResultSet rs = ps.executeQuery();
		rs.next();
		User user = new User();
		user.setId(rs.getString("id"));
		user.setName(rs.getString("name"));
		user.setPassword(rs.getString("password"));

		rs.close();
		ps.close();
		c.close();

		return user;

	}

}
```



<br/>

## 1.1.3 main()을 이용한 DAO 테스트 코드

만들어진 코드의 기능을 검증하기 위한 main메소드

```java
public static void main(String[] args) throws ClassNotFoundException, SQLException {
		UserDao dao = new UserDao();

		User user = new User();
		user.setId("whiteship");
		user.setName("정의진");
		user.setPassword("good");

		dao.add(user);

		System.out.println(user.getId() + " 등록 성공");

		User user2 = dao.get(user.getId());
		System.out.println(user2.getName());
		System.out.println(user2.getPassword());

		System.out.println(user2.getId() + " 조회 성공");

	}
```





<br/>

<br/>

# 1.2 DAO의 분리

## 1.2.1 관심사의 분리

객체지향의 세계에서는 모든 것이 변한다. 그래서 미래의 변화에 대비해야하고, 최소한의 확신을 가진 작업만으로 기능을 수정해낸 개발자가 더 미래의 변화를 잘 준비한 개발자라고 할 수 있다.

이를 위해 분리와 확장을 고려한 설계를 해야한다. 모든 변경과 발전은 한 번에 한가지의 관심사항에 집중에서 일어나기 때문에, 우리는 관심이 같은 것은 모으고, 다른 것은 떨어져 있게 해야한다.



<br/>

## 1.2.2 커넥션 만들기의 추출

### UserDao의 관심사항

- DB커넥션
- DB에 보낼 SQL문을 만들기
- Connection 오브젝트를 닫고 리소스 반환

**중복 코드의 메소드 추출**

```java
// 중복된 코드를 독립적인 메소드로 만들어서 중복을 제거했다.
private Connection getConnection() throws ClassNotFoundException, SQLException {
	Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection c = DriverManager.getConnection(
				"jdbc:oracle:thin:@127.0.0.1:1521:xe", "springbook", "springbook");
		return c;
}
```



<div class="notice--info" markdown="1">

💡 리팩토링 후에는 반드시 테스트하기!

</div>

<br/>

## 1.2.3 DB 커넥션 만들기의 독립

UserDao의 내부코드를 공개하지 않고 N사와 D사에게 connection 만 바꿔서 사용하라 하고 싶을때

⇒ **getConnection을 추상메서드로!**

**상속을 통한 확장**

<img src="../../img/tobi-spring/1-1/4DEE3FB2-EE6F-43A8-A476-794A3ACF7783.jpeg" alt="4DEE3FB2-EE6F-43A8-A476-794A3ACF7783.jpeg" style="zoom:50%;" />

```java
public abstract class UserDao {
	
	public void add(User user) throws ClassNotFoundException, SQLException {
		Connection c = getConnection();
		
		//....
		
	}
	
	public User get(String id) throws ClassNotFoundException, SQLException {
		Connection c = getConnection();
		
		//...
		
	}
	
	public abstract Connection getConnection() throws ClassNotFoundException, SQLException;
	// 구현코드는 제거되고 추상메소드로 바뀌었다. 메소드의 구현은 서브클래스가 담당한다.
}

public class DUserDao extends UserDao{
	public Connection getConnection() throws ClassNotFoundException, SQLException{
		// D사 DB Connection 생성코드
	}
}

public class NUserDao extends UserDao{
	public Connection getConnection() throws ClassNotFoundException, SQLException{
		// D사 DB Connection 생성코드
	}
}
```

클래스 계층구조를 통해 두 개의 관심이 독립적으로 분리되면서 변경작업은 한층 용이해졌다.



<br/>

### (1) 템플릿 메소드 패턴

- 슈퍼클래스에 기본적인 로직의 흐름을 만들고(커멕션 가져오기), 그 기능의 일부를 추상 메소드나 오버라이딩이 가능한 protected 메소드로 만든 뒤 서브클래스에서 필요에 맞게 구현
- 변하지 않는 기능은 슈퍼클래스에, 자주 변하는 기능은 서브클래스에서 구현

### (2) 팩토리 메소드 패턴

- UserDao의 getConnection 메서드는 어떤 Connection 클래스의 오브젝트를 어떻게 생성할 것인지를 결정하는 방법이라고 볼 수 있다. 이렇게 서브클래스에서 구체적인 오브젝트 생성 방법을 결정하게 하는 것
- 주로 인터페이스 타입으로 리턴하므로, 서브클래스에서 어떤 클래스를 리턴할지 슈퍼클래스에서 알지 못함



<img src="../../img/tobi-spring/1-1/26F56E8C-4F60-492D-A224-E933752C42CC.jpeg" alt="26F56E8C-4F60-492D-A224-E933752C42CC.jpeg" style="zoom:50%;" />

<div class="notice--info" markdown="1">
💡 UserDao는 Connection 인터페이스 타입의 오브젝트라는 것 외에는 관심을 두지 않는다. 어떤 방법으로 GetConnection 을 사용하는지는 NUserDao 와 DUserDao의 관심사항일 뿐이다.
</div>


