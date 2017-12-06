from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)


listnums= ["+19998887777"]
outbound= ["+19998887777"]
text = [" update"]
	
sched = BlockingScheduler()

def job_function():
	for num in listnums:
		message = client.messages.create(
  			to= num,
    		from_= outbound,
    		body=  text)

		print('Id # ' + message.sid + " has sent: " + str(text))

#Schedule job function to be called every 60 seconds
sched.add_job(job_function, 'interval', seconds = 1)
