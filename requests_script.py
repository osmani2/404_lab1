import requests as rs


print("REQUESTS VERSION:")
print(rs.__version__)

print("\nGET GOOGLE HOMEPAGE:")
res = rs.get("https://www.google.com/")
print("STATUS CODE: ",res.status_code,"\n","CONTENT: ",res.text)

print("\nGET SCRIPT:")
res = rs.get("https://raw.githubusercontent.com/osmani2/404_lab1/master/requests_script.py")
print(res.text)