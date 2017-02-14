#!/usr/bin/python3.5
'''
import requests apt-get install python3-requests
if youre using this on windows download the MP3 from here: https://a.pomf.cat/wgdhym.mp3 save it as beep.mp3
'''
import requests, sys, time, threading, subprocess, os
os.system('cls' if os.name == 'nt' else 'clear')
print("""                 ,,,,,,
             o#'9MMHb':'-,o,
          .oH":HH$' "' ' -*R&o,
         dMMM*""'`'      .oM"HM?.
       ,MMM'          "HLbd< ?&H\\
      .:MH ."\\          ` MM  MM&b
     . "*H    -        &MMMMMMMMMH:
     .    dboo        MMMMMMMMMMMM.
     .   dMMMMMMb      *MMMMMMMMMP.
     .    MMMMMMMP        *MMMMMP .
          `#MMMMM           MM6P ,
      '    `MMMP"           HM*`,
       '    :MM             .- ,
        '.   `#?..  .       ..'
           -.   .         .-
             ''-.oo,oo.-''
VPN kill switch by @rek7""")
systime = str(time.ctime())
count = 0
useragent = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"}
url = requests.get('https://api.ipify.org/', headers=useragent)
url1 = (url.content).decode('unicode_escape')
print("[+]  [" + systime + "] | Is your masked ip: " + str(url1))
userinputip = input("Yes or no: ").lower()
try:
    if userinputip == "yes" or userinputip == "y":
        systime = str(time.ctime())
        print("[+] " + systime + "| Your current ip is: " + str(url1))
        def trying():
            while 1:
                try:
                    global count
                    count += 1
                    systime = str(time.ctime())
                    probingurl = requests.get('https://api.ipify.org/', headers=useragent)
                    probingurl1 = (probingurl.content).decode('unicode_escape')
                    if probingurl1 != url1:
                        systime = str(time.ctime())
                        print("[-] [" + systime + "] | The masked ip is: " + str(url1) + " Your current ip: " + str(probingurl1))
                        print("[-] [" + systime + "] | Turning your internet off")
                        if sys.platform == "linux" or sys.platform == "linux2":
                            subprocess.call(["ip link down eth0"], shell=True)
                            subprocess.call(["ip link down enp0s25"], shell=True)
                            subprocess.call(["ip link down wlp3s0"], shell=True)
                            subprocess.call(["ip link down wlp20s0"], shell=True)
                            subprocess.call(["ip link down tun0"], shell=True)
                            print("[-] " + systime + "| Internet turned off")
                        else:
                            while(1):
                                subprocess.call(["beep.mp3"], shell=True)
                                time.sleep(1)
                        break
                        sys.exit()
                    else:
                        systime = str(time.ctime())
                        print("[+] [" + systime + "] | Your current ip is: " + str(url1) + " retrying in 5 seconds request #"+ str(count))
                        time.sleep(5)
                        continue
                except Exception as e:
                    print("[-] [" + systime + "] | An error occured: " + str(e))
        trying()         
    elif userinputip == "no" or userinputip == "n":
        print("[-] [" + systime + "] | Check to see if your vpn was set up correctly exiting script")
        sys.exit()
    else:
        print("[-] [" + systime + "] | invalid input exiting script")
        sys.exit()
except Exception as e:
    print("[-] [" + systime + "] | An error occured: " + str(e))
