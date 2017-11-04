import re
number = '\d'
numbers  = "[\d]+"
not_numbers = "[\D]+"

charactor = '\w'
string = "[\w]+"

# MOBILE : + <isd-code> - <10 digit mobile number >
mobile = r'\+?[\d]+-[\d]+'

# EMAIL  <word/digit/dot/hyphen>@<word/digit/dot/hyphen>
email = r'[\w\.\d-]+@[\w\.-]+'

# WEBSITE  http<s>//:<word/hyphen/digit/dot>
website = r"http[s]?://[\w\d\.-]+\.[\w]+"

data = """ Hello compasscek@gmail.com is our email and http://www.compasscek.in is our website,
you can contact us on contact@compasscek.in !
or for any assistance about our college,log on  to https://cek.ac.in or dial us +91-9492768548  9752886259"""

print re.findall(email, data)
print re.findall(website, data)
print re.findall(mobile, data)
