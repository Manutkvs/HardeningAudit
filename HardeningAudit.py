import os
import subprocess

def check_ssh_config():
    """Verifica si el acceso root por SSH está deshabilitado."""
    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            content = f.read()
            if "PermitRootLogin no" in content:
                print("[+] SSH: PermitRootLogin está deshabilitado (Seguro).")
            else:
                print("[!] SSH: ¡CUIDADO! PermitRootLogin podría estar habilitado.")
    except Exception as e:
        print(f"[-] Error al leer SSH: {e}")

def check_open_ports():
    """Lista puertos abiertos utilizando netstat o ss."""
    print("[*] Escaneando puertos en escucha...")
    result = subprocess.run(['ss', '-tuln'], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    print("--- Auditor de Seguridad Basico ---")
    check_ssh_config()
    check_open_ports()
