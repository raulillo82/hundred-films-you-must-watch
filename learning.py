from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", rel="noreferrer")
article_texts = []
article_links = []
for article in articles:
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)

article_upvotes = [int(article.getText().split()[0])
                   if article.getText != None else 0
                   for article in
                   soup.find_all(name="span", class_="score")]

#print(article_texts)
#print(article_links)
#print(article_upvotes)

print(len(article_texts), len(article_links), len(article_upvotes))
index = article_upvotes.index(max(article_upvotes))
print(index)
print(article_texts[index])
print(article_links[index])
print(article_upvotes[index])

#HTML_FILE = "website.html"
#with open(HTML_FILE, "r") as html_file_data:
#    contents = html_file_data.read()
#
#soup = BeautifulSoup(contents, "html.parser")

#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup)
#print(soup.prettify())

#print(soup.p)

#all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

#for tag in all_anchor_tags:
    #print(tag.getText())
    #print(tag.get("href"))
    #pass

#heading = soup.find(name="h1", id="name")
#print(heading)
#section_heading = soup.find(name="h3", class_="heading")
#print(section_heading)

#company_url = soup.select_one(selector="p a")
#print(company_url)
#
#name = soup.select_one(selector="#name")
#print(name)
#
#headings = soup.select(".heading")
#print(headings)


