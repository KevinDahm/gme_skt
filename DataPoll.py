from bs4 import BeautifulSoup as BS
import urllib3
import requests

def worth(website, line_num, lim):

    #item/item calulcations
    text = requests.get(website).text
    soup = BS(text, 'html.parser')
    data = soup.find_all('div',{"class":"displayoffer-middle"}, limit=lim)

    #Calculated worth from line 7.
    a = (data[line_num].text).split("⇐ ")
    x = int(a[0])/int(a[1])
    return(x)


#iteration for chaos/alterations value of alts per chaos.
chaos_2_alts = worth('http://currency.poe.trade/search?league=Delve&online=x&stock=&want=1&have=4',7,8)
print(chaos_2_alts)