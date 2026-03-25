import sqlite3

# Connect to database (creates if not exists)
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Drop old table
c.execute("DROP TABLE IF EXISTS monuments")

# Create updated monuments table with all 8 sub-marker fields + Hindi equivalents
c.execute("""
CREATE TABLE monuments (

    id           INTEGER PRIMARY KEY AUTOINCREMENT,

    name         TEXT,
    hi_name      TEXT,

    lat          REAL,
    lon          REAL,

    color        TEXT,

    image_url    TEXT,

    -- English content fields
    history      TEXT,
    secondary    TEXT,
    visitor      TEXT,
    experience   TEXT,
    nearby       TEXT,
    condition    TEXT,
    translation  TEXT,

    -- Hindi content fields
    hi_history      TEXT,
    hi_secondary    TEXT,
    hi_visitor      TEXT,
    hi_experience   TEXT,
    hi_nearby       TEXT,
    hi_condition    TEXT,
    hi_translation  TEXT

)
""")


# ── MONUMENT DATA ─────────────────────────────────────────────────────────────

data = [

    # ── 1. TOMB OF IMAM ZAMIN ──────────────────────────────────────────────────
    (
        # name, hi_name
        "Tomb of Imam Zamin",
        "इमाम ज़ामिन का मकबरा",

        # lat, lon
        28.5243,
        77.1852,

        # color (marker color on map)
        "#c47c1a",

        # image_url (comma-separated)
        "https://picsum.photos/600/400?random=10,https://picsum.photos/600/400?random=11,https://picsum.photos/600/400?random=12",

        # --- ENGLISH ---

        # history
        """Imam Zamin, whose real name was Muhammad Ali, was a Sufi saint and Islamic cleric who migrated 
        from Turkestan to Delhi around 1500 AD during the reign of Sultan Sikandar Lodi. He became the 
        chief imam (priest) of the Quwwat-ul-Islam mosque at the Qutb Minar complex. He was a direct 
        descendant of Prophet Muhammad and belonged to the Chishti sect of Sufism. He commissioned and 
        built his own tomb between 1537–1538 AD during the reign of Mughal Emperor Humayun, and was 
        buried there upon his death in 1538–1539 AD. It was the last structure added to the Qutb 
        Minar complex, a UNESCO World Heritage Site.""",

        # secondary
        """Primary scholarly references include: G.H.R. Tillotson, <em>Mughal India</em> (1990, Chronicle 
        Books, pp. 33–34); R. Nath, <em>Monuments of Delhi</em> (1979, Ambika Publications, p. 47); 
        and the <em>Epigraphia Indica</em> series published by the Archaeological Survey of India (ASI). 
        The inscription over the entrance doorway — written in the Naskh script — is a key primary 
        source confirming the construction date and the saint's identity. ASI conservation records 
        also document the stucco work and jali screens in detail.""",

        # visitor
        """Located inside the Qutb Minar Complex, Mehrauli, New Delhi — a UNESCO World Heritage Site. 
        Entry fee: ₹35 for Indian nationals, ₹250 for foreign tourists (as per ASI rates). 
        Timings: Open daily, sunrise to sunset (approximately 7:00 AM – 5:30 PM). 
        Nearest Metro: Qutb Minar Metro Station (Yellow Line) — approximately 800m walk. 
        Nearest Airport: Indira Gandhi International Airport (~10 km). 
        Photography is free; video recording charges may apply. 
        Best visited in the cooler months: October through March.""",

        # experience
        """Visitors often describe the tomb as a hidden gem overshadowed by the towering Qutb Minar 
        nearby. The perforated sandstone jali screens cast extraordinary geometric shadow patterns 
        inside the chamber in the afternoon light. Many visitors feel a sense of quiet spirituality 
        within the small interior, which retains its white polished plaster finish. The marble 
        cenotaph and mihrab on the western wall are frequently cited as the most beautiful details. 
        The tomb's elevated platform offers excellent views of the adjacent Alai Darwaza, making it 
        a favourite photography spot for those exploring the complex.""",

        # nearby
        """Within the Qutb Complex: Qutb Minar (UNESCO), Alai Darwaza, Quwwat-ul-Islam Mosque, 
        Iron Pillar, Iltutmish's Tomb, Alai Minar (unfinished). 
        Nearby attractions: Mehrauli Archaeological Park (~0.5 km), Balban's Tomb, Jamali Kamali 
        Mosque and Tomb (~1 km), Adham Khan's Tomb (~1 km), Dargah Qutb Sahib (~1 km). 
        Food & rest: Several cafes and dhabas in Mehrauli village; Saket Mall (~3 km) 
        for restaurants and shopping.""",

        # condition
        """The tomb is under the protection of the Archaeological Survey of India (ASI) and is 
        generally well maintained. The sandstone exterior retains original carved jali work on 
        three sides. Remnants of the original polished stucco coating are still visible. 
        The marble mihrab and cenotaph inside are intact. Some weathering to the sandstone 
        is evident on the outer dome and kangura (battlement) ornamentation. 
        Conservation work has been undertaken periodically by ASI to prevent further deterioration.""",

        # translation
        """The name "Imam Zamin" translates as: <em>Imam</em> — Islamic priest or leader of prayer; 
        <em>Zamin</em> — from Persian/Arabic, meaning "the one who stands surety" or "guarantor". 
        The inscription above the entrance doorway is written in the <strong>Naskh script</strong> 
        (a flowing Arabic calligraphic style). It records the saint's full name: 
        <em>Muhammad Ali Fakir Sayyid Imam Zamin</em>, and the construction date in the Islamic 
        Hijri calendar (943–944 AH), corresponding to 1537–1538 CE.""",


        # --- HINDI ---

        # hi_history
        """इमाम ज़ामिन, जिनका असली नाम मुहम्मद अली था, एक सूफ़ी संत और इस्लामी धर्मगुरु थे जो 
        लगभग 1500 ई. में सुल्तान सिकंदर लोदी के शासनकाल में तुर्किस्तान से दिल्ली आए। वे 
        क़ुतुब मीनार परिसर की क़ुव्वत-उल-इस्लाम मस्जिद के मुख्य इमाम बने। वे पैगंबर मुहम्मद 
        के प्रत्यक्ष वंशज थे और चिश्ती सूफ़ी सम्प्रदाय से संबंधित थे। उन्होंने मुग़ल बादशाह 
        हुमायूँ के शासनकाल में 1537–1538 ई. के बीच अपना मकबरा स्वयं बनवाया और 1538–1539 ई. 
        में अपनी मृत्यु के बाद यहीं दफ़नाए गए। यह यूनेस्को विश्व धरोहर स्थल, क़ुतुब मीनार 
        परिसर में जोड़ी गई अंतिम इमारत थी।""",

        # hi_secondary
        """प्रमुख विद्वत्तापूर्ण संदर्भ: जी.एच.आर. टिलॉटसन की <em>मुग़ल इंडिया</em> (1990); 
        आर. नाथ की <em>मॉन्युमेंट्स ऑफ़ दिल्ली</em> (1979, पृ. 47); तथा भारतीय पुरातत्व 
        सर्वेक्षण (ASI) द्वारा प्रकाशित <em>एपिग्राफिया इंडिका</em> श्रृंखला। प्रवेश द्वार 
        के ऊपर नस्ख़ लिपि में अंकित शिलालेख एक महत्त्वपूर्ण मूल स्रोत है जो निर्माण तिथि 
        और संत की पहचान की पुष्टि करता है।""",

        # hi_visitor
        """स्थान: क़ुतुब मीनार परिसर, महरौली, नई दिल्ली (यूनेस्को विश्व धरोहर स्थल)। 
        प्रवेश शुल्क: भारतीय नागरिकों के लिए ₹35, विदेशी पर्यटकों के लिए ₹250। 
        समय: प्रतिदिन सूर्योदय से सूर्यास्त तक (लगभग सुबह 7 बजे से शाम 5:30 बजे तक)। 
        निकटतम मेट्रो: क़ुतुब मीनार मेट्रो स्टेशन (यलो लाइन) — लगभग 800 मीटर। 
        निकटतम हवाई अड्डा: इंदिरा गांधी अंतर्राष्ट्रीय हवाई अड्डा (~10 किमी)। 
        अक्टूबर से मार्च के बीच यात्रा सबसे उपयुक्त है।""",

        # hi_experience
        """पर्यटक अक्सर इस मकबरे को क़ुतुब मीनार की छाया में छुपा हुआ एक अनमोल रत्न बताते हैं। 
        बलुआ पत्थर की जाली से दोपहर की रोशनी में अंदर पड़ने वाली ज्यामितीय छाया अद्भुत दृश्य 
        बनाती है। छोटे कक्ष के भीतर सफ़ेद पलस्तर और पश्चिमी दीवार पर संगमरमर की मेहराब 
        सबसे सुंदर विवरण माने जाते हैं। ऊँचे चबूतरे से अलाई दरवाज़े का दृश्य फ़ोटोग्राफ़ी 
        के लिए विशेष रूप से लोकप्रिय है।""",

        # hi_nearby
        """क़ुतुब परिसर में: क़ुतुब मीनार, अलाई दरवाज़ा, क़ुव्वत-उल-इस्लाम मस्जिद, 
        लौह स्तम्भ, इल्तुतमिश का मकबरा, अलाई मीनार (अधूरा)। 
        आस-पास के आकर्षण: महरौली पुरातत्व उद्यान (~0.5 किमी), बलबन का मकबरा, 
        जमाली कमाली मस्जिद एवं मकबरा (~1 किमी), आधम खान का मकबरा (~1 किमी)। 
        खान-पान: महरौली गाँव में कई कैफ़े व ढाबे; साकेत मॉल (~3 किमी)।""",

        # hi_condition
        """यह मकबरा भारतीय पुरातत्व सर्वेक्षण (ASI) के संरक्षण में है और सामान्यतः अच्छी 
        स्थिति में है। बलुआ पत्थर के बाहरी भाग पर तीन दिशाओं में मूल जाली कार्य संरक्षित है। 
        मूल पलस्तर के अवशेष अभी भी दिखाई देते हैं। भीतर संगमरमर की मेहराब और कब्र 
        सुरक्षित हैं। गुंबद और कंगूरा अलंकरण पर मौसम का प्रभाव दिखता है।""",

        # hi_translation
        """"इमाम ज़ामिन" का अर्थ: <em>इमाम</em> — नमाज़ का नेतृत्व करने वाला धर्मगुरु; 
        <em>ज़ामिन</em> — फ़ारसी/अरबी में "ज़मानत देने वाला" या "संरक्षक"। 
        प्रवेश द्वार के ऊपर का शिलालेख <strong>नस्ख़ लिपि</strong> में है और संत का 
        पूरा नाम <em>मुहम्मद अली फ़क़ीर सैय्यद इमाम ज़ामिन</em> तथा निर्माण वर्ष 
        इस्लामी हिजरी कैलेंडर में 943–944 हिजरी (1537–1538 ई.) दर्ज है।""",
    ),


    # ── 2. TOMB OF SHAH ALAM ───────────────────────────────────────────────────
    (
        # name, hi_name
        "Tomb of Shah Alam",
        "शाह आलम का मकबरा",

        # lat, lon (Wazirabad, Delhi — near Outer Ring Road & Loni Road intersection)
        28.7215,
        77.2341,

        # color
        "#7a5c2e",

        # image_url
        "https://picsum.photos/600/400?random=20,https://picsum.photos/600/400?random=21,https://picsum.photos/600/400?random=22",

        # --- ENGLISH ---

        # history
        """Shah Alam was a revered Sufi saint who rose to prominence during the reign of Feroze Shah 
        Tughlaq in the 14th century AD. The mausoleum was commissioned and built by Feroze Shah 
        Tughlaq himself in honour of the saint following his death — a rare gesture indicating the 
        saint's exceptional spiritual standing. The tomb is located in the Wazirabad locality, near 
        the banks of the Yamuna River, in northern Delhi. Historically, this area near Wazirabad is 
        significant as the site where the Central Asian conqueror Timur (Tamerlane) camped before 
        crossing the Yamuna River during his 1398 invasion of Delhi, making the tomb's surroundings 
        a layered historical landscape.""",

        # secondary
        """References include records from the <em>Archaeological Survey of India</em> (ASI) 
        listing the site as a protected monument of the Tughlaq period. The tomb is referenced in 
        Percy Brown's <em>Indian Architecture (Islamic Period)</em> and in Zafar Hasan's 
        <em>Monuments of Delhi</em> (Vol. IV). Local historical gazettes of the Delhi territory 
        from the colonial period also document the site. The associated nine-arched bridge over 
        the adjacent nullah (drain) is cited as one of Delhi's oldest surviving bridges, 
        constructed in rubble masonry to resist Yamuna flood waters.""",

        # visitor
        """Location: Wazirabad area, near the intersection of Outer Ring Road and Loni Road, 
        northern Delhi — close to the banks of the Yamuna River. 
        This is a lesser-visited monument; the site is often locked — carry contact details for 
        the ASI caretaker (chowkidar) or inquire locally before visiting. 
        No fixed entry fee as of last records; ASI protected site. 
        Best reached by cab or auto-rickshaw from the Timarpur or Wazirabad bus stands. 
        Nearest Metro: Tis Hazari or Kashmere Gate stations (then auto/cab, ~5–7 km). 
        Recommended visiting hours: Morning, 8 AM – 12 PM for best light and cooler temperatures.""",

        # experience
        """Shah Alam's Tomb is one of Delhi's quieter, more atmospheric historical sites — far 
        removed from tourist crowds. Visitors describe arriving at what feels like a medieval 
        enclave: partially worn structures, a three-domed mosque, and the square tomb set in a 
        courtyard. The stone jaali (latticework) screens of the women's prayer chamber are 
        considered remarkably well-preserved. The nine-arched bridge nearby adds to the sense 
        of stepping back in time. One reviewer noted that the monument had to be unlocked by 
        a caretaker, lending it an almost secret quality. The Yamuna riverbank setting creates 
        a peaceful, contemplative atmosphere.""",

        # nearby
        """Nearby historical sites: Coronation Durbar Memorial (~4 km north), 
        Pir Ghaib Observatory Hunting Lodge (~3 km), Flagstaff Tower (~3 km), 
        Qudsia Gardens (~5 km), Kashmere Gate (~6 km). 
        Nature: Wazirabad Barrage and Yamuna riverbank are within walking distance 
        — a quiet spot for birdwatching during winter migratory season. 
        Transport hubs: ISBT Kashmere Gate (~6 km). 
        Accommodation and dining options are available in Civil Lines (~5 km).""",

        # condition
        """The site is an ASI-protected monument but receives limited maintenance compared to 
        more prominent Delhi landmarks. The three-domed mosque structure is largely intact, 
        with five arches and two prayer chambers preserved. The women's chamber retains its 
        original stone jaali screens. The square tomb in the courtyard, set on a raised platform 
        supported by stone pillars, has some structural weathering. The nine-arched rubble 
        bridge is still standing but shows signs of age. The monument is often locked; a 
        caretaker manages access. Signage and visitor infrastructure are minimal.""",

        # translation
        """The name "Shah Alam" is a Persian title meaning <em>Shah</em> — King or Sovereign, 
        and <em>Alam</em> — World. Together: <strong>"King of the World"</strong> — a grand 
        Sufi honorific given to saints of the highest spiritual rank. The inscriptions at the 
        tomb are in <strong>Persian</strong>, the court and literary language of Sultanate and 
        Mughal-era India. The Tughlaq-era calligraphic style used is angular and formal, 
        contrasting with the more flowing Naskh style popular in later Mughal monuments. 
        The saint's full title reflects the Sufi tradition of attributing cosmic spiritual 
        authority to enlightened masters.""",


        # --- HINDI ---

        # hi_history
        """शाह आलम एक प्रतिष्ठित सूफ़ी संत थे जो 14वीं सदी में फ़िरोज़ शाह तुगलक के 
        शासनकाल में प्रसिद्ध हुए। उनकी मृत्यु के बाद फ़िरोज़ शाह तुगलक ने स्वयं यह 
        मकबरा बनवाया — संत की असाधारण आध्यात्मिक प्रतिष्ठा का प्रमाण। यह मकबरा 
        उत्तरी दिल्ली के वज़ीराबाद क्षेत्र में यमुना नदी के किनारे स्थित है। ऐतिहासिक 
        रूप से यह क्षेत्र महत्त्वपूर्ण है क्योंकि 1398 ई. में तैमूर (तिमूर लंग) ने 
        दिल्ली पर आक्रमण से पहले यहीं यमुना पार करने से पूर्व डेरा डाला था।""",

        # hi_secondary
        """संदर्भ: भारतीय पुरातत्व सर्वेक्षण (ASI) की तुगलक काल की संरक्षित इमारतों की 
        सूची; पर्सी ब्राउन की <em>इंडियन आर्किटेक्चर (इस्लामिक पीरियड)</em>; और 
        ज़फ़र हसन की <em>मॉन्युमेंट्स ऑफ़ दिल्ली</em> (खंड IV)। औपनिवेशिक काल के 
        दिल्ली क्षेत्र के ऐतिहासिक गज़ेटियर भी इस स्थल का उल्लेख करते हैं। पास की 
        नौ-मेहराब वाली पुल को दिल्ली का सबसे पुराना जीवित पुल माना जाता है।""",

        # hi_visitor
        """स्थान: वज़ीराबाद क्षेत्र, आउटर रिंग रोड और लोनी रोड के चौराहे के पास, 
        उत्तरी दिल्ली। 
        यह एक कम-भ्रमण स्थल है; अक्सर बंद रहता है — ASI के चौकीदार से संपर्क करें। 
        प्रवेश शुल्क: अंतिम जानकारी के अनुसार नि:शुल्क (ASI संरक्षित)। 
        पहुँचने का तरीका: तिमारपुर या वज़ीराबाद बस स्टैंड से ऑटो/कैब। 
        निकटतम मेट्रो: तीस हज़ारी या कश्मीरी गेट (~5–7 किमी, फिर ऑटो)। 
        भ्रमण का सर्वोत्तम समय: सुबह 8 से 12 बजे।""",

        # hi_experience
        """शाह आलम का मकबरा दिल्ली के शांत और वातावरण-प्रधान ऐतिहासिक स्थलों में से 
        एक है — पर्यटकों की भीड़ से बिल्कुल दूर। आगंतुक बताते हैं कि यहाँ पहुँचना 
        किसी मध्यकालीन परिसर में प्रवेश जैसा लगता है: तीन-गुंबद वाली मस्जिद, आँगन 
        में चौकोर मकबरा और महिला नमाज़ कक्ष की पत्थर की जाली। पास की नौ-मेहराब 
        वाली पुल इस अनुभव को और भी ऐतिहासिक बना देती है। यमुना के किनारे की 
        शांत सेटिंग आत्ममंथन के लिए आदर्श है।""",

        # hi_nearby
        """आस-पास के ऐतिहासिक स्थल: कोरोनेशन दरबार स्मारक (~4 किमी उत्तर), 
        पीर गैब वेधशाला (~3 किमी), फ़्लैगस्टाफ़ टावर (~3 किमी), 
        क़ुदसिया बाग़ (~5 किमी), कश्मीरी गेट (~6 किमी)। 
        प्रकृति: वज़ीराबाद बैराज और यमुना तट पास में हैं — सर्दियों में 
        प्रवासी पक्षी देखने का अच्छा स्थान। 
        आवास व भोजन: सिविल लाइंस (~5 किमी) में उपलब्ध।""",

        # hi_condition
        """यह स्थल ASI-संरक्षित है लेकिन प्रमुख दिल्ली स्मारकों की तुलना में 
        इसका रखरखाव सीमित है। तीन-गुंबद वाली मस्जिद की पाँच मेहराबें और दो 
        नमाज़ कक्ष मुख्यतः सुरक्षित हैं। महिला कक्ष की जाली संरक्षित है। 
        आँगन में पत्थर के खंभों पर टिका चौकोर मकबरा कुछ मौसमी क्षरण दिखाता है। 
        नौ-मेहराब वाला पुल खड़ा है पर जर्जर है। स्मारक अक्सर बंद रहता है 
        और सूचना-पट्ट की भारी कमी है।""",

        # hi_translation
        """"शाह आलम" एक फ़ारसी उपाधि है: <em>शाह</em> — राजा या शासक, 
        <em>आलम</em> — संसार या जगत। मिलकर: <strong>"जगत का राजा"</strong> — 
        उच्चतम आध्यात्मिक दर्जे के सूफ़ी संतों को दी जाने वाली भव्य उपाधि। 
        मकबरे के शिलालेख <strong>फ़ारसी भाषा</strong> में हैं — सल्तनत और 
        मुग़लकालीन भारत की दरबारी भाषा। तुगलक-काल की लिपि शैली कोणीय और 
        औपचारिक है, जो बाद के मुग़ल स्मारकों की प्रवाहमयी नस्ख़ शैली से 
        भिन्न है।""",
    ),

]


# ── INSERT ─────────────────────────────────────────────────────────────────────

c.executemany("""
INSERT INTO monuments (
    name, hi_name,
    lat, lon,
    color,
    image_url,
    history, secondary, visitor, experience, nearby, condition, translation,
    hi_history, hi_secondary, hi_visitor, hi_experience, hi_nearby, hi_condition, hi_translation
)
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
""", data)

conn.commit()
conn.close()

print("✅ Database created successfully with Tomb of Imam Zamin and Tomb of Shah Alam.")