"""
الهوية الرسمية لنظام كازاريلا - Official Identity of Kasarella AI System

This module defines the official identity of the Kasarella AI assistant.
The identity is defined once here and can be used throughout the project.
"""

# الاسم الرسمي بالعربية - Official Name in Arabic
NAME_AR = "كازاريلا ما بي تي"

# الاسم الرسمي بالإنجليزية - Official Name in English
NAME_EN = "Kasarella AI MBT"

# المؤسس - Founder
FOUNDER = "المهندس الخبير الدغريري"

# تاريخ التأسيس - Founding Date
FOUNDED = "25-01-2026"

# الوصف الرسمي بالعربية - Official Description in Arabic
DESCRIPTION_AR = "منصة ذكاء اصطناعي تقنية احترافية للتفكير، التحليل، وصناعة القرار"

# الوصف الرسمي بالإنجليزية - Official Description in English
DESCRIPTION_EN = "Professional technical AI platform for thinking, analysis, and decision making"


def banner(language="ar"):
    """
    إرجاع بانر تعريفي للهوية الرسمية
    Returns an identity banner for the official identity.
    
    Args:
        language (str): Language for the banner ("ar" for Arabic, "en" for English)
        
    Returns:
        str: Formatted banner text
    """
    if language.lower() == "en":
        return f"""
╔═══════════════════════════════════════════════════════════════════╗
║                      {NAME_EN:^41s}                      ║
║                           {NAME_AR:^31s}                           ║
╠═══════════════════════════════════════════════════════════════════╣
║  Founder: {FOUNDER:<54s} ║
║  Founded: {FOUNDED:<54s} ║
║                                                                   ║
║  {DESCRIPTION_EN:<63s} ║
╚═══════════════════════════════════════════════════════════════════╝
""".strip()
    else:  # Arabic (default)
        return f"""
╔═══════════════════════════════════════════════════════════════════╗
║                      {NAME_AR:^41s}                      ║
║                      {NAME_EN:^41s}                      ║
╠═══════════════════════════════════════════════════════════════════╣
║  المؤسس: {FOUNDER:<55s} ║
║  تاريخ التأسيس: {FOUNDED:<49s} ║
║                                                                   ║
║  {DESCRIPTION_AR:<57s} ║
╚═══════════════════════════════════════════════════════════════════╝
""".strip()


def identity():
    """
    إرجاع قاموس يحتوي على معلومات الهوية الكاملة
    Returns a dictionary containing complete identity information.
    
    Returns:
        dict: Identity information including name, founder, date, and description
    """
    return {
        "name_ar": NAME_AR,
        "name_en": NAME_EN,
        "founder": FOUNDER,
        "founded": FOUNDED,
        "description_ar": DESCRIPTION_AR,
        "description_en": DESCRIPTION_EN
    }


def get_full_name(language="ar"):
    """
    الحصول على الاسم الكامل بلغة محددة
    Get the full name in a specific language.
    
    Args:
        language (str): Language code ("ar" for Arabic, "en" for English)
        
    Returns:
        str: Full name in the requested language
    """
    if language.lower() == "en":
        return NAME_EN
    return NAME_AR


def get_description(language="ar"):
    """
    الحصول على الوصف بلغة محددة
    Get the description in a specific language.
    
    Args:
        language (str): Language code ("ar" for Arabic, "en" for English)
        
    Returns:
        str: Description in the requested language
    """
    if language.lower() == "en":
        return DESCRIPTION_EN
    return DESCRIPTION_AR
