from fastapi import FastAPI, Request               # The main FastAPI import and Request Body object
from fastapi.responses import HTMLResponse      # Used for returning HTML responses (JSON is default)
from fastapi.staticfiles import StaticFiles     # Used for making static resources available to server
import uvicorn
import sendgrid
import os
from sendgrid.helpers.mail import *
from dotenv import load_dotenv

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Configuration
app = FastAPI()                              # Specify the "app" that will run the routing
app.mount("/public", StaticFiles(directory="public"), name="public")

# load_dotenv("api.env")
# sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
# print(f'API Key: {os.environ.get("SENDGRID_API_KEY")}')
#
# from_email = Email("lkimdaryl@gmail.com")
# to_email = To("lkimdaryl@gmail.com")
# subject = "Sending with SendGrid is Fun"
# content = Content("text/plain", "and easy to do anywhere, even with Python")
# mail = Mail(from_email, to_email, subject, content)
#
# try:
#     response = sg.send(mail)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Example route: return a static HTML page
@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
  with open("public/index.html") as html:
    return HTMLResponse(content=html.read())

@app.post("/send_message")
async def send_message(request: Request):
  form_data =await request.json()
  # print(form_data)
  # print(form_data['email'])
  # print(type(form_data['message']))

  load_dotenv("api.env")
  sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
  # print(f'API Key: {os.environ.get("SENDGRID_API_KEY")}')

  from_email = Email(os.environ.get("EMAIL"))
  to_email = To(os.environ.get("EMAIL"))
  subject = f"Message by: {form_data['name']}"
  content = Content("text/plain", form_data['message'])
  mail = Mail(from_email, to_email, subject, content)

  try:
    response = sg.send(mail)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return {'Status': 'Success'}
  except Exception as e:
    print(e)
    return {'Status': 'Fail'}


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# If running the server directly from Python as a module
if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8000)