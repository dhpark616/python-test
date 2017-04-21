class Players(dict):
    def add(self, conn_idx, player):
        self[conn_idx] = player

    def remove(self, conn_idx):
        if conn_idx in self:
            del self[conn_idx]


PLAYERS = Players()
