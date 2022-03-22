import os
import subprocess

#os.system('ls')
#subprocess.run(['ls','-al'])

#shell=Trueは非推奨
#subprocess.run('ls -al | grep 102', shell=True)
#r = subprocess.run('lsa -al | grep 102', shell=True)
#print(r.returncode)
#r = subprocess.run('lsa -al | grep 102', shell=True, check=True)

#openの利用
#p1 = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
#p2 = subprocess.Popen(['grep','102'], stdin=p1.stdout, stdout=subprocess.PIPE)
#p1.stdout.close()
#output = p2.communicate()[0]
#print(output)