import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
        self.response = requests.get(self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, "html.parser")

    def product_title(self):
        title  = self.soup.find("span",{"class":"LMizgS"})
        if title is not None:
            return title.text

    def product_price(self):
        price  = self.soup.find("div",{"class":"hZ3P6w bnqy13"})
        if price is not None:
            return price.text




device = PriceTracer(url="https://www.flipkart.com/egate-atom-2x-200-lm-1-speaker-wireless-remote-controller-android-13-200-iso-lumens-720p-native-1080p-4k-support-manual-focus-automatic-keystone-netflix-prime-etc-wifi-6-bt-screen-mirroring-1gb-ram-8gb-rom-smart-projector/p/itm42103c06ea518?pid=PROEHHH6UPZNTP5D&lid=LSTPROEHHH6UPZNTP5DBMRSWT&marketplace=FLIPKART&store=6bo%2Ftia%2F1hx&srno=b_1_1&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_4_L2_view-all&fm=organic&iid=en__TZMjE1x_ovSXx8hVXYGn42seJVZurVEM7L8tQlev0F4RN6sz085VTGq2_RRuYph_DQQzOO84pqV6OzIRP0dWg%3D%3D&ppt=hp&ppn=homepage&ssid=e34wxtxtds0000001768392844741")
print("Title:",device.product_title())
print("Price:",device.product_price())
# print(device.soup)

