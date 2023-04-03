from bs4 import BeautifulSoup

with open('website.html') as file:
    content = file.read()


soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.p)

# find all items
all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # get text/value of the tag
    # print(tag.getText())

    # get the value of an attribute
    # print(tag.get('href'))
    pass


# `soup.find` is to find the first item
heading = soup.find(name='h1', id='name') # find the first h1 that has an id of 'name'
# print(heading)

section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.getText()) # get text
# print(section_heading.name) # get element name (i.e. 'h3')
# print(section_heading.get('class')) # get calue of an attribute


company_url = soup.select_one(selector='p a')
print(company_url)

name = soup.select_one(selector='#name')
print(name)

headings = soup.select('.heading')
print(headings)