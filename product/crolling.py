from selenium import webdriver
import time
import os
import urllib.request
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import json

def fetch_adidas_shoes():
    # Edge WebDriver 설정
    edge_options = webdriver.EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("--headless")  # 브라우저를 표시하지 않음

    # WebDriver 초기화
    driver = webdriver.Edge(options=edge_options)

    # 아디다스 쇼핑몰 메인 페이지로 이동
    driver.get('https://abcmart.a-rt.com/promotion/planning-display/detail/main?utm_term=abc%EB%A7%88%ED%8A%B8&gclid=CjwKCAjwloynBhBbEiwAGY25dKX1_y-F8jf0P9RpeYaUb5PoCvyhwF5iatSQui-orzdxk8wVWk4nJBoC7uMQAvD_BwE&utm_campaign=sa_pc&utm_medium=cpc&gad=1&gclsrc=aw.ds&plndpNo=2000003540&utm_source=google')

    # 신발 카테고리 페이지로 이동
    driver.get('https://abcmart.a-rt.com/display/category/main?genderGbnCode=10000&ctgrNo=1000000441&page=1')

    time.sleep(5)  # 페이지 로딩 대기

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    shoe_list = soup.find_all("div", class_="prod-item-inner")  # 신발 목록의 클래스 이름에 따라 수정
    # 작업 디렉토리 경로 가져오기
    current_directory = os.getcwd()
    img_folder_name = 'img3/'
    img_path = os.path.join(current_directory, img_folder_name)
    #img_path = 'c:\\Users\\chqh1\\img3\\'  # 이미지 저장 경로

    # 신발 정보를 저장할 리스트 초기화
    shoe_data = []

    # 이미지 저장 폴더 생성
    if not os.path.exists(img_path):
        os.makedirs(img_path)

    # ...
    for idx, shoe in enumerate(shoe_list, 1):
        # 신발 이름 초기화
        shoe_name = "Unknown Shoe Name"

        # 신발 가격 초기화
        shoe_price = "Unknown Price"

        # 신발 이미지 URL 가져오기
        shoe_img_element = shoe.find("img")
        if shoe_img_element:
            shoe_img = shoe_img_element["src"]

            # 이미지 URL이 유효한지 확인하고 다운로드
            if shoe_img.startswith("http") or shoe_img.startswith("https"):
                img_filename = f"{img_path}{idx}_adidas.jpg"

                # 신발 이름 가져오기
                shoe_name_element = shoe.find("span", class_="prod-name")
                if shoe_name_element:
                    shoe_name = shoe_name_element.text

                # 신발 가격 가져오기
                shoe_price_element = shoe.find("span", class_="price-cost")
                if shoe_price_element:
                    shoe_price = shoe_price_element.text

                urllib.request.urlretrieve(shoe_img, img_filename)
                print(f"Downloaded {idx}: {shoe_name} - {img_filename}")
                print(shoe_name)
                print(shoe_price)
            else:
                print(f"Invalid image URL for {shoe_name}")
        else:
            print(f"No image found for {shoe_name}")

        shoe_data.append({"name": shoe_name, "price": shoe_price})

    driver.quit()
    with open("shoe_data.json", "w") as json_file:
        json.dump(shoe_data, json_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    fetch_adidas_shoes()
