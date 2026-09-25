# The single responsibility (SRP) states that a class should have only one reason to change
# For example
# A class that manages user data should not also handle writing data to files
# By separating responsibilities , changes in one part of the system won't break unrelated parts

class User:
    def __init__(self , name , email):
        self.name = name
        self.email = email
        
    def get_user_info(self):
        return f'User : {self.name} , Email : {self.email}'
    
    
class UserFileManager:
    def save_to_file(self , user : User , filename):
        with open(filename , 'w') as f:
            f.write(user.get_user_info())
            
class UserLogger:
    def print_user(self , user : User):
        print(user.get_user_info())
        
        
u = User('Dracula' , 'dracula@gmail.com')
logger = UserLogger()
file_manager = UserFileManager()

logger.print_user(u)
file_manager.save_to_file(u , 'users.txt')