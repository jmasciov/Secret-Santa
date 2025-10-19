# from graph import hamilton_path
import configparser
import smtplib
from email.message import EmailMessage

from members import Member
from member_details import members_dict


config = configparser.ConfigParser()
config.read('config.ini')

"""
1. Gather Hamilton path from graph.py
    save to folder as text file

2. Iterate through path (2 pointer)
    Each person gets and email with their target information
        (i gets details of i+1)
        Account for out of range

    2a. For each person, i
        create a text file of details of i+1
        save to local folder
        send contents to person i
"""
####################
####################
###
def receiver_info(sender:Member, receiver: Member) -> str:
    email_message = f"""
    Hello {sender.name_card},
    You will be mailing to {receiver.name_card}. 
    Name on envelope: {receiver.name_envelope}.
    Address: {receiver.address}.
    Pronouns: {receiver.pronouns}.
    Theme: {receiver.theme}.
    Requests: {receiver.requests}.
    Interests: {receiver.interests}.
    """
    return email_message
###



####################
####################
EMAIL_TEXT_FILE = "MembersInformation/"

"""
hamilton_path = ['B', 'C', 'D', 'A', 'G', 'E', 'F', 'B']
print(hamilton_path)
hamilton_path_string = str(hamilton_path)

for i in range(len(hamilton_path)-1):
    print(i, hamilton_path[i], hamilton_path[i+1])
    hamilton_path_string += f"\n{hamilton_path[i]} => {hamilton_path[i+1]}"

with open("MembersInformation/hamilton_path.txt", "w") as text_file:
    text_file.write(str(hamilton_path_string))


for i in range(len(hamilton_path)-1):
    print(i, hamilton_path[i], hamilton_path[i+1])
"""

hamilton_path = ['Josh', 'Molly', 'Morgon', 'Josh']

for i in range(len(hamilton_path)-1):
    sender_name = hamilton_path[i]
    receiver_name = hamilton_path[i+1]
    message = receiver_info(members_dict[sender_name], members_dict[receiver_name])

    with open("MembersInformation/"+sender_name+".txt", "a") as text_file:
        text_file.write(message)

    ##
    ## SEND EMAIL
    ##


body = "This is email body"
subject = "Testing email subject"
receiver_email = members_dict['Molly'].email


msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg['From'] = config['smtp']['EMAIL_USERNAME']
msg['To'] = receiver_email


smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login(config['smtp']['EMAIL_USERNAME'], config['smtp']['APP_SPECIFIC_PASSWORD'])
smtp.send_message(msg)
print("Email success.")

