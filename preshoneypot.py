#!/usr/bin/python
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                    ..__...__.........._____.
#                    _/  |_|__|._______/  ___\
#                    \   __\  |/  ___/\   __\.
#                    .|  |.|  |\___ \..|  |...
#                    .|__|.|__/____  >.|__|...
#                    ..............\/.........
#
#                   NetCat Presistent Honey Pot
#
#     This file will create a honeypot and establish it every
#        time it goes down. It will save log file for the
#             connection to capture.txt and will add 
#                    banner from 'welcome.txt'
#
#       Build by Yuval (tisf) Nativ from See-Security Group
#                  http://www.see-security.com
#                 https://avtacha.wordpress.com
#
#     .__.................__......................_._.........
#     / _\.___..___....../ _\.___..___._..._._.__(_) |_._..._.
#     \ \./ _ \/ _ \_____\ \./ _ \/ __| |.| | '__| | __| |.| |
#     _\ \  __/  __/_____|\ \  __/ (__| |_| | |..| | |_| |_| |
#     \__/\___|\___|.....\__/\___|\___|\__,_|_|..|_|\__|\__, |
#     ..................................................|___/.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
import sys
import getopt
import os
 
def printhelp():
   print ''
   print '                    ..__...__.........._____.'
   print '                    _/  |_|__|._______/  ___\ '
   print '                    \   __\  |/  ___/\   __\.'
   print '                    .|  |.|  |\___ \..|  |...'
   print '                    .|__|.|__/____  >.|__|...'
   print '                    ..............\/.........'
   print ''
   print '          Created By Yuval Nativ (tisf) of See-Security'
   print '                   http://www.see-security.org'
   print '                  https://avtacha.wordpress.com'
   print ''
   print 'Syntax not used properly.'
   print 'Use the -p or --port for the target port.'
   print 'If you use port which is larger than 1024 run as root.'
   print 'The banner for the honey pot is at welcome.txt .'
   print 'The log will be saved to capture.txt .'
   print ''
   print '      ex.:  ./preshoneypot.py -p 44254'
   print ''
 
def main(argv):
   portAsked = ''
   rootBar = 1024
 
   try:
      opts, args = getopt.getopt(argv,"hp:h",["port=","help="])
   except getopt.GetoptError:
      printhelp()
      sys.exit(2)
   for opt, arg in opts:
      if opt == ('-h', '--help'):
         printhelp()
         sys.exit()
      elif opt in ('-p', '--port'):
         portAsked = arg
   if portAsked=='':
      printhelp()
      sys.exit()
 
   if int(portAsked) > int(65535):
      sys.exit('Port cannot be bigger then 65535...')
   if int(portAsked) < int(rootBar):
      if not os.geteuid() == 0:
         sys.exit('For using this script under port 1024 please run as root.')
 
   i=0  
   i=str("while [ 1 ]; do echo 'Got a connection'; nc -lvvv "+portAsked+" < honeywelcome.txt >> capture.txt; done")
   os.system(i)
 
if __name__ == "__main__":
   main(sys.argv[1:])
