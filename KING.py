import os, sys, platform,time
try:
    import requests
except:
    os.system('pip install requests')

bit = platform.architecture()[0]
if bit == '64bit':
    import data64
elif bit == '32bit':
    import data32
