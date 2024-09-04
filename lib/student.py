class Student:
    def hello (self):
        print("Hey there! I'm so excited to learn stuff.")

      # Method to print a message when raising hand
    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    def hello(self):
        super().hello()

        # Print the additional chatty message
        print("How are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! "
              "Oh man, it was so crazy! What, you don't want any spoilers? "
              "Okay well let me just tell you who died...")
        
    # Override the raise_hand method to call the parent method 10 times
    def raise_hand(self):
        for _ in range(10):  # Loop 10 times
            super().raise_hand()  # Call the raise_hand method from the parent class

    
