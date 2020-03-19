from sys import argv
import subprocess

script = argv
print ("script: ", script)
name = str(script[0])
print ("name: ", name)
direc = "direct"
#subprocess.call(["dir"], shell=True)
#subprocess.call(["md", direc], shell = True)
#subprocess.call(["copy", name, direc], shell = True)
subprocess.call(["mkdir",direc])#, shell = True)
subprocess.call(["cp", name, direc])#, shell = True)