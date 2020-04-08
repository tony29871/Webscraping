import requests
from bs4 import BeautifulSoup

LIMIT = 50

URL = f"https://www.indeed.com/jobs?q=Python&limit={LIMIT}"

def extract_indeed_pages(): 
    result = requests.get(URL)
    # 웹을 스크래이핑함

    soup = BeautifulSoup(result.text,"html.parser")
    #html로 인식해라, 데이터 탐색 추출이 용이한 object(soup)

    #참고) 크롬에서 개발자 도구(ctrl+shift+i)를 들어가면 웹 구성 볼 수 있음

    pagination = soup.find("div",{"class":"pagination"})

    links = pagination.find_all('a')
    #pagination중 'a'찾기(페이지 1,2,...,20)

    pages = []
    for link in links[:-1]:
        pages.append(int(link.find('span').string))
        #append : 리스트에 추가하는 함수 #sting은 태그 안에서 내용만 추출(soup페이지 참조)

    max_page = pages[-1] #마지막 페이지 숫자
    return max_page


def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result = requests.get(f"{URL}&start= {page*LIMIT}") #모든 페이지들 확인
        print(result.status_code)