import datetime
import pandas


columns = [
 "name",
 "project_description",
 "project_type",
 "personal_contributions",
 "activities",
 "tools",
 "data_type",
 "project_page",
 "project_link",
 "completion",
 "tags"
]

def convert_tags_to_classes(tags, class_head = 'tag-class-'):
  return ','.join([ class_head+tag for tag in tags.split(', ') ])


def create_tag_list(portfolio):
  tags = set([])
  for item in portfolio:
    item_tags = item['tags'].split(', ')
    tags.update(item_tags)
  return list(tags)

def date_sort_key_function(r):
  d = r['completion']
  if(d == 'Ongoing'):
    return str(datetime.date.today())
  if(len(d) == 7):
    return d + '-99'
  return d


def sort_by_date(portfolio_list):
  return sorted(portfolio_list, key = date_sort_key_function, reverse = True)
  
  

def load_portfolio():
  portfolio_data = pandas.read_csv('static/data/portfolio.csv')
  portfolio_data = portfolio_data[columns].fillna('')
  portfolio_columns = [ ' '.join([ w.capitalize() for w in c.split('_') ]) for c in portfolio_data.columns ]
  portfolio = sort_by_date([ dict(row[1]) for row in portfolio_data.iterrows() ])
  tag_list = create_tag_list(portfolio)
  for i in range(len(portfolio)):
    portfolio[i]['tag_classes'] = convert_tags_to_classes(portfolio[i]['tags'])
  return portfolio_columns, portfolio, tag_list




