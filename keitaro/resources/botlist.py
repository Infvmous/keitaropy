from keitaro.api import API
from keitaro.utils import list_to_string


class BotList(API):

    def __init__(self, client, endpoint='botlist'):
        super(BotList, self).__init__(client, endpoint)

    def get(self):
        """
        Retrieves rows from the Bot List
        """
        return super(BotList, self).get()

    def add(self, ip_list):
        """
        Adds IPs to the Bot List
        """
        return super(BotList, self).post('add', value=list_to_string(ip_list))

    def exclude(self, ip_list):
        """
        Removes IPs from the Bot List
        """
        return super(BotList, self).post(
            'exclude', value=list_to_string(ip_list))

    def update(self, ip_list):
        """
        Replaces all botlist IPs with new ip_list
        """
        return super(BotList, self).put(value=list_to_string(ip_list))
