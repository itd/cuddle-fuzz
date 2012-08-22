     .__.................__......................_._.........
     / _\.___..___....../ _\.___..___._..._._.__(_) |_._..._.
     \ \./ _ \/ _ \_____\ \./ _ \/ __| |.| | .__| | __| |.| |
     _\ \  __/  __/_____|\ \  __/ (__| |_| | |..| | |_| |_| |
     \__/\___|\___|.....\__/\___|\___|\__,_|_|..|_|\__|\__, |
     ..................................................|___/.

                Created By Bar Hofesh (ba7a7chy)
                             And 
               Yuval Nativ (tisf) of See-Security
                   http://www.see-security.org
                  https://avtacha.wordpress.com


Use the -p or --port for the target port to fuzz.
Use the -t or --target for the target IP address.
Use the -r or --header to type the header to fuzz. Type & where you wish the fuzzing to occur.
Use the -s or --string for the fuzzing content.
Use the -j or --jumps for the multiplying of the string.

      ex.:  ./fuzzy.py -t localhost -p 139 -r "hello &" -s A -j 4

