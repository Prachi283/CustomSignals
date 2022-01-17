from django.dispatch import Signal,receiver
# Creating Signal

notification = Signal()

#  Receiver Function

@receiver(notification)
def show_notification(sender,**kwargs):
	print("\n Sender: ",sender)
	print("\n")
	print("Arguments:",f'{kwargs}')	
	print("Notification\n")
