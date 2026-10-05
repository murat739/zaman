import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Namaz Rehberi",
    page_icon="🕌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Profesyonel CSS Tasarımı
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    .title-text {
        font-size: 2.2rem;
        color: #1b4332;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .subtitle-text {
        font-size: 1.1rem;
        color: #52796f;
        margin-bottom: 2rem;
    }
    .card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.5rem;
        border-left: 5px solid #2d6a4f;
    }
    .source-box {
        background-color: #e9f5ed;
        padding: 1.2rem;
        border-radius: 8px;
        border-left: 4px solid #52b788;
        margin-top: 1rem;
        color: #2d3748;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    .bibliography-box {
        background-color: #f1f3f5;
        padding: 1.2rem;
        border-radius: 8px;
        border-left: 4px solid #495057;
        margin-top: 2rem;
        color: #343a40;
        font-size: 0.9rem;
    }
    .badge-farz { background-color: #d8f3dc; color: #1b4332; padding: 4px 10px; border-radius: 12px; font-weight: 600; font-size: 0.85rem; }
    .badge-vacip { background-color: #faedcd; color: #856404; padding: 4px 10px; border-radius: 12px; font-weight: 600; font-size: 0.85rem; }
    .badge-sunnet { background-color: #e2ece9; color: #2d6a4f; padding: 4px 10px; border-radius: 12px; font-weight: 600; font-size: 0.85rem; }
    .badge-nafile { background-color: #f1f3f5; color: #495057; padding: 4px 10px; border-radius: 12px; font-weight: 600; font-size: 0.85rem; }
    </style>
""", unsafe_allow_html=True)

# Kapsamlı Namaz Veritabanı (Teravih Namazı Detaylandırıldı)
NAMAZ_VERITABANI = {
    "Beş Vakit Namazlar": {
        "Sabah Namazı": {
            "hukum": "Sünnet-i Müekkede & Farz",
            "tur": "badge-farz",
            "rekat": "2 Rekat Sünnet + 2 Rekat Farz (Toplam 4 Rekat)",
            "kilinis": """
1. **Sabah Namazının Sünneti:** 
   * **1. Rekat:** Sübhaneke + Euzü-Besmele + Fatiha + Zammı Sure (örn. Fil ve Kureyş süreleri) okunur, rüku ve secde yapılır.
   * **2. Rekat:** Besmele + Fatiha + Zammı Sure okunur, rüku ve secdeden sonra Tahiyyat, Salli-Barik ve Rabbena duaları ile selam verilir.
2. **Sabah Namazının Farzı:** 
   * İkamet getirilir. Sünnetin kılınışındaki tertiple aynı şekilde 2 rekat olarak kılınır (Fatiha ve zammı sure okunur).
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>İsrâ Suresi, 17/78:</b> <i>"Güneşin batıya kaymasından, gecenin kararmasına kadar (belli vakitlerde) namaz kıl; bir de sabah namazını kıl. Çünkü sabah namazı şahitlidir (melekler tarafından şahitlik edilir)."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Teheccüd, 7; Müslim, Salatü'l-Müsafirîn, 96.<br>
            • <b>Fıkhi Dayanak (Hanefi):</b> Mergınani, <i>El-Hidaye</i>; İbn Abidin, <i>Raddü'l-Muhtar</i>."""
        },
        "Öğle Namazı": {
            "hukum": "Farz",
            "tur": "badge-farz",
            "rekat": "4 Rekat İlk Sünnet + 4 Rekat Farz + 2 Rekat Son Sünnet (Toplam 10 Rekat)",
            "kilinis": """
1. **İlk Sünnet (4 Rekat):** 
   * **1. ve 2. Rekat:** Fatiha ve zammı sure okunur. 2. rekat sonunda sadece Tahiyyat okunup ayağa kalkılır.
   * **3. ve 4. Rekat:** Sübhaneke okunmadan Euzü-Besmele çekilerek Fatiha ve zammı sure okunur, rüku-secde tamamlanıp oturulur (Tahiyyat, Salli-Barik, Rabbena).
2. **Farz (4 Rekat):** 
   * İlk iki rekatta Fatiha ve zammı sure okunur. 3. ve 4. rekatlarda ise sadece Besmele ile Fatiha okunur (zammı sure eklenmez).
3. **Son Sünnet (2 Rekat):** Sabah namazının sünneti gibi kılınarak tamamlanır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • Vakitlerin tayini genel olarak İsrâ Suresi 78. ayet ve Nîsâ Suresi 103. ayetteki (*"...Şüphesiz namaz, müminler üzerine vakitleri belirlenmiş bir farzdır."*) hükümlere dayanır.<br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Tirmizî, Salat, 201; Ebû Dâvûd, Tatavvu, 3.<br>
            • <b>Fıkhi Dayanak:</b> Serahsî, <i>El-Mebsût</i>."""
        },
        "İkindi Namazı": {
            "hukum": "Farz",
            "tur": "badge-farz",
            "rekat": "4 Rekat Sünnet (Gayri Müekkede) + 4 Rekat Farz (Toplam 8 Rekat)",
            "kilinis": """
1. **Sünnet (4 Rekat):** Öğle namazının ilk sünneti gibi kılınır; ancak 1. oturumda Tahiyyat'tan sonra Salli-Barik duaları da okunur ve 3. rekata kalkıldığında baştan Sübhaneke okunarak başlanır. Fatiha ve zammı sure okunur.
2. **Farz (4 Rekat):** Öğle namazının farzı gibi 4 rekat olarak kılınır (İlk iki rekatta Fatiha + zammı sure, son iki rekatta yalnızca Fatiha).
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • <b>Bakara Suresi, 2/238:</b> <i>"Namazlara ve orta namaza (ikindi namazına) devam edin; gönülden boyun eğerek Allah için kalkıp namaza durun."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Tirmizî, Salat, 201; Nesâî, İftitah, 17.<br>
            • <b>Fıkhi Dayanak:</b> Kasânî, <i>Bedâiü's-Sanâi</i>."""
        },
        "Akşam Namazı": {
            "hukum": "Farz",
            "tur": "badge-farz",
            "rekat": "3 Rekat Farz + 2 Rekat Son Sünnet (Toplam 5 Rekat)",
            "kilinis": """
1. **Farz (3 Rekat):** 
   * **1. ve 2. Rekat:** Sesli (cehren) kıraat yapılır; Fatiha ve zammı sure okunur. 2. rekat sonunda oturulup sadece Tahiyyat okunur ve 3. rekata kalkılır.
   * **3. Rekat:** Sadece Besmele ve Fatiha okunur, zammı sure okunmaz. Rüku ve secde yapılarak oturulur ve tamamlanır.
2. **Son Sünnet (2 Rekat):** 2 rekatlık normal nafile düzeninde kılınarak tamamlanır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • Vakit temeli İsrâ Suresi 78. ayet bağlamındadır.<br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Taberânî, <i>El-Mu'cemü'l-Kebîr</i>; Buhârî, Mevâkîtü'l-Salât.<br>
            • <b>Fıkhi Dayanak:</b> İbn Nüceym, <i>El-Bahrü'r-Râik</i>."""
        },
        "Yatsı Namazı": {
            "hukum": "Farz",
            "tur": "badge-farz",
            "rekat": "4 Rekat İlk Sünnet + 4 Rekat Farz + 2 Rekat Son Sünnet + 3 Rekat Vitir Vacip (Toplam 13 Rekat)",
            "kilinis": """
1. **İlk Sünnet ve Farz:** Öğle namazının sünnet ve farzları gibi kılınır. Farzda ilk iki rekatta kıraat açıktan (cehren) yapılır (Fatiha ve zammı sure).
2. **Son Sünnet (2 Rekat):** İki rekatlık sünnet düzeninde kılınır.
3. **Vitir Namazı (3 Rekat):** 
   * **1. ve 2. Rekat:** Fatiha ve zammı sure okunur, 2. rekat sonunda oturulup sadece Tahiyyat okunur ve 3. rekata kalkılır.
   * **3. Rekat:** Fatiha ve zammı sure okunur. Rükuya varmadan önce eller kulaklara kaldırılarak tekbir alınır (Kunut Tekbiri) ve eller bağlanarak Kunut Duaları (Kunut-1 ve Kunut-2) okunur, ardından rüku ve secdelerle namaz tamamlanır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • Gece karanlığının bastırmasıyla giren yatsı vakti, İsrâ Suresi 78. ayetin kapsamındadır.<br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Ebû Dâvûd, Vitir, 1; Tirmizî, Vitir, 1.<br>
            • <b>Fıkhi Dayanak:</b> Aliyyü'l-Kârî, <i>Fethu'b-Bab</i>."""
        }
    },
    "Özel ve Mevsimsel Namazlar": {
        "Cuma Namazı": {
            "hukum": "Farz-ı Ayn",
            "tur": "badge-farz",
            "rekat": "10 Rekat (4 ilk sünnet + hutbe + 2 farz + 4 son sünnet)",
            "kilinis": """
1. **İlk Sünnet (4 Rekat):** Öğle namazının ilk sünneti gibi kılınır.
2. **Farz (2 Rekat):** Hatip minbere çıkıp hutbe irad eder. Hutbe bittikten sonra imamın arkasından cemaatle sesli (cehren) olarak Fatiha ve zammı sure okunan 2 rekat Cuma farzı kılınır.
3. **Son Sünnet (4 Rekat):** Öğle namazının son sünneti/ilk sünneti tertibiyle kılınarak tamamlanır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>Cuma Suresi, 62/9:</b> <i>"Ey iman edenler! Cuma günü namaza çağrıldığı (ezan okunduğu) zaman, hemen Allah’ı anmaya koşun ve alışverişi bırakın..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Müslim, Cuma, 11; Ebû Dâvûd, Salat, 211.<br>
            • <b>Fıkhi Dayanak:</b> Diyanet İşleri Başkanlığı İlmihali."""
        },
        "Bayram Namazı": {
            "hukum": "Vâcip",
            "tur": "badge-vacip",
            "rekat": "2 Rekat (Ziyade tekbirlerle cemaatle kılınır)",
            "kilinis": """
1. **1. Rekat:** Niyet edilir, imama uyularak iftitah tekbiri alınır ve Sübhaneke okunur. Ardından imamla birlikte eller kulaklara kaldırılarak üç kez zevaid tekbiri alınır (ilk ikisinde eller yanlara salınır, üçüncüsünde bağlanır). İmam gizli/açık Fatiha ve zammı sure okur, rüku ve secde yapılır.
2. **2. Rekat:** Ayağa kalkıldığında imam Fatiha ve zammı sure okur. Rükuya varmadan önce yine üç kez zevaid tekbiri alınır, dördüncü tekbirle rükuya varılır. Selam sonrasında hatip minbere çıkarak hutbe irad eder.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>Kevser Suresi, 108/2:</b> <i>"Öyleyse Rabbin için namaz kıl ve kurban kes."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Nesâî, İdeyn, 2; İbn Mâce, İkâmet, 167.<br>
            • <b>Fıkhi Dayanak:</b> İbn Âbidîn, <i>Raddü'l-Muhtar</i>."""
        },
        "Teravih Namazı": {
            "hukum": "Sünnet-i Müekkede",
            "tur": "badge-sunnet",
            "rekat": "20 Rekat (İkişer veya dörder rekatta bir kılınır)",
            "kilinis": """
Ramazan ayına mahsus, yatsı namazından sonra (vitir namazından önce veya sonra) kılınan 20 rekatlık müekked sünnettir. 

* **Genel Tertip ve Sure Düzenleri:**
  1. **İkişer Rekatta Bir Kılınış (Efdal Olan):** Her iki rekatta bir selam verilerek toplam 10 kez ikişer rekat kılınır. Her rekatta Fatiha'dan sonra Kur'an hatmi yapılıyorsa cüz sırasıyla, hatim yapılmıyorsa sırasıyla Fil suresinden Nas suresine kadar olan kısa sureler (veya Fil-Fil, Fil-Kureyş gibi tertipler ya da Âyetel Kürsi, İhlas vb.) okunur.
  2. **Dörder Rekatta Bir Kılınış:** Dileyenler dörder rekatta bir de selam verebilir (Öğlenin ilk sünneti gibi kılınır, 2. rekat sonunda Tahiyyat için oturulur, 3. rekata kalkınca Sübhaneke okunur).

* **Her Dört Rekat Sonundaki Dinlenme ve Dua (Tervihe):**
  * Teravih namazında her 4 rekatın sonunda kısa bir süre oturulur (istirahat edilir). Bu aralarda salavat getirilir, ilahiler okunur veya şu meşhur **Teravih Duası (Münacaat)** seslendirilir:
    <i>"Sübhâne zî'l-mülki ve'l-melekût... Sübhâne zî'l-izzeti ve'l-azameti ve'l-kudreti ve'l-kibriyâi ve'l-ceberût..."</i> (Ey mülk ve melekûtun sahibi Allah'ım, seni her türlü noksanlıktan tenzih ederim...)

* **Cemaatle ve Münferit Kılınış:**
  * Camilerde cemaatle kılınırken imam ayakta açıktan (cehren) kıraat eder. Evde tek başına (münferit) kılacak olan kimse de aynı şekilde Fatiha ve sureleri açıktan veya içinden okuyarak 20 rekatı tamamlayabilir. Ardından yatsının vitir namazı cemaatle veya münferit olarak kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • Gece ibadetlerini teşvik eden genel ayetler (Furkan Suresi 64: <i>"Onlar ki, geceler Rablerine secde ederek ve kıyam durarak dururlar..."</i>) kapsamındadır.<br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, İman, 37; Müslim, Salatü'l-Müsafirîn, 174.<br>
            • <b>Fıkhi Dayanak:</b> Dört Mezhebin uygulamaları ve Hanefi fıkhı muteber kaynakları."""
        },
        "Cenaze Namazı": {
            "hukum": "Farz-ı Kifâye",
            "tur": "badge-farz",
            "rekat": "Rüku ve secdesi olmayan 4 tekbirli namaz",
            "kilinis": """
Ayakta cemaatle kılınır. Rüku ve secdesi yoktur.
1. **1. Tekbir:** Sübhaneke duası ("ve celle senaüke" cümlesiyle) okunur.
2. **2. Tekbir:** Allâümme salli ve Allâümme bârik duaları okunur.
3. **3. Tekbir:** Cenaze duası (Bilenler için özel cenaze duaları, bilmeyenler için Kunut duaları veya Fatiha duası niyetiyle okunur).
4. **4. Tekbir:** Hiçbir şey okunmadan doğrudan sağa ve sola selam verilerek tamamlanır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • <b>Tevbe Suresi, 9/84</b> hükmü ve meşruiyet temellerine dayanır.<br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> İbn Mâce, Cenâiz, 33; Buhârî, Cenâiz, 65."""
        }
    },
    "Nafile ve Dilek Namazları": {
        "Teheccüd Namazı": {
            "hukum": "Nafile (Kuvvetli Sünnet)",
            "tur": "badge-nafile",
            "rekat": "2 ile 12 rekat arası (İkişer rekatta bir kılınması efdaldir)",
            "kilinis": """
Gece uykusundan uyandıktan sonra kılınır. Her iki rekatta bir Fatiha ve dilediğiniz sureler okunarak selam verilir, dileyen sonuna vitir ekler.
            """,
            "kaynak": """<b>📖 İlgili Ayetler ve Mealleri:</b><br>
            • <b>İsrâ Suresi, 17/79:</b> <i>"Gecenin bir kısmında uyanıp, sadece sana mahsus bir nafile olarak namaz kıl..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Teheccüd, 1; Müslim, Salatü'l-Müsafirîn, 168."""
        },
        "Tesbih Namazı": {
            "hukum": "Müstehap / Faziletli Nafile",
            "tur": "badge-nafile",
            "rekat": "4 Rekat",
            "kilinis": """
Toplamda 300 tesbih çekilen 4 rekatlık özel namazdır. Her rekatta şu tertiple 75 tesbih ("Sübhânallâhi ve'l-hamdü lillâhi ve lâ ilâhe illallâhü vallâhü ekber") okunur:
1. Sübhaneke'den sonra **15 defa**
2. Fatiha ve zammı sureden sonra rükuya varmadan **10 defa**
3. Rükuda tesbihten sonra **10 defa**
4. Rükudan kalkınca (kavmede) **10 defa**
5. Birinci secdede tesbihten sonra **10 defa**
6. İki secde arasındaki oturuşta (celsede) **10 defa**
7. İkinci secdede tesbihten sonra **10 defa**
(Bu tertip 4 rekat boyunca tekrarlanır).
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • <b>Tâhâ Suresi, 20/130:</b> <i>"...Güneşin doğmasından ve batmasından önce Rabbini hamd ile tesbih et..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Ebû Dâvûd, Salat, 303; Tirmizî, Vitir, 19."""
        },
        "Evvâbîn Namazı": {
            "hukum": "Nafile",
            "tur": "badge-nafile",
            "rekat": "6 Rekat (İkişer rekatta bir kılınır)",
            "kilinis": """
Akşam namazının ardından ara vermeden ya da kısa bir fasıla ile ikişer rekatlık dilimler halinde Fatiha ve zammı sureler okunarak 6 rekat kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>İsrâ Suresi, 17/25:</b> <i>"...Şüphesiz o, evvâbîn (Allah'a çok dönenler) için çok bağışlayıcıdır."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Tirmizî, Salat, 431; İbn Mâce, İkâmet, 185."""
        },
        "Duha (Kuşluk) Namazı": {
            "hukum": "Nafile",
            "tur": "badge-nafile",
            "rekat": "2, 4, 8 veya 12 rekat",
            "kilinis": """
Güneş doğup yükseldikten sonra öğleye kadar ikişer rekatlık dilimler halinde Fatiha ve dilediğiniz sureler okunarak kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>Sâd Suresi, 38/18:</b> <i>"...akşam vakti ve kuşluk vakti tesbih ederlerdi."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Müslim, Müsafirîn, 84; Buhârî, Teheccüd, 7."""
        },
        "İstihare Namazı": {
            "hukum": "Nafile",
            "tur": "badge-nafile",
            "rekat": "2 Rekat",
            "kilinis": """
Yatmadan önce Fatiha ve dilediğiniz surelerle (örneğin 1. rekatta Kafirun, 2. rekatta İhlas sureleri) 2 rekat kılınır, ardından özel İstihare Duası okunur.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • <b>Âl-i İmrân Suresi, 3/159:</b> <i>"...Gezip dolaştığın zaman (işinde) onlarla istişare et; karar verince de Allah'a güven..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Teheccüd, 25; Tirmizî, Vitir, 18."""
        },
        "Hacet Namazı": {
            "hukum": "Nafile",
            "tur": "badge-nafile",
            "rekat": "2, 4 veya 12 Rekat",
            "kilinis": """
Güzelce abdest alınıp Fatiha ve dilediğiniz surelerle (genellikle 2 veya 4 rekat olarak) kılınır, son oturuşta dualar edilerek selam verilir.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>Bakara Suresi, 2/45:</b> <i>"Sabır ve namaz ile (Allah'tan) yardım dileyin..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Tirmizî, Vitir, 17; İbn Mâce, İkâmet, 189."""
        },
        "Tahiyyetü'l-Mescid Namazı": {
            "hukum": "Müstehap",
            "tur": "badge-nafile",
            "rekat": "2 Rekat",
            "kilinis": """
Camiye girildiğinde oturmadan önce Fatiha ve kolayınıza gelen surelerle 2 rekat kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>Tevbe Suresi, 9/18:</b> <i>"Allah'ın mescitlerini ancak Allah'a ve ahiret gününe inanan... kimseler imar eder."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Salât, 60; Müslim, Salatü'l-Müsafirîn, 11."""
        },
        "Abdest ve Gusül Sünneti": {
            "hukum": "Müstehap",
            "tur": "badge-nafile",
            "rekat": "2 Rekat",
            "kilinis": """
Abdest veya gusül alındıktan hemen sonra 2 rekat nafile namaz kılınır (Fatiha ve sureler okunur).
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>Mâide Suresi, 5/6:</b> <i>"Ey iman edenler! Namaza kalkacağınız zaman yüzlerinizi, ellerinizi dirseklere kadar yıkayın..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Teheccüd, 17; Müslim, Fezâilü's-Sahâbe, 108."""
        },
        "Tövbe Namazı": {
            "hukum": "Müstehap",
            "tur": "badge-nafile",
            "rekat": "2 Rekat",
            "kilinis": """
Abdest alınıp Fatiha ve dilediğiniz sureler okunarak 2 rekat kılınır, ardından tesbih ve istiğfarlarla bağışlanma dilenir.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>Âl-i İmrân Suresi, 3/135:</b> <i>"Ve onlar bir kötülük yaptıklarında ya da kendilerine zulmettiklerinde Allah'ı hatırlayıp günahlarından dolayı hemen bağışlanma dileyenlerdir..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Ebû Dâvûd, Vitir, 26; Tirmizî, Tefsir (Sûre 3), 9."""
        },
        "Hûsûf ve Kûsûf Namazları": {
            "hukum": "Sünnet-i Müekkede",
            "tur": "badge-sunnet",
            "rekat": "2 Rekat (Cemaatle veya münferit kılınır)",
            "kilinis": """
Güneş veya ay tutulmasında kılınır. Normal namazlardan farklı olarak her rekatta iki defa rükuya varmak (uzun kıraat ve uzun rükularla) sünnettir. Fatiha ve uzun sureler okunur.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>Fussilet Suresi, 41/37:</b> <i>"Gece, gündüz, güneş ve ay O'nun delillerindendir..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Küsûf, 2; Müslim, Küsûf, 1."""
        },
        "İstiskâ (Yağmur Duası) Namazı": {
            "hukum": "Sünnet",
            "tur": "badge-sunnet",
            "rekat": "2 Rekat (Bayram namazı gibi tekbirlerle cemaatle kılınır)",
            "kilinis": """
Açık alanda bayram namazı düzeninde (fazladan zevaid tekbirleriyle, Fatiha ve zammı sureler okunarak) cemaatle kılınır, ardından hutbe ve dua edilir.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>A'râf Suresi, 7/57:</b> <i>"Rahmetinin önünde müjdeleyici olarak rüzgarları gönderen O'dur..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Tirmizî, Cum'a, 41; Ebû Dâvûd, Salat, 245."""
        },
        "Yolculuğa Çıkış ve Dönüş Namazı": {
            "hukum": "Müstehap",
            "tur": "badge-nafile",
            "rekat": "2 Rekat",
            "kilinis": """
Yolculuğa çıkmadan evde veya seyahatten dönünce ilk varılan yerde Fatiha ve dilediğiniz sureler okunarak 2 rekat nafile namaz kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • <b>Zuhruf Suresi, 43/13-14:</b> <i>"Üzerlerine kurulasınız diye, sonra da kurulduğunuz zaman Rabbinizin nimetini zikredesiniz..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Bezzâr, <i>El-Müsned</i>; Heysemî, <i>Mecmeu'z-Zevâid</i>."""
        }
    }
}

# Yan Menü (Sol Taraf) Yapılandırması
st.sidebar.markdown("### 🕌 Namaz Rehberi")
st.sidebar.markdown("---")

kategori_secimi = st.sidebar.radio(
    "Namaz Kategorisi Seçiniz:",
    list(NAMAZ_VERITABANI.keys())
)

st.sidebar.markdown("---")
namaz_secimi = st.sidebar.radio(
    "İlgili Namazı Seçiniz:",
    list(NAMAZ_VERITABANI[kategori_secimi].keys())
)

st.sidebar.markdown("---")
st.sidebar.info("💡 *Bilgi:* Sol menüden dilediğiniz kategoriyi seçip altındaki tüm özel ve nafile namaz çeşitlerine, sure düzenlerine ulaşabilirsiniz.")

# Ana Ekran (Sağ Taraf) İçerik Alanı
st.markdown('<p class="title-text">🕌 Profesyonel İslam İbadet ve Namaz Rehberi</p>', unsafe_allow_html=True)
st.markdown(f'<p class="subtitle-text">Seçilen Kategori: <b>{kategori_secimi}</b> &nbsp;|&nbsp; Seçilen Namaz: <span style="color: #2d6a4f; font-weight: bold;">{namaz_secimi}</span></p>', unsafe_allow_html=True)

# Seçilen Namaz Bilgilerini Çekme
namaz_detay = NAMAZ_VERITABANI[kategori_secimi][namaz_secimi]

# Kart Yapısı İçerisinde Detayları Gösterme
st.markdown(f"""<div class="card">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <h2 style="margin: 0; color: #1b4332;">{namaz_secimi}</h2>
        <span class="{namaz_detay['tur']}">{namaz_detay['hukum']}</span>
    </div>
    <hr style="margin: 0.5rem 0 1rem 0; border: none; border-top: 1px solid #eaeaea;">
    <h4 style="color: #2d6a4f; margin-top: 1.0rem;">📌 Rekat ve Vakit Bilgisi</h4>
    <p style="font-size: 1.05rem; font-weight: 500; color: #334155;">{namaz_detay['rekat']}</p>
    <h4 style="color: #2d6a4f; margin-top: 1.5rem;">📖 Adım Adım Detaylı Kılınış, Sure ve İstirahat Düzeni</h4>
</div>""", unsafe_allow_html=True)

# Kılınış Açıklamaları (Teravih detaylarıyla)
st.markdown(namaz_detay['kilinis'])

# Kaynaklar, Ayetler ve Deliller Bölümü
st.markdown("### 📚 Ayet Mealleri, Fıkhi Dayanak ve Hadis Kaynakları")
st.markdown(f"""
<div class="source-box">
    {namaz_detay['kaynak']}
</div>
""", unsafe_allow_html=True)

# Genel Kaynakça ve Telif/Metodoloji Bilgi Kutusu
st.markdown("""
<div class="bibliography-box">
    <b>📚 Genel Kaynakça ve Telif Metodolojisi:</b><br>
    Bu yazılımda sunulan ibadet rehberi bilgileri, <b>Kur'an-ı Kerim Mealleri</b>, İslam fıkhının ana kaynakları olan <b>Kütüb-i Sitte</b> (Buhârî, Müslim, Ebû Dâvûd, Tirmizî, Nesâî, İbn Mâce), Hanefi fıkhının muteber metinleri (Merginani'nin <i>El-Hidaye</i>'si, Serahsî'nin <i>El-Mebsût</i>'ü, İbn Âbidîn'in <i>Raddü'l-Muhtar</i>'ı) ve Diyanet İşleri Başkanlığı Din İşleri Yüksek Kurulu yayınları referans alınarak derlenmiştir. Açık kaynak kodlu ve eğitim/bilgilendirme amaçlıdır.
</div>
""", unsafe_allow_html=True)

# Altbilgi
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #8c8c8c; font-size: 0.85rem;'>"
    "Güvenilir Ayet, Hadis, Teravih Usulleri ve Fıkhi Kaynaklar Esas Alınmıştır"
    "</div>", 
    unsafe_allow_html=True
)