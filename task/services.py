import time

class Utils:

    def __init__(self, namespace,ip):
        self.time_ = str(self.til_next_millis(self.get_timestamp())).replace(".","")
        self.namespace = namespace
        self.ip = str(ip).replace(".","")

    def _unique_id(self):
        unique_id = "{}{}".format(self.ip,self.time_)
        return "{0}-{1}".format(self.namespace, unique_id)


    def get_timestamp(self):
        now = int((time.time()) * 1000)
        return now

    def til_next_millis(self,last):
        timestamp = self.get_timestamp()
        while timestamp <= last:
            timestamp = self.get_timestamp()
        return timestamp

