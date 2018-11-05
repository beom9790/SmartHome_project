############################## 시뮬레이션 모드 모듈

from URL_Request_Json_Read_HomeNetwork import *

g_Radiator = False              ## 난방기
g_Airconditioner = False        ## 에어컨
g_Aircleaner = False            ## 공기청정기
g_Humidifier = False            ## 가습기
g_Dehumidifier = False          ## 제습기
g_Gas_Valve = False             ## 가스밸브
g_Balcony_Windows = False       ## 발코니(베란다) 창문
g_Door = False                  ## 출입문
g_AI_Mode = False               ## 인공지능 모드


def Simulation_Mode():      ## 시뮬레이션 모드 메뉴
    global g_Balcony_Windows, g_Humidifier, g_Dehumidifier
    print("<<시뮬레이션 모드 메뉴입니다. 원하는 서비스의 번호를 입력하세요>>".center(45))
    menu_num = int(input("1. 비오는 날 시뮬레이션\n2. 건조한 날 시뮬레이션\n3. 습한 날 시뮬레이션\n"
                         "4. 상쾌한 날 시뮬레이션\n0. 돌아가기\n-> "))

    if menu_num == 0:
        return
    elif menu_num < 1 or menu_num > 5:
        print("입력이 올바르지 않습니다.")
        return

    get_Realtime_Weather_Info()     ## JSon 파일 만들기 전 함수

    total_weather = Read_Weather_Json()     ## JSon 파일을 불러오는 함수

################################### 비오는 날 시뮬레이션
    if menu_num == 1:
        rain_num = 0   ## 창문 인공지능 모드
        for window_status in total_weather:
            if window_status.get('category') == "PTY":
                rain_num += window_status.get('fcstValue')
                break
        rain_num = 0

        if rain_num == 0:  ## 강수 확률이 있으면 창문을 닫아라
            if g_Balcony_Windows == True:  ## 창문이 열려 있으면
                g_Balcony_Windows = not g_Balcony_Windows  ## 창문을 닫아라
                print("강수 확률이 있어 창문을 닫습니다:)")
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
            else:  ## 창문이 닫혀 있으면
                print("강수 확률이 있어 닫힌 창문 상태를 유지합니다:)")  ## 계속해서 창문을 닫아 놔라
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == False: print("닫힘\n")
        else:  ## 강수 확률이 없으면 창문을 열어라
            if g_Balcony_Windows == True:  ## 창문이 열려 있으면
                print("햇살이 좋아 열린 창문 상태를 유지합니다:)")
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == True: print("열림\n")
            elif g_Balcony_Windows == False:  ## 창문이 닫혀 있으면
                g_Balcony_Windows = not g_Balcony_Windows
                print("햇살이 좋아 창문을 엽니다:)")
                print("발코니(베란다) 창문 상태 : ", end="")
                if g_Balcony_Windows == True: print("열림\n")

################################### 건조한 날 시뮬레이션
    elif menu_num == 2:
        humidity_status_num = 0
        for humidity_status in total_weather:
            if humidity_status.get('category') == "REH":
                humidity_status_num += humidity_status.get('fcstValue')
                break
        print("현재 습도 : %s%%" % humidity_status_num)

        if humidity_status_num < 45:  ## 평균 습도가 45% 이하면 가습기를 켜라
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                g_Humidifier = not g_Humidifier  ## 가습기 켜라
                print("현재 습도가 낮습니다. 가습기를 작동시킵니다:)")
                print("가습기 상태 : ", end="")
                if g_Humidifier == True: print("작동\n")
            else:  ## 가습기가 켜져 있으면
                print("현재 습도가 낮습니다. 작동 중인 가습기 상태를 유지합니다:)")  ## 계속 가습기를 켜 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == True: print("작동\n")

        elif humidity_status_num >= 45 and humidity_status_num <= 55:
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                print("현재 습도는 적정 습도입니다. 작동 중인 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")
            else:  ## 가습기가 켜져 있으면
                g_Humidifier = not g_Humidifier
                print("현재 습도는 적정 습도입니다. 가습기를 정지시킵니다:)")  ## 가습기를 꺼라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")

        elif humidity_status_num > 55:  ## 평균 습도가 55% 이상이면 가습기를 꺼라
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                print("현재 습도 : %s%%" % humidity_status_num)
                print("현재 습도가 높습니다. 정지된 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")
            else:  ## 가습기가 켜져 있으면
                g_Humidifier = not g_Humidifier
                print("현재 습도 : %s%%" % humidity_status_num)
                print("현재 습도가 높습니다. 가습기를 정지시킵니다:)")  ## 가습기를 꺼라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")

################################### 습한 날 시뮬레이션
    elif menu_num == 3:
        humidity_status_num = 0
        for humidity_status in total_weather:
            if humidity_status.get('category') == "REH":
                humidity_status_num += humidity_status.get('fcstValue')
                break
        humidity_status_num = 75
        print("현재 습도 : %s%%" % humidity_status_num)

        if humidity_status_num > 70:
            if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
                g_Dehumidifier = not g_Dehumidifier
                print("현재 습도가 높습니다. 제습기를 작동시킵니다:)")  ## 제습기를 켜라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == True: print("작동\n")
            else:  ## 제습기가 켜져 있으면
                print("현재 습도가 높습니다. 작동된 제습기 상태를 유지합니다:)")  ## 계속 제습기를 켜 놔라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == True: print("작동\n")

        elif humidity_status_num < 55:
            if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
                print("현재 습도가 제습기 작동 범위 이하입니다. 정지된 제습기 상태를 유지합니다:)")  ## 계속해서 제습기를 꺼 놔라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")
            else:  ## 제습기가 켜져 있으면
                g_Dehumidifier = not g_Dehumidifier
                print("현재 습도가 제습기 작동 범위 이하입니다. 제습기를 정지시킵니다:)")  ## 제습기를 꺼라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")

################################### 상쾌한 날 시뮬레이션
    elif menu_num == 4:
        humidity_status_num = 0   ## 가습기 / 제습기 인공지능 모드
        for humidity_status in total_weather:
            if humidity_status.get('category') == "REH":
                humidity_status_num += humidity_status.get('fcstValue')
                break
        humidity_status_num = 50

        if 45 <= humidity_status_num and humidity_status_num <= 55:
            print("\n현재 습도 : %s%%\n" % humidity_status_num)
            if g_Humidifier == False:  ## 가습기가 꺼져 있으면
                print("현재 습도는 적정 습도입니다. 정지된 가습기 상태를 유지합니다:)")  ## 계속 가습기를 꺼 놔라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")
            else:  ## 가습기가 켜져 있으면
                g_Humidifier = not g_Humidifier
                print("현재 습도는 적정 습도입니다. 가습기를 정지시킵니다:)")  ## 가습기를 꺼라
                print("가습기 상태 : ", end="")
                if g_Humidifier == False: print("정지\n")

            if g_Dehumidifier == False:  ## 제습기가 꺼져 있으면
                print("정지된 제습기 상태를 유지합니다:)")  ## 계속해서 제습기를 꺼 놔라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")
            else:  ## 제습기가 켜져 있으면
                g_Dehumidifier = not g_Dehumidifier
                print("제습기를 정지시킵니다:)")  ## 제습기를 꺼라
                print("제습기 상태 : ", end="")
                if g_Dehumidifier == False: print("정지\n")