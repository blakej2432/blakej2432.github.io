---
title: "[azure] azure mysql database 만들기"
date: 2021-11-21 20:40:28 +0900
categories: settings
tags: 
  - azure
  - mysql
header:
  teaser: "../../img/cover/azure.png"
---





Azure 무료계정을 생성하고 mysql database를 생성해보자

<img src="../../img/2021-11-21-azure-mysql-database/image-20211121190618201.png" alt="image-20211121190618201" style="zoom:67%;" />

![image-20211121190658602](../../img/2021-11-21-azure-mysql-database/image-20211121190658602.png)

![image-20211121191437509](../../img/2021-11-21-azure-mysql-database/image-20211121191437509.png)



중간에 서버 구성을 클릭하고 제일 낮은 것으로 설정해주자. (안그러면 요금이 많이 나오니까)



![image-20211121194542989](../../img/2021-11-21-azure-mysql-database/image-20211121194542989.png)



![image-20211121195638469](../../img/2021-11-21-azure-mysql-database/image-20211121195638469.png)





### 방화벽 설정

![image-20211121202200305](../../img/2021-11-21-azure-mysql-database/image-20211121202200305.png)





azure database는 기본적으로 <u>특정 IP를 제외한 IP에서 연결이 불가능하도록 방화벽 설정</u>이 되어있다.   
그러나 다수와 협업을 하거나, 카페를 옮겨다니면서 코딩을 해서 불규칙한 IP에서 접속해야하는 경우 **Azure 서비스 방문 허용**을 예로 설정하면 사용이 가능하다.

![image-20211121202304273](../../img/2021-11-21-azure-mysql-database/image-20211121202304273.png)





### References

- [Azure Database for mysql 공식문서](https://docs.microsoft.com/ko-kr/azure/mysql/quickstart-create-mysql-server-database-using-azure-portal)
- [MySQL용 Azure 데이터베이스 서버 방화벽 규칙 공식문서](https://docs.microsoft.com/ko-kr/azure/mysql/concepts-firewall-rules)
- [youtube - Microsoft Azure를 사용하여 5 분 이내에 MySQL 데이터베이스 서버 만들기](https://www.youtube.com/watch?v=fJEfBqWwcL0)



