# python-test
python test

asyncio 서버/클라 테스트
  - 기본 구조 정리
  - socket option 설정(TCP_NODELAY)

함수 복사 테스트
  - 클라에게 받은 패킷마다 고유한 키값을 유지시키고 싶을 때 유용함.

주번호(ex. 201727) 생성 테스트
  - 특정 요일, 특정 시간을 초기화 시간으로 설정
  - 주단위 랭킹등을 관리할때 유용함.
  
파일 로그 테스트
  - jsonlogger를 이용하여 json형태로 파일로그 남김(엘라스틱서치에서 검색이 용이함. 가독성 떨어짐.)
  - utc + offset으로 계산된 localtime을 asctime으로 출력(시스템 timezone 설정이 아닌 설정파일(+9:00)에 의한 localtime을 얻음.)
  
게임 시간함수 테스트
  - 글로벌 서비스를 위해서 utc 타임스템프를 기준으로 설정(클라에게 서버시간 보낼때, DB에 시간저장할때)
  - 서버시간을 local_dateitme 으로 가져오는 함수
  - utc 타임스템프를 local_datetime 으로 변경하는 함수
  - 기획데이터에 설정된 시간문자열('2017-04-10 17:30:00')을 local_datetime으로 변경하는 함수
  