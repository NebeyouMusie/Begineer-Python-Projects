email = str(input("Enter you eamil: "))
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format = "Your user name is {} and your domain name is {}".format(username, domain_name)
print(format)