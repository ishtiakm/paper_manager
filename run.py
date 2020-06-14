filename="record.txt"

in1=input("Do you intend to search? or write new record? Type s to search, w to write or t to see all the tags: ")
if in1.lower() == "w":
    record=open(filename,"a")
    temp=[]
    name=input("Enter the name of the paper (full name not required): ")
    temp.append(name)
    folder=input("Enter the name of the folder where it is stored: ")
    temp.append(folder)
    other=(";").join(temp)
    print("Enter the names of tags; you can use space in a tag; after each tag insert enter. When you are done, type DONE : ")
    tag="EV"
    tags=[]
    while tag.lower()!="done":

      tags.append(tag.lower())
      tag=input()

    temptag=(",").join(tags[1:])
    line=(";").join([other,temptag,"\n"])
    record.write(line)
    record.close()

if in1.lower() == "s":
  record=open(filename,"r")
  topic=input("what tag you want to search?: ")
  papers=[]
  for item in record:
    items=item.split(";")
    tags=items[-2].split(",")
    if topic.lower() in tags:
      t=(">").join(items[:2])
      papers.append(t)
  if len(papers)==0:
    print("No paper on this topic")
    print(papers)
  else:
    for paper in papers:
      print(paper)
  record.close

if in1.lower() == "t":
  record=open(filename,"r")
  from collections import Counter
  store=[]
  for line in record:
    temp=line.split(";")
    tags=temp[-2]
    tags2=tags.split(",")
    for i in tags2:
      store.append(i)

  topics=Counter(store)
  for keys,values in topics.items():
      print(keys,":",values)
  record.close
