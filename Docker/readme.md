# Table of contents

- [Table of contents](#table-of-contents)
  - [Docker cheatsheet](#docker-cheatsheet)
    - [Docker images](#docker-images)
    - [Dockerfiles](#dockerfiles)
      - [Dockerfile reference](#dockerfile-reference)
    - [Docker compose](#docker-compose)
      - [Basic structure of a Docker Compose YAML file](#basic-structure-of-a-docker-compose-yaml-file)
    - [Build](#build)
    - [Share](#share)
    - [Note](#note)
    - [volumes](#volumes)
    - [use existing mysql container](#use-existing-mysql-container)
    - [how to share a mysql docker container](#how-to-share-a-mysql-docker-container)
    - [most frequently used commands](#most-frequently-used-commands)

## Docker cheatsheet

<https://groupe-sii.github.io/cheat-sheets/docker/index.html>

### Docker images

`stretch/buster/jessie`

> Images tagged with stretch, buster, or jessie are codenames for _different Debian releases_.

`-alpine`

> This image is the most highly recommended if space is a concern.

> Alpine images are based on the _Alpine Linux Project_, which is an operating system that was built specifically for use inside of containers.

> The main reason to use an Alpine image is to make your resulting image as small as possible.

`-slim`

> This image generally only installs the minimal packages needed to run your particular tool.

### Dockerfiles

> Dockerfiles are how we containerize our application, or how we build a new container from an already pre-built image and add custom logic to start our application. From a Dockerfile, we use the Docker build command to create an image.

> Think of a Dockerfile as a text document that contains the commands we call on the command line to build an image.

#### Dockerfile reference

### Docker compose

> Docker Compose is a Docker tool used to define and run multi-container applications. With Compose, you use a YAML file to configure your application’s services and create all the app’s services from that configuration.

#### Basic structure of a Docker Compose YAML file

```yaml
version: '3' # version of docker compose, will provide appropriate features
services:
  web:
    # Path to dockerfile.
    # '.' represents the current directory in which
    # docker-compose.yml is present.
    build: .

    # Mapping of container port to host, (host:container)

    ports:
      - "5000:5000"
    # Mount volume
    volumes:
      - "/usercode/:/code"

    # Link database container to app container
    # for reachability.
    links:
      - "database:backenddb"

  database:

    # image to fetch from docker hub
    image: mysql/mysql-server:5.7

    # Environment variables for startup script
    # container will use these variables
    # to start the container with these define variables.
    environment:
      - "MYSQL_ROOT_PASSWORD=root"
      - "MYSQL_USER=testuser"
      - "MYSQL_PASSWORD=admin123"
      - "MYSQL_DATABASE=backend"
    # Mount init.sql file to automatically run
    # and create tables for us.
    # everything in docker-entrypoint-initdb.d folder
    # is executed as soon as container is up nd running.
    volumes:
      - "/usercode/db/init.sql:/docker-entrypoint-initdb.d/init.sql"
    depends_on:
      - redis
```

> `version '3': This denotes that we are using version 3 of Docker Compose, and Docker will provide the appropriate features. At the time of writing this article, version 3.7 is latest version of Compose.`

> `services: This section defines all the different containers we will create. In our example, we have two services, web and database.`

> `web: This is the name of our Flask app service. Docker Compose will create containers with the name we provide.`

> `build: This specifies the location of our Dockerfile, and . represents the directory where the docker-compose.yml file is located.`

> `ports: This is used to map the container’s ports to the host machine.`

> `volumes: This is just like the -v option for mounting disks in Docker. In this example, we attach our code files directory to the containers’ ./code directory. This way, we won’t have to rebuild the images if changes are made.`

> `command: command overrides the default command declared by the container image (i.e. by Dockerfile’s CMD).`

> `links: This will link one service to another. For the bridge network, we must specify which container should be accessible to which container using links.`

> `image: If we don’t have a Dockerfile and want to run a service using a pre-built image, we specify the image location using the image clause. Compose will fork a container from that image.`

> `environment: The clause allows us to set up an environment variable in the container. This is the same as the -e argument in Docker when running a container.`

> `depends_on: We kept this service dependent on redis so that untill redis won’t start, backend service will not start.`

### Build

Build an image from the Dockerfile in the current directory and tag the image

```sh
docker build -t myimage:1.0 .
```

List all images that are locally stored with the Docker Engine

```sh
docker image ls
```

Delete an image from the local image store

```sh
docker image rm alpine:3.4
```

build with proxy

```sh
docker build --build-arg HTTP_PROXY=http://host.docker.internal:3128 --build-arg HTTPS_PROXY=http://host.docker.internal:3128 --build-arg http_proxy=http://host.docker.internal:3128 --build-arg https_proxy=http://host.docker.internal:3128 --tag name .

docker-compose build --build-arg HTTP_PROXY=http://host.docker.internal:3128 --build-arg HTTPS_PROXY=http://host.docker.internal:3128 --build-arg http_proxy=http://host.docker.internal:3128 --build-arg https_proxy=http://host.docker.internal:3128
```

### Share

[Deploy to another registry](https://sylhare.github.io/2019/08/05/Docker-private-registry.html)

```sh
# prepare docker image, tag the image
# docker tag [OPTIONS] IMAGE[:TAG] [REGISTRYHOST/][USERNAME/]NAME[:TAG]
docker tag python3-pytest artifactory.private.registry.ca:5000/python/python3-pytest:1
# login
docker login artifactory.private.registry.ca:5000
# upload to private registry, push using that same tag
docker push artifactory.private.registry.ca:5000/python/python3-pytest:1
```

Pull an image from a registry

```sh
docker pull myimage:1.0
```

Retag a local image with a new image name and tag

```sh
docker tag myimage:1.0 myrepo/myimage:2.0
```

Push an image to a registry

```sh
docker push myrepo/myimage:2.0
```

Run a container from the Alpine version 3.9 image, name the running container "web" and expose port 5000 externally, mapped to port 80 inside the container.

```sh
docker container run --name web -p 5000:80 alpine:3.9
```

Stop a running container through SIGTERM

```sh
docker container stop web
```

Stop a running container through SIGKILL

```sh
docker container kill web
```

List the networks

```sh
docker network ls
```

List the running containers (add --all to include stopped containers)

```sh
docker container ls
```

Delete all running and stopped containers

```sh
docker container rm -f $(docker ps -aq)
```

Print the last 100 lines of a container’s logs

```sh
docker container logs --tail 100 web
```

### Note

```sh
docker run -it --rm python:rc
```

`-it: running container interactive`

`--rm: remove container after use`

`rc: shorthand tag for release candiate and points to the latest development version`

```sh
docker-compose -f docker-compose.yml up -d
```

### volumes

The reason for specifying volumes and networks twice is to define them globally at the top level and make them available for reuse by multiple services.

By defining volumes and networks globally, you can reuse them across multiple services. `This can be particularly useful in more complex setups where multiple services need to share the same volume or be connected to the same network.` It promotes modularity and simplifies the management of volumes and networks within the Compose file.

volumes: The volumes section at the top level defines a named volume called db-data. This named volume can be used by any service within the Compose file. In this specific case, the mysql service uses the db-data volume to persist its MySQL database data.

networks: The networks section at the top level defines a network called overlay. Similar to volumes, this network can be utilized by multiple services within the Compose file. `Both the wordpress and mysql services are connected to the overlay network, allowing them to communicate with each other.`

```yml
version: "3.8"

services:
  wordpress:
    image: wordpress
    ports:
      - "8080:80"
    networks:
      - overlay
    deploy:
      mode: replicated
      replicas: 2
      endpoint_mode: vip

  mysql:
    image: mysql
    volumes:
       - db-data:/var/lib/mysql/data
    networks:
       - overlay
    deploy:
      mode: replicated
      replicas: 2
      endpoint_mode: dnsrr

volumes:
  db-data:

networks:
  overlay:
```

### use existing mysql container

```yml
version: '3'

services:
  db:
    image: mysql:8
    restart: always
    container_name: db
    ports:
      - "3306:3306"
    environment:
      MYSQL_DATABASE: 'viteadmin'
      MYSQL_USER: 'ets1szh'
      MYSQL_PASSWORD: 'estbangbangde6'
      MYSQL_ROOT_PASSWORD: 'root'
      MYSQL_ROOT_HOST: '%'
    volumes:
      - db_volume:/var/lib/mysql

volumes:
  db_volume:
    external: true
    name: mysql_volume
```

### how to share a mysql docker container

```sh
docker network create mysql_network
```

### most frequently used commands

```sh
docker ps
docker volume ls
docker volume inspect <volume name>
docker container ls
docker image ls
docker image rm <image name>:<tag>
docker image prune
docker compose build --no-cache
docker compose -f docker-compose.yml pull
docker compose -f docker-compose.yml up -d
docker compose -f docker-compose.yml down
docker exec -it <container name> bash
docker logs <container name>
```
