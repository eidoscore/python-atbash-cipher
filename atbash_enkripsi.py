

#mulai enkripsi
def encrypting():
    huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #BALIK HURUF DENGAN KURANGI -1
    rev_huruf = huruf[::-1]

    pesan = input("Masukan Teks : ").upper();

    encrypt_text = ""

    for i in range(len(pesan)):
        if pesan[i] == chr(32):
            encrypt_text += " "
        else:
            for j in range(len(huruf)):
                if pesan[i] == huruf[j]:
                    encrypt_text += rev_huruf[j]
                    break


    print ("Pesan Terenkripsi : {}".format(encrypt_text))

#mulai dekripsi
def decrypting():
    huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #BALIK HURUF DENGAN KURANGI 1
    rev_huruf = huruf[::-1]

    pesan = input ("Masuan Teks: ")

    decrypt_text = ""

    for i in range(len(pesan)):
        if pesan[i] == chr(32):
            decrypt_text += " "
        else:
            for j in range(len(rev_huruf)):
                if pesan[i] == rev_huruf[j]:
                    decrypt_text += huruf[j]
                    break

    print ("Pesan Terdekripsi : {}".format(decrypt_text))


def main():
    choice = int(input("Pilih Menu Program\n1.Menu Enkripsi\n2. Menu Dekripsi\n: "))
    if choice == 1:
        print("--Mulai Enkripsi--")
        encrypting()
    elif choice == 2:
        print("--Meulai Dekripsi--")
        decrypting()
    else:
        print("Salah Pilih")


if __name__ == "__main__":
    main()
