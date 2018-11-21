# 2018-2 객체지향 프로그래밍 프로젝트 - **(economic)**
구성원: 2-2 강태원 | 2-6 오은제 | 2-1 윤성민

## 1. 주제
수요/공급 변동 요인을 배우는 게임

## 2. 동기
최근 정치경제 시간에 수요/공급 변화의 요인을 배운 뒤 게임을 통해 원리를 파악해 보았다. 
이 게임을 파이썬으로 시각화하면 생동감 있게 진행되어 재미있을 것 같아서, 객체지향 프로그래밍 프로젝트로서 만들고자 한다.

## 3. 프로그램 사용 대상
정치경제 수강생, 경제에 관심이 많은 중/고등학생

## 4. 목적
경제학에서 수요는 소비자들이 일정기간 동안에 상품을 구입하고자 하는 욕구이고, 공급은 공급자들이 일정기간동안에 상품을 판매하고자 하는 욕구이다. 
수요 변동의 요인에는 수요자의 기호, 인구, 소득 변화, 연관재의 가격 변화, 해당 재화의 가격상승에 대한 기대, 미래 경기 등이 있고, 공급 변화의 요인에는 생산요소의 가격 변화, 생산기술의 변화, 공급자의 수 변화, 가격상승에 대한 기대, 미래 경기 등이 있다. 이러한 요인들에 의해 수요/공급이 변동하면 수요-공급 곡선에서 볼 수 있듯이 균형가격(시장가격)이 변동한다. 따라서 이 교육용 게임의 목적은 수요와 공급의 변동 요인을 이해하고 현실 속에 적용하는 것이며, 이를 통해 시장 가격의 형성과 변동을 이해할 수 있을 것이다.

## 5. 주요기능
1. 일정 인원이 게임에 참가할 때 까지 대기한다.
2. 게임이 시작되면 해당 인원만 게임에 참여할 수 있도록 하고, 해당 인원이 아닌 경우 방 접속을 차단한다.
3. 사기/팔기 기능이 플레이어별로 제공된다. 이 때 제한시간을 설정하여 게임 시간이 너무 길어지지 않도록 한다.
4. 3번 프로세스를 각 Turn마다 반복한다. 각 Turn마다 플레이어별로 자신의 수익을 표시하며, 모두에게 각각의 누적 수익이 표시된다.
5. 누적 수익이 높은 사람이 승리자가 되며, 마지막 Turn이 지나면 순위와 게임의 승리자를 출력한다.

## 6. 프로젝트 핵심
게임의 핵심이 되는 주요 기능은 GUI로 가격의 변동을 나타내는 텍스트를 그림과 함께 출력하는 것이다.

## 7. 구현에 필요한 라이브러리나 기술
PyQt5 등의 라이브러리를 사용하여 GUI 표현을 한다. 게임을 플레이하는 사용자들이 재미있게 게임을 플레이할 수 있도록 데이터를 시각화한다.


## 8. **분업 계획**
### 강태원
 * GUI 구현
 * 외부 라이브러리 테스트
 * 클래스 설계

### 오은제
 * 일러스트 제작
 * System Coding
 
### 윤성민
 * 아이디어 제시
 * System Coding

## 9. 기타

<hr>


#### readme 작성관련 참고하기 [바로가기](https://heropy.blog/2017/09/30/markdown/)

#### 예시 계획서 [[예시 1]](https://docs.google.com/document/d/1hcuGhTtmiTUxuBtr3O6ffrSMahKNhEj33woE02V-84U/edit?usp=sharing) | [[예시 2]](https://docs.google.com/document/d/1FmxTZvmrroOW4uZ34Xfyyk9ejrQNx6gtsB6k7zOvHYE/edit?usp=sharing)
