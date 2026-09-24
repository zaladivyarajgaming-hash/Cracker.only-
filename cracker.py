#!/usr/bin/env python3
"""
cracker.py - Numeric PIN brute-forcer for YOUR OWN files/hashes only.

Supports:
  - Cracking a hash (md5/sha1/sha256) of a numeric PIN
  - Cracking a password-protected ZIP file with a numeric PIN

Usage:
  python cracker.py --hash <hash> --algo sha256 --min 4 --max 6
  python cracker.py --zip locked.zip --min 4 --max 6

Only use this on data/files you own or are authorized to test.
"""

import argparse
import hashlib
import itertools
import sys
import zipfile
import time


def crack_hash(target_hash, algo, min_len, max_len):
    target_hash = target_hash.lower().strip()
    algo = algo.lower()
    if algo not in hashlib.algorithms_available:
        print(f"[!] Unsupported algorithm: {algo}")
        sys.exit(1)

    tried = 0
    start = time.time()
    for length in range(min_len, max_len + 1):
        for combo in itertools.product("0123456789", repeat=length):
            pin = "".join(combo)
            h = hashlib.new(algo, pin.encode()).hexdigest()
            tried += 1
            if h == target_hash:
                elapsed = time.time() - start
                print(f"\n[+] FOUND: {pin}  ({tried} tries, {elapsed:.2f}s)")
                return pin
            if tried % 50000 == 0:
                print(f"[.] tried {tried} combos...", end="\r")

    print(f"\n[-] Not found after {tried} attempts.")
    return None


def crack_zip(zip_path, min_len, max_len):
    try:
        zf = zipfile.ZipFile(zip_path)
    except FileNotFoundError:
        print(f"[!] File not found: {zip_path}")
        sys.exit(1)

    tried = 0
    start = time.time()
    for length in range(min_len, max_len + 1):
        for combo in itertools.product("0123456789", repeat=length):
            pin = "".join(combo)
            tried += 1
            try:
                zf.extractall(pwd=pin.encode())
                elapsed = time.time() - start
                print(f"\n[+] FOUND: {pin}  ({tried} tries, {elapsed:.2f}s)")
                return pin
            except (RuntimeError, zipfile.BadZipFile):
                pass
            if tried % 5000 == 0:
                print(f"[.] tried {tried} combos...", end="\r")

    print(f"\n[-] Not found after {tried} attempts.")
    return None


def main():
    p = argparse.ArgumentParser(description="Numeric PIN cracker (authorized use only)")
    p.add_argument("--hash", help="Target hash to crack")
    p.add_argument("--algo", default="sha256", help="Hash algorithm (md5, sha1, sha256, ...)")
    p.add_argument("--zip", help="Path to password-protected zip file")
    p.add_argument("--min", type=int, default=4, help="Minimum PIN length")
    p.add_argument("--max", type=int, default=6, help="Maximum PIN length")
    args = p.parse_args()

    if not args.hash and not args.zip:
        print("[!] Provide --hash or --zip. See --help.")
        sys.exit(1)

    print("=== cracker.py — numeric PIN brute-forcer ===")
    print("Use only on data you own or are authorized to test.\n")

    if args.hash:
        crack_hash(args.hash, args.algo, args.min, args.max)
    elif args.zip:
        crack_zip(args.zip, args.min, args.max)


if __name__ == "__main__":
    main()
