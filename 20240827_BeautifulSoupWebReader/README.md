# BeautifulSoupWebReader 사용 중 불편한 점

1. User-Agent가 requests를 이용하여 만든 것으로 보이는데, 특정 사이트에서는 python-requests가 차단되는 것으로 보임.
![image](https://github.com/user-attachments/assets/c24ee97f-a5bd-471a-bb50-9a8b1409f758)

base.py에서 아래와 같이 수정

![image](https://github.com/user-attachments/assets/6aa6e932-62e0-4bf9-8dfc-6aaa81f04f1e)
