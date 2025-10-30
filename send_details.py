from graph import hamilton_path
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
    
    Dear elf {str(sender.name_card).split()[0]},
    
    Happy Prom! Happy Holidays! Thank you for spreading joy with this group of Inside Jokesters.
    
    {receiver.name_card} is on the nice list this year. Please mail a {receiver.theme} card to be opened during prom on December 6th.
    Requests: {receiver.requests}
    Interests: {receiver.interests}
    Pronouns: {receiver.pronouns}
    
    Address: {receiver.address}
    
    Looking forward to another wonderful Prom Night! Please message us with questions/concerns.
    
    From, Santa Rats Molly and Josh
    """
    return email_message
###



####################
####################
EMAIL_TEXT_FILE = "MembersInformation/"

# print(hamilton_path)
hamilton_path_string = str(hamilton_path)

for i in range(len(hamilton_path)-1):
    # print(i, hamilton_path[i], hamilton_path[i+1])
    hamilton_path_string += f"\n{hamilton_path[i]} => {hamilton_path[i+1]}"

with open("MembersInformation/hamilton_path.txt", "w") as text_file:
    text_file.write(str(hamilton_path_string))
# for i in range(len(hamilton_path)-1):
#     print(i, hamilton_path[i], hamilton_path[i+1])


subject = "SecRat Santa 2025"

###
print("Sending emails...")
for i in range(len(hamilton_path)-1):
    sender_name = hamilton_path[i]
    receiver_name = hamilton_path[i+1]
    message = receiver_info(members_dict[sender_name], members_dict[receiver_name])

    with open("MembersInformation/"+sender_name+".txt", "w", encoding='utf-8') as text_file:
        text_file.write(message)

    with open("MembersInformation/master_list.txt", "a", encoding='utf-8') as text_file:
        text_file.write(message)
        text_file.write("\n" + "-"*30 + "\n")

    ##
    ## SEND EMAIL
    ##
    body = message
    sender_email = members_dict[sender_name].email

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = config['smtp']['EMAIL_USERNAME']
    msg['To'] = sender_email

    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(config['smtp']['EMAIL_USERNAME'], config['smtp']['APP_SPECIFIC_PASSWORD'])
    # smtp.login(config['smtp']['EMAIL_USERNAME'], config['smtp']['EMAIL_PASSWORD'])
    smtp.send_message(msg)
    print("Email success.")
###
print("Emails complete!")

