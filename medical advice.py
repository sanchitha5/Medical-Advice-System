name=str(input(" Enter your name : "))

import time
t = time.strftime( " %H : %M : %S ")
hour = int(time.strftime( " %H " ))
if ( hour>=0 and hour<12 ):
    wish = "Good Morning!"
elif( hour>=12 and hour<16 ):
    wish = "Good Afternoon!"
elif( hour>=16 and hour<18 ):
    wish = "Good Evening!"
else:
    wish = "Good Night!"

print ( f" Hello { name } , { wish } " )

print( "\n WELCOME TO SANCHITHA'S ONLINE MEDICINAL ADVICE \n")

diseases = [ " Common cold ", " Diabetes ", " Asthma ", " Fever ", " Headache ", " Body pain ", " Food poisoning ", " Malaria ", " Cough ", " Stomach aches ", " Yellow fever ", " Skin rashes ", " Urinary tract infection ", " Breathing problems ", " Vomit "]


information = [ "A viral infection of the nose and throat, characterized by a runny or stuffy nose, sore throat, cough, and sneezing " , " A chronic condition that affects how your body turns food into energy, leading to high blood sugar levels. There are two main types: Type 1 and Type 2. ", " A respiratory condition in which the airways become inflamed, narrow, and swell, causing difficulty in breathing, coughing, wheezing, and shortness of breath. ", "  A temporary increase in body temperature, often due to an infection or illness. It is a common symptom of many conditions. ", " Pain or discomfort in the head or face area, which can be caused by various factors including stress, tension, or underlying medical conditions.", " Generalized pain or discomfort in muscles, joints, or other parts of the body, often due to physical exertion, illness, or injury. ", "  Illness caused by consuming contaminated food or water, characterized by symptoms like nausea, vomiting, diarrhea, and abdominal pain. ", " A mosquito-borne infectious disease caused by Plasmodium parasites, leading to symptoms like fever, chills, and flu-like illness. ", " A reflex action to clear your airways of mucus, irritants, or foreign particles. It can be a symptom of many respiratory conditions. ", " Pain or discomfort in the stomach area, which can be caused by various digestive issues, infections, or other conditions. ", " A viral disease transmitted by mosquitoes, characterized by fever, chills, jaundice (yellowing of the skin and eyes), and sometimes fatal organ damage. ", " Changes in the skin's color, appearance, or texture, often due to irritation, infection, or allergic reactions. ", " An infection in any part of the urinary system, including the kidneys, bladder, or urethra, often causing pain, frequent urination, and cloudy urine. ", " Difficulty in breathing, which can be due to various conditions such as asthma, bronchitis, pneumonia, or chronic obstructive pulmonary disease (COPD). ", " The forceful expulsion of stomach contents through the mouth, often due to infections, food poisoning, motion sickness, or other medical conditions. " ]

medicines = [ " Pseudoephedrine Cetirizine Acetaminophen", " Metformin Insulin Glipizide " , " Albuterol Fluticasone Montelukast " , " Acetaminophen Ibuprofen Naproxen " , " Acetaminophen Ibuprofen Aspirin " , " Acetaminophen Ibuprofen Naproxen " , " Oral Rehydration Salts Ondansetron Ciprofloxacin " , " Chloroquine Artemisinin-based combination therapies (ACTs) Quinine " , " Dextromethorphan Guaifenesin Codeine "  , " Aluminum hydroxide Omeprazole Dicyclomine " , " Rehydration solutions Acetaminophen " , " Hydrocortisone Diphenhydramine Calamine " , " Trimethoprim/sulfamethoxazole Nitrofurantoin Ciprofloxacin " , " Albuterol Ipratropium Prednisone " ,  " Ondansetron Promethazine Metoclopramide " ]
        
for index, disease in enumerate( diseases, start=1 ):
    print(index,disease)
choice = (int(input( "\n Please choose your disease from the list above ( 1-15 ) : ")))

if 1 <= choice <= len(diseases):
    print ( f"\n You choose : { diseases[choice-1]}")
    print ( f"\n Description : { information[choice-1]}")
    print ( f" \n Here are your medicines : { medicines[choice]}\n")
    print(" Please give your feedback ! ")
    print( f' Thank You for visiting us! { name }.') 
    
else :
    print( " Invalid Choice. Please select a number from 1 to 15. ")


