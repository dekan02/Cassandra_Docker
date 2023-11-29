CREATE KEYSPACE IF NOT EXISTS stories
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE IF NOT EXISTS stories.user (
    user TEXT,
    stories TEXT,
    PRIMARY KEY ((user, stories))
) WITH comment = 'Table with user and stories';

CREATE TABLE IF NOT EXISTS stories.stories (
    user TEXT,
    stories TEXT,
    media_type TEXT,
    owner TEXT,
    duration BLOB,
    url TEXT,
    expired_date DATE,
    PRIMARY KEY ((user, stories), expired_date)
) WITH CLUSTERING ORDER BY (expired_date DESC)
    AND comment = 'Stories ordered closest to deletion';