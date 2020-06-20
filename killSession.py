import subprocess

def killSession(screenId):
    cmd = 'screen -X -S %s quit' % screenId
    subprocess.check_output(cmd, shell=True)

def loopThroughSession():
    f = open('output.txt', 'r')
    
    for x in f:
        try:
            screen_id = int(x.split('.')[0])
            killSession(screen_id)
        except Exception as e:
            pass
    
    f.close()



if __name__ == "__main__":
    loopThroughSession()
