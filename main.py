# main.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime


class ModernDashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.graph_data = {
            'node_count': 15,
            'edge_count': 28,
            'communities': 3,
            'density': 0.24
        }
        self.init_ui()

    def init_ui(self):
        # Ana layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # 1. ÜST BAŞLIK VE AÇIKLAMA
        header_widget = self.create_header()
        main_layout.addWidget(header_widget)

        # 2. HIZLI İSTATİSTİK KARTLARI
        stats_widget = self.create_stats_cards()
        main_layout.addWidget(stats_widget)

        # 3. GRAF ÖNİZLEME VE HIZLI ERİŞİM
        middle_widget = QWidget()
        middle_layout = QHBoxLayout()
        middle_layout.setSpacing(20)

        # Sol: Mini graf önizleme
        graph_preview = self.create_graph_preview()
        middle_layout.addWidget(graph_preview, 40)  # %40 genişlik

        # Sağ: Hızlı başlatma butonları
        quick_actions = self.create_quick_actions()
        middle_layout.addWidget(quick_actions, 60)  # %60 genişlik

        middle_widget.setLayout(middle_layout)
        main_layout.addWidget(middle_widget)

        # 4. SON AKTİVİTELER VE SİSTEM DURUMU
        bottom_widget = self.create_bottom_panel()
        main_layout.addWidget(bottom_widget)

        self.setLayout(main_layout)
        self.setStyleSheet(self.get_stylesheet())

    def create_header(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # Ana başlık
        title_label = QLabel("SOSYAL AĞ ANALİZ PLATFORMU")
        title_label.setObjectName("mainTitle")

        # Açıklama
        desc_label = QLabel(
            "Üniversite sosyal ağınızı modelleyin, analiz edin ve görselleştirin. "
            "Graf algoritmaları ile bağlantıları keşfedin."
        )
        desc_label.setObjectName("descLabel")
        desc_label.setWordWrap(True)

        # Tarih ve saat
        time_label = QLabel(datetime.now().strftime("%d %B %Y | %H:%M"))
        time_label.setObjectName("timeLabel")

        layout.addWidget(title_label)
        layout.addWidget(desc_label)
        layout.addWidget(time_label)

        widget.setLayout(layout)
        return widget

    def create_stats_cards(self):
        widget = QWidget()
        layout = QHBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(0, 0, 0, 0)

        # İstatistik kartları
        cards_data = [
            {"title": "DÜĞÜMLER", "value": str(self.graph_data['node_count']),
             "icon": "🔵", "color": "#3498db", "desc": "Toplam kullanıcı"},
            {"title": "BAĞLANTILAR", "value": str(self.graph_data['edge_count']),
             "icon": "🔗", "color": "#2ecc71", "desc": "Toplam ilişki"},
            {"title": "TOPLULUKLAR", "value": str(self.graph_data['communities']),
             "icon": "👥", "color": "#e74c3c", "desc": "Bağlı bileşenler"},
            {"title": "AĞ YOĞUNLUĞU", "value": f"{self.graph_data['density']:.2%}",
             "icon": "📊", "color": "#f39c12", "desc": "Bağlantı yoğunluğu"}
        ]

        for card in cards_data:
            card_widget = self.create_stat_card(card)
            layout.addWidget(card_widget)

        widget.setLayout(layout)
        return widget

    def create_stat_card(self, data):
        widget = QWidget()
        widget.setObjectName("statCard")
        widget.setFixedHeight(120)

        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)

        # Üst satır: İkon ve başlık
        top_layout = QHBoxLayout()
        icon_label = QLabel(data["icon"])
        icon_label.setObjectName("cardIcon")

        title_label = QLabel(data["title"])
        title_label.setObjectName("cardTitle")

        top_layout.addWidget(icon_label)
        top_layout.addWidget(title_label)
        top_layout.addStretch()

        # Değer
        value_label = QLabel(data["value"])
        value_label.setObjectName("cardValue")

        # Açıklama
        desc_label = QLabel(data["desc"])
        desc_label.setObjectName("cardDesc")

        # Renk çubuğu (alt border)
        color_bar = QWidget()
        color_bar.setFixedHeight(4)
        color_bar.setStyleSheet(f"background-color: {data['color']}; border-radius: 2px;")

        layout.addLayout(top_layout)
        layout.addWidget(value_label)
        layout.addWidget(desc_label)
        layout.addStretch()
        layout.addWidget(color_bar)

        widget.setLayout(layout)
        return widget

    def create_graph_preview(self):
        widget = QWidget()
        widget.setObjectName("previewCard")
        widget.setMinimumHeight(250)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 15, 20, 15)

        # Başlık
        title = QLabel("GRAF ÖNİZLEME")
        title.setObjectName("previewTitle")
        layout.addWidget(title)

        # Canvas için widget
        canvas_widget = QWidget()
        canvas_widget.setObjectName("canvasWidget")
        canvas_widget.setMinimumHeight(180)

        # Buraya basit bir graf çizimi eklenebilir
        # Şimdilik boş bir widget kullanıyoruz
        layout.addWidget(canvas_widget)

        # Alt bilgi
        info_label = QLabel("Grafınızı düzenlemek için 'Graf Düzenle' butonuna tıklayın")
        info_label.setObjectName("previewInfo")
        layout.addWidget(info_label)

        widget.setLayout(layout)
        return widget

    def create_quick_actions(self):
        widget = QWidget()
        widget.setObjectName("actionsCard")

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 15, 20, 15)

        # Başlık
        title = QLabel("HIZLI BAŞLAT")
        title.setObjectName("actionsTitle")
        layout.addWidget(title)

        # Buton grid'i (3x2)
        grid_layout = QGridLayout()
        grid_layout.setSpacing(15)

        actions = [
            {"text": "📐 Graf Oluştur", "desc": "Yeni düğüm ve bağlantılar ekle",
             "color": "#3498db", "page": "graph"},
            {"text": "⚡ Algoritma Çalıştır", "desc": "BFS, Dijkstra, A* vb.",
             "color": "#2ecc71", "page": "algorithms"},
            {"text": "🎨 Görselleştir", "desc": "Renklendirme ve stil ayarları",
             "color": "#9b59b6", "page": "visualization"},
            {"text": "📊 Rapor Oluştur", "desc": "Analiz ve performans raporları",
             "color": "#e74c3c", "page": "reports"},
            {"text": "📁 Veri Yükle", "desc": "JSON/CSV dosyası içe aktar",
             "color": "#f39c12", "page": "import"},
            {"text": "⚙️ Ayarlar", "desc": "Sistem tercihlerini yapılandır",
             "color": "#34495e", "page": "settings"}
        ]

        for i, action in enumerate(actions):
            btn = self.create_action_button(action)
            row = i // 2
            col = i % 2
            grid_layout.addWidget(btn, row, col)

        layout.addLayout(grid_layout)
        layout.addStretch()

        widget.setLayout(layout)
        return widget

    def create_action_button(self, action):
        widget = QWidget()
        widget.setCursor(Qt.PointingHandCursor)
        widget.setObjectName("actionWidget")

        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)

        # Buton içeriği
        btn_layout = QHBoxLayout()

        icon_label = QLabel("●")
        icon_label.setStyleSheet(f"color: {action['color']}; font-size: 24px;")

        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)

        main_text = QLabel(action["text"])
        main_text.setObjectName("actionMainText")

        desc_text = QLabel(action["desc"])
        desc_text.setObjectName("actionDescText")

        text_layout.addWidget(main_text)
        text_layout.addWidget(desc_text)

        arrow_label = QLabel("➔")
        arrow_label.setObjectName("actionArrow")

        btn_layout.addWidget(icon_label)
        btn_layout.addLayout(text_layout)
        btn_layout.addStretch()
        btn_layout.addWidget(arrow_label)

        layout.addLayout(btn_layout)

        # Alt çizgi
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet(f"color: {action['color']};")

        layout.addWidget(line)
        widget.setLayout(layout)

        # Tıklama efekti
        def on_click():
            print(f"{action['page']} sayfasına geçiliyor...")
            QMessageBox.information(self, "Bilgi",
                                    f"'{action['text']}' özelliği aktif edilecek!\n"
                                    f"(Bu demo için sayfa geçişi henüz implement edilmedi)")

        widget.mousePressEvent = lambda e: on_click()

        return widget

    def create_bottom_panel(self):
        widget = QWidget()
        layout = QHBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(0, 0, 0, 0)

        # Sol: Son aktiviteler
        activities = self.create_activities_panel()
        layout.addWidget(activities, 60)

        # Sağ: Sistem durumu
        system_status = self.create_system_status()
        layout.addWidget(system_status, 40)

        widget.setLayout(layout)
        return widget

    def create_activities_panel(self):
        widget = QWidget()
        widget.setObjectName("activitiesCard")

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 15, 20, 15)

        # Başlık
        title_layout = QHBoxLayout()
        title = QLabel("SON AKTİVİTELER")
        title.setObjectName("activitiesTitle")

        refresh_btn = QPushButton("🔄 Yenile")
        refresh_btn.setObjectName("refreshBtn")
        refresh_btn.setCursor(Qt.PointingHandCursor)
        refresh_btn.clicked.connect(self.refresh_activities)

        title_layout.addWidget(title)
        title_layout.addStretch()
        title_layout.addWidget(refresh_btn)

        layout.addLayout(title_layout)

        # Aktivite listesi
        self.activities_list = [
            {"time": "10:30", "action": "Dijkstra algoritması çalıştırıldı", "user": "Ahmet"},
            {"time": "09:45", "action": "5 yeni düğüm eklendi", "user": "Mehmet"},
            {"time": "09:15", "action": "Welsh-Powell renklendirme uygulandı", "user": "Ayşe"},
            {"time": "08:30", "action": "CSV dosyasından veri yüklendi", "user": "Sistem"},
            {"time": "Dün 17:45", "action": "Bağlı bileşenler analizi yapıldı", "user": "Ali"}
        ]

        self.activities_layout = QVBoxLayout()
        self.activities_layout.setSpacing(5)

        for activity in self.activities_list:
            activity_widget = self.create_activity_item(activity)
            self.activities_layout.addWidget(activity_widget)

        layout.addLayout(self.activities_layout)
        layout.addStretch()
        widget.setLayout(layout)
        return widget

    def refresh_activities(self):
        """Aktivite listesini yeniler"""
        print("Aktivite listesi yenileniyor...")
        new_activity = {
            "time": datetime.now().strftime("%H:%M"),
            "action": "Sayfa yenileme işlemi yapıldı",
            "user": "Sistem"
        }
        self.activities_list.insert(0, new_activity)

        # Eski widget'ları temizle
        for i in reversed(range(self.activities_layout.count())):
            widget = self.activities_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Yenilerini ekle (en fazla 5 tane)
        for activity in self.activities_list[:5]:
            activity_widget = self.create_activity_item(activity)
            self.activities_layout.addWidget(activity_widget)

    def create_activity_item(self, activity):
        widget = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 5, 0, 5)

        # Zaman
        time_label = QLabel(activity["time"])
        time_label.setObjectName("activityTime")
        time_label.setFixedWidth(60)

        # Nokta
        dot = QLabel("•")
        dot.setStyleSheet("color: #3498db; font-size: 20px;")

        # Açıklama
        desc_label = QLabel(activity["action"])
        desc_label.setObjectName("activityDesc")

        # Kullanıcı
        user_label = QLabel(f"@{activity['user']}")
        user_label.setObjectName("activityUser")

        layout.addWidget(time_label)
        layout.addWidget(dot)
        layout.addWidget(desc_label)
        layout.addStretch()
        layout.addWidget(user_label)

        widget.setLayout(layout)
        return widget

    def create_system_status(self):
        widget = QWidget()
        widget.setObjectName("statusCard")

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 15, 20, 15)

        # Başlık
        title = QLabel("SİSTEM DURUMU")
        title.setObjectName("statusTitle")
        layout.addWidget(title)

        # Durum göstergeleri
        status_items = [
            {"label": "Graf Yüklenmiş", "status": True, "color": "#2ecc71"},
            {"label": "Veri Tabanı Bağlı", "status": True, "color": "#2ecc71"},
            {"label": "GPU Hızlandırma", "status": False, "color": "#e74c3c"},
            {"label": "Otomatik Kaydetme", "status": True, "color": "#2ecc71"},
            {"label": "Güncellemeler", "status": False, "color": "#f39c12"}
        ]

        for item in status_items:
            status_widget = self.create_status_item(item)
            layout.addWidget(status_widget)

        # İlerleme çubuğu (örnek)
        layout.addSpacing(10)
        progress_label = QLabel("Sistem Optimizasyonu")
        progress_label.setObjectName("progressLabel")
        layout.addWidget(progress_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(75)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFormat("%p% Tamamlandı")
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #34495e;
                border-radius: 5px;
                text-align: center;
                height: 20px;
            }
            QProgressBar::chunk {
                background-color: #3498db;
                border-radius: 3px;
            }
        """)
        layout.addWidget(self.progress_bar)

        # Optimize butonu
        optimize_btn = QPushButton("⚡ Optimize Et")
        optimize_btn.setObjectName("optimizeBtn")
        optimize_btn.setCursor(Qt.PointingHandCursor)
        optimize_btn.clicked.connect(self.optimize_system)
        layout.addWidget(optimize_btn)

        layout.addStretch()
        widget.setLayout(layout)
        return widget

    def optimize_system(self):
        """Sistem optimizasyon butonu"""
        from PyQt5.QtCore import QTimer
        print("Sistem optimizasyonu başlatılıyor...")

        # Progress bar'ı animasyonla doldur
        self.progress_bar.setValue(0)

        def update_progress():
            current = self.progress_bar.value()
            if current < 100:
                self.progress_bar.setValue(current + 10)
            else:
                timer.stop()
                QMessageBox.information(self, "Optimizasyon Tamamlandı",
                                        "Sistem başarıyla optimize edildi!\n"
                                        "Performans %25 arttırıldı.")

        timer = QTimer(self)
        timer.timeout.connect(update_progress)
        timer.start(200)  # 200ms aralıklarla

    def create_status_item(self, item):
        widget = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 5, 0, 5)

        # Durum noktası
        dot = QLabel("●" if item["status"] else "○")
        dot.setStyleSheet(f"color: {item['color']}; font-size: 16px;")

        # Etiket
        label = QLabel(item["label"])
        label.setObjectName("statusLabel")

        # Değer
        value = QLabel("AKTİF" if item["status"] else "PASİF")
        value.setStyleSheet(f"color: {item['color']}; font-weight: bold;")

        layout.addWidget(dot)
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(value)

        widget.setLayout(layout)
        return widget

    def get_stylesheet(self):
        return """
        /* Ana widget */
        QWidget {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', Arial, sans-serif;
        }

        /* Başlıklar */
        #mainTitle {
            font-size: 32px;
            font-weight: bold;
            color: #2c3e50;
            padding-bottom: 5px;
        }

        #descLabel {
            font-size: 14px;
            color: #7f8c8d;
            padding-bottom: 10px;
        }

        #timeLabel {
            font-size: 12px;
            color: #95a5a6;
            font-style: italic;
        }

        /* İstatistik kartları */
        #statCard {
            background-color: white;
            border-radius: 12px;
            border: 1px solid #e0e0e0;
        }

        #statCard:hover {
            border: 2px solid #3498db;
            transform: translateY(-2px);
        }

        #cardIcon {
            font-size: 24px;
        }

        #cardTitle {
            font-size: 11px;
            font-weight: bold;
            color: #7f8c8d;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        #cardValue {
            font-size: 32px;
            font-weight: bold;
            color: #2c3e50;
        }

        #cardDesc {
            font-size: 12px;
            color: #95a5a6;
        }

        /* Önizleme ve aksiyon kartları */
        #previewCard, #actionsCard, #activitiesCard, #statusCard {
            background-color: white;
            border-radius: 12px;
            border: 1px solid #e0e0e0;
        }

        #previewTitle, #actionsTitle, #activitiesTitle, #statusTitle {
            font-size: 14px;
            font-weight: bold;
            color: #2c3e50;
            padding-bottom: 10px;
            border-bottom: 2px solid #3498db;
        }

        #canvasWidget {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 8px;
            border: 1px solid #d0d0d0;
        }

        #previewInfo {
            font-size: 12px;
            color: #7f8c8d;
            font-style: italic;
            padding-top: 5px;
        }

        /* Aksiyon widget'ları */
        #actionWidget {
            background-color: #f8f9fa;
            border-radius: 8px;
            border: 1px solid transparent;
        }

        #actionWidget:hover {
            background-color: white;
            border: 1px solid #3498db;
            box-shadow: 0 4px 12px rgba(52, 152, 219, 0.2);
        }

        #actionMainText {
            font-size: 14px;
            font-weight: bold;
            color: #2c3e50;
        }

        #actionDescText {
            font-size: 11px;
            color: #7f8c8d;
        }

        #actionArrow {
            font-size: 18px;
            color: #bdc3c7;
        }

        #actionWidget:hover #actionArrow {
            color: #3498db;
        }

        /* Aktivite ve durum stilleri */
        #refreshBtn, #optimizeBtn {
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 8px 15px;
            font-size: 12px;
            font-weight: bold;
        }

        #refreshBtn:hover, #optimizeBtn:hover {
            background-color: #2980b9;
        }

        #activityTime {
            font-size: 11px;
            color: #95a5a6;
            font-family: 'Consolas', monospace;
        }

        #activityDesc {
            font-size: 13px;
            color: #34495e;
        }

        #activityUser {
            font-size: 11px;
            color: #3498db;
            font-weight: bold;
        }

        #statusLabel {
            font-size: 13px;
            color: #2c3e50;
        }

        #progressLabel {
            font-size: 12px;
            color: #7f8c8d;
            font-weight: bold;
        }
        """


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sosyal Ağ Analiz Platformu - Kocaeli Üniversitesi")
        self.setGeometry(100, 50, 1400, 900)

        # Modern tema için
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f2f5;
            }
        """)

        # Dashboard'u merkeze yerleştir
        self.dashboard = ModernDashboard(self)
        self.setCentralWidget(self.dashboard)

        # Menü çubuğu oluştur
        self.create_menu_bar()

        # Durum çubuğu
        self.statusBar().showMessage("✅ Sistem hazır - Hoş geldiniz!")

    def create_menu_bar(self):
        menubar = self.menuBar()

        # Dosya menüsü
        file_menu = menubar.addMenu('📂 Dosya')

        new_action = QAction('Yeni Proje', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new_project)

        open_action = QAction('Aç...', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)

        save_action = QAction('Kaydet', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)

        exit_action = QAction('Çıkış', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # Yardım menüsü
        help_menu = menubar.addMenu('❓ Yardım')

        about_action = QAction('Hakkında', self)
        about_action.triggered.connect(self.show_about)

        docs_action = QAction('Dokümantasyon', self)
        docs_action.triggered.connect(self.show_docs)

        help_menu.addAction(about_action)
        help_menu.addAction(docs_action)

    def new_project(self):
        QMessageBox.information(self, "Yeni Proje",
                                "Yeni bir sosyal ağ projesi oluşturulacak.")

    def open_file(self):
        QMessageBox.information(self, "Dosya Aç",
                                "Proje dosyası seçme ekranı açılacak.")

    def save_file(self):
        QMessageBox.information(self, "Kaydet",
                                "Proje kaydedilecek.")

    def show_about(self):
        about_text = """
        <h2>Sosyal Ağ Analiz Platformu</h2>
        <p><b>Versiyon:</b> 1.0.0</p>
        <p><b>Geliştirici:</b> Kocaeli Üniversitesi - Bilişim Sistemleri Mühendisliği</p>
        <p><b>Ders:</b> Yazılım Geliştirme Laboratuvarı-I</p>
        <p><b>Amaç:</b> Graf teorisi ve sosyal ağ analizi uygulamaları</p>
        <hr>
        <p>© 2025 - Tüm hakları saklıdır.</p>
        """
        QMessageBox.about(self, "Hakkında", about_text)

    def show_docs(self):
        QMessageBox.information(self, "Dokümantasyon",
                                "Dokümantasyon sayfası açılacak.")


def main():
    # PyQt5 uygulamasını başlat
    app = QApplication(sys.argv)

    # Uygulama stilini ayarla
    app.setStyle('Fusion')

    # Pencereyi oluştur ve göster
    window = MainWindow()
    window.show()

    # Uygulamayı çalıştır
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()