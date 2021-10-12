with open("srs.doc", 'rb') as rf:
  with open("srs_copy.txt", 'wb') as wf:
    for line in rf:
      wf.write(line)
 
