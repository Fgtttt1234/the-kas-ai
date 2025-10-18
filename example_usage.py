"""
مثال على استخدام الخبير الدغريري
Example usage of the Daghreeri Expert
"""

from experts import DaghreerIExpert


def main():
    """Demonstrate the usage of الخبير الدغريري."""
    
    # Create an instance of the Daghreeri Expert
    expert = DaghreerIExpert()
    
    print("=" * 60)
    print(f"الخبير: {expert.name}")
    print("=" * 60)
    
    # Get expert information
    info = expert.get_info()
    print(f"\nالوصف: {info['description']}")
    print(f"الأسلوب: {info['style']}")
    print("\nالقدرات:")
    for capability in info['capabilities']:
        print(f"  • {capability}")
    
    # Example questions
    questions = [
        "ما هي أفضل طريقة لتعلم البرمجة؟",
        "كيف أبدأ مشروعي الخاص؟",
        "ما هي النصيحة الأهم للنجاح؟"
    ]
    
    print("\n" + "=" * 60)
    print("أمثلة على الأسئلة والأجوبة")
    print("=" * 60)
    
    for i, question in enumerate(questions, 1):
        print(f"\n[مثال {i}]")
        print(f"السؤال: {question}")
        print("-" * 60)
        
        response = expert.process_question(question)
        print(response['answer'])
        print()


if __name__ == "__main__":
    main()
