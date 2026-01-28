"""
الهوية الرسمية - Official Identity
This module defines the official identity of Kasarella AI MBT.

استخدام - Usage:
    from core.identity import banner, identity
    
    # عرض البانر - Display banner
    print(banner())
    
    # الحصول على معلومات الهوية - Get identity information
    info = identity()
    print(info['name_ar'])
"""

# الهوية الرسمية - Official Identity
name_ar = "كازاريلا ما بي تي"
name_en = "Kasarella AI MBT"
founder = "المهندس الخبير الدغريري"
founded = "25-01-2026"
description = "منصة ذكاء اصطناعي تقنية احترافية للتفكير، التحليل، وصناعة القرار."


def banner():
    """
    عرض بانر الهوية الرسمية
    Display the official identity banner.
    
    Returns:
        str: بانر متناسق يحتوي على معلومات الهوية
             A formatted banner containing identity information
    
    Example:
        >>> print(banner())
        ╔══════════════════════════════════════════════════════════════╗
        ║  🤖 كازاريلا ما بي تي - Kasarella AI MBT                  ║
        ╠══════════════════════════════════════════════════════════════╣
        ║  منصة ذكاء اصطناعي تقنية احترافية للتفكير، التحليل، وصناعة   ║
        ║  القرار.                                                     ║
        ╠══════════════════════════════════════════════════════════════╣
        ║  المؤسس: المهندس الخبير الدغريري                           ║
        ║  تاريخ التأسيس: 25-01-2026                                  ║
        ╚══════════════════════════════════════════════════════════════╝
    """
    # Fixed width for banner content
    box_width = 62
    border_top = "╔" + "═" * box_width + "╗"
    border_mid = "╠" + "═" * box_width + "╣"
    border_bot = "╚" + "═" * box_width + "╝"
    
    # Build title line with name
    title = f"🤖 {name_ar} - {name_en}"
    
    # Build content lines
    lines = [
        border_top,
        f"║  {title:<{box_width-2}}║",
        border_mid,
        f"║  منصة ذكاء اصطناعي تقنية احترافية للتفكير، التحليل، وصناعة{'  ' :<{box_width-58}}║",
        f"║  القرار.{' ' * (box_width - 10)}║",
        border_mid,
        f"║  المؤسس: {founder:<{box_width-12}}║",
        f"║  تاريخ التأسيس: {founded:<{box_width-20}}║",
        border_bot
    ]
    
    return '\n'.join(lines)


def identity():
    """
    الحصول على معلومات الهوية الرسمية
    Get the official identity information.
    
    Returns:
        dict: قاموس يحتوي على جميع معلومات الهوية
              A dictionary containing all identity information
    
    Example:
        >>> info = identity()
        >>> print(info['name_ar'])
        كازاريلا ما بي تي
        >>> print(info['founder'])
        المهندس الخبير الدغريري
    """
    return {
        'name_ar': name_ar,
        'name_en': name_en,
        'founder': founder,
        'founded': founded,
        'description': description
    }


# للاستخدام المباشر من سطر الأوامر
# For direct use from command line
if __name__ == "__main__":
    print(banner())
    print("\n" + "=" * 62)
    print("معلومات الهوية - Identity Information:")
    print("=" * 62)
    info = identity()
    for key, value in info.items():
        print(f"{key}: {value}")
