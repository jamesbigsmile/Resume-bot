#!/usr/bin/env python3
"""
Resume & Cover Letter Generator - PORTFOLIO VERSION
⚠️  TEMPLATE ONLY - Edit MASTER_RESUME_DATA with your info
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import anthropic
from weasyprint import HTML
import markdown

# Load environment variables
load_dotenv()

# PORTFOLIO TEMPLATE - Customize this!
MASTER_RESUME_DATA_TEMPLATE = {
    "name": "Your Name Here",
    "email": "your.email@example.com",
    "phone": "+1-XXX-XXX-XXXX",
    "location": "Your City, ST",
    "linkedin": "https://linkedin.com/in/yourprofile",
    "portfolio": "https://your-portfolio.com",
    "summary_variants": {
        "partnership": "Template summary for partnerships...",
        "implementation": "Template summary for implementations..."
    },
    # ... rest is template data
}

RESUME_GENERATION_PROMPT_TEMPLATE = """
You are an expert resume writer. Follow these CRITICAL constraints:

CRITICAL CONSTRAINTS (ZERO TOLERANCE):
- NO HALLUCINATIONS: Only use Master Resume Data provided
- NO FABRICATED METRICS: Numbers must exist in data
- NO KEYWORD STUFFING: Pivot to transferable skills only

FORMAT OUTPUT AS MARKDOWN with this header:
# {name}
[Target Role] | {location} | Remote-Ready | [LinkedIn]({linkedin})

{email} | {phone}

## PROFESSIONAL SUMMARY
...

# DEMO: This generates ATS-friendly PDFs with custom styling
"""

def demo_pdf_styling():
    """Demo the PDF conversion with sample content"""
    sample_md = """
# Sample Resume
**Sample Role** | Sample City, ST | Remote-Ready | [LinkedIn](https://linkedin.com)

[sample@email.com](mailto:sample@email.com) | 555-123-4567

## PROFESSIONAL SUMMARY
This demonstrates professional PDF styling with:
- Proper margins (0.5in × 0.6in)
- Dark teal headers (#1a4d5c)
- Blue links (#0056b3)
- Calibri font, 10.5pt
"""
    
    html_content = markdown.markdown(sample_md)
    full_html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @page {{ margin: 0.5in 0.6in 0.5in 0.6in; }}
            body {{ 
                font-family: Calibri, Arial, sans-serif; 
                line-height: 1.5; 
                color: #2c3e50; 
                font-size: 10.5px; 
            }}
            h1 {{ color: #1a4d5c; font-size: 18px; }}
            h2 {{ color: #1a4d5c; font-size: 11px; border-bottom: 1px solid #1a4d5c; }}
            a {{ color: #0056b3; }}
        </style>
    </head>
    <body>{html_content}</body>
    </html>
    """
    
    output = Path("demo_resume.pdf")
    HTML(string=full_html).write_pdf(output)
    print(f"✅ Demo PDF created: {output}")

if __name__ == "__main__":
    print("🚀 Resume Generator Portfolio Demo")
    print("📖 Edit MASTER_RESUME_DATA_TEMPLATE with your info")
    print("🎨 Run demo_pdf_styling() to see PDF styling")
    demo_pdf_styling()
