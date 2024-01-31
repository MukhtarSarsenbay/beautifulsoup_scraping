import requests
from bs4 import BeautifulSoup

# # response = requests.get('/website.html')®
# # print(response.text)
# with open("website.html") as file:
#     data = file.read()
#     print(data)
#
# soup = BeautifulSoup(data, "html.parser")

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
articles_text = []
articles_link = []
loc_max = 0
for article_tag in articles:
    article_v1 = article_tag.find(name="a")
    article_text = article_v1.getText()
    articles_text.append(article_text)
    article_link = article_v1.get("href")
    articles_link.append(article_link)
articles_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

print(articles_upvotes)
print(articles_link)
print(articles_text)
largest = max(articles_upvotes)
index = articles_upvotes.index(largest)
print(articles_upvotes[index])
print(articles_link[index])
print(articles_text[index])
