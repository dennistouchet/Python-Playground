import requests, bs4, re, urllib, os
from time import sleep

pofhome = 'http://www.pof.com/viewprofile.aspx?profile_id=133116417'
pofprofile = 'https://www.pof.com/viewprofile.aspx?profile_id='
pofSoup = None
pidregex = re.compile(r'(\d){7,10}')
liregex = re.compile(r'http:.*\.jpg')
cwd = os.getcwd()

print('folder count: ' + str(len(list(os.walk(cwd)))))   

def get_page(url):
    global pofSoup
    req = requests.get(url)
    req.raise_for_status()
    pofSoup = bs4.BeautifulSoup(req.text, "lxml")    

def save_images(folder, ils):
    thisdir = cwd + '/' + folder
    print(thisdir)
    os.mkdir(thisdir)
    for n in range(len(ils)):
        with open(folder + '/image' + str(n) + '.jpg', 'wb') as handle:
            response = requests.get(ils[n], stream=True)
            if not response.ok:
                print(response)
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)

print("Starting PoF Image Account Image Ripper")

#Pull PoF HomePage
get_page(pofhome)

# Get All Profile Links
links = pofSoup.select('.imagebarsingle a')

pids = []

for i in range(len(links)):
    pids = pids + [pidregex.search(str(links[i].get('href'))).group()]
    print(pids[i-1])
    
#Pull PoF Profile Page
pofSoup = None
print(pofprofile + str(pids[0]))


#get profile images
def get_profile(pid):
    get_page(pofprofile + str(pid))

    links = pofSoup.select('.image-thumb-wrap a')
    username = pofSoup.select('#username')[0].getText()
    age = pofSoup.select('#age')[0].getText()
    folder = str(pid) + '_' + str(username) + '_' + str(age)
    print(folder)
    imglinks = []
    if int(age) >= 21 and len(links) > 5:
        for j in range(len(links)):
            imglinks = imglinks + [liregex.search(str(links[j].get('href'))).group()]    
        save_images(folder, imglinks)

for i in range(len(pids)):
    get_profile(pids[i])
    sleep(1)
    
print('done')
