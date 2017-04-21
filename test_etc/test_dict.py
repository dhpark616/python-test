class Players(dict):
    def add(self, conn_idx, player):
        self[conn_idx] = player

    def remove(self, conn_idx):
        if conn_idx in self:
            del self[conn_idx]

PLAYERS = Players()


def main():
    player = {'char_idx': 100}
    PLAYERS.add(1, player)
    print(PLAYERS)

    print(PLAYERS[1])

    PLAYERS.remove(1)
    print(PLAYERS)


if __name__ == "__main__":
    main()
