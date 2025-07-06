# Engagement Rings Collection - Django E-commerce Application

Bu proje, nişan yüzükleri için modern bir e-ticaret web uygulamasıdır. Django framework'ü kullanılarak geliştirilmiştir.

## 🚀 Özellikler

### Frontend Özellikleri
- **Modern ve Responsive Tasarım**: Bootstrap 5 ile mobil uyumlu tasarım
- **Ürün Galerisi**: Farklı renk seçenekleri ile ürün görüntüleme
- **Gelişmiş Filtreleme**: Popülerlik, ağırlık, renk ve arama filtreleri
- **Sıralama Seçenekleri**: Popülerlik, isim ve ağırlığa göre sıralama
- **Ürün Detay Sayfaları**: Detaylı ürün bilgileri ve görselleri
- **Animasyonlar**: Smooth hover efektleri ve geçişler

### Backend Özellikleri
- **RESTful API**: Django REST Framework ile API endpoints
- **Veritabanı Yönetimi**: SQLite veritabanı (production'da PostgreSQL kullanılabilir)
- **Admin Paneli**: Django admin ile ürün yönetimi
- **Filtreleme ve Arama**: Gelişmiş filtreleme sistemi
- **JSON Veri Yükleme**: Management command ile veri import

## 🛠️ Teknolojiler

- **Backend**: Django 5.2, Django REST Framework
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Veritabanı**: SQLite (Development), PostgreSQL (Production)
- **İkonlar**: Font Awesome 6
- **Ek Paketler**: django-cors-headers, django-filter

## 📦 Kurulum

### Gereksinimler
- Python 3.8+
- pip

### Adım Adım Kurulum

1. **Projeyi klonlayın**
```bash
git clone <repository-url>
cd engagement-rings-app
```

2. **Virtual environment oluşturun**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Bağımlılıkları yükleyin**
```bash
pip install -r requirements.txt
```

4. **Veritabanını oluşturun**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Ürün verilerini yükleyin**
```bash
python manage.py load_products
```

6. **Superuser oluşturun**
```bash
python manage.py createsuperuser
```

7. **Sunucuyu başlatın**
```bash
python manage.py runserver
```

## 🌐 Kullanım

### Ana Sayfalar
- **Ana Sayfa**: `http://localhost:8000/`
- **Ürün Listesi**: `http://localhost:8000/products/`
- **Admin Paneli**: `http://localhost:8000/admin/`

### API Endpoints
- **Tüm Ürünler**: `GET /api/products/`
- **Ürün Detayı**: `GET /api/products/{id}/`
- **Popüler Ürünler**: `GET /api/products/popular/`
- **Renk Listesi**: `GET /api/products/colors/`
- **Ürün Görselleri**: `GET /api/products/{id}/images/`

### Filtreleme Parametreleri
- `search`: Ürün adında arama
- `min_popularity` / `max_popularity`: Popülerlik skoru aralığı
- `min_weight` / `max_weight`: Ağırlık aralığı
- `color`: Renk filtresi (white, yellow, rose)
- `ordering`: Sıralama (name, -name, weight, -weight, -popularity_score)

## 📁 Proje Yapısı

```
engagement-rings-app/
├── engagement_rings_backend/    # Ana Django projesi
├── products/                    # Ürün uygulaması
│   ├── models.py               # Ürün modeli
│   ├── views.py                # API views
│   ├── serializers.py          # API serializers
│   ├── admin.py                # Admin paneli
│   └── management/             # Management commands
├── frontend/                   # Frontend uygulaması
│   ├── views.py                # Template views
│   └── urls.py                 # URL patterns
├── templates/                  # HTML templates
│   ├── base.html              # Ana template
│   └── frontend/              # Frontend templates
├── static/                     # Statik dosyalar
│   ├── css/                   # CSS dosyaları
│   └── js/                    # JavaScript dosyaları
├── manage.py                   # Django management
├── products.json              # Ürün verileri
└── README.md                  # Bu dosya
```

## 🎨 Özelleştirme

### CSS Özelleştirme
Ana CSS dosyası: `static/css/style.css`

### JavaScript Özelleştirme
Ana JS dosyası: `static/js/main.js`

### Template Özelleştirme
Templates klasöründe bulunan HTML dosyalarını düzenleyebilirsiniz.

## 🔧 Yönetim Komutları

### Ürün Verilerini Yükleme
```bash
python manage.py load_products
```

### Veritabanı Yedekleme
```bash
python manage.py dumpdata products > products_backup.json
```

### Veritabanı Geri Yükleme
```bash
python manage.py loaddata products_backup.json
```

## 🚀 Production Deployment

### Gereksinimler
- PostgreSQL veritabanı
- Gunicorn veya uWSGI
- Nginx web sunucusu
- SSL sertifikası

### Environment Variables
```bash
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=yourdomain.com
```

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 👨‍💻 Geliştirici

**Erkan Turgut**
- Email: turguterkan55@gmail.com
- GitHub: [@erkan1205](https://github.com/erkan1205)

## 🙏 Teşekkürler

- Django ekibine harika framework için
- Bootstrap ekibine responsive tasarım için
- Font Awesome ekibine ikonlar için 