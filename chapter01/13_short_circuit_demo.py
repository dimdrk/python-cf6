name = "Bob"

print("===========or============")
valid_user = None or "User"
print("Hello", valid_user)

valid_user = name or "User"
print("Hello", valid_user)

print("==========and============")
email = "bob@example.com"
valid_email = email and email != ""

print(valid_email)

if(valid_email):
    print(f"Hello {valid_user}, your email is {email}.")
else:
    print(f"Hello {valid_user}, please give you email.")