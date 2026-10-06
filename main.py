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
    .saint-box {
        background-color: #fcf6bd;
        padding: 1.2rem;
        border-radius: 8px;
        border-left: 4px solid #d4a373;
        margin-top: 1rem;
        color: #382c1e;
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

# Kapsamlı Namaz Veritabanı (Veli/Alim Görüşleri ve Güncellenmiş Cenaze Detayıyla)
NAMAZ_VERITABANI = {
    "Beş Vakit Namazlar": {
        "Sabah Namazı": {
            "hukum": "Sünnet-i Müekkede & Farz",
            "tur": "badge-farz",
            "rekat": "2 Rekat Sünnet + 2 Rekat Farz (Toplam 4 Rekat)",
            "kilinis": """
1. **Sabah Namazının Sünneti:** 
   * **1. Rekat:** Sübhaneke + Euzü-Besmele + Fatiha + Zammı Sure okunur, rüku ve secde yapılır.
   * **2. Rekat:** Besmele + Fatiha + Zammı Sure okunur, secdelerden sonra Tahiyyat, Salli-Barik ve Rabbena duaları ile selam verilir.
2. **Sabah Namazının Farzı:** 
   * İkamet getirilir. Sünnetin kılınışındaki tertiple aynı şekilde 2 rekat olarak kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>İsrâ Suresi, 17/78:</b> <i>"Güneşin batıya kaymasından... bir de sabah namazını kıl. Çünkü sabah namazı şahitlidir."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Teheccüd, 7; Müslim, Salatü'l-Müsafirîn, 96.<br>
            • <b>Fıkhi Dayanak:</b> Mergınani, <i>El-Hidaye</i>.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>İmam Gazâlî (k.s.)</b> şöyle buyurmuştur: <i>"Sabah namazının sünneti, dünya ve içindeki her şeyden daha hayırlıdır. Kulun güne Allah'ın zikriyle ve peygamberin sünnetine ittiba ederek başlaması, bütün gününün bereketini tayin eder."</i>"""
        },
        "Öğle Namazı": {
            "hukum": "Farz",
            "tur": "badge-farz",
            "rekat": "4 Rekat İlk Sünnet + 4 Rekat Farz + 2 Rekat Son Sünnet (Toplam 10 Rekat)",
            "kilinis": """
1. **İlk Sünnet (4 Rekat):** 
   * **1. ve 2. Rekat:** Fatiha ve zammı sure okunur. 2. rekat sonunda sadece Tahiyyat okunup ayağa kalkılır.
   * **3. ve 4. Rekat:** Sübhaneke okunmadan Fatiha ve zammı sure okunur, oturuşta Tahiyyat, Salli-Barik, Rabbena okunur.
2. **Farz (4 Rekat):** 
   * İlk iki rekatta Fatiha + zammı sure, son iki rekatta sadece Fatiha okunur.
3. **Son Sünnet (2 Rekat):** Sabah namazının sünneti gibi kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • Nîsâ Suresi, 4/103: <i>"...Şüphesiz namaz, müminler üzerine vakitleri belirlenmiş bir farzdır."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Tirmizî, Salat, 201; Ebû Dâvûd, Tatavvu, 3.<br>
            • <b>Fıkhi Dayanak:</b> Serahsî, <i>El-Mebsût</i>.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>Mevlânâ Celâleddîn-i Rûmî (k.s.):</b> <i>"Öğle vakti, dünyanın gürültüsünden ve meşgalelerinden kalbin bunaldığı andır. Öğle namazı ise ruha üflenen bir serinlik, hakiki bir dinlenme ve huzur limanıdır."</i>"""
        },
        "İkindi Namazı": {
            "hukum": "Farz",
            "tur": "badge-farz",
            "rekat": "4 Rekat Sünnet (Gayri Müekkede) + 4 Rekat Farz (Toplam 8 Rekat)",
            "kilinis": """
1. **Sünnet (4 Rekat):** 1. oturumda Tahiyyat'tan sonra Salli-Barik okunur, 3. rekata kalkıldığında Sübhaneke ile başlanır.
2. **Farz (4 Rekat):** Normal 4 rekatlı farz düzeninde kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • <b>Bakara Suresi, 2/238:</b> <i>"Namazlara ve orta namaza (ikindi namazına) devam edin..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Tirmizî, Salat, 201; Nesâî, İftitah, 17.<br>
            • <b>Fıkhi Dayanak:</b> Kasânî, <i>Bedâiü's-Sanâi</i>.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>İmam Rabbânî (k.s.):</b> <i>"İkindi namazı, günün telvesinde ve yorgunluğunda kulun mizan üzerindeki en büyük koruyucusudur. İkindi namazını hakkıyla kılan kimse, o günün meleklerinin hüsnü şehadetine nail olur."</i>"""
        },
        "Akşam Namazı": {
            "hukum": "Farz",
            "tur": "badge-farz",
            "rekat": "3 Rekat Farz + 2 Rekat Son Sünnet (Toplam 5 Rekat)",
            "kilinis": """
1. **Farz (3 Rekat):** 
   * **1. ve 2. Rekat:** Sesli kıraat yapılır; Fatiha ve zammı sure okunur. 2. rekat sonunda oturulup Tahiyyat okunur.
   * **3. Rekat:** Sadece Fatiha okunur. Rüku ve secdeyle tamamlanır.
2. **Son Sünnet (2 Rekat):** Normal nafile düzeninde kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • Vakit temeli İsrâ Suresi 78. ayet bağlamındadır.<br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Mevâkîtü'l-Salât; Taberânî.<br>
            • <b>Fıkhi Dayanak:</b> İbn Nüceym, <i>El-Bahrü'r-Râik</i>.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>Şah-ı Nakşibend (k.s.):</b> <i>"Güneşin batışı, gaflette olanlar için bir hüzün vakti iken; arifler için vefâ, hşû ve Rabb'e iltica vaktidir. Akşam namazı, günün muhasebesini yapıp kapıyı çalmaktır."</i>"""
        },
        "Yatsı Namazı": {
            "hukum": "Farz",
            "tur": "badge-farz",
            "rekat": "4 Rekat İlk Sünnet + 4 Rekat Farz + 2 Rekat Son Sünnet + 3 Rekat Vitir Vacip (Toplam 13 Rekat)",
            "kilinis": """
1. **İlk Sünnet ve Farz:** Öğle namazının sünnet ve farzları gibi kılınır.
2. **Son Sünnet (2 Rekat):** İki rekatlık sünnet düzeninde kılınır.
3. **Vitir Namazı (3 Rekat):** 3. rekatta Kunut tekbiri alınarak Kunut duaları (Kunut-1 ve Kunut-2) okunur.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • İsrâ Suresi 78. ayetin kapsamındadır.<br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Ebû Dâvûd, Vitir, 1; Tirmizî, Vitir, 1.<br>
            • <b>Fıkhi Dayanak:</b> Aliyyü'l-Kârî, <i>Fethu'b-Bab</i>.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>Abdülkâdir-i Geylânî (k.s.):</b> <i>"Yatsı namazı ve arkasından kılınan vitir, gece karanlığında kulun yalnızlığını gideren en mukaddes nurdur. Vitir namazını terk etmeyiniz; çünkü o, arşı ala ile bağ kuran özel bir ibadettir."</i>"""
        }
    },
    "Özel ve Mevsimsel Namazlar": {
        "Cuma Namazı": {
            "hukum": "Farz-ı Ayn",
            "tur": "badge-farz",
            "rekat": "10 Rekat (4 ilk sünnet + hutbe + 2 farz + 4 son sünnet)",
            "kilinis": """
1. **İlk Sünnet (4 Rekat):** Öğle namazının ilk sünneti gibi kılınır.
2. **Farz (2 Rekat):** Hutbe dinlenir. İmamın arkasından cemaatle sesli olarak Fatiha ve zammı sure okunan 2 rekat farz kılınır.
3. **Son Sünnet (4 Rekat):** Öğle namazının son sünneti tertibiyle tamamlanır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>Cuma Suresi, 62/9:</b> <i>"Ey iman edenler! Cuma günü namaza çağrıldığı zaman, hemen Allah’ı anmaya koşun..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Müslim, Cuma, 11; Ebû Dâvûd, Salat, 211.<br>
            • <b>Fıkhi Dayanak:</b> Diyanet İşleri Başkanlığı İlmihali.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>İmam Şafii (r.a.):</b> <i>"Cuma günü, müminlerin haftalık bayramıdır. Bu günde öyle bir an vardır ki, kul o anda dua ederse duası reddolunmaz. Cuma namazı, o günün ruhaniyetini kuşanma anahtarıdır."</i>"""
        },
        "Bayram Namazı": {
            "hukum": "Vâcip",
            "tur": "badge-vacip",
            "rekat": "2 Rekat (Ziyade tekbirlerle cemaatle kılınır)",
            "kilinis": """
1. **1. Rekat:** Sübhaneke'den sonra üç kez zevaid tekbiri alınır. İmam Fatiha ve zammı sure okur.
2. **2. Rekat:** İmamın kıraatinden sonra rükuya varmadan yine üç kez zevaid tekbiri alınır, dördüncü tekbirle rükuya varılır. Selam sonrası hutbe irad edilir.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>Kevser Suresi, 108/2:</b> <i>"Öyleyse Rabbin için namaz kıl ve kurban kes."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Nesâî, İdeyn, 2; İbn Mâce, İkâmet, 167.<br>
            • <b>Fıkhi Dayanak:</b> İbn Âbidîn, <i>Raddü'l-Muhtar</i>.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>Hasan-ı Basri (k.s.):</b> <i>"Bayram namazı, kulun Allah'ın ikramına nankörlük etmeyip, toplumla birlikte şükür meydanında buluştuğu en coşkulu kulluk nişanesidir."</i>"""
        },
        "Teravih Namazı": {
            "hukum": "Sünnet-i Müekkede",
            "tur": "badge-sunnet",
            "rekat": "20 Rekat (İkişer veya dörder rekatta bir kılınır)",
            "kilinis": """
Ramazan ayına mahsus, yatsı namazından sonra kılınan 20 rekatlık müekked sünnettir. 
* **Her Dört Rekat Sonundaki Dinlenme ve Dua (Tervihe):** Her 4 rekatın sonunda kısa bir süre oturulur, salavat getirilir ve Teravih Münacaat Duası okunur.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • Furkan Suresi 64: <i>"Onlar ki, geceler Rablerine secde ederek ve kıyam durarak dururlar..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, İman, 37; Müslim, Salatü'l-Müsafirîn, 174.<br>
            • <b>Fıkhi Dayanak:</b> Dört Mezhebin uygulamaları.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>İmam Zührî (r.a.):</b> <i>"Ramazan ayında teravih namazı, Kur'an'ın kalbe yerleşmesini sağlayan ve müminlerin ruhunu meleklerin seviyesine çıkaran mukaddes bir gecelik ibadet meclisidir."</i>"""
        },
        "Cenaze Namazı": {
            "hukum": "Farz-ı Kifâye",
            "tur": "badge-farz",
            "rekat": "Rüku ve secdesi olmayan 4 tekbirli namaz",
            "kilinis": """
Ayakta cemaatle kılınır. Rüku ve secdesi yoktur.
1. **1. Tekbir:** Sübhaneke duası ("ve celle senaüke" cümlesiyle) okunur.
2. **2. Tekbir:** Allâümme salli ve Allâümme bârik duaları okunur.
3. **3. Tekbir:** Cenaze duası okunur (Bilenler için özel cenaze duaları okunur; bilmeyenler için Kunut duaları veya Fatiha duası niyet edilerek okunabilir).
4. **4. Tekbir:** Bu tekbirden sonra doğrudan selam verilmez; **bilen kişilerin hem vefat eden mümin için hem de bütün ölmüş ve kalan müminler için içtenlikle af, mağfiret ve rahmet duası etmesi (müminlere ve merhuma hüsnü şehadette bulunulması) sünnettir/gereklidir.** Ardından sağa ve sola selam verilerek namaz tamamlanır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • Tevbe Suresi, 9/84 hükmü ve meşruiyet temellerine dayanır.<br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> İbn Mâce, Cenâiz, 33; Buhârî, Cenâiz, 65.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>İbrahim Ethem (k.s.):</b> <i>"Cenaze namazı, insana dünya hayatının sonunu hatırlatan en sessiz ve en tesirli vaazdır. Bir gün herkesin bu musalla taşında olacağı hakikatini kalbe nakşeder."</i>"""
        }
    },
    "Nafile ve Dilek Namazları": {
        "Teheccüd Namazı": {
            "hukum": "Nafile (Kuvvetli Sünnet)",
            "tur": "badge-nafile",
            "rekat": "2 ile 12 rekat arası (İkişer rekatta bir kılınması efdaldir)",
            "kilinis": """
Gece uykusundan uyandıktan sonra ikişer rekatta bir Fatiha ve dilediğiniz sureler okunarak kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayetler ve Mealleri:</b><br>
            • <b>İsrâ Suresi, 17/79:</b> <i>"Gecenin bir kısmında uyanıp, sadece sana mahsus bir nafile olarak namaz kıl..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Teheccüd, 1; Müslim, Salatü'l-Müsafirîn, 168.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>Hasan-ı Basri (k.s.):</b> <i>"Gecenin karanlığında kılınan teheccüd namazı, yüzde oluşan bir nur, kalpteki sönmez bir ışık ve ruhanîlerin fevkalade bir ziyafetidir."</i>"""
        },
        "Tesbih Namazı": {
            "hukum": "Müstehap / Faziletli Nafile",
            "tur": "badge-nafile",
            "rekat": "4 Rekat",
            "kilinis": """
Toplamda 300 tesbih ("Sübhânallâhi ve'l-hamdü lillâhi ve lâ ilâhe illallâhü vallâhü ekber") çekilen 4 rekatlık özel namazdır. Her rekatta 75 tesbih okunur.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • Tâhâ Suresi, 20/130: <i>"...Güneşin doğmasından ve batmasından önce Rabbini hamd ile tesbih et..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Ebû Dâvûd, Salat, 303; Tirmizî, Vitir, 19.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>Abdullah İbn Abbas (r.a.) / İslam Alimleri:</b> <i>"Tesbih namazı, büyük günahların affına vesile olan, kulun defterini nurlandıran en kıymetli nafile hazinelerinden biridir."</i>"""
        },
        "Evvâbîn Namazı": {
            "hukum": "Nafile",
            "tur": "badge-nafile",
            "rekat": "6 Rekat (İkişer rekatta bir kılınır)",
            "kilinis": """
Akşam namazının ardından ara vermeden ya da kısa bir fasıla ile ikişer rekatlık dilimler halinde 6 rekat kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • <b>İsrâ Suresi, 17/25:</b> <i>"...Şüphesiz o, evvâbîn (Allah'a çok dönenler) için çok bağışlayıcıdır."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Tirmizî, Salat, 431; İbn Mâce, İkâmet, 185.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>İmam Nevevî (r.h.):</b> <i>"Evvâbîn namazı, tövbe edenlerin ve kalbini daima Allah'a bağlayanların kıldığı pek faziletli bir taattir."</i>"""
        },
        "Duha (Kuşluk) Namazı": {
            "hukum": "Nafile",
            "tur": "badge-nafile",
            "rekat": "2, 4, 8 veya 12 rekat",
            "kilinis": """
Güneş doğup yükseldikten sonra öğleye kadar ikişer rekatlık dilimler halinde kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • Sâd Suresi, 38/18: <i>"...akşam vakti ve kuşluk vakti tesbih ederlerdi."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Müslim, Müsafirîn, 84; Buhârî, Teheccüd, 7.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>Ebû Hüreyre (r.a.):</b> <i>"Dostum Hz. Muhammed (s.a.v.) bana kuşluk namazını kılmamı vasiyet etti. Kuşluk namazı, rızkın bereketlenmesine ve kalbin inşirah bulmasına sebeptir."</i>"""
        },
        "İstihare Namazı": {
            "hukum": "Nafile",
            "tur": "badge-nafile",
            "rekat": "2 Rekat",
            "kilinis": """
Yatmadan önce 2 rekat kılınır, ardından özel İstihare Duası okunur.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • Âl-i İmrân Suresi, 3/159: <i>"...Karar verince de Allah'a güven..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Teheccüd, 25; Tirmizî, Vitir, 18.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>İmam Gazâlî (k.s.):</b> <i>"İstihare eden insan, kendi nefsinden vazgeçip işini Hak Teâlâ'nın iradesine teslim etmiştir. Bu teslimiyet kul için en hayırlı limandır."</i>"""
        },
        "Hacet Namazı": {
            "hukum": "Nafile",
            "tur": "badge-nafile",
            "rekat": "2, 4 veya 12 Rekat",
            "kilinis": """
Güzelce abdest alınıp 2 veya 4 rekat olarak kılınır, son oturuşta dualar edilerek selam verilir.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • Bakara Suresi, 2/45: <i>"Sabır ve namaz ile (Allah'tan) yardım dileyin..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Tirmizî, Vitir, 17; İbn Mâce, İkâmet, 189.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>Süfyan es-Sevrî (r.h.):</b> <i>"Dünyevi ya da uhrevi hangi hacetin olursa olsun, abdest alıp secdeye kapanan ve derdini O'na döken kul, asla hüsrana uğramaz."</i>"""
        },
        "Tahiyyetü'l-Mescid Namazı": {
            "hukum": "Müstehap",
            "tur": "badge-nafile",
            "rekat": "2 Rekat",
            "kilinis": """
Camiye girildiğinde oturmadan önce 2 rekat kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • Tevbe Suresi, 9/18: <i>"Allah'ın mescitlerini ancak Allah'a ve ahiret gününe inanan kimseler imar eder."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Salât, 60; Müslim, Salatü'l-Müsafirîn, 11.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>İmam Malik (r.h.):</b> <i>"Mescide hürmet, ev sahibinin huzuruna çıkarken iki rekatla selam vermektir."</i>"""
        },
        "Abdest ve Gusül Sünneti": {
            "hukum": "Müstehap",
            "tur": "badge-nafile",
            "rekat": "2 Rekat",
            "kilinis": """
Abdest veya gusül alındıktan hemen sonra 2 rekat nafile namaz kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • Mâide Suresi, 5/6: <i>"Ey iman edenler! Namaza kalkacağınız zaman yüzlerinizi, ellerinizi yıkayın..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Teheccüd, 17; Müslim, Fezâilü's-Sahâbe, 108.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>Bilal-i Habeşi (r.a.):</b> <i>"Ne zaman abdest alırsam, mutlaka arkasından elimden geldiğince namaz kılardım."</i> (Hz. Peygamber bu sünneti övmüştür)."""
        },
        "Tövbe Namazı": {
            "hukum": "Müstehap",
            "tur": "badge-nafile",
            "rekat": "2 Rekat",
            "kilinis": """
Abdest alınıp 2 rekat kılınır, ardından tesbih ve istiğfarlarla bağışlanma dilenir.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • Âl-i İmrân Suresi, 3/135: <i>"Ve onlar bir kötülük yaptıklarında ya da kendilerine zulmettiklerinde Allah'ı hatırlayıp günahlarından dolayı hemen bağışlanma dileyenlerdir..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Ebû Dâvûd, Vitir, 26; Tirmizî, Tefsir, 9.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>Bayezid-i Bestami (k.s.):</b> <i>"Tövbe, kulun günah kirinden arınarak Allah'ın kapısına yeniden tertemiz bir çocuk gibi dönmesidir."</i>"""
        },
        "Hûsûf ve Kûsûf Namazları": {
            "hukum": "Sünnet-i Müekkede",
            "tur": "badge-sunnet",
            "rekat": "2 Rekat (Cemaatle veya münferit kılınır)",
            "kilinis": """
Güneş veya ay tutulmasında kılınır. Her rekatta iki defa rükuya varmak sünnettir.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • Fussilet Suresi, 41/37: <i>"Gece, gündüz, güneş ve ay O'nun delillerindendir..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Buhârî, Küsûf, 2; Müslim, Küsûf, 1.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>İmam Şafiî (r.h.):</b> <i>"Kâinattaki bu muazzam ilahi ayetler karşısında müminin tavrı korku, dehşet ve secdeye kapanmaktır."</i>"""
        },
        "İstiskâ (Yağmur Duası) Namazı": {
            "hukum": "Sünnet",
            "tur": "badge-sunnet",
            "rekat": "2 Rekat (Bayram namazı gibi tekbirlerle cemaatle kılınır)",
            "kilinis": """
Açık alanda bayram namazı düzeninde zevaid tekbirleriyle cemaatle kılınır, ardından hutbe ve dua edilir.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Meali:</b><br>
            • A'râf Suresi, 7/57: <i>"Rahmetinin önünde müjdeleyici olarak rüzgarları gönderen O'dur..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Tirmizî, Cum'a, 41; Ebû Dâvûd, Salat, 245.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>Ömer bin Hattâb (r.a.):</b> <i>"Yağmur, gökten ancak kulların istiğfarı ve topluca yapılan yalvarışlarla iner."</i>"""
        },
        "Yolculuğa Çıkış ve Dönüş Namazı": {
            "hukum": "Müstehap",
            "tur": "badge-nafile",
            "rekat": "2 Rekat",
            "kilinis": """
Yolculuğa çıkmadan evde veya seyahatten dönünce ilk varılan yerde 2 rekat nafile namaz kılınır.
            """,
            "kaynak": """<b>📖 İlgili Ayet ve Genel Düzen:</b><br>
            • Zuhruf Suresi, 43/13-14: <i>"Üzerlerine kurulasınız diye, sonra da kurulduğunuz zaman Rabbinizin nimetini zikredesiniz..."</i><br><br>
            <b>📚 Hadis ve Fıkhi Dayanaklar:</b><br>
            • <b>Hadis Kaynakları:</b> Bezzâr, <i>El-Müsned</i>; Heysemî.""",
            "veli_sozu": """<b>🌟 Büyük Bir Veli/Alimin Görüşü:</b><br>
            • <b>İmam Âzam Ebû Hanife (r.h.):</b> <i>"Evden çıkarken ve eve dönerken iki rekat namaz kılmak, seyahatin selameti ve kalbin emniyeti için en güzel azıkdır."</i>"""
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
st.sidebar.info("💡 *Bilgi:* Sol menüden dilediğiniz kategoriyi seçip altındaki tüm nafile, farz ve özel namazların fıkhi detaylarına, ayetlerine ve alimlerin hikmetli sözlerine ulaşabilirsiniz.")

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
    <h4 style="color: #2d6a4f; margin-top: 1.5rem;">📖 Adım Adım Detaylı Kılınış ve Usul</h4>
</div>""", unsafe_allow_html=True)

# Kılınış Açıklamaları
st.markdown(namaz_detay['kilinis'])

# Veli/Alim Görüşü Bölümü
st.markdown(f"""
<div class="saint-box">
    {namaz_detay['veli_sozu']}
</div>
""", unsafe_allow_html=True)

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
    Bu yazılımda sunulan ibadet rehberi bilgileri, <b>Kur'an-ı Kerim Mealleri</b>, İslam fıkhının ana kaynakları olan <b>Kütüb-i Sitte</b> (Buhârî, Müslim, Ebû Dâvûd, Tirmizî, Nesâî, İbn Mâce), Hanefi fıkhının muteber metinleri (Merginani'nin <i>El-Hidaye</i>'si, Serahsî'nin <i>El-Mebsût</i>'ü, İbn Âbidîn'in <i>Raddü'l-Muhtar</i>'ı), Tasavvufi/Ahlaki eserler ve Diyanet İşleri Başkanlığı Din İşleri Yüksek Kurulu yayınları referans alınarak derlenmiştir. Açık kaynak kodlu ve eğitim/bilgilendirme amaçlıdır.
</div>
""", unsafe_allow_html=True)

# Altbilgi
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #8c8c8c; font-size: 0.85rem;'>"
    "Güvenilir Ayet, Hadis, Veli Sözleri ve Fıkhi Kaynaklar Esas Alınmıştır"
    "</div>", 
    unsafe_allow_html=True
)