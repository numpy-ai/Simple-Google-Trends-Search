from pytrends.request import TrendReq
import pytrends
from datetime import datetime
import plotly.express as px

pytrends = TrendReq(hl='ko', tz=540)
class Google_Trend :
    def __init__(self):
        self.today = datetime.today().strftime("%Y-%m-%d")
        self.kw = []
        self.trends_data = 0
    def kw_input(self, kw: list):
        """
        키워드를 입력 받는다.
        키워드는 최대 5개까지 가능하다.
        :param kw:
        :return:
        """
        self.kw = kw
    def set_trends(self, start, end):
        """
        트렌드 그래프를 설정함
        날짜는 "연도-월-일" 형식으로 입력해야 함
        :param start: 시작 날짜 (처음 날짜)
        :param end: 끝 날짜 (마지막 날짜 )
        :return: None
        """
        pytrends.build_payload(self.kw, cat=0, timeframe=f"{start} {end}", geo="KR")
        self.trends_data = pytrends.interest_over_time()
        self.trends_data = self.trends_data.reset_index()
    def show_head(self, num: int):
        """
        트렌드 데이터의 head를 출력함.
        :param num: head가 출력될 개수
        :return: head
        """
        print(self.trends_data.head(num))
    def show_graph(self, set_title):
        """
        그래프를 보여주는 함수
        :param set_title: "그래프의 제목을 설정함"
        :return: 그래프 출력 (localhost로 열림)
        """
        fig = px.line(self.trends_data, x='date', y=self.kw, title=set_title)  # 데이터 입력, x, y는 데이터에 있는 값만 지정 가능
        fig.show()




