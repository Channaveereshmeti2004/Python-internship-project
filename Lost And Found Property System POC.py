class LostProperty:
    def __init__(self):
        self.property_records = {}
        self.claims = {}

    def create_lost_property_record(self, property_id, description, location_found, contact_info):
        self.property_records[property_id] = {
            'description': description,
            'location_found': location_found,
            'contact_info': contact_info,
            'status': 'lost'
        }
        print(f"Lost property record {property_id} created successfully.")

    def read_lost_property_records(self):
        print("Lost Property Records:")
        for property_id, details in self.property_records.items():
            print(f"Property ID: {property_id}, Details: {details}")

    def update_lost_property_record(self, property_id, new_info):
        if property_id in self.property_records:
            old_info = self.property_records[property_id].copy()  # Copy old records
            self.property_records[property_id].update(new_info)
            print(f"Property record {property_id} updated successfully.")
            print("Old Record:", old_info)  # Print old record
        else:
            print("Property record not found.")

    def delete_lost_property_record(self, property_id):
        if property_id in self.property_records:
            del self.property_records[property_id]
            print(f"Property record {property_id} deleted successfully.")
        else:
            print("Property record not found.")

    def log_lost_property(self, property_id):
        if property_id in self.property_records:
            self.property_records[property_id]['status'] = 'found'
            print(f"Property {property_id} logged as found.")
        else:
            print("Property record not found.")

    def manage_property_claim(self, claim_id, property_id):
        if property_id in self.property_records and self.property_records[property_id]['status'] == 'found':
            self.claims[claim_id] = property_id
            self.property_records[property_id]['status'] = 'claimed'
            print(f"Claim {claim_id} successfully managed for property {property_id}.")
        else:
            print("Property not found or already claimed.")


# Function to handle user input
def handle_user_input(option, lost_property_system):
    switch = {
        '1': create_record,
        '2': read_records,
        '3': update_record,
        '4': delete_record,
        '5': log_property,
        '6': manage_claim,
        '7': exit_program
    }
    func = switch.get(option)
    if func:
        return func(lost_property_system)
    else:
        print("Invalid option. Please choose again.")


#function invocations
def create_record(lost_property_system):
    property_id = input("Enter property ID: ")
    description = input("Enter property description: ")
    location_found = input("Enter location found: ")
    contact_info = input("Enter contact information: ")
    lost_property_system.create_lost_property_record(property_id, description, location_found, contact_info)


def read_records(lost_property_system):
    lost_property_system.read_lost_property_records()


def update_record(lost_property_system):
    property_id = input("Enter property ID to update: ")
    if property_id in lost_property_system.property_records:
        print("Current details of the property:")
        print(lost_property_system.property_records[property_id])

        new_info = {}
        new_info['description'] = input("Enter new description (Press Enter to keep old value): ")
        new_info['location_found'] = input("Enter new location found (Press Enter to keep old value): ")
        new_info['contact_info'] = input("Enter new contact information (Press Enter to keep old value): ")

        # Retain old values for fields not updated
        for key, value in new_info.items():
            if not value:  # If input is empty, retain old value
                new_info[key] = lost_property_system.property_records[property_id].get(key, '')

        lost_property_system.update_lost_property_record(property_id, new_info)
    else:
        print("Property record not found.")


def delete_record(lost_property_system):
    property_id = input("Enter property ID to delete: ")
    lost_property_system.delete_lost_property_record(property_id)


def log_property(lost_property_system):
    property_id = input("Enter property ID to log as found: ")
    lost_property_system.log_lost_property(property_id)


def manage_claim(lost_property_system):
    claim_id = input("Enter claim ID: ")
    property_id = input("Enter property ID for the claim: ")
    lost_property_system.manage_property_claim(claim_id, property_id)


def exit_program(lost_property_system):
    print("Exiting program.")
    exit()


lost_property_system = LostProperty()

while True:
    print("\nLost and Found Property System:")
    print("1. Create Lost Property Record")
    print("2. Read Lost Property Records")
    print("3. Update Lost Property Record")
    print("4. Delete Lost Property Record")
    print("5. Log Lost Property as Found")
    print("6. Manage Property Claim")
    print("7. Exit")

    option = input("Enter your choice (1-7): ")
    handle_user_input(option, lost_property_system)
