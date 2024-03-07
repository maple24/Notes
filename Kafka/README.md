# Reference

[Apache Kafka](https://towardsdatascience.com/how-to-install-apache-kafka-using-docker-the-easy-way-4ceb00817d8b)
[topics, partitions, offsets](https://www.geeksforgeeks.org/topics-partitions-and-offsets-in-apache-kafka/)

## Terminology rundown

Kafka — Basically an event streaming platform. It enables users to collect, store, and process data to build real-time event-driven applications. It’s written in Java and Scala, but you don’t have to know these to work with Kafka. There’s also a Python API.

Kafka broker — A single Kafka Cluster is made of Brokers. They handle producers and consumers and keeps data replicated in the cluster.

Kafka topic — A category to which records are published. Imagine you had a large news site — each news category could be a single Kafka topic.

Kafka partition - different data stream in a topic.

Kafka offset - kind like ID of message in each partition.

Kafka producer — An application (a piece of code) you write to get data to Kafka.

Kafka consumer — A program you write to get data out of Kafka. Sometimes a consumer is also a producer, as it puts data elsewhere in Kafka.

Zookeeper — Used to manage a Kafka cluster, track node status, and maintain a list of topics and messages. Kafka version 2.8.0 introduced early access to a Kafka version without Zookeeper, but it’s not ready yet for production environments.

> In Kafka we have Topics and Topics represent a particular stream of data. So a Kafka Topic is going to be pretty similar to what a table is in a database without all the constraints, so if you have many tables in a database you will have many topics in Apache Kafka. You can have as many Topics as you want in Apache Kafka and the way to identify a Topic is by its name. So when you name a Topic it will need to have a unique name. Topics are split into Partitions. So when you create a Kafka Topic we will have to specify how many Partitions we want for the Kafka topics. Each partition is going to be a stream of data as well and each Partition will have the data in it being ordered and each message within a Partition will get an incremental ID which is the position of the message in the Partition and that specific ID is called an Offset.

> The group ID is very important to how different consumers "load balance" partitions. For example, if you have a topic with 10 partitions then two consumers with the same groupId will read from 5 partitions each.

> If you have two consumers with different group ids, both consumers will read from 10 partitions.

## workflow

![workflow](!assets/workflow.png)

## deploy in docker

```yml
# docker-compose
version: '3'

services:
  zookeeper:
    image: wurstmeister/zookeeper
    container_name: zookeeper
    ports:
      - "2181:2181"
  kafka:
    image: wurstmeister/kafka
    container_name: kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: localhost
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
```

## connect to kafka shell

```sh
# Just replace kafka with the value of container_name
docker exec -it kafka /bin/sh
```

## commit offset
>
> Committing an offset for a partition is the action of saying that the offset has been processed so that Kafka cluster won't send the committed records for the same partition.

> For a consumer, we can enable auto commit by setting enable.auto.commit property to true.

## example

```python
'''
bootstrp_server: Default port is 9092. If no servers are specified, will default to localhost:9092.
topic: optional list of topics to subscribe to
partition: data stream in each topic 
offset: id of message in each partition
key:
value:
group_id: The group.id is how you distinguish different consumer groups. Remember that consumers work together in groups to read data from a particular topic.
One partition of a topic can only be consumed by one consumer within the same ConsumerGroup.

If you do not set the group.id, the KafkaConsumer will generate a new, random group.id for you. As this group.id is unique you will see data is being consumed.

If you have multiple consumers running with the identical group.id, only one consumer will read the data whereas the other one stays idle not consuming anything.

auto_offset_reset: read from the very first one if set "earliest". Default "latest"
enable_auto_commit: True by default
consumer_timeout_ms: close connection when no message fetched
'''
# create a new topic
from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092", 
    client_id='test'
)

topic_list = []
topic_list.append(NewTopic(name="example_topic", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)


# ================================================
# create a new partition for a topic
from kafka import KafkaAdminClient
from kafka.admin import NewPartitions

topic = 'mytopic1'
bootstrap_servers = 'localhost:9092'

admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
topic_partitions = {}
topic_partitions[topic] = NewPartitions(total_count=4)
admin_client.create_partitions(topic_partitions)


# ================================================
# retrieve partitions of a topic
from kafka import KafkaConsumer, TopicPartition
from kafka.structs import TopicPartition

topic = 'mytopic1'
bootstrap_servers = 'localhost:9092'
consumer = KafkaConsumer(
    bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest')

partitions = consumer.partitions_for_topic(topic)
print(partitions)

first_topic_part = TopicPartition(topic, 2)
print(first_topic_part)

consumer.assign([first_topic_part])

partitions = consumer.assignment()
print(partitions)



# ================================================
# read from a specific partition
from kafka import KafkaConsumer
from kafka.structs import TopicPartition

topic = 'mytopic'
bootstrap_servers = 'localhost:9092'
consumer = KafkaConsumer(
    bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest')
# Read the specified partition
consumer.assign([TopicPartition(topic, 1)])
for msg in consumer:
    print(msg.value.decode("utf-8"))
    

# position (partition need to be assigned, do not specify topic for instance)
partition = TopicPartition(topic=topic, partition=0)
consumer.assign([partition])
for msg in consumer:
    print(consumer.position(partition))
    print(msg)

# ================================================
# commit (group_id need to specified)
for msg in consumer:
    print(msg.value.decode("utf-8"))
    consumer.commit()


# ================================================
# seek (do not set auto offset)
topic = 'mytopic'
bootstrap_servers = 'localhost:9092'
consumer = KafkaConsumer(
    topic,
    client_id='local-test',
    bootstrap_servers=bootstrap_servers,
    # auto_offset_reset='earliest'
)

consumer.partitions_for_topic(topic)
partition = TopicPartition(topic=topic, partition=1)
consumer.seek(partition=partition, offset=1)
for message in consumer:
    print(message)
    

# ================================================
# seek to beginning (works the same as `earliest` offset reset)
topic = 'mytopic'
bootstrap_servers = 'localhost:9092'
consumer = KafkaConsumer(
    topic,
    client_id='local-test',
    bootstrap_servers=bootstrap_servers,
    # auto_offset_reset='earliest'
)

consumer.partitions_for_topic(topic)
consumer.seek_to_beginning()
for message in consumer:
    print(message)


# ================================================
# assign (do not specify topic for instance)
bootstrap_servers = 'localhost:9092'
consumer = KafkaConsumer(
    client_id='local-test',
    bootstrap_servers=bootstrap_servers,
)

topic = 'mytopic'
partition = TopicPartition(topic=topic, partition=1)
consumer.assign([partition])
for message in consumer:
    print(message)
    
    
# ================================================
# poll
while True:
    print('polling...')
    records = consumer.poll(timeout_ms=1000)
    for _, consumer_records in records.items():
        # Parse records
        for consumer_record in consumer_records:
            print(str(consumer_record.value.decode('utf-8')))
        continue
    

```
