################################### 인공지능 모드 - 2. 현재 뉴스 상위 1~20위 / 3. 현재 연예 뉴스 상위 1~20위

import urllib.request             ## 소스 코드를 따기 위해 브라우저에 request 보내는
from bs4 import BeautifulSoup     ## 따온 소스 코드는 XML 형식으로 저장 -> HTML로 바꿔 주는
from URL_Request_Json_Read_HomeNetwork import *

def Print_News(each_today_news_info, news_num):     ## 현재 인기 뉴스 / 현재 인기 연예 뉴스 프린트 함수
    news_title_link = each_today_news_info.a        ## <li class="ranking_item is_num1"> 에 포함되어 있는 <a> 소스코드를 가져오는
    print("<< %s 위 >>" % news_num)
    print("제목 : %s" % news_title_link['title'])    ## <li class="num1"> 에 포함되어 있는 <a> 에 포함되어 있는 title 속성을 가져오는
    print("바로 가기 ☞  http://news.naver.com%s\n" % news_title_link['href'])    ## <li class="num1"> 에 포함되어 있는 <a> 에 포함되어 있는 href 속성을 가져오는

def Response_News(soup):        ## (모든 소스코드에서) 상위 1~20의 뉴스를 뽑아 내는 함수
    news_num = 0

    while True:
        news_num += 1
        each_today_news_info = soup.find('li', attrs={'class': 'ranking_item is_num%s' % news_num})  ## <li class="num1"> 에 포함되어 있는 소스코드를 가져오는

        Print_News(each_today_news_info, news_num)     ## 현재 인기 뉴스 / 한 주간의 뉴스 프린트 함수

        if news_num == 20: break

def Today_Top_News():       ## 현재 인기 뉴스 상위 1~20위를 보여 주는 함수
    html = urllib.request.urlopen('http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=102&date=%s' % yyyymmdd)
    soup = BeautifulSoup(html, 'html.parser')  ## 모든 소스코드를 따오는

    print("")
    print("<< 현재 인기 뉴스 상위 1 ~ 20위 목록입니다:) 관심 있는 뉴스는 바로 가기를 클릭해 주세요~ >>\n".center(75))

    Response_News(soup)     ## (모든 소스코드에서) 상위 1~20의 뉴스를 뽑아 내는 함수

def Ent_Top_News():         ## 현재 인기 연예 뉴스 상위 1~20위를 보여 주는 함수
    html = urllib.request.urlopen('http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=106')
    soup = BeautifulSoup(html, 'html.parser')  ## 모든 소스코드를 따오는

    print("")
    print("<< 현재 인기 연예 뉴스 상위 1 ~ 20위 목록입니다:) 관심 있는 뉴스는 바로 가기를 클릭해 주세요~ >>\n".center(75))

    Response_News(soup)     ## (모든 소스코드에서) 상위 1~20의 뉴스를 뽑아 내는 함수