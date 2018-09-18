import requests
class PostRequest:

	link = None

	def __init__(self, link):
		self.link = link

	def postRequestStatus(self):
		print(requests.post(self.link).status_code)
	
	def postRequestResponse(self):
		print(requests.post(self.link).text)

	




