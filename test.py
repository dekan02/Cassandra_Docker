from cassandra.cluster import Cluster, NoHostAvailable
from cassandra.query import dict_factory

TTL = 3600*24
IP_ADDRESS = [
    'localhost',
]
PORT = [9042]
KEYSPACE = 'stories'

def insert(session, records: list, cmd: str):
    for record in records:
        session.execute(
            cmd.format(keyspace=KEYSPACE, user=record[0], stories=record[1], time_to_live=TTL)
        )

def select(session, cmd:str):
    items = session.execute(
        cmd.format(keyspace=KEYSPACE)
    )

    return items

test_records = [
    ['Khang', 'test1'],
    ['Vy', 'test2'],
    ['Quan', 'test3'],
]

insert_cmd = '''INSERT INTO {keyspace}.user (
    user, stories
    ) VALUES (
    '{user}', '{stories}'
    ) USING TTL {time_to_live};'''

select_cmd = '''SELECT * FROM {keyspace}.user;'''

if __name__ == "__main__":
    for port in PORT:
        cluster = Cluster(
            IP_ADDRESS,
            port=port
        )

        try:
            # session = cluster.connect(keyspace=KEYSPACE, wait_for_all_pools=True)
            session = cluster.connect()
            session.row_factory = dict_factory # Return results as dictionary
            break
        except NoHostAvailable as e:
            print(f"Port: {port}:\n[{e}]")
            continue
    
    if session:
        rows = select(session, select_cmd)
        for row in rows:
            print(row)