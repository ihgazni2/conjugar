
import sys
import os
import subprocess
import shlex

def pipe_shell_cmds(shell_CMDs):
    '''
        shell_CMDs = {}
        shell_CMDs[1] = 'netstat -n'
        shell_CMDs[2] = "awk {'print $6'}"
    '''
    len = shell_CMDs.__len__()
    p = {}
    p[1] = subprocess.Popen(shlex.split(shell_CMDs[1]), stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    for i in range(2,len):
        p[i] = subprocess.Popen(shlex.split(shell_CMDs[i]), stdin=p[i-1].stdout, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if(len > 1):
        p[len] = subprocess.Popen(shlex.split(shell_CMDs[len]), stdin=p[len-1].stdout, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    result = p[len].communicate()
    if(len > 1):
        for i in range(2,len+1):
            returncode = p[i].wait()
    else:
        returncode = p[len].wait()
    return(result)

#dname="./Main" dname="./edict"
def check(fname,dname="./conjugar"):
    fl = []
    shell_CMDs = {}
    shell_CMDs[1] = 'tree -f ' + dname
    shell_CMDs[2] = 'egrep "py|sh"'
    shell_CMDs[3] = 'egrep ""'
    rslt = pipe_shell_cmds(shell_CMDs)[0].decode('utf-8')
    fl = rslt.replace(chr(9500),"").replace(chr(9472),"").replace(chr(9474),"").replace("\xa0","").replace(chr(9492),"").split("\n")
    for i in range(0,fl.__len__() -1):
        ele = fl[i].strip(' ').strip('\t').strip(' ').strip('\t')
        fl[i] = 'cat ' + ele 
    fl.pop(fl.__len__() -1)
    for cmd in fl:
        shell_CMDs = {}
        shell_CMDs[1] = cmd
        shell_CMDs[2] = "egrep " + '"' + fname + '"'
        rslt = pipe_shell_cmds(shell_CMDs)
        if(rslt == (b'', b'')):
            pass
        else:
            print("---location---")
            print(cmd)
            print("---rslt----")
            print(rslt[0].decode('utf-8'))
            print("----info---")
            print(rslt[1].decode('utf-8'))

try:
    check(sys.argv[1],sys.argv[2])
except:
    check(sys.argv[1])
else:
    pass
