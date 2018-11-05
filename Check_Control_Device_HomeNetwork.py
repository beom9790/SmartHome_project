############################## 장비 상태 확인 / 장비 제어하는 모듈

def Print_Device_fir_Status(device_name, device_status):    ## 장비 상태 출력 함수 1-1
    print(">> %s 상태: " % device_name, end="")

    if device_status == True: print("작동")
    else: print("정지")

def Print_Device_snd_Status(device_name, device_status):    ## 장비 상태 출력 함수 1-2
    print(">> %s 상태: " % device_name, end="")

    if device_status == True: print("열림")
    else: print("닫힘")

def Check_Device_Status(device, device_name):

    print("")
    print("===================================")
    for idx, (deviceNM, deviceBD) in enumerate(zip(device_name, device)):
        if idx < 5:
            Print_Device_fir_Status(deviceNM, deviceBD)
        else:
            Print_Device_snd_Status(deviceNM, deviceBD)
    print("===================================")
    print("")

def Control_Device(device, device_name):       ## 장비 제어 함수

    Check_Device_Status(device, device_name)
    menu_num = int(input("<< 상태 변경할 기기의 번호를 입력하세요 >>\n"
                         "1. 난방기\n2. 에어컨\n3. 공기청정기\n4. 가습기\n5. 제습기\n"
                         "6. 가스밸브\n7. 창문\n8. 출입문\n0. 돌아가기\n-> "))

    if 1<= menu_num and menu_num <= 8:
        device[menu_num - 1] = not device[menu_num - 1]
    elif menu_num == 0:
        return
    else:
        print("입력이 올바르지 않습니다!")

    print("")

    Check_Device_Status(device, device_name)