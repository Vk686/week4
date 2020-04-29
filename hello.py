tempName = "Hello <<UserName>>, How are you?"
username = input("Enter User Name: ")
if len(username) < 5:
	print("User Name must have 5 characters.")
else:
	print(tempName.replace("<<UserName>>",username))
