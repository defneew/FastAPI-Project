# Hotel Management API

Bu proje, **FastAPI** ve **SQLite** kullanılarak geliştirilmiş bir otel yönetim sistemidir.  
Projede otel, oda, misafir, rezervasyon ve hizmet (service) varlıkları (entity) bulunmakta ve aralarındaki ilişkiler modellenmiştir.  
Temel **CRUD (Create, Read, Update, Delete)** işlemleri yapılabilmektedir.

## Kullanılan Teknolojiler

- **FastAPI**: Modern, hızlı (high-performance) Python web framework'ü.
- **SQLAlchemy**: Veritabanı ORM (Object-Relational Mapping) kütüphanesi.
- **SQLite**: Hafif, dosya tabanlı ilişkisel veritabanı.

## Veritabanı Yapısı ve İlişkiler

### Varlıklar (Entities)

- **Hotel (`tb_hotels`)**
  - `id`, `name`, `address`, `city`
  - Bir otelin birden fazla odası (**one-to-many**) olabilir.

- **Room (`tb_rooms`)**
  - `id`, `room_number`, `room_type`, `price_per_night`, `hotel_id`
  - Her oda bir otele bağlıdır (**many-to-one**).
  - Oda ile hizmetler arasında çoktan çoğa (**many-to-many**) ilişki vardır.

- **Guest (`tb_guests`)**
  - `id`, `first_name`, `last_name`, `phone_number`
  - Bir misafirin birden fazla rezervasyonu (**one-to-many**) olabilir.

- **Booking (`tb_bookings`)**
  - `id`, `guest_id`, `room_id`, `check_in_date`, `check_out_date`
  - Her rezervasyon bir misafire ve bir odaya bağlıdır (**many-to-one** ilişkiler).

- **Service (`tb_services`)**
  - `id`, `name`, `description`
  - Hizmetler odalarla çoktan çoğa (**many-to-many**) ilişkilidir.

### İlişki Tabloları

- **room_service_association**: Oda ve hizmetler arasında köprü görevinde olan ilişki tablosu.

## Proje Yapısı

- FastAPI uygulaması `app = FastAPI()` ile başlatılmıştır.
- SQLAlchemy ORM kullanılarak modeller (`Base` sınıfı üzerinden) tanımlanmıştır.
- `create_engine` ile SQLite veritabanı bağlantısı sağlanmıştır.
- `SessionLocal` ile her istek için veritabanı bağlantı oturumu oluşturulmuştur.
- `get_db` fonksiyonu ile her işlemde veritabanı bağlantısı yönetilmektedir.

## CRUD İşlemleri

Proje içerisinde her varlık için temel **CRUD** (Oluşturma, Okuma, Güncelleme, Silme) işlemleri gerçekleştirilmiştir:

- **Create (Oluşturma)**: Yeni otel, oda, misafir, rezervasyon veya hizmet kaydı eklenebilir.
- **Read (Okuma)**: Mevcut kayıtlar listelenebilir ve istenirse tekil olarak görüntülenebilir.
- **Update (Güncelleme)**: Mevcut kayıtların bilgileri değiştirilebilir.
- **Delete (Silme)**: Kayıtlar veritabanından silinebilir.

## Projeyi Çalıştırmak İçin Gerekli Adımlar

### 1. Gerekli Paketleri Yükleyin
Öncelikle, projenin bağımlılıklarını yüklemeniz gerekmektedir.
### 2. Aşağıdaki komutları çalıştırın
cd FastAPI_Project

uvicorn main:app --reload
### Oluşturulan url de /docs adresinde api dökümantasyonuna ulaşabilirsiniz.
