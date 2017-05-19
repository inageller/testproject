#import elasticsearch

#es = elasticsearch.Elasticsearch("https://iprice:fGcXoXcBtYaWfUpE@es-qa.ipricegroup.com:443")

import requests

#res = requests.post("https://iprice:fGcXoXcBtYaWfUpE@es-qa.ipricegroup.com:443", )
#print res.headers
#princontentt res.
import requests
import json
import numpy as np
import csv
import sys

import ast

HEADERS = {'content-type': 'application/json'}
url = "https://iprice:fGcXoXcBtYaWfUpE@es-qa.ipricegroup.com:443/product_my/_search"

data = {
   "track_scores": False,
   "query": {
      "bool": {
         "must": [
            {
               "match": {
                  "brand.name": ""
               }
            },
            {
               "match": {
                  "category.name": ""
               }
            },
            {
               "match": {
                  "comparable": False
               }
            }
         ]
      }
   },
   "aggs": {
      "shingles": {
         "terms": {
            "field": "name.shingle",
            "size": 100000,
            "min_doc_count": 3,
            "order": {
               "_count": "desc"
            }
         }
      }
   },
   "size": 0
}




#params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}

res = requests.post(url, data=json.dumps(data), headers=HEADERS)

#print res.content

#sys.exit()

result = json.loads(res.content)



buckets = result['aggregations']['shingles']['buckets']




writer = csv.writer(open("shingles.csv","wb"),delimiter=";")
for bucket in buckets:
    writer.writerow([bucket['key'],bucket['doc_count']])

#shingles = np.array([buckets['key']],[buckets['doc_count']])

#print shingles