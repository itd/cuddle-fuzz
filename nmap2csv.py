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
#                A script to take nmap scan results
#              and output it to a convinient CSV file
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
   print 'Use the -t for the IP address or IP range to scan.'
   print 'Use the -o option for the file name to save in.'
   print ''
   print '      ex.:  ./nmap2csv.py -t 192.168.1.1 -o me.csv'
   print ''
 
def main(argv):
   targets = ''
   fileoutput = ''
   try:
      opts, args = getopt.getopt(argv,"ht:o:h",["target=","filename=","help="])
   except getopt.GetoptError:
      printhelp()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         printhelp()
         sys.exit()
      elif opt in ("-t", "--target"):
         targets = arg
      elif opt in ("-h", "--help"):
         help = arg
      elif opt in ("-o", "--file"):
         fileoutput = arg
   if fileoutput=='':
      printhelp()
      sys.exit()
   if targets=='':
      printhelp()
      sys.exit()
   i=0  
   i=str("nmap "+targets+" -A -p 1-1000 | egrep -i 'open|state' | sed 's/  */,/;s/  */,/' >"+fileoutput)
   os.system(i)
 
if __name__ == "__main__":
   main(sys.argv[1:])
