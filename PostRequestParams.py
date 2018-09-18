import requests
class PostRequestParams:

	link = None
	key = None
	value = None

	def __init__(self, link, key, value):
		self.link = link
		self.key = key
		self.value = value

	def postRequestParamsStatus(self):
		print(requests.post(self.link, data = {self.key:self.value}).status_code)

    def postRequestParamsResponse(self)
    	print(requests.post(self.link, data = {self.key:self.value}).text)




