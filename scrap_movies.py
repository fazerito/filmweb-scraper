import requests
import bs4


FILMWEB_URL = 'https://www.filmweb.pl'


def scrape_films(url, filename):
    r = requests.get(url)
    soup_obj = bs4.BeautifulSoup(r.content, 'lxml')
    titles = [title['href'] for title in soup_obj.find_all('a', 'film__link', href=True)]

    for title in titles:
        url = FILMWEB_URL + title
        soup = create_soup(url)
        
        scrape_titles(soup, filename)
        scrape_genres(soup, filename)
        scrape_director(soup, filename)
        scrape_date(soup, filename)

        awards_url = url + '/awards'
        awards_soup = create_soup(awards_url)
        scrape_awards_counter(awards_soup, filename)


def scrape_titles(soup, filename):
    polish_title = scrape_polish_title(soup)
    append_to_file(polish_title, filename)

    original_title_soup = scrape_original_title(soup)

    if original_title_soup:
        original_title = original_title_soup.getText()
        append_to_file(original_title, filename)
    else:
        append_to_file(polish_title, filename)


def scrape_polish_title(soup):
    polish_title = soup.find('h1', class_='inline filmTitle')
    polish_title = polish_title.find('a').getText()
    return polish_title


def scrape_original_title(soup):
    original_title_soup = soup.find('h2', class_='cap s-16 top-5')
    return original_title_soup


def scrape_genres(soup, filename):
    genre = soup.find('ul', class_='inline sep-comma genresList')
    genre = genre.find('a').getText()
    append_to_file(genre, filename)


def scrape_director(soup, filename):
    director = soup.find(itemprop='director')
    director = director.find('a').getText()
    append_to_file(director, filename)


def scrape_date(soup, filename):
    film_info = soup.find('div', class_='filmInfo bottom-15')
    date = film_info.find('span').getText().strip()
    append_to_file(date, filename)


def scrape_awards_counter(soup, filename):
    awards_list = soup.find('ul', class_='awardCounter')
    awards_list = awards_list.find('li').getText().split()
    awards_counter = str(awards_list[1])
    if awards_counter == 'nagród':
        awards_counter = str(0)
    append_to_file(awards_counter, filename)
    break_line_in_file(filename)


def create_soup(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, 'lxml')
    return soup


def append_to_file(text, filename):
    with open(filename, mode='a') as f:
        f.write(text + '\n')


def break_line_in_file(filename):
    with open(filename, mode='a') as f:
        f.write('\n')


if __name__ == '__main__':
    for page_number in range(5):
        scrape_films(FILMWEB_URL + f'/ajax/ranking/film/{page_number}', 'filmweb.txt')