import subprocess
import requests


def start_shell():
    print("start shell...\n")
    subprocess.run('./SecScan.sh')



def read_result():
    with open("result.txt",'r') as r_txt:
        s = r_txt.read()
        #print(s)
        #check connect to vpn
        target = "- If"
        find_str = s.find(target)
        res = s[:find_str]
        print(res)

        #Check GlobalIP over VPN
        Get_IP = requests.get("http://inet-ip.info/ip")
        print("GlobalIP over VPN:  " + Get_IP.text + "\n")

        #knhunter slice
        kh_target = 'System checks summary'
        kh_result = s.find(kh_target)
        kh_r = s[kh_result:]
        print(kh_r)
        subprocess.run(['rm','result.txt'])
        r_txt.close()

if __name__ == "__main__":
    start_shell()
    read_result()
