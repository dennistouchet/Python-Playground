import requests, bs4, re, urllib

pofhome = 'http://www.pof.com'
pofprofile = 'https://www.pof.com/viewprofile.aspx?profile_id='
pofSoup = None
pidregex = re.compile(r'(\d){7,10}')
liregex = re.compile(r'http:.*\.jpg')

def get_page(url):
    global pofSoup
    req = requests.get(url)
    req.raise_for_status()
    pofSoup = bs4.BeautifulSoup(req.text, "lxml")    

print("Starting PoF Image Account Image Ripper")

#Pull PoF HomePage
get_page(pofhome)

# Get All Profile Links
links = pofSoup.select('.headline .link')

pids = []

for i in range(len(links)):
    pids = pids + [pidregex.search(str(links[i].get('href'))).group()]
    print(pids[i-1])
    
#Pull PoF Profile Page
pofSoup = None
print(pofprofile + str(pids[0]))


#TODO: Check if Profile Already Exists
get_page(pofprofile + str(pids[0]))

links = pofSoup.select('.image-thumb-wrap a')
imglinks = []
for j in range(len(links)):
    imglinks = imglinks + [liregex.search(str(links[j].get('href'))).group()]

def save_images(ils):
    for n in range(len(ils)):
        with open('pic' + str(n) + '.jpg', 'wb') as handle:
            response = requests.get(ils[n], stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

save_images(imglinks)
    
print('done')
