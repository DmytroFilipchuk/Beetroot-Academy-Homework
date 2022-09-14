"""
Task 1

Create a class method named `validate`, which should be called from the `__init__`
method to validate parameter email, passed to the constructor. The logic inside the
`validate` method could be to check if the passed email parameter is a valid email string.

Email validations:

Valid email address format

Email address

"""

class Email():


    def __init__(self,email):

        self.email = email

        def validate():

            def allowed_charecters():  # checks if email consists only of allowed charecters

                special_characters = "!#$%^&*\ ()+?=,<>/"

                return any(c in special_characters for c in email)

            def first_element():  # checks the first element

                return email[0] == "."

            def ending(): # checks the ending

                return not email[-2:].isalpha()

            def at_sign(): # checks the at sign

                return "@" not in email or email.count("@") > 1

            def dot_in_domain(): # checks if there is one and only one dot in the domain

                domain_start = email.find("@")

                return "." not in email[domain_start:] or email[domain_start:].count(".") > 1

            def correct_following():  # An underscore, period, or dash must be followed by one or more letter or number

                special_char_idx = [i for i, c in enumerate(email) if c == "." or c == "-" or c == "_"]
                following_idx = [i + 1 for i in special_char_idx]
                following_elements = [email[i] for i in following_idx]

                for i in following_elements:
                    if not i.isalpha():
                        return True
                    else:
                        return False

            check = [allowed_charecters(),
                     first_element(),
                     ending(),
                     at_sign(),
                     dot_in_domain(),
                     correct_following()
                     ]

            if True in check:
                print("Invalid input")
            else:
                print("Good job")

        validate()


invalid_email_addresses = ["abc-@mail.com",
                   "abc..def@mail.com",
                   ".abc@mail.com",
                   "abc#def@mail.com",
                   "abc.def@mail.c",
                   "abc.def@mail#archive.com",
                   "abc.def@mail",
                   "abc.def@mail..com"
]

valid_email_addresses = ["abc-d@mail.com",
                           "abc.def@mail.com",
                           "abc@mail.com",
                           "abc_def@mail.com",
                           "abc.def@mail.cc",
                           "abc.def@mail-archive.com",
                           "abc.def@mail.org",
                           "abc.def@mail.com"
]

for i in valid_email_addresses:
    a = Email(i)

for i in invalid_email_addresses:
    a = Email(i)



