import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="판매 대시보드",
    page_icon='📊',
    layout="wide",
)

TARGET_DIR = 'data'
TARGET_CSV = 'data.csv'

# 이 함수를 실행한 파일의 절대경로를 객체로 만들어준다!
BASE_DIR = Path(__file__).resolve().parent # parent까지 하면 root 디렉토리를 잡아준다.(현재 파일 기준으로 설명해주시는듯?)
DATA_PATH = BASE_DIR / TARGET_DIR / TARGET_CSV # 재정의되어있기때문(문자열은 이대로 이어지지않음)


df = pd.read_csv(DATA_PATH)






st.title("판매 대시보드")

with st.sidebar:
    st.header('조회조건')
    region = st.selectbox(
        '지역',
        # [
        #     '전체',
        # ]+df['region'].unique().tolist()
        [
            '전체',
            *(df['region'].unique().tolist()) # 이거 튜플을 나누는거임!!
        ]
    )

    minimum_sales = st.slider(
        '최소 매출',
        min_value=0,
        max_value=int(df['sales'].max()), # numpy 정수로 되기때문에 형변환을 해줘야한다.
        value=0,
        step=100_000,
    )

# 지역은 범주형 데이터라 가격을 먼저 필터링해줘야 함.
filtered = df[
    df['sales']>=minimum_sales
].copy()

if region != '전체':
    filtered[filtered['region'] == region]
# else :
#     filtered

# st.dataframe(filtered)

## KPI
## 1. 총 매출
## 2. 총 판매량
## 3. 평균 매출
## 4. KPI 계산에 사용된 데이터 행수(조회 건수)


st.divider()

if filtered.empty:
    st.warning('조건에 맞는 데이터가 없음')

