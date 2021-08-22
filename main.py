import eel
from rakuten import *

@eel.expose
def rakuten_search(keyword,sort,count,csv):
    main(keyword,sort,count,csv)

eel.init("web")
eel.start("main.html")