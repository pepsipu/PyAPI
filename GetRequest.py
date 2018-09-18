import requests
class GetRequest:

	link = None
	def __init__(self, link):
		self.link = link
    
	def getRequestStatus(self):
		requests.get(self.link)
		print(requests.get(self.link).status_code)

	def getRequestText(self):
		print("Your response is...")
		print(requests.get(self.link).text)

