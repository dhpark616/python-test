import logging


class ConnIDX:
    def __init__(self):
        self._conn_idx = 0

    def get_next_idx(self):
        self._conn_idx += 1
        return self._conn_idx


class Conns(dict):
    def add(self, conn_idx, conn):
        self[conn_idx] = conn

    def remove(self, conn_idx):
        if conn_idx in self:
            del self[conn_idx]

    def send(self, conn_idx, msg):
        if conn_idx in self:
            try:
                self[conn_idx].transport.write(msg)
            except Exception as e:
                extra = {'conn_idx': conn_idx}
                logging.exception(repr(e), extra=extra)

    def send_all(self, msg, except_conn_idx=0):
        for k, v in self.items():
            if except_conn_idx != 0 and except_conn_idx == k:
                continue
            try:
                v.transport.write(msg)
            except Exception as e:
                extra = {'conn_idx': k}
                logging.exception(repr(e), extra=extra)


CONNS = Conns()
CONN_IDX = ConnIDX()
