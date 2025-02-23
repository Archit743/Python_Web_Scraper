from bs4 import BeautifulSoup
import requests
import time

unfamilier_skill = input('Enter some unfamiliar skills: ')
print(f'Filtering out {unfamilier_skill}')

def find_jobs():
    # html_text = requests.get('https://www.bbc.co.uk/news').text
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&&txtLocation=&txtKeywords=%22Java+Developer%22%2C%22PHP+Developer%22%2C%22Android+Developer%22%2C%22Content+Writer%22%2C%22Business+Development+Manager%22%2C').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('div', class_='more-skills-sections').find_all('span')
            cleaned_skills = ', '.join(skill.text.strip() for skill in skills)
            more_info = job.header.h2.a['href']
            if unfamilier_skill not in cleaned_skills:
                with open(f'Web_Scraping/website_scraping/posts/{index}.txt', 'w') as f:
                    f.write(f'\nCompany Name: {company_name}\nRequired Skills: {cleaned_skills}\nMore Info: {more_info}\n')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)