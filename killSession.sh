screen -list | grep -v PI_BOY | grep -v direct > output.txt && python killSession.py && rm -rf output.txt
