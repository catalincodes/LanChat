@echo off

@echo on
@echo Creating container: %1
@echo off

docker run --name %1 -d -it --network ChatNet centos /bin/bash
docker network connect ChatNet %1

@echo on
@echo Running prerequisites
@echo off

docker exec -it %1 yum update
docker exec -it %1 yum -y install yum-utils
docker exec -it %1 yum -y groupinstall development

@echo on
@echo Installing python
@echo off

docker exec -it %1 yum -y install https://centos7.iuscommunity.org/ius-release.rpm
docker exec -it %1 yum -y install python36u
docker exec -it %1 yum -y install python36u-pip
docker exec -it %1 yum -y install python36u-devel

@echo on
@echo Adding chat.py to %1
@echo off
docker cp chat.py %1:/chat.py