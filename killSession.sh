screen -list | grep -v PI_BOY,direct > output.txt && python killSession.py && rm -rf output.txt
