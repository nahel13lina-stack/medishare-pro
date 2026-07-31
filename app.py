import customtkinter as ctk
import os
import urllib.parse
from datetime import datetime, timezone

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

CLE_ADMIN_SECRET = "ADMIN2026"
CLE_PRO_VALIDE = "PRO2026"
LIMIT_PARTICULIER = 3

TRADUCTIONS = {
    "Français": {
        "title": "🩺 MediShare Pro - Solidarité & Matériel Médical",
        "account_type_lbl": "👤 Type de Compte :",
        "acc_types": ["🙋 Particulier (3 gratuites max)", "🏢 Professionnel / Entreprise (Abonnement Pro)", "👑 Administrateur (Gestion App)"],
        "key_lbl": "🔑 Clé d'accès (Pro ou Admin) :",
        "key_ph": "Entrez votre clé...",
        "badge_pro": "⭐ PRO VÉRIFIÉ",
        "badge_boost": "⚡ À LA UNE (PREMIUM)",
        "req_lbl": "👤 Nom / Raison sociale :",
        "req_ph": "Ex: Amel Goudali, Pharmacie...",
        "contact_lbl": "📧 Email / 📞 N° WhatsApp :",
        "contact_ph": "Ex: 213612345678 ou 0612345678",
        "cat_lbl": "📦 Catégorie de matériel :",
        "cats": [
            "🩹 Orthopédie & Maintien (Attelles...)",
            "♿ Mobilité & Autonomie (Béquilles...)",
            "🛏️ Lits médicalisés & Accessoires",
            "🫁 Assistance Respiratoire (Concentrateur O2...)",
            "🩺 Suivi & Diagnostic (Tensiomètre...)",
            "🛠️ Autre matériel"
        ],
        "nom_lbl": "🏥 Nom & Modèle du matériel :",
        "nom_ph": "Ex: Concentrateur d'oxygène 5L, Fauteuil roulant...",
        "desc_lbl": "📝 Description détaillée (État, détails) :",
        "desc_ph": "Ex: État parfait, fourni avec masque...",
        "type_lbl": "🤝 Type de publication :",
        "types": ["🎁 Offre - Don gratuit", "🤝 Offre - Prêt solidaire", "🏷️ Offre - Cession / Prix abordable", "💼 Offre - Vente/Location Pro", "🚨 RECHERCHE URGENTE (Besoin d'aide)"],
        "price_lbl": "💶 Prix / Conditions :",
        "price_ph": "Ex: Gratuit, Sur devis...",
        "loc_lbl": "📍 Localisation (Ville, Pays) :",
        "loc_ph": "Ex: Maghnia (Algérie), Oran...",
        "stat_lbl": "🚦 Statut de disponibilité :",
        "stats": ["🟢 Disponible immédiat", "🟡 En cours de prêt", "🔴 Non disponible / Clôturé", "🚨 Recherche active / Urgence"],
        "btn_save": "💾 Publier l'annonce",
        "btn_clear": "🗑️ Réinitialiser tout",
        "btn_buy_extra": "💳 Pack Extra / RIB",
        "inv_lbl": "📋 Annonces publiées (Mise en relation WhatsApp) :",
        "empty": "Aucune annonce pour le moment.",
        "err_key": "❌ Clé d'accès invalide !",
        "pro_banner": "💼 Espace Solidaire & Santé : Mise en relation directe via WhatsApp 💬.",
        "security_note": "🛡️ Sécurité : MediShare Pro encourage le don et le prêt solidaire sans intermédiaire financier non vérifié."
    },
    "العربية": {
        "title": "🩺 MediShare Pro - التضامن والمعدات الطبية",
        "account_type_lbl": "👤 نوع الحساب :",
        "acc_types": ["🙋 فردي (3 مجاناً كحد أقصى)", "🏢 مهني / شركة (اشتراك متميز)", "👑 مدير التطبيق (Espace Admin)"],
        "key_lbl": "🔑 مفتاح الدخول (مهني أو مدير) :",
        "key_ph": "أدخل المفتاح...",
        "badge_pro": "⭐ مهني موثوق",
        "badge_boost": "⚡ مميز (في الصدارة)",
        "req_lbl": "👤 الاسم / اسم الشركة :",
        "req_ph": "مثال: أمينة، صيدلية الأمل...",
        "contact_lbl": "📧 البريد / 📞 رقمواتساب :",
        "contact_ph": "مثال: 213612345678 أو 0612345678",
        "cat_lbl": "📦 الفئة :",
        "cats": [
            "🩹 تقويم العظام والدعم",
            "♿ التنقل والاستقلالية",
            "🛏️ أسرة طبية ومستلزماتها",
            "🫁 المساعدة على التنفس",
            "🩺 المتابعة والتشخيص",
            "🛠️ معدات أخرى"
        ],
        "nom_lbl": "🏥 اسم / نوع المعدات :",
        "nom_ph": "مثال: عكازات، جهاز قياس الضغط...",
        "desc_lbl": "📝 الوصف التفصيلي :",
        "desc_ph": "مثال: الجهاز في حالة ممتازة...",
        "type_lbl": "🤝 نوع المنشور :",
        "types": ["🎁 عرض - تبرع مجاني", "🤝 عرض - إعارة تضامنية", "🏷️ عرض - تنازل بسعر مناسب", "💼 عرض - بيع/تأجير مهني", "🚨 بحث عاجل (طلب مساعدة)"],
        "price_lbl": "💶 السعر / الشروط :",
        "price_ph": "مثال: مجاني، عاجل...",
        "loc_lbl": "📍 الموقع (المدينة، الدولة) :",
        "loc_ph": "مثال: مغنية (الجزائر)...",
        "stat_lbl": "🚦 حالة التوفر :",
        "stats": ["🟢 متوفر حاليا", "🟡 قيد الإعارة", "🔴 غير متوفر / مغلق", "🚨 بحث نشط / عاجل"],
        "btn_save": "💾 نشر الإعلان",
        "btn_clear": "🗑️ إعادة ضبط",
        "btn_buy_extra": "💳 حزمة إعلان / حساب بنكي",
        "inv_lbl": "📋 الإعلانات المسجلة (تواصل مباشر عبرواتساب) :",
        "empty": "لا توجد إعلانات حالياً.",
        "err_key": "❌ مفتاح الدخول غير صحيح!",
        "pro_banner": "💼 منصة التضامن الطبي: التواصل المباشر والسريع عبر واتساب 💬.",
        "security_note": "🛡️ أمان: يشجع التطبيق التبرع والإعارة التضامنية المباشرة بدون وسطاء."
    },
    "English": {
        "title": "🩺 MediShare Pro - Solidarity & Medical Equipment",
        "account_type_lbl": "👤 Account Type:",
        "acc_types": ["🙋 Individual (3 free max)", "🏢 Professional / Business (Pro Plan)", "👑 Administrator (App Management)"],
        "key_lbl": "🔑 Access Key (Pro or Admin):",
        "key_ph": "Enter your key...",
        "badge_pro": "⭐ VERIFIED PRO",
        "badge_boost": "⚡ FEATURED (PREMIUM)",
        "req_lbl": "👤 Name / Company:",
        "req_ph": "Ex: Amel Goudali, Pharmacy...",
        "contact_lbl": "📧 Email / 📞 WhatsApp Number:",
        "contact_ph": "Ex: 213612345678",
        "cat_lbl": "📦 Equipment Category:",
        "cats": [
            "🩹 Orthopedics & Support",
            "♿ Mobility & Autonomy",
            "🛏️ Medical Beds & Accessories",
            "🫁 Respiratory Assistance",
            "🩺 Monitoring & Diagnostics",
            "🛠️ Other Equipment"
        ],
        "nom_lbl": "🏥 Equipment Name & Model:",
        "nom_ph": "Ex: Oxygen Concentrator 5L, Wheelchair...",
        "desc_lbl": "📝 Detailed Description:",
        "desc_ph": "Ex: Perfect condition, comes with mask...",
        "type_lbl": "🤝 Publication Type:",
        "types": ["🎁 Offer - Free Donation", "🤝 Offer - Solidarity Loan", "🏷️ Offer - Affordable Price", "💼 Offer - Pro Sale/Rental", "🚨 URGENT SEARCH (Help Needed)"],
        "price_lbl": "💶 Price / Conditions:",
        "price_ph": "Ex: Free, On request...",
        "loc_lbl": "📍 Location (City, Country):",
        "loc_ph": "Ex: Maghnia (Algeria), Oran...",
        "stat_lbl": "🚦 Availability Status:",
        "stats": ["🟢 Immediate availability", "🟡 On loan", "🔴 Not available / Closed", "🚨 Active search / Urgent"],
        "btn_save": "💾 Publish Listing",
        "btn_clear": "🗑️ Reset All",
        "btn_buy_extra": "💳 Extra Pack / Bank Details",
        "inv_lbl": "📋 Published Listings (WhatsApp Direct Contact):",
        "empty": "No listings at the moment.",
        "err_key": "❌ Invalid access key!",
        "pro_banner": "💼 Health & Solidarity Space: Direct connection via WhatsApp 💬.",
        "security_note": "🛡️ Security: MediShare Pro encourages donations and solidarity loans without unverified financial intermediaries."
    },
    "Español": {
        "title": "🩺 MediShare Pro - Solidaridad y Material Médico",
        "account_type_lbl": "👤 Tipo de Cuenta:",
        "acc_types": ["🙋 Particular (3 gratis máx)", "🏢 Profesional / Empresa (Plan Pro)", "👑 Administrador (Gestión de App)"],
        "key_lbl": "🔑 Clave de acceso (Pro o Admin):",
        "key_ph": "Introduce tu clave...",
        "badge_pro": "⭐ PRO VERIFICADO",
        "badge_boost": "⚡ DESTACADO (PREMIUM)",
        "req_lbl": "👤 Nombre / Empresa:",
        "req_ph": "Ej: Amel Goudali, Farmacia...",
        "contact_lbl": "📧 Email / 📞 N° de WhatsApp:",
        "contact_ph": "Ej: 213612345678",
        "cat_lbl": "📦 Categoría de material:",
        "cats": [
            "🩹 Ortopedia y Soporte",
            "♿ Movilidad y Autonomía",
            "🛏️ Camas médicas y accesorios",
            "🫁 Asistencia Respiratoria",
            "🩺 Seguimiento y Diagnóstico",
            "🛠️ Otro material"
        ],
        "nom_lbl": "🏥 Nombre y Modelo del material:",
        "nom_ph": "Ej: Concentrador de oxígeno 5L, Silla de ruedas...",
        "desc_lbl": "📝 Descripción detallada:",
        "desc_ph": "Ej: Estado perfecto, incluye mascarilla...",
        "type_lbl": "🤝 Tipo de publicación:",
        "types": ["🎁 Oferta - Donación gratuita", "🤝 Oferta - Préstamo solidario", "🏷️ Oferta - Precio asequible", "💼 Oferta - Venta/Alquiler Pro", "🚨 BÚSQUEDA URGENTE (Ayuda necesaria)"],
        "price_lbl": "💶 Precio / Condiciones:",
        "price_ph": "Ej: Gratis, A consultar...",
        "loc_lbl": "📍 Ubicación (Ciudad, País):",
        "loc_ph": "Ej: Maghnia (Argelia), Oran...",
        "stat_lbl": "🚦 Estado de disponibilidad:",
        "stats": ["🟢 Disponible de inmediato", "🟡 En préstamo", "🔴 No disponible / Cerrado", "🚨 Búsqueda activa / Urgente"],
        "btn_save": "💾 Publicar anuncio",
        "btn_clear": "🗑️ Borrar todo",
        "btn_buy_extra": "💳 Paquete Extra / RIB",
        "inv_lbl": "📋 Anuncios publicados (Contacto directo por WhatsApp):",
        "empty": "No hay anuncios por el momento.",
        "err_key": "❌ ¡Clave de acceso no válida!",
        "pro_banner": "💼 Espacio de Salud y Solidaridad: Conexión directa vía WhatsApp 💬.",
        "security_note": "🛡️ Seguridad: MediShare Pro fomenta la donación y el préstamo solidario sin intermediarios financieros no verificados."
    }
}

extras_achetes = {}
infos_paiement = {
    "titulaire": "MME GOUDALI AMEL",
    "rip_ccp": "00799999004471253133",
    "badr_eur": "521001299320184",
    "badr_agence": "521 (BADR Bank)"
}

app = ctk.CTk()
app.title("MediShare Pro")
app.geometry("620x860")

scroll_container = ctk.CTkScrollableFrame(app, width=580, height=830)
scroll_container.pack(padx=10, pady=10, fill="both", expand=True)

top_frame = ctk.CTkFrame(scroll_container, fg_color="transparent")
top_frame.pack(fill="x", padx=10, pady=5)

title_label = ctk.CTkLabel(top_frame, text="🩺 MediShare Pro", font=("Arial", 16, "bold"), text_color="#1a5276")
title_label.pack(side="left")

option_langue = ctk.CTkOptionMenu(top_frame, values=["Français", "العربية", "English", "Español"], width=130, height=28, font=("Arial", 11, "bold"))
option_langue.pack(side="right")

pro_banner_frame = ctk.CTkFrame(scroll_container, fg_color="#d4efdf", corner_radius=6)
pro_banner_frame.pack(padx=5, pady=4, fill="x")
lbl_pro_banner = ctk.CTkLabel(pro_banner_frame, text="", font=("Arial", 10, "italic"), text_color="#196f3d", wraplength=540)
lbl_pro_banner.pack(padx=8, pady=6)

frame = ctk.CTkFrame(scroll_container, fg_color="#ebf5fb")
frame.pack(padx=5, pady=5, fill="x")

lbl_acc_type = ctk.CTkLabel(frame, text="", font=("Arial", 12, "bold"), text_color="#1b4f72")
lbl_acc_type.pack(anchor="w", padx=10, pady=(6, 0))

def gerer_champ_pro(choix):
    is_pro_or_admin = any(mot in choix for mot in ["Professionnel", "مهني", "Professional", "Profesional", "Administrateur", "مدير", "Administrator"])
    if is_pro_or_admin:
        lbl_key.pack(anchor="w", padx=10, pady=(4, 0), before=lbl_req)
        entry_key.pack(padx=10, pady=2, before=lbl_req)
    else:
        lbl_key.pack_forget()
        entry_key.pack_forget()

option_acc_type = ctk.CTkOptionMenu(frame, width=520, height=28, fg_color="#2e86c1", command=gerer_champ_pro)
option_acc_type.pack(padx=10, pady=2)

lbl_key = ctk.CTkLabel(frame, text="", font=("Arial", 11, "bold"), text_color="#b03a2e")
entry_key = ctk.CTkEntry(frame, width=520, height=28, show="*")

lbl_req = ctk.CTkLabel(frame, text="", font=("Arial", 12, "bold"), text_color="#1b4f72")
lbl_req.pack(anchor="w", padx=10, pady=(4, 0))
entry_req = ctk.CTkEntry(frame, width=520, height=28)
entry_req.pack(padx=10, pady=2)

lbl_contact = ctk.CTkLabel(frame, text="", font=("Arial", 12, "bold"), text_color="#1b4f72")
lbl_contact.pack(anchor="w", padx=10, pady=(4, 0))
entry_contact = ctk.CTkEntry(frame, width=520, height=28)
entry_contact.pack(padx=10, pady=2)

lbl_cat = ctk.CTkLabel(frame, text="", font=("Arial", 12, "bold"), text_color="#1b4f72")
lbl_cat.pack(anchor="w", padx=10, pady=(4, 0))
option_cat = ctk.CTkOptionMenu(frame, width=520, height=28)
option_cat.pack(padx=10, pady=2)

lbl_nom = ctk.CTkLabel(frame, text="", font=("Arial", 12, "bold"), text_color="#1b4f72")
lbl_nom.pack(anchor="w", padx=10, pady=(4, 0))
entry_nom = ctk.CTkEntry(frame, width=520, height=28)
entry_nom.pack(padx=10, pady=2)

lbl_desc = ctk.CTkLabel(frame, text="", font=("Arial", 12, "bold"), text_color="#1b4f72")
lbl_desc.pack(anchor="w", padx=10, pady=(4, 0))
entry_desc = ctk.CTkEntry(frame, width=520, height=32)
entry_desc.pack(padx=10, pady=2)

lbl_type = ctk.CTkLabel(frame, text="", font=("Arial", 12, "bold"), text_color="#1b4f72")
lbl_type.pack(anchor="w", padx=10, pady=(4, 0))
option_type = ctk.CTkOptionMenu(frame, width=520, height=28)
option_type.pack(padx=10, pady=2)

lbl_price = ctk.CTkLabel(frame, text="", font=("Arial", 12, "bold"), text_color="#1b4f72")
lbl_price.pack(anchor="w", padx=10, pady=(4, 0))
entry_price = ctk.CTkEntry(frame, width=520, height=28)
entry_price.pack(padx=10, pady=2)

lbl_ville = ctk.CTkLabel(frame, text="", font=("Arial", 12, "bold"), text_color="#1b4f72")
lbl_ville.pack(anchor="w", padx=10, pady=(4, 0))
entry_ville = ctk.CTkEntry(frame, width=520, height=28)
entry_ville.pack(padx=10, pady=2)

lbl_etat = ctk.CTkLabel(frame, text="", font=("Arial", 12, "bold"), text_color="#1b4f72")
lbl_etat.pack(anchor="w", padx=10, pady=(4, 0))
option_etat = ctk.CTkOptionMenu(frame, width=520, height=28, fg_color="#27ae60")
option_etat.pack(padx=10, pady=4)

var_boost = ctk.BooleanVar(value=False)
chk_boost = ctk.CTkCheckBox(frame, text="⚡ Option 'À la Une' (Premium)", variable=var_boost, font=("Arial", 11, "bold"), text_color="#d35400")
chk_boost.pack(anchor="w", padx=10, pady=6)

lbl_error = ctk.CTkLabel(frame, text="", font=("Arial", 11, "bold"), text_color="#c0392b", wraplength=500)

def changer_langue(langue_choisie):
    t = TRADUCTIONS[langue_choisie]
    title_label.configure(text=t["title"])
    lbl_pro_banner.configure(text=t["pro_banner"])
    lbl_acc_type.configure(text=t["account_type_lbl"])
    option_acc_type.configure(values=t["acc_types"])
    option_acc_type.set(t["acc_types"][0])
    gerer_champ_pro(t["acc_types"][0])
    lbl_key.configure(text=t["key_lbl"])
    entry_key.configure(placeholder_text=t["key_ph"])
    lbl_req.configure(text=t["req_lbl"])
    entry_req.configure(placeholder_text=t["req_ph"])
    lbl_contact.configure(text=t["contact_lbl"])
    entry_contact.configure(placeholder_text=t["contact_ph"])
    lbl_cat.configure(text=t["cat_lbl"])
    option_cat.configure(values=t["cats"])
    option_cat.set(t["cats"][0])
    lbl_nom.configure(text=t["nom_lbl"])
    entry_nom.configure(placeholder_text=t["nom_ph"])
    lbl_desc.configure(text=t["desc_lbl"])
    entry_desc.configure(placeholder_text=t["desc_ph"])
    lbl_type.configure(text=t["type_lbl"])
    option_type.configure(values=t["types"])
    option_type.set(t["types"][0])
    lbl_price.configure(text=t["price_lbl"])
    entry_price.configure(placeholder_text=t["price_ph"])
    lbl_ville.configure(text=t["loc_lbl"])
    entry_ville.configure(placeholder_text=t["loc_ph"])
    lbl_etat.configure(text=t["stat_lbl"])
    option_etat.configure(values=t["stats"])
    option_etat.set(t["stats"][0])
    btn_save.configure(text=t["btn_save"])
    btn_clear.configure(text=t["btn_clear"])
    btn_buy_extra.configure(text=t["btn_buy_extra"])
    lbl_liste.configure(text=t["inv_lbl"])
    lbl_secu.configure(text=t["security_note"])

option_langue.configure(command=changer_langue)

def compter_annonces_particulier(identifiant):
    if not os.path.exists("materiel.txt"):
        return 0
    count = 0
    with open("materiel.txt", "r", encoding="utf-8") as file:
        content = file.read()
        blocks = [b.strip() for b in content.split("=" * 55) if b.strip()]
        for b in blocks:
            if "⭐ PRO VÉRIFIÉ" not in b and identifiant.lower() in b.lower():
                count += 1
    return count

def rafraichir_liste():
    textbox.delete("1.0", "end")
    if os.path.exists("materiel.txt"):
        with open("materiel.txt", "r", encoding="utf-8") as file:
            content = file.read()
            blocks = [b.strip() for b in content.split("=" * 55) if b.strip()]
            
            boost_blocks = [b for b in blocks if "⚡" in b]
            pro_blocks = [b for b in blocks if "⭐" in b and b not in boost_blocks]
            standard_blocks = [b for b in blocks if b not in boost_blocks and b not in pro_blocks]
            
            sorted_content = ""
            for b in boost_blocks:
                sorted_content += "🔥 [MIS EN AVANT - À LA UNE] 🔥\n" + b + "\n" + ("=" * 55) + "\n\n"
            for b in pro_blocks:
                sorted_content += b + "\n" + ("=" * 55) + "\n\n"
            for b in standard_blocks:
                sorted_content += b + "\n" + ("=" * 55) + "\n\n"
                
            textbox.insert("1.0", sorted_content)
    else:
        langue = option_langue.get()
        textbox.insert("1.0", TRADUCTIONS[langue]["empty"])

def ouvrir_panneau_admin():
    win_admin = ctk.CTkToplevel(app)
    win_admin.title("👑 Panneau d'Administration - MediShare Pro")
    win_admin.geometry("540x520")
    
    lbl_admin_title = ctk.CTkLabel(win_admin, text="👑 Dashboard Administrateur (Amel Goudali)", font=("Arial", 14, "bold"), text_color="#1a5276")
    lbl_admin_title.pack(pady=10)
    
    nb_annonces = 0
    if os.path.exists("materiel.txt"):
        with open("materiel.txt", "r", encoding="utf-8") as file:
            nb_annonces = len([b for b in file.read().split("=" * 55) if b.strip()])
            
    lbl_stats = ctk.CTkLabel(win_admin, text=f"📊 Titulaire : {infos_paiement['titulaire']}\n• Annonces actuellement publiées : {nb_annonces}", font=("Arial", 11, "bold"), justify="left")
    lbl_stats.pack(padx=20, pady=5, anchor="w")
    
    lbl_rip_title = ctk.CTkLabel(win_admin, text="💳 RIP Algérie Poste (Dinars / BaridiMob) :", font=("Arial", 11, "bold"), text_color="#27ae60")
    lbl_rip_title.pack(padx=20, pady=(8, 0), anchor="w")
    entry_rip = ctk.CTkEntry(win_admin, width=480, height=28)
    entry_rip.pack(padx=20, pady=2)
    entry_rip.insert(0, infos_paiement["rip_ccp"])
    
    lbl_badr_title = ctk.CTkLabel(win_admin, text="💶 Compte Devises BADR (EUR €) :", font=("Arial", 11, "bold"), text_color="#2980b9")
    lbl_badr_title.pack(padx=20, pady=(8, 0), anchor="w")
    entry_badr = ctk.CTkEntry(win_admin, width=480, height=28)
    entry_badr.pack(padx=20, pady=2)
    entry_badr.insert(0, infos_paiement["badr_eur"])
    
    def sauvegarder_comptes():
        infos_paiement["rip_ccp"] = entry_rip.get().strip()
        infos_paiement["badr_eur"] = entry_badr.get().strip()
        lbl_msg_admin.configure(text="✅ Vos comptes bancaires (CCP & BADR) ont été enregistrés !")
        
    btn_save_comptes = ctk.CTkButton(win_admin, text="💾 Mettre à jour les comptes", command=sauvegarder_comptes, fg_color="#27ae60", height=30)
    btn_save_comptes.pack(pady=12)
    
    lbl_msg_admin = ctk.CTkLabel(win_admin, text="✅ Configuration active (CCP + BADR Devises)", font=("Arial", 11, "bold"), text_color="#27ae60")
    lbl_msg_admin.pack(pady=2)

def enregistrer():
    langue = option_langue.get()
    type_compte = option_acc_type.get()
    
    if any(mot in type_compte for mot in ["Administrateur", "مدير", "Administrator"]):
        cle_saisie = entry_key.get().strip()
        if cle_saisie == CLE_ADMIN_SECRET:
            lbl_error.pack_forget()
            ouvrir_panneau_admin()
        else:
            lbl_error.configure(text=TRADUCTIONS[langue]["err_key"])
            lbl_error.pack(padx=10, pady=2)
        return

    is_pro = any(mot in type_compte for mot in ["Professionnel", "مهني", "Professional", "Profesional"])
    demandeur = entry_req.get().strip() if entry_req.get().strip() else "Anonyme / Particulier"
    contact = entry_contact.get().strip() if entry_contact.get().strip() else "Non renseigné"
    
    if is_pro:
        cle_saisie = entry_key.get().strip()
        if cle_saisie != CLE_PRO_VALIDE:
            lbl_error.configure(text=TRADUCTIONS[langue]["err_key"])
            lbl_error.pack(padx=10, pady=2)
            return
    else:
        identifiant = contact if contact != "Non renseigné" else demandeur
        annonces_existantes = compter_annonces_particulier(identifiant)
        quota_max = LIMIT_PARTICULIER + extras_achetes.get(identifiant.lower(), 0)
        
        if annonces_existantes >= quota_max:
            lbl_error.configure(text=f"⚠️ Limite atteinte ({annonces_existantes}/{quota_max} annonces). Cliquez sur 'Pack Extra' pour étendre.")
            lbl_error.pack(padx=10, pady=2)
            return

    lbl_error.pack_forget()
    
    badges = ""
    if is_pro:
        badges += f" [{TRADUCTIONS[langue]['badge_pro']}]"
    if var_boost.get():
        badges += f" [{TRADUCTIONS[langue]['badge_boost']}]"
        
    cat = option_cat.get()
    nom = entry_nom.get()
    desc = entry_desc.get().strip() if entry_desc.get().strip() else "Aucune description complémentaire."
    type_echange = option_type.get()
    prix = entry_price.get() if entry_price.get() else "Gratuit / N/A"
    ville = entry_ville.get() if entry_ville.get() else "Non spécifiée"
    etat = option_etat.get()
    date_utc = datetime.now(timezone.utc).strftime("%d/%m/%Y à %H:%M UTC")
    
    numero_clean = contact.replace(" ", "").replace("+", "").replace("-", "")
    if numero_clean.startswith("0"):
        numero_clean = "213" + numero_clean[1:]
        
    msg_wa = f"Bonjour, je vous contacte depuis MediShare Pro au sujet de votre annonce : '{nom}' ({ville})."
    url_wa = f"https://wa.me/{numero_clean}?text={urllib.parse.quote(msg_wa)}"
    
    if nom:
        with open("materiel.txt", "a", encoding="utf-8") as file:
            file.write(f"📅 Date (UTC) : {date_utc}\n")
            file.write(f"👤 Nom/Organisme : {demandeur}{badges}\n")
            file.write(f"📞 Contact : {contact}\n")
            file.write(f"🏥 Matériel : {nom}\n")
            file.write(f"📝 Description : {desc}\n")
            file.write(f"📍 Localisation : {ville}\n")
            file.write(f"🤝 Publication : {type_echange} | Conditions : {prix}\n")
            file.write(f"📦 Catégorie : {cat}\n")
            file.write(f"🚦 Statut : {etat}\n")
            file.write(f"💬 Lien WhatsApp Direct : {url_wa}\n")
            file.write("=" * 55 + "\n\n")
        
        entry_key.delete(0, 'end')
        entry_req.delete(0, 'end')
        entry_contact.delete(0, 'end')
        entry_nom.delete(0, 'end')
        entry_desc.delete(0, 'end')
        entry_price.delete(0, 'end')
        entry_ville.delete(0, 'end')
        var_boost.set(False)
        rafraichir_liste()

def acheter_extra():
    msg_coordonnees = (
        f"💳 VOS COORDONNÉES DE PAIEMENT :\n"
        f"1️⃣ Dinars (RIP CCP) : {infos_paiement['rip_ccp']}\n"
        f"2️⃣ Devises EUR € (BADR Agence {infos_paiement['badr_agence']}) : N° {infos_paiement['badr_eur']}\n"
        f"👤 Titulaire du compte : {infos_paiement['titulaire']}"
    )
    lbl_error.configure(text=msg_coordonnees)
    lbl_error.pack(padx=10, pady=2)

def effacer_tout():
    if os.path.exists("materiel.txt"):
        os.remove("materiel.txt")
    rafraichir_liste()

btn_frame = ctk.CTkFrame(scroll_container, fg_color="transparent")
btn_frame.pack(pady=6)

btn_save = ctk.CTkButton(btn_frame, text="", command=enregistrer, fg_color="#28a745", hover_color="#218838", font=("Arial", 12, "bold"), width=160, height=34)
btn_save.pack(side="left", padx=3)

btn_clear = ctk.CTkButton(btn_frame, text="", command=effacer_tout, fg_color="#dc3545", hover_color="#c82333", font=("Arial", 12, "bold"), width=110, height=34)
btn_clear.pack(side="left", padx=3)

btn_buy_extra = ctk.CTkButton(btn_frame, text="", command=acheter_extra, fg_color="#8e44ad", hover_color="#732d91", font=("Arial", 11, "bold"), width=180, height=34)
btn_buy_extra.pack(side="left", padx=3)

lbl_liste = ctk.CTkLabel(scroll_container, text="", font=("Arial", 13, "bold"), text_color="#1a5276")
lbl_liste.pack(anchor="w", padx=10, pady=(4, 0))

textbox = ctk.CTkTextbox(scroll_container, width=540, height=160, font=("Courier New", 10))
textbox.pack(padx=10, pady=5)

lbl_secu = ctk.CTkLabel(scroll_container, text="", font=("Arial", 9, "italic"), text_color="#7f8c8d", wraplength=540)
lbl_secu.pack(padx=10, pady=4)

changer_langue("Français")
rafraichir_liste()

app.mainloop()
