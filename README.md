# 2**9-1st-JULABO-backend**

본 프로젝트는 학습을 목적으로  LE-LABO 사이트를 클론하여 진행되었습니다.

 [시연 영상 링크](https://youtu.be/FHodh-FGYuU)

## **🔎 Project Description**

**개발 기간** 22. 01.24 ~ 22. 02. 11

**개발 인원**

- Frontend : 윤남주 , 석정도, 김창규
- Backend : 최창현, 김지연, 최형택

## **🔨 기술 스택**

### Frontend
- HTML/CSS
- JavaScript
- React
- SASS

### Backend
- python
- django
- mysql
- postman

### Version Control
- github

### Communication
- Trello
- Slack
- Notion

## **📝 ERD**

![julabo (1)](https://user-images.githubusercontent.com/66771425/153746775-ac1158fc-321e-4134-891c-281d5c3eca45.png)

## **🖥 구현 기능**

> 최창현
> 

### **판매 상품 조회**

- 카테고리별 전체 상품 리스트 데이터 반환
- Type(ml)에 따라 상품 필터링

### **판매 상품 검색**

- 키워드를 통해 상품의 이름을 검색
- 검색된 상품 리스트 데이터 반환

### 인기 상품

- 로그인된 유저가 상품을 조회(클릭) 시 해당 데이터를 저장
- 유저의 중복 조회 방지 기능 구현
- 저장된 데이터를 기반으로 가장 많이 클릭된 5가지 상품을 반환

> 김지연
> 

### 상품 상세 페이지

- 요청한  `product_id` 를 받아 해당 상품, 해당 상품과 같은 그룹에 있는 상품 목록의정보를 반환

### **장바구니**

- 장바구니 상품 추가, 조회, 수정, 삭제 기능 구현
- `login_decorator` 를 이용해 로그인된 유저만 장바구니 기능을 이용할수 있도록 함
- 장바구니에 담긴 상품의 `subcategory` 를 바탕으로 연관 상품 추천

> 최형택
> 

### **회원가입 및 로그인**

- 정규 표현식을 통한 아이디 및 비밀번호 유효성 검사
- 비밀번호 암호화 및 JWT 발급
- 요청 헤더에 담긴 토큰을 통해 로그인 여부를 검사하는 데코레이터 구현

### 제품 추천 조회 기능

- 제품과 유저 정보를 가져와 데이터를 저장하고 가장 많이 클릭된 상위 5개를 반환

## API Documentation
- [LINK](https://warped-resonance-891074.postman.co/workspace/My-Workspace~b131c86b-70c5-4537-8d26-b4a265c11c26/collection/19259271-054e1ba1-cd0a-4439-8881-1e94d4a9c8f8?ctx=documentation)

## ****Reference****

- 이 프로젝트는 르라보(lelabo) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무 수준의 프로젝트 이지만 학습용 으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제가 될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
