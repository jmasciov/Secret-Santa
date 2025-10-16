from MembersInformation.MembersDetails import members_list

"""
Include information about each participant.
Use to gather information about recipient, included in email.
Sourced from Google form
"""

print(members_list)

for x in members_list:
    print(x.name)