import requests
from bs4 import BeautifulSoup
import os

url = ['https://www.shutterstock.com/search/piano?image_type=photo&measurement=px&min_width=224&min_height=224',
       'https://www.shutterstock.com/search/violin?image_type=photo&measurement=px&min_width=224&min_height=224',
       'https://www.shutterstock.com/search/flute?image_type=photo&measurement=px&min_width=224&min_height=224'
        ]

usr_agent = {
    'User-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

def down_images(url,name,start):
    r = requests.get(url,headers=usr_agent)
    soup = BeautifulSoup(r.text,'html.parser')
    image = soup.findAll('img', class_ = 'z_h_9d80b z_h_2f2f0', limit=700)
    for i, img in enumerate(image):
        link = img.get('src')
        with open(name + str(i+start)+'.jpg','wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('writing: ',i+start)

def get_image_details(url):
    r = requests.get(url, headers=usr_agent)
    soup = BeautifulSoup(r.text,'html.parser')
    for i, image in enumerate(soup.findAll('img', class_='z_h_9d80b z_h_2f2f0', limit=150)):
        image = image.get('src')
        print(f'{i}_____{image}______')

if __name__=='__main__':
    os.mkdir(os.path.join(os.getcwd(),'instruments'))
    os.chdir(os.path.join(os.getcwd(),'instruments'))

    down_images(url[0],'piano',0)
    for x in range(2,150):
        down_images(url[0]+'&page='+str(x),'piano',(x-1)*20)

    down_images(url[1],'violin',0)
    for x in range(2,150):
        down_images(url[1]+'&page='+str(x),'violin',(x-1)*20)

    down_images(url[2],'flute',0)
    for x in range(2,150):
        down_images(url[2]+'&page='+str(x),'flute',(x-1)*20)
