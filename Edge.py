class Edge:



    def __init__(self, transferDay, value, source, target):
        self.transferDay=transferDay
        if (value!=''):
            self.value = float(value.replace(',','.'))
        else:
            self.value=0

        self.source=source
        self.target=target

    def add_node(self, node):
        self.targetNode=node