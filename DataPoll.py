from bs4 import BeautifulSoup as BS
import urllib3
import requests
from urllist import *

def worth(website, line_num, lim):

    #item/item calulcations
    text = requests.get(website).text
    soup = BS(text, 'html.parser')
    data = soup.find_all('div',{"class":"displayoffer-middle"}, limit=lim)

    #Calculated worth from line 7.
    a = (data[line_num].text).split("⇐ ")
    return(a)


#iteration for what price we sell at
print("Alt per Chaos =", worth(alt_per_chaos,7,8))
print("Fus per Chaos =", worth(fus_per_chaos,7,8))
print("Alc per Chaos =", worth(alc_per_chaos,7,8))
print("Gc per Chaos =", worth(gc_per_chaos,7,8))
print("Ex per Chaos =", worth(ex_per_chaos,7,8))
print("Chr per Chaos =", worth(chr_per_chaos,7,8))
print("Jew per Chaos =", worth(jew_per_chaos,7,8))
print("Chi per Chaos =", worth(chi_per_chaos,7,8))
print("Asx per Chaos =", worth(asx_per_chaos,7,8))
print("Jsx per Chaos =", worth(jsx_per_chaos,7,8))
print("Msx per Chaos =", worth(msx_per_chaos,7,8))

#iteration for what price we buy at
print("Chaos per Alt =", worth(chaos_per_alt,7,8))
print("Chaos per Fus =", worth(chaos_per_fus,7,8))
print("Chaos per Alc =", worth(chaos_per_alc,7,8))
print("Chaos per Gc =", worth(chaos_per_gc,7,8))
print("Chaos per Ex =", worth(chaos_per_ex,7,8))
print("Chaos per Chr =", worth(chaos_per_chr,7,8))
print("Chaos per Jew =", worth(chaos_per_jew,7,8))
print("Chaos per Chi =", worth(chaos_per_chi,7,8))
print("Chaos per Asx =", worth(chaos_per_asx,7,8))
print("Chaos per Jsx =", worth(chaos_per_jsx,7,8))
print("Chaos per Msx =", worth(chaos_per_msx,7,8))