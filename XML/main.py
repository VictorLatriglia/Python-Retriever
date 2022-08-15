from bs4 import BeautifulSoup
 
 
# Reading the data inside the xml
# file to a variable under the name
# data
with open('hurricanes.xml', 'r') as f:
    data = f.read()
 
# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object
Bs_data = BeautifulSoup(data, "xml")
 
# # Finding all instances of tag
# # `unique`
b_unique = Bs_data.find_all('May')
 
#print(b_unique)
 
# # Using find() to extract attributes
# # of the first instance of the tag
b_name = Bs_data.find('May')
 
print(b_name)
 
 
 