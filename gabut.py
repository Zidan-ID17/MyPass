#coding=utf-8
import os, sys, time, random, string

w = "\033[97m"
r = "\033[91m"
g = "\033[92m"
gy = "\033[90m"
duar = "cls"
hmm = "clear"
kuk = 1

def generate(entry):
    random_char = []

    for char in entry:
        random_char.append(char)
        if random.choice([True, False]):
            random_char.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

        if random.choice([True, False]):
            random_char.append(random.choice(string.digits))

    random.shuffle(random_char)
    return "".join(random_char)

def main():
    os.system(duar if os.name == "nt" else hmm)
    time.sleep(kuk)
    print(f"{gy}="*35,f"\n{g} __  __       ____   ")
    print(f"{g} |  \/  |_   _|  _ \ __ _ ___ ___ ")
    print(f"{g} | |\/| | | | | |_) / _` / __/ __|")
    print(f"{g} | |  | | |_| |  __/ (_| \__ \__ \\")
    print(f"{g} |_|  |_|\__, |_|   \__,_|___/___/")
    print(f"{g}         |___/             \n",f"{gy}="*35)
    entry = input(f"\n{w}masukkan kata dasar > ")

    if not entry:
        print(f"\n{w}input tidak boleh kosong{r}!!")

    result = generate(entry)
    print(f"\n{w}kata sandi yang dihasilkan = {g}{result}")

    ask = input(f"\n{w}ingin mencoba lagi? (y/n)").lower()
    if ask == "y":
        main()
    else:
        print(f"\n{w}hehehe....\n")
        time.sleep(kuk)
        sys.exit()

if __name__ == "__main__":
    main()