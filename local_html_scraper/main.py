from bs4 import BeautifulSoup

with open('Web_Scraping/simple_html_scraper/home2.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    # courses_html_tags = soup.find('h5') for one tag
    courses_html_tags = soup.find_all('h5') # for all tags
    # print(courses_html_tags)
    for course in courses_html_tags:
        # print(course.text)
        pass
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
    