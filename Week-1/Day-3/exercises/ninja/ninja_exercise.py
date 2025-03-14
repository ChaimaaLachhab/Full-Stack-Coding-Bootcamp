class Phone:
    def __init__(self, phone_number):
        """Initialize the phone with a phone number, an empty call history, and an empty message list."""
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        """Log a call made from this phone to another phone."""
        call_log = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_log)
        self.call_history.append(call_log)

    def show_call_history(self):
        """Display the call history."""
        if not self.call_history:
            print("No call history.")
        else:
            print("Call History:")
            for call in self.call_history:
                print(call)

    def send_message(self, other_phone, content):
        """Send a message to another phone and store it in the messages list."""
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)  # Also add the message to the receiver's messages
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: {content}")

    def show_outgoing_messages(self):
        """Show all messages sent by this phone."""
        print(f"Outgoing Messages from {self.phone_number}:")
        outgoing = [msg for msg in self.messages if msg["from"] == self.phone_number]
        if not outgoing:
            print("No outgoing messages.")
        else:
            for msg in outgoing:
                print(f"To {msg['to']}: {msg['content']}")

    def show_incoming_messages(self):
        """Show all messages received by this phone."""
        print(f"Incoming Messages for {self.phone_number}:")
        incoming = [msg for msg in self.messages if msg["to"] == self.phone_number]
        if not incoming:
            print("No incoming messages.")
        else:
            for msg in incoming:
                print(f"From {msg['from']}: {msg['content']}")

    def show_messages_from(self, other_phone):
        """Show all messages received from a specific number."""
        print(f"Messages from {other_phone.phone_number} to {self.phone_number}:")
        specific_messages = [
            msg for msg in self.messages
            if msg["from"] == other_phone.phone_number and msg["to"] == self.phone_number
        ]
        if not specific_messages:
            print("No messages from this number.")
        else:
            for msg in specific_messages:
                print(f"{msg['content']}")

# ---- Testing the Phone class ----
phone1 = Phone("06-0000-0000")
phone2 = Phone("06-1111-1111")

# Making calls
phone1.call(phone2)
phone2.call(phone1)

# Viewing call history
phone1.show_call_history()
phone2.show_call_history()

# Sending messages
phone1.send_message(phone2, "Hey, how are you?")
phone2.send_message(phone1, "I'm good, thanks!")

# Viewing messages
phone1.show_outgoing_messages()
phone1.show_incoming_messages()

phone2.show_outgoing_messages()
phone2.show_incoming_messages()

# Viewing messages from a specific number
phone1.show_messages_from(phone2)
phone2.show_messages_from(phone1)
