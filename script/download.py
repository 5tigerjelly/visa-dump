from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import requests
import os.path
from multiprocessing.pool import ThreadPool

us_department_of_labor_root = 'https://www.foreignlaborcert.doleta.gov'
us_department_of_labor_link = us_department_of_labor_root + '/performancedata.cfm#dis'

def extract_xlsx(url, root):
    ret = []
    content = urlopen(url)
    soup = BeautifulSoup(content.read(), "html.parser")
    for link in soup.select('a'):
        href = link.get('href')
        if href and href.endswith('.xlsx'):
            ret.append(root+href)
    return ret

def download(url) -> str:
    local_filename = '../data/xlsx/' + url.split('/')[-1]
    if not os.path.isfile(local_filename):
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
    return local_filename

def download_multithread(url_list):
    results = ThreadPool(3).imap_unordered(download, url_list)
    for r in results:
        print(r)

if __name__ == "__main__":
    xlsx_list = extract_xlsx(us_department_of_labor_link, us_department_of_labor_root)
    download_multithread(xlsx_list)
