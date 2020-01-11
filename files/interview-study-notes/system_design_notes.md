---
layout: page
title: System Design Notes
permalink: /system-design-notes/
---

I present very rough system design notes.

<div id="toc"></div>

##### Back of the envelope

Memorize this:

```
- 2^5 = 32
- 2^10 = 1024 = kilo
- 2^20 ~ 10^6 = mega
- 2^30 ~ 10^9 = giga
- 2^40 ~ 10^12 = tera
- 2^50 ~ 10^15 = peta
- 2^60 ~ 10^18 = exa
- There are roughly 10^5 seconds in a day
```

##### Some Concepts

Vertical Scaling: Add more resources (i.e. more CPUs/RAM/Disk) to current server or buy a bigger one. Limits are that you hit technology or monetary constraints. 

Horizontal Scaling: Add several cheaper/smaller resources vs a few expensive/large resources.

Load Balancing: Balances the traffic amongst many servers.

Round Robin: Cycle through the servers in order. Limits: One of the servers can get overloaded.

RAID (Redundant Array of Independent Disk): Store data amongst many disks instead of just one.  
Striping: while waiting for one disk to write data, you write to another disk, RAID0.

Mirroring: when you copy the same data to multiple disks, RAID1.

Caching - to speed up processing and reduce load on database or web server.

Database Replication - for redundancy.

Database Partitioning/Sharding - for distributing data on multiple devices.

##### Tradeoffs

###### Performance vs Scalability

A performance problem is when your system is slow for a single user. A scalability problem is when your system is fast for a single user and slow when you scale to many users.

###### Latency vs Throughput

Latency is the time to perform some action or to produce some result.

Throughput is the number of such actions or results per unit of time.

Generally, you should aim for maximal throughput with acceptable latency.

###### Availability vs Consistency

We need to tradeoff availability vs consistency when dealing with distributed systems. 

- **C**onsistency - A read is guaranteed to return the most recent write for a given client.
- **A**vailability - A non-failing node will return a reasonable response within a reasonable amount of time (no error or timeout).
- **P**artition Tolerance - The system will continue to function when network partitions occur.

CAP theorem: since Partition Tolerance is always required for distributed systems (network failures always happen), we can only have one of Consistency or Availability. If we go for consistency, a client might get timeout errors if there is a network partition (we need to wait for the network split to be resolved). If we go for Availability, the response might not have the correct data when there is a network partition, but the client gets a response in a reasonable amount of time.


###### Consistency Patterns

Some patterns for CP systems:

- Weak Consistency: the data you get is consistent, but you might get network interruptions. Good for real-time streaming of video/calls
- Eventual Consistency: Your data is consistent in the long-run, think DNS, SMTP, AWS S3
- Strong Consistency: The data is always consistent, writes happen synchronously to all locations. Think RDBMs (relational database management systems).

###### Availability Patterns

Two availability patterns are fail-over and replication. Fail-over is for services, that operate either in active-passive or active-active mode. In active-passive mode, heartbeats are sent between the services, and when one goes down, the other will take over. In active-active mode, the load is shared between the two services.

##### Relational Database Management Systems

ACID -- properties of RDB transactions

- **A**tomicity: Your transactions either happen or do not happen. There is no in between state. 
- **C**onsistency: Transactions bring your DB from one valid state to another.
- **I**solation: Results of transactions executed concurrently is the same as transactions executed serially.
- **D**urability: A committed transaction is a done deal.

###### Scaling

Replication: 

- Master-slave replication: Master reads/writes, replicates writes to one or more slaves. Slaves are read only. If master goes offline, system continues to operate in read only mode, until there is a new master. Disadvantages: logic for promoting a slave to master.
- Master-Master replication: more than one master. Disadvantages: Load balancer is needed. Most master-master systems are loosely consistent (violates ACID) or have increased write latency.


Scaling:

- Federation (functional partitioning) splits up DBs by function, i.e. 2 DBs, users, products to minimize read/write traffic to each DB. Disadvantages are that the application logic becomes more complex, deciding which DB to write to.
- Sharding: Distribute data across different DBs so each DB only manages a subset of the data. Sharding is typically done based on hashing keys, so that when a new query comes in, you know which DB shard to send the query to.
- Denormalization:  Denormalization improves read performance by creating redundant copies of your data in multiple tables to avoid complex joins. Under heavy write load, denormalized tables will perform worse. Table normalization on the other hand is when we split tables to helps avoid data corruption.

First Normal Form: The table must not contain repeating groups of data (phone numbers should be in a separate table since there can be many phone numbers per person.)

Second Normal Form: No field should only be partially dependent on a candidate key in the table.

Third Normal Form: Columns should depend only upon the primary key of the table.

Indexes: Table indexes speed up lookups on columns by using hashes or B-trees, so that we can avoid full scans.

##### NoSQL

Data represented in a key-value store, document-store, wide column store, or graph database. Data is denormalized. Most NoSQL DBs favor eventual consistency and lack true ACID transactions. 

BASE: NoSQL chooses availability over consistency.

- **B**asically **A**vailable: System guarantees availability
- **S**oft state: The state of the system may change over time even without input.
- **E**ventual consitency: The system will become consistent overtime.

Key-value store: Hash map.  O(1) reads and writes. High performance. Often used for simple data or rapidly changing data. Examples: Redis, memcached.

Document store: key-value store with documents stored as value. Document has all information for a given object. Ocassionaly changing data. Examples: MongoDB, CouchDB.

Wide Column Store: Nested map. Often used for very large datasets. Examples: BigTable, HBase, Cassandra

Graph DBs: represent graph relationships.

##### Caching

Cache-aside: Cache doesn't interact with the storage directly. The client interfaces with the cache and the DB.

```
item = cache.get(key); 
if not item:
    item = db.get(key)
    cache.save(item)
return item
```

Disadvantages: after each cache miss, you have 3 calls and you have to rely on TTL for updates in cache. When a node fails, you have to refill the cache and latency increases.

Write-through: Application uses cache as the main data store, and the cache is responsible for writing to the DB. Advantage is the application does only 1 call to retrieve data.

Write-behind: Add/update entry in the cache. Asynchronously write entry to the data store improving write performance. Disadvantages: There could be data loss if cache goes down before content is written to DB.

Refresh-ahead: DB writes to cache, and it refreshes the cache for future requests.  Disadvantages: hard to time the refresh, hard to know when to invalidate the cache.

##### Asynchronism

Asynchronous workflows reduce request times for expensive operations by doing them in advance or planning for them in the future.

- Message Queues: Message queues receive, hold, and deliver messages. Workflow: Application publishes a job to the queue, notifies user of the job status. Worker picks up a job from the queue, processes it, signals that job is complete.
- Task Queues: Task queues receive tasks with data, run them, and then deliver their results. Scheduling is supported and can be used to run computationally intensive tasks in the background.

Back Pressure: When queue size becomes larger than memory, it results in cache misses, more disk reads, slow performance. Back pressure limits the queue size to maintain high throughput rate and good response times for jobs already in the queue. When queue fills up, client gets server busy error to try again later. 

Disadvantages of asynchronism: adds complexity.

##### Communication:

- HTTP (application layer protocol): An HTTP request consists of a request line (GET/POST), zero or more header lines, and empty line to separate the head from the body, and then the body.
- TCP (transport layer): Connection established through a handshake and makes sure that packets are sent in the right order and without corruption by using checksum fields, sequence numbers, and acknowledgment packets for automatic retransmission.  Used for high reliability.
- UDP (transport layer): UDP is low latency and used for real-time applications like video chat and streaming.
- RPC (Remote Procedure Call): A request for a procedure to execute on a different address space (usually a remote server). It's coded as if it were a local procedure call, but runs remotely.
- Websocket: A persistent connection between client and server. The first request is a GET with a header of "Upgrade: websocket". The server completes the websocket handshake.The connetion then uses TCP/IP and data can be sent back and forth through the connection.
