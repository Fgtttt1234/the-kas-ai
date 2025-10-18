"""
KAS AI - نظام الذكاء الاصطناعي
Main application file for the KAS AI system with expert integration.
"""

from experts import DaghreerIExpert


class KasAI:
    """
    نظام KAS للذكاء الاصطناعي
    
    Main AI system that integrates different experts to answer questions.
    """
    
    def __init__(self):
        self.experts = {}
        self._initialize_experts()
    
    def _initialize_experts(self):
        """Initialize all available experts."""
        # Initialize الخبير الدغريري
        daghreeri = DaghreerIExpert()
        self.experts["daghreeri"] = daghreeri
        self.experts["الدغريري"] = daghreeri
    
    def ask(self, question, expert_name="daghreeri"):
        """
        Ask a question to a specific expert.
        
        Args:
            question (str): The question to ask
            expert_name (str): Name of the expert to use
            
        Returns:
            dict: Response from the expert
        """
        if expert_name not in self.experts:
            return {
                "error": f"Expert '{expert_name}' not found",
                "available_experts": list(self.experts.keys())
            }
        
        expert = self.experts[expert_name]
        return expert.process_question(question)
    
    def list_experts(self):
        """
        List all available experts.
        
        Returns:
            list: Information about all experts
        """
        experts_info = []
        seen = set()
        
        for expert in self.experts.values():
            expert_id = id(expert)
            if expert_id not in seen:
                experts_info.append(expert.get_info())
                seen.add(expert_id)
        
        return experts_info


def main():
    """Main entry point for the application."""
    print("=" * 60)
    print("مرحباً بك في نظام KAS للذكاء الاصطناعي")
    print("Welcome to KAS AI System")
    print("=" * 60)
    
    # Initialize the AI system
    kas = KasAI()
    
    # List available experts
    print("\nالخبراء المتاحون - Available Experts:")
    print("-" * 60)
    experts = kas.list_experts()
    for expert in experts:
        print(f"\n📚 {expert['name']}")
        print(f"   الوصف: {expert['description']}")
        print(f"   القدرات:")
        for capability in expert['capabilities']:
            print(f"   • {capability}")
    
    # Example usage with الخبير الدغريري
    print("\n" + "=" * 60)
    print("مثال على الاستخدام - Example Usage")
    print("=" * 60)
    
    example_question = "ما هو أفضل وقت للدراسة؟"
    print(f"\nالسؤال: {example_question}")
    print("\nيجيب الخبير الدغريري:")
    print("-" * 60)
    
    response = kas.ask(example_question, "الدغريري")
    print(response['answer'])
    
    print("\n" + "=" * 60)
    print("شكراً لاستخدامك نظام KAS AI")
    print("=" * 60)


if __name__ == "__main__":
    main()
