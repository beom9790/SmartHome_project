################################## 인공지능 모드 - 7. 음악 듣기
import urllib.request             ## 소스 코드를 따기 위해 브라우저에 request 보내는
from bs4 import BeautifulSoup     ## 따온 소스 코드는 XML 형식으로 저장 -> HTML로 바꿔 주는
from random import *              ## 음악 랜덤 추천을 위한 난수 생성
import webbrowser                 ## 랜덤 추천 음악을 사이트(유튜브)에서 열기 위해

def Listen_Music():      ## 음악 듣기 함수
    print("")
    print("<< 음악 감상 모드입니다:) >>\n".center(40))
    inp_want_music = input("듣고 싶은 노래 제목이나 가수 이름을 입력해 주세요 : ")

    html = urllib.request.urlopen('https://www.youtube.com/results?search_query=%s' % urllib.parse.quote(inp_want_music))
    soup = BeautifulSoup(html, 'html.parser')  ## 모든 소스코드를 따오는

    ## 모든 소스코드에서 <h3 class="yt-lockup-title "> 하위 소스코드만 따오는
    music_info = soup.findAll('h3', attrs={'class': 'yt-lockup-title '})

    print("")
    print("<< '%s' 노래 목록입니다:) 원하시는 노래는 바로 가기를 클릭해 주세요~ >>\n".center(65) % inp_want_music)

    random_music = randint(1, 10)   ## 1 ~ 10 사이 난수 생성

    music_count = 0
    while True:
        music_count += 1
        url = "https://www.youtube.com%s" % music_info[music_count].a.get('href')

        ## music_info = soup.findAll('h3', attrs={'class': 'yt-lockup-title '})가 리스트로 이루어져 있음
        ## 리스트에서 하나씩 뽑아 <a aria-describedby="description-id-841094" class="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link " data-sessionlink="itct=CFkQ3DAYACITCJXFm4jrjdkCFQRYYAodGLMBsSj0JFIG7J2066Oo" dir="ltr" href="/watch?v=QLAmTkqzSPs" rel="spf-prefetch" title="이루 - 흰눈">이루 - 흰눈</a>
        print("제목 : %s" % music_info[music_count].a.get('title'))  ## <a>에 포함되어 있는 title="이루 - 흰눈"을 뽑아라
        print("바로 가기 ☞  %s\n\n" % url)  ## <a>에 포함되어 있는 href="/watch?v=QLAmTkqzSPs"를 뽑아라
        if music_count == random_music:    ## 검색한 노래나 가수에 대해 랜덤으로 생성한 난수로 사이트를 하나 띄워 줌
            webbrowser.open(url)

        if music_count == 10: break  ## 노래 10개 추천하고 종료