from os import path, mkdir
from rarfile import RarFile, BadRarFile
from itertools import permutations
from string import ascii_letters, digits


def rar_bruteforce(rar_path: str) -> None:
    print(f'Starting RAR bruteforce in {rar_path}')
    archive_dir = path.dirname(rar_path)
    unrar_dir = path.join(archive_dir, rar_path + '_bruteforce')
    tentativi: int = 0
    with open(rar_path, 'rb') as rar_file:
        rar: RarFile = RarFile(rar_file)
        characters = ascii_letters + digits
        for pass_length in range(1, 13):
            for pass_combination in permutations(characters, pass_length):
                password = ''.join(pass_combination)
                print(f'Trying password: {password}')
                try:
                    tentativi += 1
                    if tentativi % 10000 == 0:
                        print(f'Tentativi: {tentativi}')
                    rar.extractall(path=archive_dir, pwd=password.encode())
                    print(f'[+] Password found: {password}')
                    if not path.exists(unrar_dir):
                        mkdir(unrar_dir)
                        print(f'Extracted files to: {unrar_dir}')
                    return password
                except BadRarFile:
                    continue


rar_bruteforce('rarfile.rar')
