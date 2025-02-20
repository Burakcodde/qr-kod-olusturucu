import os
import qrcode
from PIL import Image

# Çalışma dizinini değiştir
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Renkleri İngilizce karşılıklarına çevirmek için bir sözlük
renk_sozlugu = {
    "siyah": "black",
    "beyaz": "white",
    "kırmızı": "red",
    "yeşil": "green",
    "mavi": "blue",
    "sarı": "yellow",
    "mor": "purple",
    "turuncu": "orange",
    "gri": "gray",
}

# Kullanıcıdan metin veya URL girişi al
kullanici_girdisi = input("Lütfen bir metin veya URL girin: ")

# Kullanıcıdan QR kodu rengi ve boyutu için giriş al
qr_rengi_turkce = input("Lütfen QR kodunun rengini girin (örneğin, 'siyah'): ")
arka_plan_rengi_turkce = input("Lütfen arka plan rengini girin (örneğin, 'beyaz'): ")
kutu_boyutu = int(input("Lütfen kutu boyutunu girin (örneğin, 10): "))

# Renkleri İngilizce karşılıklarına çevir
qr_rengi = renk_sozlugu.get(qr_rengi_turkce.lower(), "black")
arka_plan_rengi = renk_sozlugu.get(arka_plan_rengi_turkce.lower(), "white")

# QR kodu oluştur
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Yüksek hata düzeltme seviyesi
    box_size=kutu_boyutu,
    border=4,
)
qr.add_data(kullanici_girdisi)
qr.make(fit=True)

# QR kodu bir görüntü olarak kaydet
img = qr.make_image(fill=qr_rengi, back_color=arka_plan_rengi).convert("RGB")

# Logoyu ekle
logo = Image.open("logo.png")  # Logonuzun dosya adı
logo_size = kutu_boyutu * 3  # Logonun boyutunu ayarlayın
logo = logo.resize((logo_size, logo_size))

# Logoyu QR kodun ortasına yerleştir
pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
img.paste(logo, pos, logo)

# QR kodunu kaydet
img.save("qrcode_with_logo.png")

# Girdiyi ekrana yazdır
print(f"Girilen metin veya URL: {kullanici_girdisi}")
print(
    f"QR kodu 'qrcode_with_logo.png' olarak kaydedildi. Renk: {qr_rengi_turkce}, Arka Plan Rengi: {arka_plan_rengi_turkce}, Kutu Boyutu: {kutu_boyutu}"
)
