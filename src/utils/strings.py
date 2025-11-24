# All user-facing strings for the Štefan pet bot (Czech, cute tone)

class CSStrings:
    # Generic
   ERROR_GENERIC = "Hoppá, valami elromlott. Kérlek, próbáld meg újra később. 🙈"
    NO_CHANNEL = "Nem találom a **#pets** csatornát. Kérlek, hozd létre, vagy állítsd be az ID-t a `config.json`-ban. 🛠️"
    NICK_SET_OK = "Új nevem van: **Štefan**. 🐠✨"
    STATUS_TITLE = "🫧 Akvárium állapota – jelentés Štefantól"
    YES = "Igen"
    NO = "Nem"

    # Feeding
    FEED_STARTS = [
        "Hééé srácok, már éhes vagyok! 🍽️🐟 Kérlek, **etetnétek meg**.",
        "Wassuuup, Štefan vagyok. Poci korog... kaja? 😇🐠",
        "Hallóó, szakácsok! Éhes vagyok, mint egy harcsa. 😤 Evés után azonnal elhallgatok, ígérem.",
        "Sziasztok, bandi! Készen állok a szemcsés all-you-can-eatre. 😎",
        "Kéééérem, csak pár szemcse és én leszek a legboldogabb hal az akváriumban! (pedig egyedül vagyok itt ...)🥺💧",
        "Figyi, ha nem kapok finomságot, elkezdem enni a dekorációt. Nem fogom kétszer elmondani. 😬",
        "Főnök, nyitva a konyha? Jövök a részemért! 🐟✨",
        "Jó napot, a mai specialitást rendelem — haltáp a Séfkonyhájából. 🍽️",
        "Filip, te vagy a legközelebb. Etess meg, kérlek. 😉",
        "Héé te pöcs, adjál enni, te. 🔪🐟",
        "Cső arcok, szórjátok a tápot, különben szétrugdosom a kavicsot. 💥",
        "More cigányok, ne idegesítsetek, már rég meg kellett volna ezt csinálni. 😠🔪",
        "Hej négerek, kajáááááát ... 😇😇😇"
    ]
    FEED_THANKS = [
        "Köszi, {mention}! Most már boldog kishal vagyok. 🐠💚",
        "{mention}, te vagy a hősöm. Tele vagyok és boldog! 😋",
        "Megetetve! {mention}, küldök egy buborékos puszit. 💋🫧",
        "Respekt, {mention}. Ez egy luxus menü volt. 😎🍽️",
        "Nagyon köszönöm, {mention}! Elmegyek egy ebéd utáni szundira. 💤",
        "Finomság megerősítve. {mention}, van nálam egy plusz pontod! ✅",
        "Jó üzlet, {mention}. Megkajáltam, kvittek vagyunk. 🫡💼"
    ]
    FEED_ALREADY = "Ma már ettem... De kösziiiii 😋"
    FEED_REMINDERS = [
        "Öööö... még mindig **nem ettem**. Hallóóó? 🥺",
        "Ki akartok éheztetni? Én hal vagyok, nem kaktusz! 😤",
        "Oké ... elkezdem enni a dekorációt... 😬",
        "Figyi te pöcs, ha nem kapok kaját, nagyon dühös leszek. 😠",
        "Ti felelőtlen faszok, egyikőtök szedje össze magát és azonnal hozza ide azt a kaját!!! 😠",
        "Tudjátok mit, húzzatok le a WC-n ..."
    ]

    # Filter cleaning (weekly)
    FILTER_ASSIGN = "🧽 **Szűrő tisztítás**: {assignee} te vagy soron. ✅ ha kész, ❌ ha gyenge vagy."
    FILTER_DONE = "✅ Köszi, {mention}! A szűrő tiszta, mint egy hegyi patak. 🏔️"
    FILTER_REMINDER = "Öööö... a szűrő magától nem tisztul meg. {assignee}, kérlek? 🧽"

    # Tank cleaning (monthly)
    TANK_ASSIGN = "🫧 **Nagytakarítás**: {assignee}, ma van a te napod! ✅ ha kész, ❌ meleg vagy :)"
    TANK_DONE = "✅ {mention} kitisztította az akváriumot! Tükröződhetek a falban. ✨"
    TANK_REMINDER = "Öööö... és az akvárium még mindig nem. {assignee}, kérlek? 🪣"

    # Admin / commands
    VACATION_ON = "✈️ {mention} most **szabadságon** van – kihagyom a rotációból."
    VACATION_OFF = "🏠 {mention} **visszatért** – visszateszem a rotációba."
    STATUS_FEED = "Etetés ma: {done}"
    STATUS_FILTER = "Szűrő (heti): hozzárendelve {assignee} • kész: {done}"
    STATUS_TANK = "Akvárium (havi): hozzárendelve {assignee} • kész: {done}"
