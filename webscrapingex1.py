import requests
import bs4

base_url = "http://quotes.toscrape.com/page/{}/"
authorset = set()
i=n=1
while (i>0 and n>0):
	scrape_url = base_url.format(i)

	i = i + 1
	res = requests.get(scrape_url)

	soup = bs4.BeautifulSoup(res.text,'lxml')
	n = int(len(soup.select('.text')))

	authors = soup.select('.author')

	for a in authors:
		authorset.add(a.text)

print(authorset)