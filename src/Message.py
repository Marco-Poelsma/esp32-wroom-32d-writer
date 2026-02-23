class Message:
    __email: str
    __content: str

    def __init__(self, email: str, content: str):
        self.__email = email
        self.__content = content

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def content(self):
        return self.__content
    
    @content.setter
    def content(self, content: str):
        self.__content = content
