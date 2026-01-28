# the-kas-ai
ذكاء اصطناعي خاص يجاوب على أي سؤال بدون اشتراك إضافي (مشروع بيك أب)

## الهوية الرسمية - Official Identity

### الاسم الرسمي - Official Name
- **بالعربية**: كازاريلا ما بي تي
- **In English**: Kasarella AI MBT

### المعلومات الأساسية - Basic Information
- **المؤسس - Founder**: المهندس الخبير الدغريري
- **تاريخ التأسيس - Founded**: 25-01-2026
- **الوصف - Description**: منصة ذكاء اصطناعي تقنية احترافية للتفكير، التحليل، وصناعة القرار
- **Description**: Professional technical AI platform for thinking, analysis, and decision making

## الخبراء المتاحون - Available Experts

### 🎯 الخبير الدغريري - Daghreeri Expert
خبير متخصص في تقديم إجابات مباشرة وصريحة بأسلوب واضح وبسيط. يتميز هذا الخبير بـ:

- **إجابات مباشرة وصريحة** - Direct and honest answers
- **تفسيرات واضحة بدون تعقيد** - Clear explanations without complexity  
- **نصائح عملية وتطبيقية** - Practical and applicable advice
- **شفافية في الإجابات** - Transparency in responses

الأسلوب الدغريري معروف بأنه مباشر ولا يستخدم تعقيدات غير ضرورية أو مجاملات.

## التثبيت - Installation

```bash
# Clone the repository
git clone https://github.com/Fgtttt1234/the-kas-ai.git
cd the-kas-ai

# Install dependencies (optional - no external dependencies required for basic usage)
pip install -r requirements.txt
```

## الاستخدام - Usage

### الاستخدام الأساسي - Basic Usage

```python
from experts import DaghreerIExpert

# Create an instance of the Daghreeri Expert
expert = DaghreerIExpert()

# Ask a question
response = expert.process_question("ما هو أفضل وقت للدراسة؟")
print(response['answer'])
```

### استخدام النظام الكامل - Using the Complete System

```bash
# Run the main application
python main.py
```

### مثال على الاستخدام - Example Usage

```bash
# Run the example script
python example_usage.py
```

## الهيكل - Structure

```
the-kas-ai/
├── experts/
│   ├── __init__.py
│   └── daghreeri_expert.py    # الخبير الدغريري
├── main.py                     # التطبيق الرئيسي
├── example_usage.py            # مثال على الاستخدام
├── requirements.txt            # المتطلبات
└── README.md                   # هذا الملف
```

## المميزات - Features

✅ خبير متخصص في الإجابات المباشرة (الخبير الدغريري)  
✅ واجهة برمجية سهلة الاستخدام  
✅ دعم اللغة العربية والإنجليزية  
✅ قابل للتوسع بإضافة خبراء جدد  
✅ بدون اشتراكات إضافية أو تكاليف خفية

## المساهمة - Contributing

نرحب بالمساهمات! يرجى فتح issue أو pull request لأي اقتراحات أو تحسينات.

## الترخيص - License

MIT License
