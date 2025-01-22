mail = dict()
l = list()
while mail_name := input():
    mail, name = mail_name.split(": ")
    login = name.split()
    for log in login:
        full = (log + "@" + mail)
        l.append(full)
l.sort()
for all in l:
    print(all)