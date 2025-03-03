import asyncio
import time
from pyrogram import Client
from pyrogram.session import StringSession
from colorama import Fore, Style

SESSION_FILE = "session.txt"

async def generate_session():
    print(f"{Fore.RED}Loading{Style.RESET_ALL}", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(f"{Fore.RED}.{Style.RESET_ALL}", end="", flush=True)
    print("\n")

    print(f"{Fore.GREEN}{Style.BRIGHT}Welcome to Pyrogram v2 String Session Generator!{Style.RESET_ALL}")
    print(f"{Fore.BLUE}By @Brokenxnetwork{Style.RESET_ALL}\n")

    api_id = int(input("Enter your API ID: ").strip())
    print(f"{Fore.GREEN}✅ Done! API ID added.{Style.RESET_ALL}\n")

    api_hash = input("Enter your API HASH: ").strip()
    print(f"{Fore.GREEN}✅ Done! API Hash added.{Style.RESET_ALL}\n")

    phone_number = input("Enter your phone number (with country code, without +): ").strip()
    print(f"{Fore.GREEN}⏳ Please wait... Sending OTP...{Style.RESET_ALL}\n")

    async with Client(StringSession(), api_id, api_hash) as app:
        sent_code = await app.send_code(phone_number)
        phone_code_hash = sent_code.phone_code_hash

        code = input("Enter the OTP sent to your Telegram: ").strip()
        await app.sign_in(phone_number, code, phone_code_hash=phone_code_hash)

        session_string = await app.export_session_string()

        with open(SESSION_FILE, "w") as f:
            f.write(session_string)

        print(f"\n{Fore.GREEN}✅ **Session Generated Successfully!**{Style.RESET_ALL}")
        print(f"🔑 **Your Session String (saved to {SESSION_FILE}):**\n{session_string}")
        print(f"\n{Fore.YELLOW}⚠️ **Save this string safely! Do not share it with anyone.**{Style.RESET_ALL}")

asyncio.run(generate_session())
