from selenium import webdriver

browser = webdriver.Chrome()

def crawl_records():
    browser.maximize_window()
    browser.get("https://www.clark.wa.gov/sheriff/jail-roster#")

    # Sort by book date descending
    browser.find_element_by_css_selector(".col-md-2").click()
    browser.find_element_by_css_selector(".col-md-2").click()

    all_records = []

    page_records = _crawl_page_records()
    while len(page_records) > 9:
        all_records = all_records + page_records
        browser.find_element_by_id("jmsInfo_next").click()
        page_records = _crawl_page_records()

    return all_records

def _crawl_page_records():
    tableRows = browser.find_element_by_id("jmsInfo").find_elements_by_tag_name("tr")

    i = 0
    records = []
    for row in tableRows:
        if i > 0:
            columns = row.find_elements_by_tag_name("td")
            cfn = columns[0].text
            name = columns[1].find_element_by_tag_name("a").text
            book_date = columns[2].text
            location = columns[3].text
            release_date = columns[4].text
            charges = columns[5].text

            records += [cfn, name, book_date, location, release_date, charges]

        i += 1

    return records

