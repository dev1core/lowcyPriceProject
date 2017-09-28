import urllib.request
from bs4 import BeautifulSoup
import time

new_path = 'C:/Users/LEO/Desktop/lowcy_price.txt'
new_price = open(new_path, 'a')

strTime = time.strftime('%X %x')
fp = urllib.request.urlopen("https://bazar.lowcygier.pl/offer/75668")
mybytes = fp.read()

mystr = mybytes.decode("utf8")

soup = BeautifulSoup(mystr, "html.parser")

#soup = BeautifulSoup(mystr)

for link in soup.find_all("div", class_="price"):
   # print(link.get_text())
    priceLabel = float(link.get_text().strip().replace(",",".").split(' ')[0])
    new_price.write("\n"+link.get_text().strip().replace(",",".").split(' ')[0]+";")
    new_price.write(strTime);
fp.close()
new_price.close();
print(priceLabel)