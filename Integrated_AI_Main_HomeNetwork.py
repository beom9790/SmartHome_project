######################################## Integrated_AI_Mode #######################################
from Integrated_AI_Food_HomeNetwork import *        ## 요리 레시피/맛집 추천 모듈
from Integrated_AI_News_HomeNetwork import *        ## 뉴스 보기 모듈
from Integrated_AI_Video_HomeNetwork import *       ## 인기 클립 영상 보기 모듈
from Integrated_AI_Music_HomeNetwork import *       ## 음악 듣기 모듈
from Smart_AI_HomeNetwork import *                  ## 인공지능 켜기 위해


def Integrated_AI_Mode(device):   ## 인공지능 모드
    # device[8] = g_AI_Mode

    if device[8] == False:  ## 인공지능 모드가 꺼져 있는 경우
        AI_Mode_TurnOn(device)    ## 켤 지 묻는 함수

    else:                   ## 인공지능 모드가 켜져 있는 경우
        pass                ## 그냥 패스

    if device[8] == False:
        return

    print("")
    print("<< 인공지능 모드 메뉴입니다. 원하는 서비스의 번호를 입력하세요 >>\n".center(50))
    menu_num = int(input("1. [Food] 나 배고파!!\n2. [News] 나 현재 소식이 궁금해!!\n"
                         "3. [Entertainment] 나 핫한 연예 소식이 궁금해!!\n4. [TV] 나 핫한 클립 영상 보고 싶어~\n"
                         "5. [Music] 나 음악 듣고 싶어~\n0. 돌아가기\n-> "))

    if menu_num == 1:
        Food_recommendation()       ## 요리 레시피 / 맛집 추천해 주는 함수
    elif menu_num == 2:
        Today_Top_News()            ## 현재 인기 뉴스 상위 1~20위를 보여 주는 함수
    elif menu_num == 3:
        Ent_Top_News()              ## 현재 인기 연예 뉴스 상위 1~20위를 보여 주는 함수
    elif menu_num == 4:
        Watch_Video()               ## 인기 클립 영상 시청 함수
    elif menu_num == 5:
        Listen_Music()              ## 음악 듣기 함수
    elif menu_num == 0:
        return
    else:
        print("입력이 올바르지 않습니다!")