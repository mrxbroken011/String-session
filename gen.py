import asyncio as a, os as o, time as t
from pyrogram import Client as C
from pyrogram.session import StringSession as S
from colorama import Fore as F, Style as Y

X = "session.txt"  

async def G():    
    print(f"{F.RED}L{Y.RESET_ALL}", end="", flush=True)
    [t.sleep(0.5) or print(f"{F.RED}.{Y.RESET_ALL}", end="", flush=True) for _ in range(3)]
    print("\n")

    print(f"{F.GREEN}{Y.BRIGHT}W{Y.RESET_ALL}")
    print(f"{F.BLUE}B@Brokenxnetwork{Y.RESET_ALL}\n")

    I = int(input("Enter your API ID: ").strip())
    print(f"{F.GREEN}✅ Done! API ID added.{Y.RESET_ALL}\n")

    H = input("Enter your API HASH: ").strip()
    print(f"{F.GREEN}✅ Done! API Hash added.{Y.RESET_ALL}\n")

    P = input("Enter your phone number (with country code, without +): ").strip()
    print(f"{F.GREEN}⏳ Please wait... Sending OTP...{Y.RESET_ALL}\n")

    async with C(S(), I, H) as A:
        S1 = await A.send_code(P)
        H1 = S1.phone_code_hash
        C1 = input("Enter the OTP sent to your Telegram: ").strip()
        await A.sign_in(P, C1, phone_code_hash=H1)
        S2 = await A.export_session_string()

        with open(X, "w") as f:
            f.write(S2)

        print(f"\n{F.GREEN}✅ **Session Generated Successfully!**{Y.RESET_ALL}")
        print(f"🔑 **Your Session String (saved to {X}):**\n{S2}")
        print(f"\n{F.YELLOW}⚠️ **Save this string safely! Do not share it with anyone.**{Y.RESET_ALL}")

a.run(G())
