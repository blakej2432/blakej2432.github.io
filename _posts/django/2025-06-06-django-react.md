---
title: "[Django] Django + React 풀스택 프로젝트 세팅하기"
date: 2025-06-06 18:24:28 +0900
categories: django
tags: django react
header:
  teaser: "../../img/cover/django_logo.png"
---

Django 와 Django template 으로 html 초기 로딩을 빠르게 하면서,<br>
동적 변화가 필요한 부분에 React를 활용하기로 했다.

세팅이 다소 복잡한데도 Vanilla JS가 아닌 React를 쓰는 이유는 역시<br>
- 컴포넌트 재사용성
- 직접 DOM을 조작하지 않고, 선언적으로 DOM 변경 -> 복잡성 감소, 테스트/디버깅/확장 용이
- 쉬운 상태 관리

가 있다.

### Django + React 프로젝트 구조

```text
myproject/
├── backend/
│   ├── myapp/
│   │   └── templates/
│   │       └── myapp/
│   │           └── race.html       ← Django 템플릿
│   ├── static/
│   │   └── js/
│   │       └── race.bundle.js      ← React 빌드된 번들 (race.jsx → Webpack/Vite로)
│   └── views.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── RaceList.tsx        ← React 컴포넌트
│   │   └── race.tsx                ← 진입 파일 (entry point)
│   └── vite.config.js / webpack.config.js
```


### React 진입점

index.html 과 main.tsx (root) 로 react 코드의 진입점을 찾는게 아니라,<br>
django template에서 동적 변화 부분에 맞게 진입점을 설정해준다


```javascript
// frontend/src/race.tsx
import React from "react";
import { createRoot } from "react-dom/client";
import RaceList from "./components/RaceList";

const container = document.getElementById("race-list");
if (container) {
  const root = createRoot(container);
  root.render(<RaceList />);
}
```

### Vite Build 로 장고와 통합하기

Vite로 React 프로젝트를 만들고, `vite.config.js` 에 build 설정을 한다.

```javascript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: '../backend/', 
    emptyOutDir: false,
    rollupOptions: {
      input: {
        race: path.resolve(__dirname, 'src/entries/race.tsx'),
        login: path.resolve(__dirname, 'src/entries/login.tsx'),
        profile: path.resolve(__dirname, 'src/entries/profile.tsx'),
      },
      output: {
        entryFileNames: (chunkInfo) => {
          const name = chunkInfo.name;
          if (name === 'race') return 'race/static/js/race.bundle.js';
          if (name === 'login') return 'account/static/js/login.bundle.js';
          if (name === 'profile') return 'user/static/js/profile.bundle.js';
          return 'static/js/[name].bundle.js';
        },
      },
    },
  },
});
```
-----------

### 장고 템플릿에서 사용하기

이렇게 하면, backend의 장고 static 폴더에 bundle.js가 들어오게 되고,<br>
다음과 같이 template에 포함시킬 수 있다.

{% raw %}
```html
<!-- backend/myapp/templates/myapp/race.html -->
{% load static %}
<html>
  <head>
    <script src="{% static 'js/race.bundle.js' %}" defer></script>
  </head>
  <body>
    <h1>레이스 목록</h1>
    <div id="race-list"></div>
  </body>
</html>
```
{% endraw %}