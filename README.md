# Filmweb scraper
Simple filmweb.pl Top100 movies scraper made with Python and Beautiful Soup 4

# Installation
You need to install pip if you want to use the script.

Clone the repo running:

```console
git clone https://github.com/fazerito/filmweb-scraper.git
```
I strongly recommend to run this script inside python virtual environment. If you don't have venv installed simply run:
```console
pip install virtualenv
```
And then create your venv.
```console
python -m venv venv
```
Or for linux users.
```console
python3 -m venv venv
```

Activate virtual environment with a single command.  
Windows:
```console
\venv\Scripts\activate
```

Linux:

```console
source venv/bin/activate
```

Go to filmweb-scraper directory and run:

```console
pip install -r requirements.txt
```
And run the script:  
Windows:  

```console
python scrape_movies.py
```
Linux:  
```console
python3 scrape_movies.py
```

# File structure
Information about every movie is saved in a .txt file.

1st line: Polish title  
2nd: Original title  
3rd: Genre  
4th: Director  
5th: Date of release  
6th: Number of awards  

**Example output:**  
Skazani na Shawshank  
The Shawshank Redemption  
Dramat  
Frank Darabont  
 16 kwietnia 1995  
6
