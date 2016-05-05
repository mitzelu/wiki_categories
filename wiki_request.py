from wikitools import wiki, category, api
import sys
import os 

from bs4 import BeautifulSoup
import urllib2

import wikipedia

def wikipedia_query(query_params):

	site = wiki.Wiki(url='http://en.wikipedia.org/w/api.php')
	request = api.APIRequest(site, query_params)
	result  = request.query(False)

	return result[query_params['action']]

def get_category_members(par_category, depth, lang='en'):
    category_name = 'Category:'+par_category
    if depth < 0:
        return 0
    
    #Begin crawling articles in category
    results = wikipedia_query({'list': 'categorymembers','cmtitle': category_name,'cmtype': 'page','cmlimit': '500','action': 'query'}) 

    #print results

    
    # Begin crawling subcategories
    results = wikipedia_query({'list': 'categorymembers',
                                   'cmtitle': category_name,
                                   'cmtype': 'subcat',
                                   'cmlimit': '500',
                                   'action': 'query'})

    subcategories = []

    if 'categorymembers' in results.keys() and len(results['categorymembers']) > 0:
        for i, category in enumerate(results['categorymembers']):
          cat_title = category['title']
          subcategories.append(cat_title.replace('Category:', ''))

    subcat= ''.join(cat.encode('latin-1', 'ignore')+',' for cat in subcategories).strip(',')

    if subcat !='':
      wp.write(par_category.encode('latin-1', 'ignore')+':'+subcat+'\n\n')

    for category in subcategories:
      get_category_members(category,depth-1)


def beuatifulsoup_wiki(item):

  print 'function'
  print item

  categories = []

  url  = 'http://en.wikipedia.org/wiki/' + item
  page = urllib2.urlopen(url)

  soup = BeautifulSoup(page, 'html5lib')

  data = soup.find('div', {'class' : 'mw-normal-catlinks'})

  data = data.findAll('a')

  for category in data:
    categories.append((category.text).encode('ascii'))

  #get_category_members(category[1], 2)

  return categories

results = wikipedia_query({'category': 'Beauty',
                'depth':  1,
                'action': 'categorytree'})

industries = ['beauty', 'fashion', 'gadgets', 'games', 'household', 'food', 'sports']

for industry in industries:

  wp = open(industry, 'w')
  category = beuatifulsoup_wiki(industry)
  print category
  get_category_members(category[1], 1)

given_word = 'soap'

categories = beuatifulsoup_wiki(given_word)

categories = del categories[0]

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


