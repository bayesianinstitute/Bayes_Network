from datetime import datetime

class Vote:
    def __init__(self, voter, candidate):
        self.voter = voter
        self.candidate = candidate
        self.timestamp = datetime.now()

    def select_master_node(self):
        pass

    def get_voter(self):
        return self.voter

    def get_candidate(self):
        return self.candidate

    def get_timestamp(self):
        return self.timestamp

    def publish_administrator(self):
        pass

    def publish_backup_administrator(self):
        pass
