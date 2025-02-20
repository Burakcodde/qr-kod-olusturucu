# QR Kod Oluşturucu

Bu proje, kullanıcıdan alınan metin veya URL'yi kullanarak bir QR kodu oluşturur. Kullanıcı ayrıca QR kodunun rengini, arka plan rengini ve kutu boyutunu belirleyebilir. QR kodunun ortasına bir logo yerleştirilebilir.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız var:

- `qrcode`
- `Pillow`

Bu kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz:

```sh
pip install qrcode[pil]
pip install pillow
```

### Kullanım
Proje dizininde app.py dosyasını çalıştırarak QR kod oluşturma işlemini başlatabilirsiniz:

```sh
python app.py
```

Kullanıcıdan sırasıyla aşağıdaki bilgiler istenecektir:

1. Metin veya URL
2. QR kodunun rengi (örneğin, 'siyah')
3. Arka plan rengi (örneğin, 'beyaz')
4. Kutu boyutu (örneğin, 10)

Girdiğiniz bilgilere göre QR kodu oluşturulacak ve qrcode_with_logo.png dosyası olarak kaydedilecektir.
