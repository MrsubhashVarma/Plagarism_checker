# pyrefly: ignore [missing-import]
import uvicorn
import os
import sys

# Ensure UTF-8 output encoding for Windows terminals
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("[+] Starting PlagCheck AI Web Application...")
    print("[+] Access Web Interface: http://127.0.0.1:8000")
    print("[+] Vercel Deployment: Ready via vercel.json & api/index.py")
    print("=" * 60 + "\n")
    uvicorn.run("api.index:app", host="127.0.0.1", port=8000, reload=True)
