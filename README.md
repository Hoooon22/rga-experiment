# RGA 실험 프로젝트

Stanford Research Systems(SRS)의 잔류 가스 분석기(RGA) 제어를 위한 실험 프로젝트입니다.

## 설치

필요한 패키지를 설치하려면:

```bash
pip install srsinst.rga
```

## 사용법

`rga_test.py` 파일은 RGA100 장치 연결을 테스트하기 위한 예제 코드입니다:

```python
from srsinst.rga import RGA100

# TCP/IP 통신
ip_address = '192.168.1.100'
user_id = 'admin'
password = 'admin'

rga = RGA100('tcpip', ip_address, user_id, password)
```

## 참고자료

- [srsinst.rga GitHub](https://github.com/thinkSRS/srsinst.rga)