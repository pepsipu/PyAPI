import time
import requests
print("PyAPI by Sammy Hajhamid. Credits to Kenneth Reitz for the request module making this program possible.")
time.sleep(1)
requestChoice = str(input("What request will you be sending today? (GET/POST)\n"))

if requestChoice == "GET":
	print("GET Request chosen. One moment please.")
	time.sleep(1)

	from GetRequest import GetRequest
	getTargetWeb = str(input("What link will you be sending a GET request to?\n"))
	getSee = str(input("What options would you like to see? (STATUS/TXT)\n"))

	if getSee == "STATUS":
		GetRequest(getTargetWeb).getRequestStatus()
		input("Type anything to finish.\n")

	elif getSee == "TXT":
		GetRequest(getTargetWeb).getRequestText()
		input("Type anything to finish.\n")

	else:
		print("That's not recognized! Exiting...")
		exit()

elif requestChoice == "POST":
	print("POST Request chosen. One moment please.")
	time.sleep(1)
	postTargetWeb = str(input("What link will you be sending a POST request to?\n"))
	postParams = str(input("Would you like to input parameters? (Y/N)\n"))

	if postParams == "Y":
		from PostRequestParams import PostRequestParams
		postParmsSee = str(input("What options would you like to see? (STATUS/TXT)\n"))

		if postParmsSee == "STATUS":
			PostRequest(postTargetWeb).postRequestParamsStatus()
			input("Type anything to finish.\n")

		elif postParmsParams == "TXT":
			PostRequest(postTargetWeb).postRequestParamsResponese()
			input("Type anything to finish.\n")

		else:
			print("That's not recognized! Exiting...")
			exit()


	elif postParams == "N":
		from PostRequest import PostRequest
		postNoParmsSee = str(input("What options would you like to see? (STATUS/TXT)\n"))

		if postNoParmsSee == "STATUS":
			PostRequest(postTargetWeb).postRequestStatus()
			input("Type anything to finish.\n")

		elif postNoParmsSee == "TXT":
			PostRequest(postTargetWeb).postRequestResponse()
			input("Type anything to finish.\n")

		else:
			print("That's not recognized! Exiting...")
			exit()
	else:
		print("That's not recognized! Exiting...")
		exit()


else:
	print("That's not recognized! Exiting...")
	exit()
print("Thanks for using PyAPI! - Sammy Hajhamid")
time.sleep(1.5)
exit()