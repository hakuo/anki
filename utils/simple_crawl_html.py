from requests_html import HTMLSession

#create the session
session = HTMLSession()

#define our URL
urls = [
    "https://www.essentialenglish.review/apps/4000-essential-english-words-4/"
]

filename = "output.txt"

with open(filename, "wb") as f:

    for url in urls:
        #use the session to get the data
        r = session.get(url)

        #Render the page, up the number on scrolldown to page down multiple times on a page
        r.html.render(sleep=1, keep_page=True, scrolldown=1)

        titles = r.html.find('.title')

        for title in titles:
            links = title.absolute_links
            if(len(links) == 0 or title.text == "Index"):
                continue
            print("Parsing title:", title.text)
            print("Link:", links)
            

            r1=session.get(list(links)[0])
            r1.html.render(sleep=1, keep_page=True, scrolldown=1)
            words = r1.html.find('.en-word')

            for word in words:
                f.write((word.text + "\n").encode("utf-8"))
