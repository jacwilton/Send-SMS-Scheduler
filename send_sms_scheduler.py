from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler

# Your Account SID from twilio.com/console
account_sid = " account_id"
# Your Auth Token from twilio.com/console
auth_token  = "account token"

client = Client(account_sid, auth_token)


listnums= ["+19999999999", "+19999999999"]
outbound= ["+19999999999"]
text = [" Drain battery."]

def job_function():
	for num in listnums:
		#for i in range(len(text))
		#print(text[i])

		message = client.messages.create(
  			to= num,
    		from_= outbound,
    		body=  text)

	print((message.sid) + " Text Message 1 has sent!" + str(text))
		
sched = BlockingScheduler()

#Schedule job function to be called every 60 seconds
sched.add_job(job_function, 'interval', seconds = 10)

sched.start()
