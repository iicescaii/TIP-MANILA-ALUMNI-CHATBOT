import os
from openai import OpenAI
from dotenv import load_dotenv 

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate(user_input):
    # This sets the chatbot's identity and core rules
    system_instruction = (
        "You are a helpful and informative chatbot for TIP Manila named yui. "
        "You respond in a friendly and professional manner and provide accurate answers based on the information provided. "
        "If unsure or the question is not about TIP Manila, or if asked math questions, "
        "say 'I'm sorry, I don't have information on that topic.'"
    )

    # Conversion of all training data to OpenAI's message format
    messages = [
        {"role": "system", "content": system_instruction},
        
        # --- CAMPUS INFO ---
        {"role": "user", "content": "What is the address of TIP Manila?"},
        {"role": "assistant", "content": "The Technological Institute of the Philippines (T.I.P.) Manila is primarily located at 363 P. Casal Street, Quiapo, Manila, 1001, Philippines. Additionally, the campus includes another building at 1338 Arlegui Street, Quiapo, Manila, 1001, Philippines."},
        
        {"role": "user", "content": "What is the telephone number of TIP Manila?"},
        {"role": "assistant", "content": "The telephone numbers of T.I.P. Manila are: (02) 8733-9117, (02) 7918-8476, and 0917-177-2566. Feel free to reach out to them for any inquiries!"},

        {"role": "user", "content": "What is the email address for TIP Manila?"},
        {"role": "assistant", "content": "The email address for TIP Manila is info@tip.edu.ph"},

        # --- PROGRAMS ---
        {"role": "user", "content": "What undergraduate programs are offered at TIP Manila?"},
        {"role": "assistant", "content": """T.I.P. Manila offers a variety of undergraduate programs:

**College of Engineering and Architecture**
* Bachelor of Science in Chemical Engineering, Civil Engineering, Computer Engineering, Electrical Engineering, Electronics Engineering, Industrial Engineering, Mechanical Engineering, and Architecture.

**College of Computer Studies**
* Bachelor of Science in Computer Science, Information Technology, and Entertainment and Multimedia Computing (Digital Animation or Game Development).

**College of Business Education**
* Bachelor of Science in Accountancy, Accounting Information System, and Business Administration (Logistics, Financial, HR, or Marketing Management).

**College of Arts**
* Bachelor of Arts in English Language and Political Science."""},

        {"role": "user", "content": "Does TIP Manila offer Senior High School?"},
        {"role": "assistant", "content": "T.I.P. Manila no longer offers Senior High School (SHS). Applicants who wish to pursue their SHS education with T.I.P. may consider enrolling at Quezon City Campus."},

        # --- ADMISSIONS ---
        {"role": "user", "content": "What are the admission requirements for freshmen at TIP Manila?"},
        {"role": "assistant", "content": """To apply as a freshman, you generally need:
1. Original High School Report Card (Form 138/SF9) in Grade 12
2. PSA Birth Certificate (Original Copy)
3. Certificate of Good Moral Character
4. Two (2) copies of 2"x2" recent ID pictures.
Special requirements apply for graduates of foreign schools or those with PEPT/ALS Certificates."""},

        {"role": "user", "content": "What are the admission requirements for transferees"},
        {"role": "assistant", "content": "1. Original Transfer Credentials, 2. Official Transcript of Records, 3. Certificate of Good Moral Character, 4. Copy of course Descriptions, 5. PSA Birth Certificate, 6. Two 2x2 ID pictures."},

        # --- HISTORY & LEADERSHIP ---
        {"role": "user", "content": "When was TIP founded?"},
        {"role": "assistant", "content": "T.I.P. was founded on February 8, 1962, by a group of educators led by Engineer Demetrio A. Quirino, Jr. and Dr. Teresita U. Quirino."},

        {"role": "user", "content": "Who is the current president of TIP?"},
        {"role": "assistant", "content": "The current president of T.I.P. is Angelo Quirino Lahoz, who assumed the role on February 21, 2025. He is the grandson of the founders."},

        {"role": "user", "content": "Who is the current Chairman of the Board of TIP?"},
        {"role": "assistant", "content": "Dr. Elizabeth Quirino-Lahoz is the current Chairman of the Board of Directors of the Technological Institute of the Philippines (T.I.P.)."},

        # --- VALUES & PHILOSOPHY ---
        {"role": "user", "content": "What are TIP's vision and mission statements?"},
        {"role": "assistant", "content": "**Vision**: TIP envisions a better life for Filipinos by empowering students with globally competitive technological education. **Mission**: Transforming students to achieve optimal outcomes through digitalization and innovation."},

        {"role": "user", "content": "What are TIP's core values?"},
        {"role": "assistant", "content": "The core values include: Commitment to Continuous Improvement, Collaborative Mindset, Community Spirit, Service Orientedness, Positive Attitude, Effective Communication, Digital Savvy, and Adaptability."},

        {"role": "user", "content": "What are TIP's core competencies?"},
        {"role": "assistant", "content": "Collaboration, Continuing Improvement, Innovativeness, Efficient Management, Willingness to Learn, Digital Competency, and Quest for Excellence."},

        {"role": "user", "content": "What is the meaning of TIP Logo?"},
        {"role": "assistant", "content": "The logo features lines and symmetry representing engineering. The 60:40 proportion between blocks reinforces stability, and the black base represents a firm foundation."},

        # --- PROCEDURES & CONTACTS ---
        {"role": "user", "content": "What is the contact information of tip manila admission?"},
        {"role": "assistant", "content": "Admissions: 8733-9117 loc. 102, 0917-1059581, or email admissions.manila@tip.edu.ph."},

        {"role": "user", "content": "When is registrar open?"},
        {"role": "assistant", "content": "Monday to Friday: 8:00 AM to 5:00 PM; Saturday: 8:00 AM to 12:00 NN."},

        {"role": "user", "content": "What is the enrollment procedure for incoming college students?"},
        {"role": "assistant", "content": "The process involves: 1. Online Registration, 2. Evaluation at SRO, 3. Interviews, 4. Entrance Exam (if applicable), 5. Registration, 6. Payment, 7. Form Issuance, 8. ID Application, 9. Math Enhancement (if needed), 10. Medical/Dental, 11. Orientation."},

        {"role": "user", "content": "What is the mode of payment of school fees?"},
        {"role": "assistant", "content": "You can pay via the T.I.P. Cashier, PayApp, DragonPay, 7/11, BDO, or Landbank. Note: T.I.P. does not use GCash or Maya."},

        {"role": "user", "content": "Is there scholarship available at tip?"},
        {"role": "assistant", "content": "Yes, T.I.P. offers the EDAQ and DTUQ Scholarship Grants, Entrance Scholarships (25% to 100% discount for honors), and a Loyalty Discount for TIP SHS Graduates."},

        # --- CURRENT USER REQUEST ---
        {"role": "user", "content": user_input}
    ]

    try:
        # Request from OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini", # You can also use "gpt-4o-mini"
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"Error: {e}")
        return "I'm sorry, I'm having trouble connecting right now. Please try again later."