import requests, bs4

result = requests.get("https://example.com")
soup = bs4.BeautifulSoup(result.text, "lxml")

htmlTitle = soup.select("title")
site_paragraphs = soup.select("p")
first_site_paragraph_text = site_paragraphs[0].getText()

res = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")
soup = bs4.BeautifulSoup(res.text, "lxml")
toc = soup.select(".vector-toc-text")
toc_text_list = [content.text for content in toc]

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, "lxml")
imgs = soup.select(".mw-file-element")
imgs_list = [img["src"] for img in imgs]

for index, img in enumerate(imgs_list):
    link = requests.get(f"https:{img}")
    f = open(f"Images\\Computer_Image_{index}.{img[-3:]}", "wb")
    f.write(link.content)
    f.close()