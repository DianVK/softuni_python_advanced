class Profile():
    def __init__(self, username: str, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 > len(value) or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value
        return

    # props
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) >= 8:
            one_letter = False
            one_num = False
            for x in value:
                if x.isdigit():
                    one_num = True
                elif x.isalpha():
                    if x.isupper():
                        one_letter = True
            if one_num and one_letter:
                self.__password = value
                return
            else:
                raise ValueError(
                    "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
