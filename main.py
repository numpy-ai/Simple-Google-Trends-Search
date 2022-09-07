from pytrends.request import TrendReq
from show_infor import Google_Trend

pytrends = TrendReq(hl='ko', tz=540)

trends = Google_Trend()
trends.kw_input(['갤럭시 플립4', '갤럭시 워치5'])
trends.set_trends("2022-07-01", "2022-09-07")
# trends.show_head(10)
trends.show_graph("Um")
# print(trends_data.head(20))


