import re

clients = [['홍길동', '010-1234-1234', 'gdHong@skshieldus.com'],
['홍길순', '010-1234-5678', 'gsHong@skshieldus.com'],
['김대감', '010-5678-1234', 'dgkim@skshieldus.com'],
['세종대왕', '011-3456-8765', 'kingejong@skshieldus.com']]


def subName(name):
    return name[0] + '*' * (len(name)-1)

def subPH(phoneNumber):
    parts = phoneNumber.split('-')
    parts[1] = re.sub('\d', '*', parts[1])
    parts[2] = re.sub('\d', '*', parts[2])
    return parts[0] + '-' + parts[1] + '-' + parts[2]

def subMail(email):
    parts = email.split('@')
    username = parts[0][0] + '*' * (len(parts[0]) - 2) + parts[0][len(parts[0]) - 1]
    domain = parts[1]
    return username + '@' + domain

for i in range(4):
    name = clients[i][0]
    clients[i][0] = subName(name)
    phoneNumber = clients[i][1]
    clients[i][1] = subPH(phoneNumber)
    email = clients[i][2]
    clients[i][2] = subMail(email)


print(clients)
