# import all the libraries we will be using
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from corona_bot.news_manager import get_news

# set up Flask to connect this code to the local host, which will
# later be connected to the internet through Ngrok
app = Flask(__name__)
    
# Main method. When a POST request is sent to our local host through Ngrok 
# (which creates a tunnel to the web), this code will run. The Twilio service # sends the POST request - we will set this up on the Twilio website. So when # a message is sent over SMS to our Twilio number, this code will run
@app.route('/', methods=['POST'])
def sms():
    response = MessagingResponse()
    message = Message()
    message.body(get_news())
    response.append(message)
    return str(response)
	
# when you run the code through terminal, this will allow Flask to work
if __name__ == '__main__':
    app.run()