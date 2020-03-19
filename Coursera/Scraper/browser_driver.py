from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("localhost:8000")
assert "Forum" in driver.title
elem = driver.find_element_by_name("content")
elem.send_keys("yeeei")
#elem.send_keys(Keys.RETURN)
post_go = driver.find_element_by_id("go")
#post_go.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print (driver.page_source)
##driver.close()


# import re
# import mechanize
# 
# url = 'http://localhost:8000'
# br = mechanize.Browser()
# page = br.open(url)
# 
# # follow second link with element text matching regular expression
# #response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
# assert br.viewing_html()
# for form in br.forms():
#     print form
#     
# br.select_form("searchform")
#   br['content'] = "Mechanize"
  
  #br.form["content"] = ["another post with mechanize"]
#response = br.submit()
#print (response.read())
