def email_list(domains):
    emails = []
    for i in domains:
        mail = ""
        for j in domains[i]:
            mail = "{}@{}".format(j, i)
            emails.append(mail)
    return emails


print(email_list(
    {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
     "hotmail.com": ["bruce.wayne"]}))
