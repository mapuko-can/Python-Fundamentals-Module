class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


emails = []

command = input()

while command != "Stop":
    send, rec, cont = command.split()
    email = Email(send, rec, cont)
    emails.append(email)
    command = input()

# send_emails = list(map(lambda x: int(x), input().split(", ")))
send_emails = [int(index) for index in input().split(", ")]

for index in send_emails:
    email = emails[index]
    email.send()

for email in emails:
    print(email.get_info())

