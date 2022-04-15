import selenium,json,time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_path ='/Users/abby/PycharmProjects/selenium/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get('https://book.douban.com/tag/%E6%82%AC%E7%96%91?type=S')

# find all books on this page
book_dict = {"悬疑":[]}

current_page = 1

while current_page < 50:

    books = driver.find_elements(By.CLASS_NAME, "subject-item")


    for book in books:
        # get douban booklink and bookname
        link_and_book = book.find_element(By.TAG_NAME,"h2")
        bookname = link_and_book.text
        link = link_and_book.find_element(By.TAG_NAME,"a").get_attribute("href")


        #get douban photo link
        photo_link_class = book.find_element(By.CLASS_NAME,"pic")
        photo_link = photo_link_class.find_element(By.TAG_NAME,"img").get_attribute("src")


        # get the other elements

        # sometimes ratings and reviwers not available

        publication = book.find_element(By.CLASS_NAME,"pub").text


        reviewer = book.find_element(By.CLASS_NAME,"pl").text
        rating = book.find_element(By.CLASS_NAME, "rating_nums").text

        new_book = {
            "bookname": bookname,
            "Author and publication": publication,
            "Rating": rating,
            "Reviewers": reviewer[1:-4],
            "Link": link,
            "Photo": photo_link
        }

        book_dict["悬疑"].append(new_book)

    current_page += 1
    page = driver.find_element(By.LINK_TEXT, str(current_page))
    page.click()
    print(current_page)


with open ('悬疑.json','w') as file:
    json.dump(book_dict,file,indent=4, ensure_ascii=False)


driver.quit()
