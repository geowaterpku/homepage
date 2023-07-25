import pandas as pd

from datetime import datetime
this_month = datetime.today().strftime('%Y-%m')

def get_google_citation():
	from scholarly import scholarly
	search_query = scholarly.search_author('Peirong Lin')
	first_author_result = next(search_query)
	n_citations = first_author_result['citedby']
	return n_citations

def get_citation(month):
	import os
	filename = 'Publications/citation.csv'

	if os.path.isfile(filename):
		# if file exist
		df = pd.read_csv(filename)
		citations = dict(zip(df.date, df.citation))
		if month in citations:
			# if there is a citation for this month
			return citations[month]
		else:
			# if there is no citation created for this month yet
			n_citations = get_google_citation()
			df = pd.concat([df,pd.DataFrame.from_dict({'date':[this_month],'citation':[n_citations]})], ignore_index=True)
			df.to_csv(filename,index=False)
			return n_citations

	else:
		# if file does not exist
		n_citations = get_google_citation()
		df = pd.DataFrame({'date':[this_month],'citation':[n_citations]})
		df.to_csv(filename,index=False)
		return n_citations
	
n_citations = get_citation(this_month)