from fastapi import FastAPI, Request            # The main FastAPI import and Request Body object
from fastapi.responses import HTMLResponse      # Used for returning HTML responses (JSON is default)
from fastapi.staticfiles import StaticFiles     # Used for making static resources available to server
import uvicorn
import sendgrid
from sendgrid.helpers.mail import *

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Configuration
app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#routes
@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
  with open("public/index.html") as html:
    return HTMLResponse(content=html.read())

@app.post("/send_message")
async def send_message(request: Request):
  form_data =await request.json()
  sg_api_key = ""
  sg = sendgrid.SendGridAPIClient(api_key=sg_api_key)

  from_email = Email("lkimdaryl@gmail.com")
  to_email = To("lkimdaryl@gmail.com")
  subject = f"Message by: {form_data['name']}"
  content = Content("text/plain", form_data['message'])
  mail = Mail(from_email, to_email, subject, content)

  try:
    sg.send(mail)
    return {'Status': 'Success'}
  except Exception as e:
    print(e)
    return {'Status': 'Fail'}


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8000)