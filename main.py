from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

pytrends = TrendReq(hl='ko', tz=540)

kw_list = ["갤럭시 워치5", "갤럭시 플립4"]

pytrends.build_payload(kw_list, cat=0, timeframe="2022-01-01 2022-08-11", geo="KR")
trends_data = pytrends.interest_over_time()
trends_data = trends_data.reset_index()

# print(trends_data.head(20))

fig = px.line(trends_data, x='date', y=kw_list, title='Search Trends') # 데이터 입력, x, y는 데이터에 있는 값만 지정 가능
fig.show()

