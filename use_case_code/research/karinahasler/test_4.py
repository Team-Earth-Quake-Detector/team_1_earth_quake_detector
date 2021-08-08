import ipinfo

access_token = "62d93ea5300e80"
handler = ipinfo.getHandler(access_token)
ip_address = '92.188.181.161'
details = handler.getDetails(ip_address)
print(details.loc)

latitude = details.loc[0:7]
longitude = details.loc[8:14]

print(latitude)
print(longitude)
