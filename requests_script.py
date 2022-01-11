import requests as rs

'''
Gets the version of the requests library
'''
print(rs.__version__)

'''
GET the google homepage
'''
res = rs.get("https://www.google.com/")
print("STATUS CODE: ",res.status_code,"\n","CONTENT: ",res.content)