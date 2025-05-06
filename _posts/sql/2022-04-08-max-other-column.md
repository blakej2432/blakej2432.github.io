---
title: "[oracle] MIN, MAX에 해당하는 다른 컬럼값"
date: 2022-04-08 23:10:28 +0900
categories: sql
tags: 
  - 집계함수
---



Group By를 이용해 Min, Max 컬럼은 다들 쉽게 구했던 경험이 있을 것이다.

예를 들어 직원테이블에서 부서별로 가장 높은 월급을 구하는 쿼리는 다음과 같다.

```sql
SELECT MAX(SALARY)
			, DEPT
FROM EMPLOYEE
GROUP BY DEPT
```



<br/>

그렇다면 부서별 가장 높은 월급을 받는 직원의 이름을 알고 싶다면 어떻게 해야할까?

**DENSE_RANK** 를 이용할 수 있다.

쿼리는 다음과 같다.
```sql
SELECT MAX( EMP_NAME ) KEEP ( DENSE_RANK FIRST ORDER BY SALARY DESC ) MAX_SALARY_EMP -- 가장 높은 월급의 직원이름
			, MIN( EMP_NAME ) KEEP ( DENSE_RANK LAST ORDER BY SALARY DESC ) MIN_SALARY_EMP -- 가장 낮은 월급의 직원이름
			, DEPT
FROM EMPLOYEE
GROUP BY DEPT
```



<br/>

### 결론

즉, 다음과 같이 일반화할 수 있다.
```sql
-- K가 가장 높은 값의 V
MAX( V ) KEEP ( DENSE_RANK FIRST ORDER BY K DESC )

-- K가 가장 낮은 값의 V
MIN( V ) KEEP ( DENSE_RANK LAST ORDER BY K DESC )
```




<br/>

**REFERENCES**

- [집계함수 MIN, MAX에 해당하는 다른 컬럼값은?](https://aseuka.tistory.com/entry/집계함수-MIN-MAX에-해당하는-다른-컬럼값은)