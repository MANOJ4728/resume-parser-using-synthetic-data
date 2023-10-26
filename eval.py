import spacy

nlp = spacy.load("./output/model-best")

text = """
Adarsh
Chintada
Mobile: +91 8985679223
n180479@rguktn.ac.in
Adarsh Linkedin
ACADEMIC QUALIFICATIONS
RGUKT, NUZVID
Andhra pradesh (India)
MHS, Amadalavalasa.
Bachelor’s of Technology – Computer
Science
Pre University Course (10+2) – MPC
10th class, SSC Andhra Pradesh
8.5/10 (CGPA)
8.6/10 (CGPA)
10/10 (CGPA)
2020-Present
2018-2020
2018
SKILLS SUMMARY
Programming
: C, Python, Java, SQL
Subject expertise : DSA, Operating Systems, Computer Networks, Software Testing.
Technologies
: Deep Learning
Frameworks
: Bootstrap, ReactJs fundamentals
Area of Interests : Deep Learning, Artificial Intelligence.
.
PROJECT EXPERIENCE
Skin Cancer
Detection
● I employed Convolutional Neural Networks (CNN) and experimented with ResNet50,
VGG16, DenseNet, and EfficientNet architectures and got accuracy of 89% for EfficientNet
architecture.
Mar’23
-
May’23
Object Detection
Using YOLOV4
● I Proficient in YOLOv4 object detection model, adeptly utilizing 80 classes for
real-time, multi-class object recognition in diverse images and videos. Recognizes
the potential for expanding class repertoire, ensuring adaptability for future
requirements.
May’23
-
June’23
Health Data
Analysis
● Analyze public health data and identify trends in health outcomes, risk factors, and disease
prevalence.The project will use Python libraries such as Pandas, NumPy, Matplotlib,
Seaborn, and Plotly to perform data cleaning, manipulation, and visualization.
Sep’22
-
nov’22
School
Management
System
● Web application using HTML5, CSS, JavaScript, and Bootstrap to streamline school
achievements, faculty details and student attendance.
May’22
-
Aug 22
POSITIONS OF RESPONSIBILITY
National
Cadet Corps
Holding a Lance Corporal rank in 17 Andhra Batallion, Vijayawada.
Contigent Commandant for SD Cadets, RGUKT Nuzvid.
2018-2021
Co-Ordinator
SDCAC
Co-ordinator for Career Guidance Club, SDCAC.
Conducted GRE and GATE sessions to help students to pursue higher education.
Conducted Mock competitive exams and Hackathon.
2022-23
Core Team
SDCAC
Pioneered as the Event manager for national level technical fest and managed over 12,000
students from 30 various institutes in India.

Organized the Teckzite 2k18, national level Technical fest.
2022
-
2023
CERTIFICATIONS
Python 3 professional Certificate by Google with Grade 93.75%.
Microsoft Professionally Certified Azure Administrator .
English for Career Development by University of Pennsylvania.
2022
2022
2023
"""

doc = nlp(text)

for ent in doc.ents:
    print(ent.text,  "\t\t==>", ent.label_)
