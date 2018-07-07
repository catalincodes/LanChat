@echo off

@echo on
@echo Executing "python3.6 chat.py on container %1"
@echo off

docker exec -it %1 python3.6 chat.py