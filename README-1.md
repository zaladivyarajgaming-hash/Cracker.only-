# cracker.py

A numeric PIN brute-forcer for Termux/Linux. Tests digit combinations against:
- A hash (MD5, SHA1, SHA256, etc.)
- A password-protected ZIP file

Intended for recovering forgotten PINs on **your own data**, or authorized security testing.

## Installation (Termux)

```bash
pkg update && pkg upgrade -y
pkg install python -y
pip install -r requirements.txt
```

## Installation (Linux/Debian/Ubuntu)

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install -r requirements.txt
```

## Usage

Crack a hash:
```bash
python cracker.py --hash <target_hash> --algo sha256 --min 4 --max 6
```

Crack a password-protected ZIP:
```bash
python cracker.py --zip locked.zip --min 4 --max 6
```

## Arguments

| Flag     | Description                          | Default |
|----------|---------------------------------------|---------|
| --hash   | Target hash to crack                 | -       |
| --algo   | Hash algorithm (md5, sha1, sha256...) | sha256  |
| --zip    | Path to password-protected zip       | -       |
| --min    | Minimum PIN length                   | 4       |
| --max    | Maximum PIN length                   | 6       |

## Legal / Ethical Use

This tool is for recovering access to **your own** files/accounts, or for security testing you are explicitly authorized to perform. Do not use it against systems, files, or accounts you do not own or lack permission to test.

## License

MIT — see [LICENSE](LICENSE).
