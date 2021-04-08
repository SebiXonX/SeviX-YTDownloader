import subprocess

def Search():
    subprocess.call('cd bin', shell=True)
    ver = "git clone "
    subprocess.call(ver, shell=True)
    import Config
    if Config.Version == Config.NewVersion:
        print("Not update a")