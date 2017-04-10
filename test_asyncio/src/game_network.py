import asyncio
from socket import TCP_NODELAY, IPPROTO_TCP

from .util import time_util


class ConnID:
    __conn_id = 0

    @staticmethod
    def get_next_id():
        ConnID.__conn_id += 1
        return ConnID.__conn_id


class Conns:
    __conns = dict()

    @staticmethod
    def add_conn(conn_id, conn):
        Conns.__conns[conn_id] = conn

    @staticmethod
    def del_conn(conn_id):
        if conn_id in Conns.__conns:
            del Conns.__conns[conn_id]

    @staticmethod
    def send(conn_id, msg):
        if conn_id in Conns.__conns:
            try:
                Conns.__conns[conn_id].transport.write(msg)
            except Exception as err:
                print('{}, send exception, {}, {}'.format(time_util.local_str(), conn_id, err))

    @staticmethod
    def send_all(msg):
        for k, v in Conns.__conns.items():
            try:
                v.transport.write(msg)
            except Exception as err:
                print('{}, send_all exception, {}, {}'.format(time_util.local_str(), k, err))


class TCPServerConnection(asyncio.Protocol):
    def __init__(self):
        self.conn_id = 0
        self.transport = None
        self.msg_buffer = b''

    def connection_made(self, transport):
        self.conn_id = ConnID.get_next_id()
        self.transport = transport
        sock = self.transport.get_extra_info('socket')
        sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)

        Conns.add_conn(self.conn_id, self)
        print('{}, connection_made, {}'.format(time_util.local_str(), self.conn_id))

    def data_received(self, data):
        print('{}, data_received, {}, {}'.format(time_util.local_str(), self.conn_id, data.decode()))
        self.transport.write(data)

    def connection_lost(self, exc):
        Conns.del_conn(self.conn_id)
        print('{}, connection_lost, {}, {}'.format(time_util.local_str(), self.conn_id, exc if exc else 'None'))


class TCPClientConnection(asyncio.Protocol):
    def __init__(self, user_id):
        self.user_id = user_id
        self.transport = None
        self.msg_buffer = b''

    def connection_made(self, transport):
        self.transport = transport
        sock = self.transport.get_extra_info('socket')
        sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
        Conns.add_conn(self.user_id, self)
        print('{}, connection_made, {}'.format(time_util.local_str(), self.user_id))

    def data_received(self, data):
        print('{}, data_received, {}, {}'.format(time_util.local_str(), self.user_id, data.decode()))

    def connection_lost(self, exc):
        Conns.del_conn(self.user_id)
        print('{}, connection_lost, {}, {}'.format(time_util.local_str(), self.user_id, exc if exc else 'None'))


def send_hello():
    msg = 'hello'.encode()
    Conns.send_all(msg)
