import requests
import sys

banner = """
███████╗██████╗ ███████╗██████╗ ██████╗  ██████╗ ██╗  ██╗
██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝
█████╗  ██████╔╝█████╗  ██║  ██║██║  ██║██║   ██║ ╚███╔╝ 
██╔══╝  ██╔══██╗██╔══╝  ██║  ██║██║  ██║██║   ██║ ██╔██╗ 
██║     ██║  ██║███████╗██████╔╝██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
"""

def main():
    try:
        print(banner)
        if len(sys.argv) != 3:
            print("[Usage] python3 XFF.py [XFF_IP] [TARGET_URL]")
            return

        xff_ip = sys.argv[1]
        target_url = sys.argv[2]
        headers = {"X-Forwarded-For": xff_ip}

        response = requests.get(target_url, headers=headers)
        if response.status_code == 200:
            print(response.content)
        else:
            print(f"[ERROR] Status Code: {response.status_code}")
            print(response.content.decode('utf-8'))

    except IndexError:
        print("[Usage] python3 XFF.py [XFF_IP] [TARGET_URL]")

if __name__ == "__main__":
    main()
