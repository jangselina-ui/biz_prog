
'''
# 비즈니스 모델 분석📚

[네이버](https://www.naver.com)  
[홍익대학교](https://www.hongik.ac.kr)


이것이 일반 본문  
**이것이 굵은 글씨**  
*이것이 기울임꼴*  
~취소선~  

:red[빨간색] :blue[파란색] :green[초록색] :yellow[노란색]  
```python
import streamlit as st

print('코드블록')
```
'''

st.caption('캡션(작고 흐린 글씨) st.caption()')

with st.echo():
    #이 블록의 코드와 결과를 출력
    name= 'CHunghun Ha'
    st.write("hello, streamlit", name)

st.latex('\int_a^b f(x)dx')
"$$\int_a^b f(x)dx$$"

'#### :orange[이미지: st.image()]'
st.image("../data/python설명.jpg", caption='파이썬 로고', width=500)

'#### :orange[오디오: st.audio()]'
st.audio("../data/mp3노래.mp3", format='audio/mp3', loop=True)

'#### :orange[동영상: st.video()]'
video_file = open("../data/연주.mp4", 'rb')
video_bytes = video_file.read()

st.video(video_bytes)


'#### :orange[Pandas 데이터프레임]'
import pandas as pd
df = pd.DataFrame(
    {'id': [1, 2, 3],
    'age': [21, 30, 22],
    'name': ['SH', 'GilDong', 'alice']
    }
)
df # 데이터프레임 출력

'''
|이름|학번|학과|
|---|---|---|
|SH|1|경영학과|
|GilDong|2|전자공학과|
|alice|3|생명과학과|
'''

st.metric('Temperature', '25 °C', '-2.5 °C') #지표 출력

'#### :orange[지표(Metric)]'
col1, col2, col3, col4 = st.columns(4) #4개의 컬럼 생성
col1.metric("temperature", "25 °C", "1.2 °C")
col2.metric("wind", "9 mph", "-8%")
col3.metric("humidity", "86%", "4%")
col4.metric('pressure', '1013 hPa', '-5 hPa')

col1.write('이것은 온도지표입니다.')
col3.latex('\int_a^b f(x)dx') #컬럼 안에 수식 출력

st.divider() #구분선


