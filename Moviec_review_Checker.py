from bs4 import BeautifulSoup
from IPython.core.display import HTML,display,Image
import requests

s = requests.session()

movie = input("Enter Movie Name: ")
movie = movie.lower()
query = "+".join(movie.split()) 
URL = "https://www.imdb.com/search/title/?title=" + query
#print(URL)

#connection
response = s.get(URL)
content = response.content
#print(response.status_code)


#print(movie)

try:
    
    soup = BeautifulSoup(response.content, features="html.parser")
    
    #fetching image
    containers = soup.find_all("div", class_="lister-item-image float-left")
    #print(containers)
    
    if len(containers) == 0:
        print("Result not found")
    
    top = 0
    for result in containers:
        if top is 0:
            imgurl = result.a.find("img",class_="loadlate")["loadlate"]
            #print(imgurl)
            display(Image(imgurl, width=70, unconfined=True))
            top+=1

    #fetching image
    containers = soup.find_all("div", class_="lister-item-content")
    #print(containers)
    
    if len(containers) == 0:
        print("Result not found")
    
    top = 0
    for result in containers:
        if top is 0:
            name1 = result.h3.a.text
            name = result.h3.a.text.lower()
 
            year = result.h3.find("span", class_="lister-item-year text-muted unbold").text.lower() 
        
            #if film found (searching using name)
            if movie in name:
                #scraping rating
                rating = result.find("div",class_="inline-block ratings-imdb-rating")["data-value"]
                #print(rating)
                
                #scraping certificate
                rate = result.p.find("span", class_="certificate")
                #print(rate)
                if rate == None:
                    rates = "Not Rated"
                else :
                    rates = rate.contents[0]
                    
                #scraping genre
                genre = result.p.find("span", class_="genre")
                genre = genre.contents[0]
                #print(genre)
                    
                names=name1
                    
                #scraping genre
                ratings=rating
        
                genres=genre[1:]
                #print(genres) 
                top+=1

            #printing data
            print("____________________________________________________________")
            print("\n Film Name:",names,"\n Year:",year,"\n Certificate:",rates,"\n Ratings:",rating,"\n Genre:",genres)
            print("____________________________________________________________")
            
except Exception as e:
        #print(e)
        print("Sorry ! Couldn't fetch data try again...!!")
