### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email():
    
    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_read(self):
        self.has_been_read = True
        
# --- Lists --- #
# Initialise an empty list to store the email objects.

inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    email1 = Email("test@email.com", "Welcome to you Inbox!", "Welcome to Hyperion Dev!")
    email2 = Email("test@email.com", "Testing1", "Great Work on the Bootcamp!")
    email3 = Email("test@email.com", "Testing2", "Your Excellent Marks!")
    new_emails = [email1, email2, email3]
    inbox.extend(new_emails)
    
def list_emails():
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for i, email in enumerate(inbox):
        print(f"{i}. {email.subject_line}")

def read_email(index):
    # Create a function which displays a selected email. 
    selected_email = inbox[index]
    print('-' * 50)
    print(f"Email Address: \t{selected_email.email_address}")
    print(f"Subject Line: \t{selected_email.subject_line}")
    print(f"Email Content: \t{selected_email.email_content}")
    print('-' * 50)
   
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    selected_email.mark_read()
    print(f"The email from {selected_email.email_address} has been marked as read!")
    print('-' * 50)

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
    print('-' * 50)
       
    if user_choice == 1:
        # add logic here to read an email
        list_emails()
        index = int(input(f"Enter the index of the email you want to read (0-{(len(inbox)-1)}): "))
        while index > (len(inbox)-1) or index < 0:
            print("Invalid index number! Try again!")
            index = int(input(f"Enter the index of the email you want to read (0-{(len(inbox)-1)}): "))
        
        read_email(index)
        
    elif user_choice == 2:
        # add logic here to view unread emails
        print('-' * 50)
        print("Unread Emails")
        print('-' * 50)
        print()
        for i, email in enumerate(inbox):
            if not email.has_been_read:
                print(f"{i}. {email.subject_line}")
        print("\n" + ('-' * 50))
                
    elif user_choice == 3:
        # add logic here to quit appplication
        print("Goodbye!")
        break
    
    else:
        print("Oops - incorrect input.")
