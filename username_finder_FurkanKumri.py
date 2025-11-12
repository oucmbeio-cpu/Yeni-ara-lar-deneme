import webbrowser
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from rich import box
import time
import os
import csv

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
 webbrowser.open("https://t.me/+UJvw_IjASME3NDI0")

def banner():
    clear()
    
    ascii_logo = """[bold magenta]
███████╗██╗   ██╗██████╗ ██╗  ██╗░█████╗░███╗   ██╗
██╔════╝██║   ██║██╔══██╗██║ ██╔╝██╔══██╗████╗  ██║
█████╗  ██║   ██║██████╔╝█████╔╝ ███████║██╔██╗ ██║
██╔══╝  ██║   ██║██╔══██╗██╔═██╗ ██╔══██║██║╚██╗██║
██║     ╚██████╔╝██║  ██║██║  ██╗██║  ██║██║ ╚████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                 [bold cyan]F U R K A N[/bold cyan]
[/bold magenta]
"""
    console.print(ascii_logo)
    info = Panel.fit(
        """
[bold cyan]🔮 Furkan OSINT — Gelişmiş Kullanıcı Adı Tarayıcı[/]

[bold]Geliştirici:[/] [green]@furkankumrit[/]
[italic yellow]56 popüler platformda kullanıcı adı doğrulaması yapar.[/]
""",
        title="🚀 Hoş Geldin, Furkan!",
        border_style="magenta",
    )
    console.print(info)
    time.sleep(0.8)

def build_sites(username):
    
    s = {
       
        "Facebook": f"https://www.facebook.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "X (Twitter)": f"https://x.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}/",
        "LinkedIn": f"https://www.linkedin.com/in/{username}/",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Tumblr": f"https://{username}.tumblr.com",
        "Medium": f"https://medium.com/@{username}",
        "WordPress": f"https://{username}.wordpress.com",
        "Blogger": f"https://{username}.blogspot.com",
        "Substack": f"https://{username}.substack.com",
        "Quora": f"https://www.quora.com/profile/{username}",

        
        "Telegram": f"https://t.me/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Discord": f"https://discord.com/users/{username}",  
        "Skype": f"https://www.skype.com/en/people/{username}",

        
        "Twitch": f"https://www.twitch.tv/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Xbox (3rd party)": f"https://xboxgamertag.com/search/{username}",
        "PSNProfiles": f"https://psnprofiles.com/{username}",
        "Battle.net (Blizzard)": f"https://playoverwatch.com/tr-tr/career/{username}",  
        "EpicGames": f"https://www.epicgames.com/id/{username}",

        
        "GitHub": f"https://github.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Bitbucket": f"https://bitbucket.org/{username}",
        "SourceForge": f"https://sourceforge.net/u/{username}/",
        "Gitea": f"https://try.gitea.io/{username}",
        "Codeberg": f"https://codeberg.org/{username}",
        "StackOverflow": f"https://stackoverflow.com/users/{username}",
        "Dev.to": f"https://dev.to/{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",

        
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "Bandcamp": f"https://{username}.bandcamp.com",
        "Mixcloud": f"https://www.mixcloud.com/{username}",
        "Last.fm": f"https://www.last.fm/user/{username}",
        "Audiomack": f"https://audiomack.com/{username}",

       
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "ArtStation": f"https://www.artstation.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}/",
        "500px": f"https://500px.com/p/{username}",

       
        "Dzen": f"https://dzen.ru/{username}",
        "Pikabu": f"https://pikabu.ru/@{username}",
        "ResearchGate": f"https://www.researchgate.net/profile/{username}",
        "Academia.edu": f"https://www.academia.edu/{username}",

        
        "Patreon": f"https://www.patreon.com/{username}",
        "Gumroad": f"https://gumroad.com/{username}",
        "Etsy": f"https://www.etsy.com/people/{username}",
        "eBay": f"https://www.ebay.com/usr/{username}",
        "Amazon Profile": f"https://www.amazon.com/gp/profile/amzn1.account.{username}",

       
        "Avito": f"https://www.avito.ru/user/{username}",
        "OLX": f"https://www.olx.com/profile/{username}",
        "MercadoLibre": f"https://perfil.mercadolibre.com/{username}",

        
        "Slashdot": f"https://slashdot.org/~{username}",
        "HackerNews": f"https://news.ycombinator.com/user?id={username}",
        "Medium (again)": f"https://{username}.medium.com",  

        #
        "AngelList": f"https://angel.co/u/{username}",
        "Glassdoor": f"https://www.glassdoor.com/profile/{username}.htm",  
    }
    
    if len(s) < 56:
        i = 1
        while len(s) < 56:
            s[f"ExtraSite{i}"] = f"https://example.com/{username}{i}"
            i += 1
    return s

def check_username(username):
    sites = build_sites(username)

    console.print(f"\n[bold bright_yellow]🔍 '{username}' kullanıcı adı {len(sites)} platformda aranıyor...[/]\n")
    time.sleep(0.2)

    table = Table(
        title=f"🧩 Kullanıcı Adı Durumları: [bold cyan]{username}[/]",
        box=box.ROUNDED,
        show_lines=True,
        border_style="bright_blue",
    )
    table.add_column("🌐 Site", justify="center", style="bold cyan")
    table.add_column("🔗 Bağlantı", justify="left", style="white")
    table.add_column("📊 Durum", justify="center", style="bold")
    table.add_column("🧾 Açıklama", justify="left", style="italic bright_white")

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    results = []

    for site, url in track(sites.items(), description="[cyan]Siteler kontrol ediliyor...[/]"):
        status = ""
        note = ""
        try:
            response = requests.get(url, headers=headers, timeout=7, allow_redirects=True)
            code = response.status_code

           
            body = response.text.lower() if response.text else ""
            uname_lower = username.lower()

            if code == 200 and uname_lower in body:
                status = "[green]✅ Bulundu[/]"
                note = "Kullanıcı profili aktif ve sayfa içeriğinde isim geçti."
            elif code == 200:
                status = "[blue]🔄 Muhtemel Eşleşme[/]"
                note = "Sayfa var ancak içerikte kullanıcı adı açıkça bulunamadı."
            elif code == 404:
                status = "[red]❌ Bulunamadı[/]"
                note = "Kullanıcı bu platformda görünmüyor (404)."
            else:
                status = f"[yellow]⚠ Kod {code}[/]"
                note = "Beklenmeyen HTTP yanıtı."
        except requests.exceptions.RequestException as e:
            status = "[yellow]⚠ Hata[/]"
            note = f"Bağlantı hatası: {str(e)}"

        table.add_row(site, url, status, note)
        results.append((site, url, status.replace("[","").replace("]",""), note))
        time.sleep(0.05)  
    console.print("\n")
    console.print(table)

   
    filename = f"results_{username}.csv"
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["site", "url", "status", "note"])
            for row in results:
                writer.writerow(row)
        console.print(f"\n[bold green]✔ Sonuçlar kaydedildi:[/] [bold]{filename}[/]")
    except Exception as e:
        console.print(f"\n[bold red]✖ Kaydetme başarısız:[/] {e}")

if __name__ == "__main__":
    banner()
    while True:
        username = console.input("\n[bold cyan]🔹 Kontrol edilecek kullanıcı adını gir ('exit' ile çık): [/]")
        if username.lower() in ["exit", "çık", "quit", "q"]:
            console.print("\n[bold green]👋 Furkan OSINT kullandığın için teşekkürler! Görüşmek üzere.[/]")
            break
        if not username.strip():
            console.print("[red]Lütfen geçerli bir kullanıcı adı gir.[/]")
            continue
        check_username(username.strip())