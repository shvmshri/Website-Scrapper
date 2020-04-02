import json
import excelmod
import verifyName

with open("students.json") as x: 
     data = json.load(x) 
path = './Abcd.xlsx'
rows = excelmod.row_count(path,"Sheet1")
cols = excelmod.col_count(path,"Sheet1")
def check(off_list,json_name):
     if json_name in off_list:
          return True
     else:
          return False
cor_row_no = []
cor_name = []

print("****Printing Invalid names****")
for i in range(3,rows+1):
     name_data = excelmod.read(path,'Sheet1',i,1)
     if verifyName.check_splcharacter(name_data) or len(name_data)==1 or name_data.lower() == name_data:
          print(name_data)
     else:
          cor_row_no.append(i)
          cor_name.append(name_data)
print("****Printing Valid names and their****")
for i in data:
     if(check(cor_name,i["n"])):
          desIn = cor_row_no[cor_name.index(i["n"])]
          print(i["n"],end=",")
          print(i["r"],end=",")
          print(i["d"],end=",")
          r=excelmod.read(path,"Sheet1",desIn,2)
          print(r,end=",")
          pn=excelmod.read(path,"Sheet1",desIn,3)
          print(pn)
          print()