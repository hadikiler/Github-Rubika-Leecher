import asyncio
import base64
import os
from rubpy import Client


async def generate_session_string():
    print("--- Rubika Session to Base64 Generator ---")

    # یک نام موقت برای فایل سشن
    session_name = "temp_session"
    session_file = f"{session_name}.rp"

    # حذف سشن قدیمی اگر وجود داشته باشد (برای شروع تازه)
    if os.path.exists(session_file):
        os.remove(session_file)

    async with Client(name=session_name) as app:
        # در این مرحله، کتابخانه از شما شماره موبایل و سپس کد OTP را در ترمینال می‌پرسد
        me = await app.get_me()
        print(f"\nSuccessfully logged in as: {me.user.first_name} (@{me.user.username})")

    # حالا که فایل .rp ساخته شده، آن را به Base64 تبدیل می‌کنیم
    if os.path.exists(session_file):
        with open(session_file, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode("utf-8")

            print("\n" + "=" * 50)
            print("YOUR BASE64 SESSION STRING (COPY EVERYTHING BELOW):")
            print("=" * 50 + "\n")
            print(encoded_string)
            print("\n" + "=" * 50)
            print("COPY THE TEXT ABOVE AND PASTE IN GITHUB SECRETS")
            print("=" * 50)

        # پاکسازی فایل موقت برای امنیت
        os.remove(session_file)
        print(f"\nTemporary file {session_file} deleted for security.")
    else:
        print("Error: Session file was not created!")


if __name__ == "__main__":
    asyncio.run(generate_session_string())
