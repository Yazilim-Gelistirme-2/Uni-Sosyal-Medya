
# Üniversite Sosyal Ağ Analizi Uygulaması

## 1. Proje Adı, Ekip Üyeleri, Tarih

- **Ders:** Yazılım Geliştirme Laboratuvarı-I  
- **Bölüm:** Bilişim Sistemleri Mühendisliği  
- **Üniversite:** Kocaeli Üniversitesi  

**Ekip Üyeleri:**
- Furkan Demirci - 231307061   
- Yekta Cengiz   - 231307080

**Tarih:** 02.01.2026

---

## 2. Giriş (Proje Tanımı ve Amaç)

Bu proje, günümüz sosyal ağlarındaki karmaşık kullanıcı ilişkilerini analiz 
etmek amacıyla geliştirilmiştir. Sosyal ağları birer yönsüz ve ağırlıklı graf olarak 
modelleyen uygulamamız; kullanıcıları **düğüm (node)**, etkileşimleri ise **kenar (edge)** olarak tanımlar. 
Temel amacımız, dinamik bir sosyal ağda en kısa yolu bulmak, 
toplulukları ayrıştırmak ve en etkili kullanıcıları (influencer) bilimsel metotlarla tespit etmektir. 
Proje sürecinde nesne yönelimli programlama (OOP) ve veri yapıları prensipleri temel alınmıştır.

---

## 3. Gerçeklenen Algoritmalar

### 3.1 Breadth First Search (BFS)

**Çalışma Mantığı:**  
BFS, bir graf veya ağaç veri yapısında gezinmek için kullanılan temel bir algoritmadır. Temel prensibi "katman katman" ilerlemektir. Başlangıç düğümünden başlar, önce o düğüme doğrudan bağlı olan tüm komşuları ziyaret eder, ardından bu komşuların komşularına geçer.

**Akış Diyagramı:**

```mermaid
graph TD
    A([Başla]) --> B{ID Graf İçinde mi?}
    B -- Hayır --> C[Hata Mesajı ve Süre: 0 Döndür]
    B -- Evet --> D[Kuyruğu Başlat ve Ziyaret Edilenlere Ekle]
    
    D --> E{Kuyruk Boş mu?}
    E -- Hayır --> F[Kuyruğun Başından Eleman Çıkar -curr_id-]
    F --> G[Düğümü Sonuç Listesine Ekle]
    G --> H[Düğümün Komşularını Döngüye Al]
    
    H --> I{Komşu Ziyaret Edildi mi?}
    I -- Hayır --> J[Komşuyu Ziyarete Ekle ve Kuyruğa At]
    I -- Evet --> K[Sıradaki Komşuya Geç]
    
    J --> K
    K -- Tüm Komşular Bittiyse --> E
    
    E -- Evet --> L[Sonuçları ve Geçen Süreyi Döndür]
    L --> M([Bitir])
```

**Zaman Karmaşıklığı:**  
- O(V + E)



---

### 3.2 Depth First Search (DFS)

**Çalışma Mantığı:**  
DFS algoritması aramaya başladığı düğümden ulaşabileceği en derin düğüme kadar gider, gidecek daha derin bir düğüm kalmadığında geri sarar ve derin düğümlere öncelik vererek gezmeye devam eder.


**Akış Diyagramı**
```mermaid
graph TD
    A([Başla]) --> B[Yığını Başlat ve Ziyaret Kümesini Oluştur]
    B --> C{Yığın Boş mu?}
    C -- Hayır --> D[Yığının En Üstündeki Elemanı Çıkar -u-]
    D --> E{u Ziyaret Edildi mi?}
    
    E -- Evet --> C
    E -- Hayır --> F[u'yu Ziyaret Edildi Olarak İşaretle]
    F --> G[u'yu Sonuç Listesine -order- Ekle]
    G --> H[u'nun Komşularını Ters Sırada Döngüye Al]
    
    H --> I{Komşu Ziyaret Edildi mi?}
    I -- Hayır --> J[Komşuyu Yığına Ekle]
    I -- Evet --> K[Sıradaki Komşuya Geç]
    
    J --> K
    K -- Tüm Komşular Bittiyse --> C
    
    C -- Evet --> L[Sıralama Listesini Döndür]
    L --> M([Bitir])
```


**Zaman Karmaşıklığı:**  
- O(V + E)

---

### 3.3 Dijkstra Algoritması

**Çalışma Mantığı:**  
Dijkstra algoritması, bir başlangıç düğümünden diğer tüm düğümlere olan en kısa yol mesafelerini bulmak için kullanılır. Temel olarak, algoritma her adımda henüz işlenmemiş düğümler arasından en kısa mesafeye sahip olanı seçer ve bu düğümü işler. Seçilen düğümün komşularının mesafelerini günceller ve ardından bir sonraki adıma geçer. Bu işlem, hedef düğüme ulaşılıncaya kadar veya tüm düğümler işlenene kadar devam eder.

```mermaid
graph TD
    A([Başla]) --> B{ID'ler Graf İçinde mi?}
    B -- Hayır --> C[Hata Mesajı Döndür]
    B -- Evet --> D[Mesafeleri Sonsuz Yap, Başlangıcı 0 Yap]
    
    D --> E[Başlangıcı Öncelikli Kuyruğa At]
    E --> F{Kuyruk Boş mu?}
    
    F -- Hayır --> G[En Küçük Mesafeli Düğümü Çıkar -u-]
    G --> H{Mesafe Kontrolü ve Hedef Kontrolü}
    H -- Hedefe ulaşıldı mı? --> I[Döngüyü Kır]
    
    H -- Hayır --> J[Komşuları Döngüye Al]
    J --> K[Yeni Mesafe Hesapla: mevcut + agirlik]
    
    K --> L{Yeni Mesafe < Mevcut Mesafe?}
    L -- Evet --> M[Mesafeyi Güncelle ve Kuyruğa Ekle]
    L -- Hayır --> N[Sıradaki Komşuya Geç]
    
    M --> N
    N -- Komşular Bitti mi? --> F
    
    F -- Evet / Döngü Kırıldı --> O{Mesafe Sonsuz mu?}
    O -- Evet --> P[Yol Bulunamadı Döndür]
    O -- Hayır --> Q[onceki Sözlüğü ile Yolu Oluştur]
    Q --> R([En Kısa Yolu ve Mesafeyi Döndür])
```

**Zaman Karmaşıklığı:**  
- O((V + E) log V)

---

### 3.4 A* Algoritması

**Çalışma Mantığı:**  
A* algoritması, temelde başlangıç düğümüyle bitiş düğümü arasındaki bütün diğer düğümlerin konumlarına göre hesaplama yaparak optimum sonuca ulaşır.

- f(n) = g(n) + h(n)

- f(n) : Hesaplanan toplam yol fonksiyonu

- g(n): İlk düğüm noktasıyla, mevcut düğüm noktası arasındaki maliyet

- h(n): Sezgisel fonksiyon

```mermaid
graph TD
    A([Başla]) --> B[g_score=sonsuz, f_score=sonsuz]
    B --> C[Başlangıç g=0, f=h_score olarak ayarla]
    C --> D{open_set Boş mu?}
    
    D -- Hayır --> E[open_set içinde f_score'u en küçük olanı seç -current-]
    E --> F{current == goal_id?}
    
    F -- Evet --> G[came_from üzerinden geri giderek yolu oluştur]
    G --> H([Yolu ve Maliyeti Döndür])
    
    F -- Hayır --> I[current'ı open_set'ten çıkar]
    I --> J[Komşuları Döngüye Al]
    
    J --> K[Yeni g_score hesapla: g_curr + ağırlık]
    K --> L{Yeni g < Mevcut g_neighbor?}
    
    L -- Evet --> M[came_from güncelle, g ve f skorlarını hesapla]
    M --> N[Komşuyu open_set'e ekle]
    L -- Hayır --> O[Sıradaki Komşuya Geç]
    
    N --> O
    O -- Tüm Komşular Bittiyse --> D
    
    D -- Evet --> P[Yol Bulunamadı Döndür]
```

**Zaman Karmaşıklığı:**  
- Ortalama: O(E)


---

### 3.5 Merkezilik (Degree Centrality)
- Bir düğümün ne kadar çok bağlantısı varsa, o kadar merkezidir mantığına dayanır. Sosyal medya üzerinden örnek verirsek; en çok takipçisi olan kişi, o ağın en merkezi kişisidir.
- Düğüm derecelerine göre en etkili kullanıcılar belirlenir
- İlk 5 düğüm tablo halinde gösterilir

```mermaid
graph TD
    A([Başla]) --> B[Graf Boyutunu Al -n-]
    B --> C[Her Düğüm İçin Döngü Başlat]
    C --> D[Düğümün Komşu Sayısını Bul]
    D --> E[Dereceyi n-1'e Böl -Normalizasyon-]
    E --> F[Sonucu Sözlüğe Kaydet]
    F --> G{Tüm Düğümler Bitti mi?}
    
    G -- Hayır --> C
    G -- Evet --> H[Tüm DC Değerlerini Al]
    
    H --> I[Değerleri Büyükten Küçüğe Sırala]
    I --> J[İlk k Tane Düğümü Seç]
    J --> K([Sonuçları Döndür])
```

**Zaman Karmaşıklığı:**  
- O(V \log V)

---

### 3.6 Welsh–Powell Graf Renklendirme

- Welsh-Powell algoritması, bir grafın düğümlerini, birbirine komşu olan iki düğüm aynı renge boyanmayacak şekilde minimum sayıda renk kullanarak boyamayı amaçlayan bir "Greedy" (açgözlü) yaklaşımdır.
- Düğümler derecelerine göre büyükten küçüğe doğru sıralanır.
- İlk renk birinci sıradaki düğüme ve bu düğümün komşusu olmayan düğümlere atanır.
- Bir sonraki renge geçilir ve bu renk sıradaki derecesi en yüksek olan düğüme ve bu düğümün komşusu olmayan düğümlere atanır.
- Süreç bu şekilde renklendirilmemiş düğüm kalmayana kadar devam ettirilir.

```mermaid
graph TD
    A([Başla]) --> B[Düğümleri Derecelerine Göre Azalan Sırada Diz]
    B --> C[Renk Sayacı: current_color = 1]
    C --> D{Boyanmamış Düğüm Kaldı mı?}
    
    D -- Evet --> E[Sıradaki Boyanmamış Düğümü Seç ve Boya]
    E --> F[Diğer Boyanmamış Düğümleri Tara]
    
    F --> G{Düğüm, current_color ile Boyanmış Biriyle Komşu mu?}
    G -- Hayır --> H[Bu Düğümü de current_color ile Boya]
    G -- Evet --> I[Bu Düğümü Atla]
    
    H --> J{Tüm Liste Kontrol Edildi mi?}
    I --> J
    
    J -- Hayır --> F
    J -- Evet --> K[current_color Değerini 1 Artır]
    K --> D
    
    D -- Hayır --> L[Renk Sözlüğünü Döndür]
    L --> M([Bitir])
```

**Zaman Karmaşıklığı:**  
- O(V^2)


---


### 3.7 Bağlı Bileşenler

- Bağlı Bileşenler (Connected Components) algoritması, bir grafın birbirine hiçbir şekilde bağlı olmayan "alt adacıklarını" tespit etmek için kullanılır.
- Sosyal medya örneğiyle açıklarsak; bir arkadaş grubu içindeki herkes birbirine bir şekilde ulaşıyorsa bu bir gruptur, ancak tamamen kopuk başka bir arkadaş grubu varsa bu ayrı bir bağlı bileşendir.

```mermaid
graph TD
    A([Başla]) --> B[Ziyaret Edilenler Seti ve Gruplar Listesi Oluştur]
    B --> C[Grafın Her Düğümünü Döndür]
    C --> D{Düğüm Ziyaret Edildi mi?}
    
    D -- Evet --> E[Sıradaki Düğüme Geç]
    D -- Hayır --> F[Yeni Bir Grup Başlat ve Düğümü Kuyruğa At]
    
    F --> G{Kuyruk Boş mu?}
    G -- Hayır --> H[Kuyruktan Eleman Çıkar ve Gruba Ekle]
    H --> I[Komşularını Kontrol Et]
    I --> J{Komşu Ziyaret Edildi mi?}
    J -- Hayır --> K[Komşuyu Ziyaret Edildi İşaretle ve Kuyruğa At]
    J -- Evet --> L[Sıradaki Komşuya Geç]
    K --> L
    L -- Tüm Komşular Bitti --> G
    
    G -- Evet --> M[Oluşan Grubu Gruplar Listesine Ekle]
    M --> E
    
    E -- Tüm Düğümler Bitti mi? --> N[Grupları ve Toplam Adedi Döndür]
    N --> O([Bitir])
```

**Zaman Karmaşıklığı:**  
- O(V + E)


---

## 4. Sınıf Yapısı ve Modüller

```mermaid
classDiagram
    class Node {
        +int id
        +string name
        +dict properties
        +list neighbors
        +__init__(id, name, properties)
    }

    class Edge {
        +Node kaynak
        +Node hedef
        +float maliyet
        +karsidakiDugumuVer(mevcutDugum)
    }

    class Graph {
        +dict nodes
        +add_node(node)
        +add_edge(source_id, target_id)
        +get_edge_weight(source_id, target_id)
        +load_from_json(path)
        +get_adjacency_matrix()
    }

    class Utils {
        <<module>>
        +get_dynamic_weight(node_i, node_j)
    }

    class Algorithms {
        <<abstract>>
        +aramaBFS
        +DFS
        +AStarAlgorithm
        +Centrality
        +WelshPowell
        +BagliBilesenler
        +dijkstra
    }

    Graph "1" *-- "many" Node : içerir
    Node "1" -- "many" Node : neighbors (ID listesi)
    Edge --> Node : referans verir
    Graph ..> Utils : maliyet hesaplar
    Algorithms ..> Graph : üzerinde işlem yapar
    Algorithms ..> Utils : maliyet hesaplar (A*, Dijkstra)
```

---

## 5. Uygulama, Testler ve Sonuçlar

### Test Sonuçları

| Düğüm Sayısı | Algoritma            | Süre (ms) |
|-------------|----------------------|-----------|
| 15          | BFS                  | 3         |
| 60          | BFS                  | 7         |
| 15          | DFS                  | 3         |
| 60          | DFS                  | 8         |
| 15          | Dijkstra             | 18        |
| 60          | Dijkstra             | 52        |
| 15          | A*                   | 14        |
| 60          | A*                   | 39        |
| 15          | Welsh–Powell         | 9         |
| 60          | Welsh–Powell         | 31        |
| 15          | Connected Components | 4         |
| 60          | Connected Components | 11        |
| 15          | Centrality           | 2         |
| 60          | Centrality           | 6         |


---

## 5. Uygulama ve Proje Görselleri

![Düğüm Yapısı](ScreenShots/resim1.png)

![BFS Tarama Sonucu](ScreenShots/resim2.png)

![Welsh Powell](ScreenShots/resim3.png)

![Dijkstra](ScreenShots/resim4.png)

![En güçlü bağlantılar](ScreenShots/resim5.png)

![Bağlı Bileşenler](ScreenShots/resim6.png)
---

## 6. Sonuç ve Tartışma

### Başarılar
- Algoritmalar başarıyla gerçeklenmiştir
- OOP prensiplerine uyulmuştur

### Sınırlılıklar
- Büyük graflarda performans düşmektedir

### Olası Geliştirmeler
- Daha gelişmiş merkezilik ölçütleri
- Büyük ölçekli graf optimizasyonları

