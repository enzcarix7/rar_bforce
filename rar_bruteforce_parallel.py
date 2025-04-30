import torch
import multiprocessing
from os.path import dirname
from itertools import product
from string import ascii_letters, digits
from rarfile import RarFile, BadRarFile

device = torch.device("mps")

def try_password(rar_path, password_batch):
    with open(rar_path, 'rb') as rar_file:
        rar = RarFile(rar_file)
        for password in password_batch:
            try:
                print(f"Provando password: {password}")
                rar.extractall(path=dirname(rar_path), pwd=password.encode())
                print(f'[+] Password trovata: {password}')
                return password
            except BadRarFile:
                pass

def generate_passwords(characters, max_length):
    for length in range(1, max_length + 1):
        for combination in product(characters, repeat=length):
            yield ''.join(combination)


def parallel_bruteforce(rar_path, num_workers=14, max_length=5, characters=ascii_letters + digits):
    print(f'Starting RAR bruteforce on {rar_path} with {num_workers} workers (CPU e GPU)')

    pool = multiprocessing.Pool(num_workers)

    password_gen = generate_passwords(characters, max_length)
    batch_size = 100

    batch = []
    for password in password_gen:
        batch.append(password)
        if len(batch) == batch_size:
            pool.apply_async(try_password, (rar_path, batch))
            batch = []

    if batch:
        pool.apply_async(try_password, (rar_path, batch))

    pool.close()
    pool.join()


def main(rar_path):
    print('Avvio il bruteforce su CPU e GPU insieme...')
    parallel_bruteforce(rar_path, num_workers=14, max_length=5)


if __name__ == "__main__":
    rar_path = 'rarfile.rar'
    main(rar_path)
