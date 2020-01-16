import os 
from git import Repo as GitRepo  #, GitRemote
from time import sleep

repo = GitRepo(path=os.path.dirname(os.path.realpath(__file__)))


def execute(cmd):
    o, e = sp.Popen(# o = output, e = error
        cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT
    ).communicate()
    return
    


while True:
    result = repo.remotes.origin.pull()
    if result[0].ERROR:
        print(result[0].ERROR)
    sleep(10)
