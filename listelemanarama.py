liste = []

print("Listeye 5 Eleman Giriniz: ")

for i in range(5):
    sayi = int(input())
    liste.append(sayi)

print("Listede aranacak elemanı giriniz: ")

eleman = int(input())

kontrol = 0;

for i in range(5):
    if eleman == liste[i]:
        print("\ngirilen eleman bulundu. İndeksi: ", i)
        kontrol = kontrol+1

if (kontrol == 0):
    print("eleman bulunamadı!")