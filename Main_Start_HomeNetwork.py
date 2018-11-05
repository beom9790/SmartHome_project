########################## Smart Home Network 기본 / 시작 모듈

import threading
from Check_Control_Device_HomeNetwork import *      ## 장비 상태 확인 / 장비 제어하는 모듈
from Simulation_HomeNetwork import *                ## 시뮬레이션 모드 모듈
from Integrated_AI_Main_HomeNetwork import *        ## 인공지능 모드 모듈


g_Radiator  = False             ## 난방기
g_Airconditioner = False        ## 에어컨
g_Aircleaner = False            ## 공기청정기
g_Humidifier = False            ## 가습기
g_Dehumidifier = False          ## 제습기
g_Gas_Valve = False             ## 가스밸브
g_Balcony_Windows = False       ## 발코니(베란다) 창문
g_Door = False                  ## 출입문
g_AI_Mode = False               ## 인공지능 모드
g_Ventilation_Mode = False      ## 환기 모드

device = [g_Radiator, g_Airconditioner, g_Aircleaner, g_Humidifier, g_Dehumidifier,
          g_Gas_Valve, g_Balcony_Windows, g_Door, g_AI_Mode, g_Ventilation_Mode]

device_name = ['난방기', '에어컨', '공기청정기', '가습기',
               '제습기', '가스밸브', '창문', '출입문']

# start point
while True:
    # device[8] = g_AI_Mode
    # device[9] = g_Ventilation_Mode

    t = threading.Thread(target=Update_Scheduler)       ## 인공지능 모드 ON일 경우,
    t.daemon = True                 ## 매 시 45분 10초 마다 실시간 정보를 업데이트 하도록 하는 스레드
    t.start()

    t = threading.Thread(target=Window_Ventilation)     ## 환기 모드 작동
    t.daemon = True                 ## -> 2시간 창문 닫고 20분 창문 열도록(2시간마다 20분씩 창문 열어서 환기) 하는 스레드
    t.start()

    print("<< Smart Home Network Program >>".center(50))
    menu_num = int(input("1. 장비 상태 확인\n2. 장비 제어\n3. 스마트 모드\n4. 인공지능 모드\n5. 시뮬레이션 모드\n0. 프로그램 종료\n\n-> "))

    if menu_num == 1:
        Check_Device_Status(device, device_name)
    elif menu_num == 2:
        Control_Device(device, device_name)
    elif menu_num == 3:
        Smart_Mode(device)
    elif menu_num == 4:
        Integrated_AI_Mode(device)
    elif menu_num == 5:
        Simulation_Mode()
    elif menu_num == 0:
        break
    else:
        print("입력이 올바르지 않습니다!")