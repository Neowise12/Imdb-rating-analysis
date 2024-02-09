from bs4 import BeautifulSoup
import requests,openpyxl


excel = openpyxl.Workbook()
sheet= excel.active
sheet.title ='250 Top Movies'
sheet.append(['Movie Rank','Movie Name','Year of Release','Imdb Rating'])

url = 'https://m.imdb.com/chart/top/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}



try:
    source = requests.get(url, headers=headers)
    source.raise_for_status()
    soup = BeautifulSoup(source.content, 'html.parser')
    div_element = soup.find('div', class_='sc-3450242-3 fLFQmt ipc-page-grid__item ipc-page-grid__item--span-2').find('ul')

    for movie in div_element:
        class_movie=movie.find('div',class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-be6f1408-9 srahg cli-title')
        class_year=movie.find('div',class_='sc-be6f1408-7 iUtHEN cli-title-metadata')
        class_rating=movie.find('div',class_='sc-e2dbc1a3-0 ajrIH sc-be6f1408-2 dAeZAQ cli-ratings-container')

        name_list =class_movie.get_text(strip=True).split('.')
        name = name_list[1][1:len(name_list[1])]
        rank =name_list[0]
        year = class_year.span.text
        rate =class_rating.span.text.split('(')[0]

        sheet.append([rank,name,year,rate])
           
except Exception as e:
    print("An error occurred:", e)

excel.save('IMDB TOP MOVIES.xlsx')