import json
import csv

from keras.utils import get_file

x = get_file('found_books_filtered.ndjson', 'https://raw.githubusercontent.com/WillKoehrsen/wikipedia-data-science/master/data/found_books_filtered.ndjson')

data = []

with open(x, 'r', encoding='utf-8') as fin:
    # Append each line to the books
    data = [json.loads(l) for l in fin]



import csv

with open('books_details.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'author', "country", 'pages', 'publisher', 'pub_date'])
    for item in data:
        if 'name' in item[1]:
            name =item[1]['name']
        else:
            name =""
        if 'author' in item[1]:
            author =item[1]['author']
        else:
            author =""

        if "country" in item[1]:
            country =item[1]["country"]
        else:
            country =""
        if 'pages' in item[1]:
            pages =item[1]['pages']
        else:
            pages =""
        
        if 'publisher' in item[1]:
            publisher =item[1]['publisher']
        else:
            publisher =""

        if 'pub_date' in item[1]:
            pub_date =item[1]['pub_date']
        else:
            pub_date =""

        writer.writerow([name, author, country, pages, publisher, pub_date])



