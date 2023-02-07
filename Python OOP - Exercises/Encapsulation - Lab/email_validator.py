class EmailValidator():
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        data = email.split("@")
        username = data[0]
        mail,domain = data[1].split(".")
        return self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))


# class EmailValidator:
#
#     def __init__(self, min_length, mails, domains):
#         self.min_length = min_length
#         self.mails = mails
#         self.domains = domains
#
#     def __is_name_valid(self, name):
#         if len(name) >= self.min_length:
#             return True
#         return False
#
#     def __is_mail_valid(self, mail):
#         for x in self.mails:
#             if x == mail:
#                 return True
#         return False
#
#     def __is_domain_valid(self, domain):
#         for x in self.domains:
#             if x == domain:
#                 return True
#         return False
#
#     def validate(self, email):
#         name_index = email.index("@")
#         mail_index = email.index(".")
#         name = email[0:name_index]
#         mail = email[name_index + 1:mail_index]
#         domain = email[mail_index + 1::]
#
#         if EmailValidator.__is_mail_valid(self,mail) and\
#                 EmailValidator.__is_domain_valid(self,domain) and\
#                 EmailValidator.__is_name_valid(self,name):
#             return True
#         return False