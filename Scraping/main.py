import requests # pip install requests를 통해 requests 설치
                # (터미널에 따로 어디 안찾아가고 바로 써도 가능)
from bs4 import BeautifulSoup  #https://www.crummy.com/software/BeautifulSoup/bs4/doc/  사이트 참조

from extracting_pages import extract_indeed_pages ,\  #\는 한줄 나눠쓰기
    extract_indeed_jobs

last_page = extract_indeed_pages()

extract_indeed_jobs(last_page)