class SeedNode:
    def __init__(self, high_availability: bool, high_performance: bool):
        self.high_availability = high_availability
        self.high_performance = high_performance

    def connect_callback(self):
        pass

    def disconnect_callback(self):
        pass

    # Other methods for handling messages, voting, and administration
