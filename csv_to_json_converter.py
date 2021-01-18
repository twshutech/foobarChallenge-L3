import csv
import json
import codecs

csv_path = "/Users/08622/Downloads/utf8csv.csv"
json_path = "/Users/08622/Documents/fooBarTest/foobarChallenge-L3/JSON_converted.json"
data = {}
c = 0

def utf_8_encoder(unicode_csv_data):
  print 'unicode_csv_data',unicode_csv_data
  for line in unicode_csv_data:
    print 'line',line
    yield line.encode('utf-8')

# csv = codecs.open(csv_path, encoding='utf-8')
# lines = csv.readlines()
# print lines[5]
# csv.close()

with open(csv_path, 'r') as f:
  reader = csv.reader(f, delimiter='\n')
  for rows in reader:
    rows = rows[0].split(',')
    print 'rows',rows
    # while c<10:
    #   c+=1
    #   print 'rows',rows
    key = rows[0]
    if len(rows) > 1:
      translation = rows[1]
      # print codecs.lookup(translation)
      try:
        # print translation,'passed translation', unicode(translation, errors='ignore')
        # print 'raw',rows[1],'decode',translation.decode('utf-8'),'encode',translation.encode('utf-8')
        translation = translation.decode('quoted-printable')
      except UnicodeError:
        print 'error translation',translation
      data[key] = translation
      # print 'data[key]',key,': "',data[key],'"'

with open(json_path, 'w') as f:
  f.write(json.dumps(data, indent=2, ensure_ascii=False).encode('utf-8'))
