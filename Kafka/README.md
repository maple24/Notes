## Reference
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
> Committing an offset for a partition is the action of saying that the offset has been processed so that Kafka cluster won't send the committed records for the same partition.

> For a consumer, we can enable auto commit by setting enable.auto.commit property to true.