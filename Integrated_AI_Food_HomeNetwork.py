################################### 인공지능 모드 - 1. 요리 레피시 / 맛집 검색
from URL_Request_Json_Read_HomeNetwork import *

client_id = "R1JCmA0iVfg4x_ecHHkN"                  ## 요리 레시피 / 맛집 검색 ID
client_secret = "EycJ4UgDEA"                        ## 요리 레시피 / 맛집 검색 Secret
display_recipe = "10"                               ## 검색 결과 출력 건수 지정 - 10 ~ 100
sort_recipe = "sim"                                 ## 정렬 옵션 : sim (유사도순), date (날짜순)
restaurant_local = "신암동"       ## "신암동" - 신암동 요리 맛집 JSon 파일 request 날릴 때, 항목
good_restaurant = "맛집"          ## "맛집" - 신암동 요리 맛집 JSon 파일 request 날릴 때, 항목


## 따옴표가 <b> </b>로 출력돼서 다시 따옴표로 바꿔주는 작업 + 링크 주소가 잘못 나와서 다시 조합하는 작업 함수
def Update_Json():
    food_blog_ls = []
    with open('%s_%s_%s.JSon' % (inp_want_food, item_type, yyyymmdd), encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        food_blog_ls = json.loads(json_string)

    for change_str in food_blog_ls.get('items'):
        ########## 따옴표가 <b> </b>로 출력돼서 다시 따옴표로 바꿔주는 작업
        if '&quot;' in change_str.get('title') or '&lt;' in change_str.get('title') or '&gt;' in change_str.get('title') or\
                        '<b>' in change_str.get('title') or '</b>' in change_str.get('title') or '&amp;' in change_str.get('title'):
            change_str['title'] = change_str.get('title').replace("&quot;", "'")
            change_str['title'] = change_str.get('title').replace("&lt;", "<")
            change_str['title'] = change_str.get('title').replace("&gt;", ">")
            change_str['title'] = change_str.get('title').replace("<b>", "")
            change_str['title'] = change_str.get('title').replace("</b>", "")
            change_str['title'] = change_str.get('title').replace("&amp;", "&")
        if '&quot;' in change_str.get('description') or '&lt;' in change_str.get('description') or '&gt;' in change_str.get(
            'description') or '<b>' in change_str.get('description') or '</b>' in change_str.get('description') or '&amp;' in change_str.get('description'):
            change_str['description'] = change_str.get('description').replace('&quot;', "'")
            change_str['description'] = change_str.get('description').replace('&lt;', "<")
            change_str['description'] = change_str.get('description').replace('&gt;', ">")
            change_str['description'] = change_str.get('description').replace('<b>', "")
            change_str['description'] = change_str.get('description').replace('</b>', "")
            change_str['description'] = change_str.get('description').replace('&amp;', "&")

        ########## 링크 주소가 잘못 나와서 다시 조합하는 작업
        ## "http://blog.naver.com/theboni?Redirect=Log&amp;logNo=221065338934"      ## 이렇게 없는 주소로 나와서
        ## -> "https://blog.naver.com/theboni/221065338934"                         ## -> 제대로 된 주소로 바꿔 줌
        ## "http://blog.naver.com/dngusghk?Redirect=Log&amp;logNo=221161588949"
        ## -> "https://blog.naver.com/dngusghk/221161588949"

        change_str['link'] += "z"  ## link에 나와 있는 마지막 12자리 숫자를 가져오기 위해 z를 마지막에 넣어 줌
        new_link = change_str.get('bloggerlink') + "/" + change_str.get('link')[-13:-1]  ## z가 없으면 마지막 숫자는 누락되니까(-1번째 자리는 포함 안 하니까)
        change_str['link'] = new_link  ## 새로운 link 주소를 입력해 줌

    with open('%s_%s_%s.JSon' % (inp_want_food, item_type, yyyymmdd), 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(food_blog_ls, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)

    return food_blog_ls

def Recipe_Request_Json(url):       ## 요리 레시피 / 맛집을 당겨오기 위해 request 보내는 함수
    req = urllib.request.Request(url)

    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(req)
    rescode = response.getcode()

    if rescode == 200:
        json_recipe_result = json.loads(response.read().decode('utf-8'))

        with open('%s_%s_%s.JSon' % (inp_want_food, item_type, yyyymmdd), 'w', encoding='utf8') as outfile:
            retJson = json.dumps(json_recipe_result, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(retJson)
            print('\n%s_%s_%s.JSon SAVED' % (inp_want_food, item_type, yyyymmdd))

    else:
        print("Error Code:" + rescode)

    ## 따옴표가 <b> </b>로 출력돼서 다시 따옴표로 바꿔주는 작업 + 링크 주소가 잘못 나와서 다시 조합하는 작업 함수
    Update_Json()

def get_Recipe_URL():       ## 요리 레시피 / 맛집을 당겨오기 위해 request 보내는 전, URL 만드는 함수

    end_point = "https://openapi.naver.com/v1/search/blog"

    parameters = "?query=" + research_food      ## 검색을 원하는 문자열로서 UTF-8로 인코딩
    parameters += "&display=" + display_recipe  ## 검색 결과 출력 건수 지정
    parameters += "&sim=" + sort_recipe         ## 정렬 옵션 : sim (유사도순), date (날짜순)

    url = end_point + parameters

    Recipe_Request_Json(url)    ## 요리 레시피 / 맛집을 당겨오기 위해 request 보내는 함수

def Food_recommendation():      ## 요리 레시피 / 맛집 추천해 주는 함수
    global inp_want_food, research_food, item_type        ## global을 안 써주면 get_Recipe_URL에서 research_food를 인식하지 못하는
                                                          ## Recipe_Request_Json에서는 inp_want_food를 인식하지 못하는
    print("")                                             ## -> get_Recipe_URL(research_food, inp_want_food) 를 넣어 줘야 하는!! global을 써주면 편하다!!
    print("<< 배고픔을 싹 날려~ 모드입니다:) >>\n".center(40))
    inp_want_food = input("드시고 싶은 요리 이름을 입력해 주세요 : ")

    ########################### 레시피 추천
    item_type = "recipe"
    want_food = urllib.parse.quote(inp_want_food)  ## 요리 레시피 JSon 파일 request 날릴 때, 항목
    recipe_food = urllib.parse.quote(" 레시피")     ## 요리 레시피 JSon 파일 request 날릴 때, 항목
    research_food = want_food + recipe_food        ## 요리 레시피 JSon 파일 request 날릴 때, 항목

    get_Recipe_URL()        ## 요리 레시피를 당겨오기 위해 request 보내는 전, URL 만드는 함수

    recipe_blog_ls = Update_Json()      ## JSon 파일에서 레시피 목록을 가져오는 변수
    print("")
    print("<< %s 레시피 추천 목록입니다:) 관심 있는 레시피는 바로 가기를 클릭해 주세요~ >>".center(55) % inp_want_food)
    for prn_recipe in recipe_blog_ls.get('items'):
        print("\n<<제목>>\n%s\n" % prn_recipe.get('title'))
        print("<<간략 소개>>\n%s\n" % prn_recipe.get('description'))
        print("바로 가기 ☞  %s\n" % prn_recipe.get('link'))
        print("=" * 150)

    ########################### 맛집 추천
    item_type = "restaurant"
    local_food = urllib.parse.quote(restaurant_local)         ## "신암동" - 신암동 요리 맛집 JSon 파일 request 날릴 때, 항목
    want_food = urllib.parse.quote(inp_want_food)             ## 신암동 요리 맛집 JSon 파일 request 날릴 때, 항목
    restaurant_food = urllib.parse.quote(good_restaurant)     ## "맛집" - 신암동 요리 맛집 JSon 파일 request 날릴 때, 항목
    research_food = local_food + want_food + restaurant_food  ## 신암동 요리 맛집 JSon 파일 request 날릴 때, 항목

    print("")
    print("=+" * 100)
    print("=+" * 100)
    get_Recipe_URL()  ## 신암동 요리 맛집을 당겨오기 위해 request 보내는 전, URL 만드는 함수

    restaurant_blog_ls = Update_Json()      ## JSon 파일에서 맛집 목록을 가져오는 변수

    print("")
    print("<< %s %s %s 추천 목록입니다:) 관심 있는 맛집은 바로 가기를 클릭해 주세요~ >>".center(55) % (restaurant_local, inp_want_food, good_restaurant))
    for prn_recipe in restaurant_blog_ls.get('items'):
        print("\n<<제목>>\n%s\n" % prn_recipe.get('title'))
        print("<<간략 소개>>\n%s\n" % prn_recipe.get('description'))
        print("바로 가기 ☞  %s\n" % prn_recipe.get('link'))
        print("=" * 150)