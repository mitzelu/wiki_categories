# to do 
from wiki_request import *


industries = ['beauty', 'fashion', 'gadgets', 'games', 'household', 'food', 'sports']

for industry in industries:

  wp = open(industry, 'w')
  category = beuatifulsoup_wiki(industry)
  print category
  get_category_members(category[1], 1)


categories = beuatifulsoup_wiki(given_word)

#start searching each category 
for item in categories:

	#in each file
	for industry in industries:

		teams = open(industry, 'r')
		teams = teams.read()

		count = 0

		if item in teams:
			count = count + 1
		
		if count != 0:
			print industry + ' -> ' + item + ': ' + str(count)




	

