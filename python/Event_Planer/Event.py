class EventPlanner:
    def __init__(self, event_name):
        self.event_name = event_name
        self.ticket_price = 0
        self.guest_list = []
    
    def set_ticket_price(self):
        """Set the ticket price for the event"""
        while True:
            try:
                self.ticket_price = float(input(f"Enter the ticket price for the event '{self.event_name}': $"))
                if self.ticket_price <= 0:
                    print("Ticket price must be a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the ticket price.")
    
    def add_guest(self):
        """Add a guest to the guest list"""
        guest_name = input("Enter the name of the guest to add: ").strip()
        if guest_name:
            self.guest_list.append(guest_name)
            print(f"{guest_name} has been added to the guest list.")
        else:
            print("Guest name cannot be empty.")
    
    def display_guests(self):
        """Display the list of guests"""
        if self.guest_list:
            print("\nGuest List:")
            for idx, guest in enumerate(self.guest_list, 1):
                print(f"{idx}. {guest}")
        else:
            print("No guests added yet.")
    
    def show_event_details(self):
        """Show the event details like name, ticket price, and guest list"""
        print(f"\nEvent: {self.event_name}")
        print(f"Ticket Price: ${self.ticket_price}")
        self.display_guests()


def main():
    print("Welcome to the Event Planner!")
    event_name = input("Enter the name of the event: ").strip()
    event = EventPlanner(event_name)

    event.set_ticket_price()

    while True:
        print("\nOptions:")
        print("1. Add Guest")
        print("2. Show Event Details")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            event.add_guest()
        elif choice == "2":
            event.show_event_details()
        elif choice == "3":
            print("Thank you for using the Event Planner!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
