"""
مثال على استخدام الخبراء
Example usage of the Experts
"""

from experts import DaghreerIExpert, KasarellaExpert


def main():
    """Demonstrate the usage of different experts."""
    
    # الخبير الدغريري - Daghreeri Expert
    print("=" * 60)
    print("🎯 الخبير الدغريري - Daghreeri Expert")
    print("=" * 60)
    
    daghreeri = DaghreerIExpert()
    info = daghreeri.get_info()
    print(f"\nالوصف: {info['description']}")
    print(f"الأسلوب: {info['style']}")
    print("\nالقدرات:")
    for capability in info['capabilities']:
        print(f"  • {capability}")
    
    print("\n" + "-" * 60)
    question1 = "ما هي أفضل طريقة لتعلم البرمجة؟"
    print(f"السؤال: {question1}")
    print("-" * 60)
    response = daghreeri.process_question(question1)
    print(response['answer'])
    
    # خبيرة كازاريلا - Kasarella Expert
    print("\n\n" + "=" * 60)
    print("✨ خبيرة كازاريلا - Kasarella Expert")
    print("=" * 60)
    
    kasarella = KasarellaExpert()
    info = kasarella.get_info()
    print(f"\nالوصف: {info['description']}")
    print(f"الأسلوب: {info['style']}")
    print("\nالقدرات:")
    for capability in info['capabilities']:
        print(f"  • {capability}")
    
    print("\n" + "-" * 60)
    question2 = "كيف أحقق أحلامي؟"
    print(f"السؤال: {question2}")
    print("-" * 60)
    response = kasarella.process_question(question2)
    print(response['answer'])
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
