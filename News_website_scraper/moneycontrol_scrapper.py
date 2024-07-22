import re.
import json
import requests
import datetime
from tqdm import tqdm
from bs4 import BeautifulSoup
from collections import defaultdict

submission = defaultdict(list)
#main url
src_url = 'https://www.moneycontrol.com/news/technical-call-221.html'

#get next page links and call scrap() on each link
def setup(url):
    nextlinks = []
    src_page = requests.get(url).text
    src = BeautifulSoup(src_page, 'lxml')

    #ignore <a> with void js as href
    anchors = src.find("div", attrs={"class": "pagenation"}).findAll(
        'a', {'href': re.compile('^((?!void).)*$')})
    nextlinks = [i.attrs['href'] for i in anchors]
    for idx, link in enumerate(tqdm(nextlinks)):
        scrap('https://www.moneycontrol.com'+link, idx)

#scraps passed page url 
def scrap(url, idx):
    src_page = requests.get(url).text
    src = BeautifulSoup(src_page, 'lxml')

    span = src.find("ul", {"id": "cagetory"}).findAll('span')
    img = src.find("ul", {"id": "cagetory"}).findAll('img')

    #<img> has alt text attr set as heading of news, therefore get img link and heading from same tag
    imgs = [i.attrs['src'] for i in img]
    titles = [i.attrs['alt'] for i in img]
    date = [i.get_text() for i in span]

    #list of dicts as values and indexed by page number
    submission[str(idx)].append({'title': titles})
    submission[str(idx)].append({'date': date})
    submission[str(idx)].append({'img_src': imgs})

#save data as json named by current date
def json_dump(data):
    date = datetime.date.today().strftime("%B %d, %Y")
    with open('moneycontrol_'+str(date)+'.json', 'w') as outfile:
        json.dump(submission, outfile)

setup(src_url)
json_dump(submission)

.
..
.
.
.
.
.
///main
///
////////
.......
main
///
**** 
,,,,

\.....
//////
  </div>
        <!--end of single store item-->
        <!-- single item -->
        <div class="col-10 col-sm-6 col-lg-4 mx-auto my-3 store-item doughnuts" data-item="dougnuts">
          <div class="card ">
            <div class="img-container">
              <img src="img/doughnut-1.jpeg" class="card-img-top store-img" alt="">
              <span class="store-item-icon">
                <i class="fas fa-shopping-cart"></i>
              </span>
            </div>
            <div class="card-body">
              <div class="card-text d-flex justify-content-between text-capitalize">
                <h5 id="store-item-name">dougnut item</h5>
                <h5 class="store-item-value">$ <strong id="store-item-price" class="font-weight-bold">5</strong></h5>

              </div>
            </div>
