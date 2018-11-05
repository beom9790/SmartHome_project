########################### URL 만들어서 request 날려서 json 파일 생성 + json 파일 읽는 모듈

import urllib.request   ## 소스 코드를 따기 위해 브라우저에 request 보내는
import datetime
import time
import json

access_key = "mCMm44itfuyVU%2BFbA2UfUkg5e0mhiGe8cfc9MeGkjna99yT90ezvAOPMqZnYBczZRSliXsaBpyfIV9ic1Bpjmw%3D%3D"
json_weather_result = []
json_atmosphere_result = []
yyyymmdd = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")
day_hour = time.strftime("%H")
day_min = time.strftime("%M")
last_thrid = "30"       ## (1) 기상 정보(동네예보정보 조회 서비스) JSon 파일 request 날릴 때, 항목
x_coodinate = "89"      ## (1) 기상 정보(동네예보정보 조회 서비스) JSon 파일 request 날릴 때, 항목
y_coodinate = "91"      ## (1) 기상 정보(동네예보정보 조회 서비스) JSon 파일 request 날릴 때, 항목
numofrows = "100"       ## (1) 기상 정보(동네예보정보 조회 서비스) JSon 파일 request 날릴 때, 항목
sidoname = "대구"       ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) JSon 파일 request 날릴 때, 항목
ver_info = "1.3"        ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) JSon 파일 request 날릴 때, 항목


def get_Request_URL(url):                 ## (1) 기상 정보(동네예보정보 조회 서비스) / (2) 통합대기환경 정보(대기오염정보 조회 서비스)
    req = urllib.request.Request(url)     ## request 날리는 함수

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_Weather_URL(day_time):       ## (1) 기상 정보(동네예보정보 조회 서비스) request 보내기 전, url 만드는 함수
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + day_time
    parameters += "&nx=" + x_coodinate
    parameters += "&ny=" + y_coodinate
    parameters += "&numOfRows=" + numofrows

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json(day_time):     ## (1) 기상 정보(동네예보정보 조회 서비스) JSon 파일 생성하는 함수
    jsonData = get_Weather_URL(day_time)

    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for prn_data in jsonData['response']['body']['items']['item']:
            json_weather_result.append({'baseDate': prn_data.get('baseDate'),
                               'baseTime': prn_data.get('baseTime'),
                               'category': prn_data.get('category'),
                               'fcstDate': prn_data.get('fcstDate'),
                               'fcstTime': prn_data.get('fcstTime'),
                               'fcstValue': prn_data.get('fcstValue'),
                               'nx': prn_data.get('nx'),
                               'ny': prn_data.get('ny')})

    with open('동구_신암동_초단기예보조회_%s.JSon' % yyyymmdd, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.JSon SAVED\n' % (yyyymmdd, day_time))

def get_Realtime_Weather_Info():        ## (1) 기상 정보(동네예보정보 조회 서비스) JSon 파일 만들기 전, 실시간 업데이트 확인 함수
    day_min_int = int(day_min)
    if 30 < day_min_int <= 59:      ## 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
        day_time = time.strftime("%H%M", time.localtime(time.time()))
        print("\n<<실시간 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

    elif 0 <= day_min_int <= 30:        ## 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        day_time = "{0:0>2}".format(day_hour_int) + last_thrid      ## 시간이 한 자리 수일 때 930 되는 것을 0930으로 바꿔 줌

        print("\n<<가장 최신 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

    return day_min_int

def Read_Weather_Json():        ## (1) 기상 정보(동네예보정보 조회 서비스) JSon 파일을 불러오는(읽는) 함수
    total_weather = []
    with open("동구_신암동_초단기예보조회_%s.JSon" % yyyymmdd, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        total_weather = json.loads(json_string)

    return total_weather

def get_Atmosphere_URL():   ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) request 보내기 전, url 만드는 함수

    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?_returnType=JSon&serviceKey=" + access_key
    parameters += "&sidoName=" + urllib.parse.quote(sidoname)
    parameters += "&ver=" + ver_info

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Atmosphere_Json():  ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) JSon 파일 생성하는 함수
    print("\n<<가장 최신 대기환경정보 업데이트를 실시합니다!!>>\n".center(30))
    jsonData = get_Atmosphere_URL()

    for prn_data in jsonData.get('list'):
        if prn_data.get('stationName') == '신암동':
            json_atmosphere_result.append({'stationName':prn_data.get('stationName'),
                           'dataTime':prn_data.get('dataTime'),
                           'pm10Value':prn_data.get('pm10Value'),       ## 10μm 이하의 미세먼지를 기준으로
                           'pm10Grade1h':prn_data.get('pm10Grade1h'),
                           'khaiValue':prn_data.get('khaiValue'),
                           'khaiGrade':prn_data.get('khaiGrade')})

    with open('동구_신암동_통합대기환경정보_%s.JSon' % yyyymmdd, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_atmosphere_result, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_통합대기환경정보_%s.JSon SAVED\n' % yyyymmdd)

def Read_Atmosphere_Json():        ## (2) 통합대기환경 정보(대기오염정보 조회 서비스) JSon 파일을 불러오는(읽는) 함수
    total_atmosphere = []
    with open("동구_신암동_통합대기환경정보_%s.JSon" % yyyymmdd, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        total_atmosphere = json.loads(json_string)

    return total_atmosphere