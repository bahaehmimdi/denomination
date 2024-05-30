from flask import Flask, jsonify,request

import requests


from bs4 import BeautifulSoup




app = Flask(__name__)



def google_search(query):
    # Replace spaces with plus signs for the query string
    query = query.replace(' ', '+')
    url = f'https://www.google.com/search?q=site:societe.com "{query}"'
   
    # Set the User-Agent to mimic a real browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Send the request to Google
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Parse the HTML content
   # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the first search result title, snippet, and link
    first_result = {}
    g = soup.find("h3")
    
    if g:
  
        title = g.find('h3')
       
        if title:
            title = title.text
            link = g.find('a', href=True)['href']
            snippet = g.find('span', class_='aCOpRe')
            if snippet:
                snippet = snippet.text
            first_result = {'title': title, 'link': link, 'snippet': snippet}
    
    return g.text.split("(")[0]
@app.route('/<path:subpath>')
def tasktest(subpath):
 
      return google_search(subpath)

if __name__ == "__main__":
    app.run()
