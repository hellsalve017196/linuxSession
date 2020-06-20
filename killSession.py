import subprocess

def killSession(screenId):
    cmd = 'screen -X -S %s quit' % screenId
    subprocess.check_output(cmd, shell=True)

def loopThroughSession():
    try:
        f = open('output.txt', 'r')
        for x in f:
            if x != '':
                screen_id = int(x.split('.')[0])
                killSession(screen_id)
        f.close()
    except Exception as e:
        pass



if __name__ == "__main__":
    loopThroughSession()
