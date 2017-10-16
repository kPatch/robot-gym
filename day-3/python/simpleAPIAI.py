import apiai

# https://dialogflow.com/docs/reference/agent/
client_token = '<YOUR CLIENT ACCESS TOKEN>'
ai = apiai.ApiAI(client_token)
request = ai.text_request()
request.session_id = 'api_ai', '<SESSION ID, UNIQUE FOR EACH USER>'
request.query = "Where do you live?"
response = request.getresponse()
print(response.read())