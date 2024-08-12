import requests, bs4

url = "https://quotes.toscrape.com/"

request = requests.get(url)
soup = bs4.BeautifulSoup(request.text, "lxml") 

authors_soup = soup.select(".author")
authors = [item.getText() for item in authors_soup]
print(set(authors))

quotes_soup = soup.select(".text")
quotes = [item.getText() for item in quotes_soup]
print(quotes)

tags_soup = soup.select(".tag-item")
for tag in tags_soup:
    anchor = tag.select("a")
    print(anchor[0].text)


nextPageExists = True
page_no = 1
base_url = "https://quotes.toscrape.com/page/{}"
authors_list = []

while nextPageExists:
    try:
        scrape_url = base_url.format(page_no)
        print(scrape_url)

        request = requests.get(scrape_url)
        soup = bs4.BeautifulSoup(request.text, "lxml")    

        if "No quotes found!" in str(soup):
            break    
        
        authors_soup = soup.select(".author")
        for item in authors_soup:
            authors_list.append(item.getText())

        page_no += 1        
    except:
        nextPageExists = False
        break

print(set(authors_list))