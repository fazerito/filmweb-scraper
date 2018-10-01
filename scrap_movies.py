import requests, bs4
site_file = open('films.html', encoding="utf8")
soup_obj = bs4.BeautifulSoup(site_file.read(), "html.parser")

def scrap_films(filename):
    titles = []
    for title in soup_obj.find_all('a', 'film__link', href=True):
        titles.append(title['href'])
        if(len(titles) == 100):
            break

    for i in titles:
        url = "http://www.filmweb.pl" + i
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.content, "html.parser")

        title_pl = soup.find('h1', class_='inline filmTitle')
        title_pl = title_pl.find('a').getText()
        title_pl_file = open(filename, 'a')
        title_pl_file.write(title_pl + '\n')
        title_pl_file.close()

        title_org = soup.find('h2', class_='cap s-16 top-5')

        if title_org:
            title_org = title_org.getText()
            title_org_file = open(filename, encoding='utf-8',mode='a')
            title_org_file.write(title_org + '\n')
            title_org_file.close()
        else:
            title_org_file = open(filename, 'a')
            title_org_file.write(title_pl + '\n')
            title_org_file.close()

        genre = soup.find('ul', class_='inline sep-comma genresList')
        genre = genre.find('a').getText()
        genre_file = open(filename, 'a')
        genre_file.write(genre + '\n')
        genre_file.close()

        director = soup.find(itemprop='director')
        director = director.find('a').getText()
        directors_file = open(filename, 'a')
        directors_file.write(director + '\n')
        directors_file.close()

        film_info = soup.find('div', class_='filmInfo bottom-15')
        date = film_info.find('span').getText()
        dates_file = open(filename, 'a')
        dates_file.write(date + '\n')
        dates_file.close()

        awards_url = 'http://www.filmweb.pl' + i + '/awards'
        req = requests.get(awards_url)
        soap_url = bs4.BeautifulSoup(req.content, 'html.parser')

        awards_list = soap_url.find('ul', class_='awardCounter')
        awards_list = awards_list.find('li').getText().split()
        awards_counter = str(awards_list[1])
        if awards_counter == 'nagród':
            awards_counter = str(0)
        awards_file = open(filename, 'a')
        awards_file.write(awards_counter)
        awards_file.write('\n\n')
        awards_file.close()
