import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# crawling logic...

def get_links(url, parse_main, list_to_crawl, external_links) :
    # Fetch the webpage content
    response = requests.get(url)

    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all 'a' tags with 'href' attribute
    for a_tag in soup.find_all("a", href=True):
        # Normalize the URL by joining the base URL and the href attribute value
        href_new = urljoin(url, a_tag["href"])
        #if internal link found
        if  urlparse(href_new).netloc == parse_main.netloc :
            list_to_crawl.append(href_new)
        #if exernal link found
        else :
            external_links.append(href_new)
        
    # Find all tags with 'src' attribute
    for tag in soup.find_all(src=True):
        # Normalize the URL by joining the base URL and the src attribute value
        src_new = urljoin(url, tag["src"])
        #if internal link found
        if  urlparse(src_new).netloc == parse_main.netloc :
            list_to_crawl.append(src_new)
        #if exernal link found
        else :
            external_links.append(src_new)
            

    



def crawl_this_one( parse_main, list_to_crawl, already_crawled, external_links) :
    
    # we will crawl the first website in list
    url = list_to_crawl[0]

    # if already crawled then return
    for link_x in already_crawled :
        if url == link_x :
            list_to_crawl.pop(0)
            return
        

    links_till_now = len(list_to_crawl)

    # function to add all the websites by crawling url
    get_links(url, parse_main, list_to_crawl, external_links)
    # Print the current URL and the number of links found
    print(f"URL: {url} - Found {len(list_to_crawl) -links_till_now} links")

    already_crawled.append(url)

    list_to_crawl.pop(0)






url_main = "https://krittikaiitb.github.io"

# in order to identify internal links
parse_main = urlparse(url_main)

# list_to_crawl a list of the links to crawl
# external_links is a list of external links
# already crawled is list that keeps track of the crawled links
 
list_to_crawl = list()
external_links = list()
already_crawled = list()

list_to_crawl.append(url_main)

while len(list_to_crawl)>0 :
    #call the crawler functiion
    crawl_this_one( parse_main, list_to_crawl, already_crawled, external_links )
    # print the no. of links to crawl, no. of links crawled, no. of external links found
    print(f" {len(list_to_crawl)} links to crawl { len(already_crawled)} links crawled and {len(external_links)} external links" )






