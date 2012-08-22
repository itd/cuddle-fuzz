#!/usr/bin/python
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#     .__.................__......................_._.........
#     / _\.___..___....../ _\.___..___._..._._.__(_) |_._..._.
#     \ \./ _ \/ _ \_____\ \./ _ \/ __| |.| | '__| | __| |.| |
#     _\ \  __/  __/_____|\ \  __/ (__| |_| | |..| | |_| |_| |
#     \__/\___|\___|.....\__/\___|\___|\__,_|_|..|_|\__|\__, |
#     ..................................................|___/.
#
#                       Simple Port Fuzzer
#
#     This script will create threading connections to a host
#   at a port given with a specific header to test and which 
#    strings can be used. It is a simple fuzzer for you to
#     use for your research. 
#           
#
#                 Created By Bar Hofesh (ba7a7chy)
#                                and
#              Yuval (tisf) Nativ from See-Security
#                     yuval@see-security.com
#                  http://www.see-security.com
#                 https://avtacha.wordpress.com
#
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
import sys
import getopt
import os
import socket
from time import sleep
import threading
 
def printhelp():
   print ''
   print '     .__.................__......................_._.........'
   print '     / _\.___..___....../ _\.___..___._..._._.__(_) |_._..._.'
   print '     \ \./ _ \/ _ \_____\ \./ _ \/ __| |.| | .__| | __| |.| |'
   print '     _\ \  __/  __/_____|\ \  __/ (__| |_| | |..| | |_| |_| |'
   print '     \__/\___|\___|.....\__/\___|\___|\__,_|_|..|_|\__|\__, |'
   print '     ..................................................|___/.'
   print ''
   print '                Created By Bar Hofesh (ba7a7chy)'
   print '                             And '
   print '               Yuval Nativ (tisf) of See-Security'
   print '                   http://www.see-security.org'
   print '                  https://avtacha.wordpress.com'
   print ''
   print 'Syntax not used properly.'
   print ''
   print 'Use the -p or --port for the target port to fuzz.'
   print 'Use the -t or --target for the target IP address.'
   print 'Use the -r or --header to type the header to fuzz. Type & where you wish the fuzzing to occur.'
   print 'Use the -s or --string for the fuzzing content.'
   print 'Use the -j or --jumps for the multiplying of the string.'
   print ''
   print '      ex.:  ./fuzzy.py -t localhost -p 139 -r "hello &" -s A -j 4'
   print ''
 
def main(argv):
   TargetPort = ''
   TargetIP = ''
   StringFuzz = ''
   TarHeader = ''
   TarJumps = ''
 
   try:
      opts, args = getopt.getopt(argv,"hp:t:r:s:j:h",["port=","help=","target=","header=","string=","jumps="])
   except getopt.GetoptError:
      printhelp()
      sys.exit(2)
   for opt, arg in opts:
      if opt == ('-h', '--help'):
         printhelp()
         sys.exit()
      elif opt in ('-p', '--port'):
         TargetPort = arg
      elif opt in ('-t', '--target'):
         TargetIP = arg
      elif opt in ('-r', '--header'):
         TarHeader = arg
      elif opt in ('-s', '--string'):
         StringFuzz = arg
      elif opt in ('-j', '--jumps'):
         TarJumps = arg
   if TargetPort=='':
      printhelp()
      sys.exit()
   if TargetIP=='':
      printhelp()
      sys.exit()
   if TarHeader=='':
      printhelp()
      sys.exit()
   if StringFuzz=='':
      printhelp()
      sys.exit()
   if TarJumps=='':
      printhelp()
      sys.exit()
    
   a=1
   host = TargetIP,int(TargetPort)
   char = StringFuzz * int(TarJumps)
   while a > 0:
        s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host))
        TarHeader = TarHeader.replace("&", StringFuzz)
        s.send(TarHeader)
        s.settimeout(7)
        data = s.recv(4)
        if data > 0:
                print "Got awnser"
        else:
                print "No awnser"       
        sleep(0.1) 
        print "Fuzzing With:", TarHeader
        TarHeader = TarHeader.replace (StringFuzz, "&")
        StringFuzz = char + StringFuzz 
        s.close()
 
if __name__ == "__main__":
   main(sys.argv[1:])
