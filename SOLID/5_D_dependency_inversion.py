# Dependency Inversion Principle (DIP)

# The Dependency Inversion Principle (DIP) states:
# - High-level modules should not depend on low-level modules. Both should depend on abstractions.
# - Abstractions should not depend on details. Details should depend on abstractions.

# 💡 Key Idea:
# - High-level modules (the core logic of the application) 
#   should not depend on low-level modules (the implementation details). 
#   Instead, they should depend on abstractions (interfaces or abstract classes).
# - Implementation details should depend on abstractions, not the other way around. 
#   This makes the code more flexible and resilient to changes.

# ❌ Violation of DIP
class EmailService:
    def send_email(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")
    
class UserService:
    def __init__(self):
        self.email_service = EmailService() # ❌ Dependency of EmailService
    
    def register_user(self, username, email):
        self.email_service.send_email(email, f"Welcome, {username}!")

user_service = UserService()
user_service.register_user("John Connor", "johnconnor@mail.com")

# UserService dependency of EmailService. If we need change EmailService alse we need change UserService logic - violation DIP

# ✅ Correct DIP Implementation
from abc import ABC, abstractmethod

# ABSTRACT - interface for send message
class MessageService(ABC):
    @abstractmethod
    def send_message(self, recipient, message):
        pass

# EmailService Realisation
class EmailService(MessageService):
    def send_message(self, recipient, message):
        print(f'Sending email to {recipient}: {message}')

# SMSService
class SMSService(MessageService):
    def send_message(self, recipient, message):
        return print(f"Sending SMS to {recipient}: {message}")
    

# Module High Level: UserService
class UserService:
    def __init__(self, message_service: MessageService):
        self.message_service = message_service # Dependency abstract throught abstraction
    
    def register_user(self, username, email):
        self.message_service.send_message(email, f"Welcome, {username}!")


email_service = EmailService()
user_service = UserService(email_service)
user_service.register_user("John Connor", "johnconnor@mail.com")

# Using another realisation
sms_service = SMSService()
user_service = UserService(sms_service)
user_service.register_user("John Doe", "johndoe@mail.com")