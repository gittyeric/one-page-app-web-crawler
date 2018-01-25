# one-page-app-web-crawler
Minimalistic example of crawling any kind of web page, including a dynamic one page app

## Setup

1. You'll need to have [Python 3](https://www.python.org/downloads/) installed on your system.

2. Now either download this project or clone with git:

	git clone https://github.com/gittyeric/one-page-app-web-crawler.git
  
3. Download the Selenium [web driver for chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) (you can use Firefox too but you'll have to change the code a bit).  This will allow you to control your browser with Python code.

4. Drop the downloaded web driver file into the root of this project.

5. (Optional) Download [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download) for easier code editing and running

## Running (Command Line)

Now simply run the python script from command line:

  cd path/to/project
  
  python clark_crawl.py
  
## Clark what?

This is a simple example written for the Clark County PD, it'll run through an inmate database, pull out all the records page-by-page and print them out at the end.  You can change the print statement in clark_crawl.py to save the result however you'd like, and you can follow the code in crawler.py to see how it's done.
