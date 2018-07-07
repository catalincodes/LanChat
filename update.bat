@echo off

@echo on
@echo Removing chat.py from ChatBot1
@echo off
docker exec -it ChatBot1 rm -rf chat.py

@echo on
@echo Removing chat.py from ChatBot2
@echo off
docker exec -it ChatBot2 rm -rf chat.py

@echo on
@echo Removing chat.py from ChatBot3
@echo off
docker exec -it ChatBot3 rm -rf chat.py

@echo on
@echo Adding chat.py to ChatBot1
@echo off
docker cp chat.py ChatBot1:/chat.py

@echo on
@echo Adding chat.py to ChatBot2
@echo off
docker cp chat.py ChatBot2:/chat.py

@echo on
@echo Adding chat.py to ChatBot3
@echo off
docker cp chat.py ChatBot3:/chat.py