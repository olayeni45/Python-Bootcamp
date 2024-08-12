import requests, bs4
# Goal: Get title of every book with a 2 star rating

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
two_star_titles = []

for n in range(1,51):
    scrape_url = base_url.format(n)
    request = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(request.text, "lxml")
    product_pod = soup.select(".product_pod")

    for book in product_pod:
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select("a")[1]["title"]
            two_star_titles.append(book_title)

print(two_star_titles)