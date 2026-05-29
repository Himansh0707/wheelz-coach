import os
import json
import random

# Base directory setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FOLDER = BASE_DIR

# Helper arrays for variations
USA_NAMES = ["Sarah", "Michael", "John", "Jessica", "David", "Emily", "Chris", "Ashley", "Robert", "Amanda", "James", "Megan", "Brian", "Nicole", "Matthew", "Heather"]
EU_NAMES = ["Thomas", "Emma", "Hans", "Sophie", "Jean", "Charlotte", "Luca", "Laura", "Oliver", "Fiona", "Arthur", "Isabella", "Lukas", "Anna", "Alistair", "Chloe"]
EAST_ASIA_NAMES = ["Kenji", "Mei", "Min-su", "Yuki", "Wei", "Ji-won", "Hiroshi", "Sakura", "Li", "Seo-yeon", "Takahiro", "Chao", "Hana", "Chen", "Kaito", "Yoon-ji"]
AFRICA_NAMES = ["Kofi", "Amina", "Nnamdi", "Tendai", "Chioma", "Zola", "Babajide", "Lindiwe", "Tariq", "Fatoumata", "Jomo", "Lerato", "Eshe", "Chidi", "Kehinde", "Sipho"]
DRIVER_NAMES = ["Driver Carlos", "Driver Marcus", "Driver Ali", "Driver Dmitry", "Driver Jose", "Driver Ken", "Driver Sam", "Driver Roger", "Driver Ahmed", "Driver Liam"]
CITIES = ["New York", "Chicago", "Los Angeles", "San Francisco", "Austin", "London", "Paris", "Berlin", "Tokyo", "Seoul", "Singapore", "Johannesburg", "Lagos", "Nairobi"]
AMOUNTS = ["$5.00", "$10.00", "$15.00", "$25.00", "$45.00", "$75.00", "€8.50", "€15.00", "€30.00", "£6.00", "£12.00", "R120", "R250", "₦4500", "₦8000", "KSh 500", "KSh 1200"]
ITEMS = ["iPhone", "wallet", "keys", "backpack", "sunglasses", "passport", "purse", "jacket", "briefcase", "laptop"]

def make_question(q_id, question, scenario, options, answer, explanation, skill):
    return {
        "id": q_id,
        "question": question,
        "scenario": scenario,
        "options": options,
        "answer": answer,
        "explanation": explanation,
        "skill": skill
    }

# 1. USA CUSTOMERS DATA GENERATION (Direct, Fast, Slang, Assertive)
def generate_usa_questions():
    questions = []
    
    templates = [
        {
            "text": "A USA customer named {name} messages: 'I was charged {price} for a no-show but I was literally standing on the corner! This is a total rip-off.' What does 'rip-off' mean here and how do you respond?",
            "scenario": "USA customer complains about cancellation fee using slang",
            "options": {
                "A": "Tell them to calm down and explain that a rip-off is a crime which we didn't do.",
                "B": "A rip-off means an unfair price or cheat. You say: 'I understand you're frustrated, {name}. Let me check this cancellation charge for you right now.'",
                "C": "Say: 'I apologize for the rip-off. I will refund you right away.'",
                "D": "Say: 'Please wait. Our drivers never lie, so you must have been late.'"
            },
            "answer": "B",
            "explanation": "USA customers appreciate active, direct help. Acknowledging their frustration and defining the issue professionally is key. 'Rip-off' means an overcharge or cheat.",
            "skill": "Slang Understanding & Empathy"
        },
        {
            "text": "An American client writes: 'My driver is taking a massive detour, I'm going to beat the clock to my meeting at {location}. Can you ping him?' What does 'beat the clock' mean?",
            "scenario": "USA rider in a hurry",
            "options": {
                "A": "It means to damage the clock in the car.",
                "B": "It means to arrive or finish before a deadline/limit. You should reassure the customer and check the route immediately.",
                "C": "It means they want to pay by cash instead.",
                "D": "It means they are canceling the ride."
            },
            "answer": "B",
            "explanation": "'Beat the clock' means to finish or arrive before a certain time. Recognizing this urgency helps you offer fast, reassuring support.",
            "skill": "American Idioms"
        },
        {
            "text": "A rider says: 'I need to split the fare with my coworker for the trip to {location}. The app is acting up.' What is the best direct response?",
            "scenario": "Fare splitting issue",
            "options": {
                "A": "I'm sorry, you cannot split the fare. Please pay separately.",
                "B": "I understand you need to split the bill, {name}. Let me guide you on how to do it in the app, or I can check the trip status for you.",
                "C": "Wait for 24 hours and the system will split it automatically.",
                "D": "Why do you want to split the fare? It's easier if one person pays."
            },
            "answer": "B",
            "explanation": "USA users expect direct, practical guideance when app features like fare splitting fail or are confusing.",
            "skill": "Direct Problem Solving"
        },
        {
            "text": "A customer in {city} says: 'My ride hit a snag and now I'm stuck on the highway.' What does 'hit a snag' mean?",
            "scenario": "USA idiom check",
            "options": {
                "A": "The vehicle was involved in a severe crash.",
                "B": "Encountered an unexpected problem or obstacle.",
                "C": "The driver took a wrong exit on purpose.",
                "D": "The app stopped responding."
            },
            "answer": "B",
            "explanation": "'Hit a snag' means encountering a minor or unexpected obstacle. Identifying this quickly helps you provide appropriate guidance.",
            "skill": "American English Vocabulary"
        },
        {
            "text": "A rider named {name} says: 'That trip was a bust. The driver's car was dirty and smelled like smoke.' What does 'a bust' mean?",
            "scenario": "Vehicle quality complaint",
            "options": {
                "A": "A complete failure or disappointment.",
                "B": "A very successful ride.",
                "C": "An expensive trip.",
                "D": "A fast ride."
            },
            "answer": "A",
            "explanation": "'A bust' is US slang for a failure or disappointment. Empathize with the poor quality and check if a refund/rating adjustment is needed.",
            "skill": "Slang & Quality Support"
        },
        {
            "text": "An American driver messages: 'The rider left a mess in my backseat and I want a cleaning fee. I have photos.' What is the best direct action?",
            "scenario": "Driver clean-up fee request",
            "options": {
                "A": "Tell the driver to clean it themselves as it's part of their job.",
                "B": "Say: 'Hey! Send me the pictures and I'll see what I can do.'",
                "C": "Say: 'Thank you for reporting this, {driver}. Let's get this sorted out. Please upload the photos here, and I'll review and apply the cleaning fee accordingly.'",
                "D": "Tell them to report it to the local police department."
            },
            "answer": "C",
            "explanation": "Professional driver support requires structured guidance, direct reassurance ('Let's get this sorted out'), and clear instructions.",
            "skill": "Driver Relations & Empathy"
        },
        {
            "text": "A US passenger writes: 'Can you pull up my receipt for trip #{id}?' What is the most natural, helpful reply?",
            "scenario": "Receipt request",
            "options": {
                "A": "No, you can check it yourself in your email inbox.",
                "B": "Sure, {name}. I can pull that up for you right now. I will also resend it to your registered email address.",
                "C": "Please wait while I search our servers. It takes about an hour.",
                "D": "Why do you need the receipt? Please verify your identity first."
            },
            "answer": "B",
            "explanation": "'Pull up' means to locate or retrieve information. Prompt and polite fulfillment of receipt requests is standard in US customer service.",
            "skill": "Action-Oriented Communication"
        },
        {
            "text": "A customer says: 'Just giving you a heads up, the driver was texting while driving.' What does 'heads up' mean?",
            "scenario": "Safety reporting",
            "options": {
                "A": "An advance warning or notification.",
                "B": "An angry complaint.",
                "C": "A polite greeting.",
                "D": "An official demand."
            },
            "answer": "A",
            "explanation": "A 'heads up' is a warning or alert. Safety reports like texting while driving must be escalated immediately to the Safety Team.",
            "skill": "Safety Escalation & Slang"
        },
        {
            "text": "A customer in {city} chats: 'My driver is driving around the block repeatedly. I think he is trying to inflate the fare.' What is the best way to handle this?",
            "scenario": "Fare inflation concern",
            "options": {
                "A": "Tell them the driver knows the route better than they do.",
                "B": "Say: 'I see what you mean, {name}. Let me check the GPS path of your ride in real-time and review the fare calculation. If there's an error, I will adjust it for you.'",
                "C": "Suggest that they cancel the ride and call another one.",
                "D": "Disconnect the chat as it's a dispute in progress."
            },
            "answer": "B",
            "explanation": "USA customers appreciate active monitoring and assurance that their money is protected against fare inflation.",
            "skill": "Fraud & Route Verification"
        },
        {
            "text": "A US client says: 'I'm in a bind. I left my laptop in the trunk and my flight leaves in 2 hours.' What does 'in a bind' mean?",
            "scenario": "Lost item urgency",
            "options": {
                "A": "In a secure position.",
                "B": "In a difficult or tight situation.",
                "C": "Very angry and aggressive.",
                "D": "Satisfied with support."
            },
            "answer": "B",
            "explanation": "'In a bind' means in distress or a difficult situation. High-urgency lost items (like laptops, passports) before flights need immediate outreach to the driver.",
            "skill": "Urgency Handling & Idioms"
        }
    ]
    
    random.seed(42)
    id_counter = 1
    
    # First, populate the base templates with different values
    for i in range(20):
        for template in templates:
            name = random.choice(USA_NAMES)
            driver = random.choice(DRIVER_NAMES)
            city = random.choice(CITIES[:5])
            price = random.choice(AMOUNTS[:6])
            item = random.choice(ITEMS)
            location = random.choice(["LAX Airport", "Downtown", "Broadway", "Times Square", "Union Station"])
            ride_id = random.randint(100000, 999999)
            
            q_text = template["text"].format(
                name=name, driver=driver, city=city, price=price, item=item, location=location, id=ride_id
            )
            
            opts = {}
            for key, val in template["options"].items():
                opts[key] = val.format(
                    name=name, driver=driver, city=city, price=price, item=item, location=location, id=ride_id
                )
                
            questions.append(make_question(
                q_id=id_counter,
                question=q_text,
                scenario=template["scenario"],
                options=opts,
                answer=template["answer"],
                explanation=template["explanation"].format(name=name, price=price),
                skill=template["skill"]
            ))
            id_counter += 1
            if len(questions) >= 200:
                break
        if len(questions) >= 200:
            break
            
    while len(questions) < 200:
        name = random.choice(USA_NAMES)
        city = random.choice(CITIES[:5])
        price = random.choice(AMOUNTS[:6])
        questions.append(make_question(
            q_id=id_counter,
            question=f"A rider from {city} named {name} writes: 'I was charged an extra {price} for a toll, but we never crossed any toll bridge!' What is your direct action?",
            scenario="USA Toll dispute",
            options={
                "A": "Tell them tolls are automated and they cannot be refunded.",
                "B": "Say: 'Let me pull up the trip route map, {name}. If we verify that no toll road was crossed, I'll refund the {price} toll charge instantly.'",
                "C": "Tell them to dispute it with their credit card company.",
                "D": "Say: 'Relax. It is only {price}. You shouldn't worry about it.'"
            },
            answer="B",
            explanation="Verify the route map and refund incorrect toll charges. Direct, clear, and reassuring tone is preferred.",
            skill="Billing Dispute Resolution"
        ))
        id_counter += 1
        
    return questions

# 2. EUROPE CUSTOMERS DATA GENERATION (Polite, Structured, GDPR, Spelling, Accents)
def generate_europe_questions():
    questions = []
    
    templates = [
        {
            "text": "A European customer named {name} writes: 'I left my {item} in the boot of the vehicle.' What does 'boot' refer to?",
            "scenario": "European terminology query",
            "options": {
                "A": "The driver's footwear.",
                "B": "The glove compartment.",
                "C": "The trunk of the car.",
                "D": "The back seat."
            },
            "answer": "C",
            "explanation": "In UK and parts of Europe, 'boot' is used to refer to the trunk of a car. Knowing regional terms prevents confusion.",
            "skill": "European Terminology"
        },
        {
            "text": "A client from Germany asks for a complete invoice detailing the VAT charges. What is the most appropriate professional response?",
            "scenario": "Invoice and VAT request",
            "options": {
                "A": "We don't send invoices. You can see it on the screen.",
                "B": "Sure, {name}. I have generated your official VAT invoice for trip #{id} and emailed it to your registered address in PDF format.",
                "C": "Invoices are only for premium users. Please upgrade.",
                "D": "Please write a physical letter to our headquarters for VAT details."
            },
            "answer": "B",
            "explanation": "European customers, especially in Germany, are highly detail-oriented and often need PDF invoices with VAT (Value Added Tax) details for expense tracking.",
            "skill": "Professional Support"
        },
        {
            "text": "Under GDPR regulations, a customer named {name} from {city} asks: 'Please delete all my personal data and trip history from your systems.' How must you handle this?",
            "scenario": "GDPR data deletion request",
            "options": {
                "A": "Delete the account immediately without verification.",
                "B": "Explain that we cannot delete data due to tax rules and ignore the request.",
                "C": "Acknowledge the request politely, verify their identity, and guide them through our official GDPR privacy portal or escalate to the Privacy Team.",
                "D": "Tell them to delete the app and the data will delete itself."
            },
            "answer": "C",
            "explanation": "GDPR compliance is critical in Europe. Requests for data deletion (Right to Be Forgotten) must be handled through verified privacy protocols or escalated to privacy specialists.",
            "skill": "Privacy & GDPR Compliance"
        },
        {
            "text": "A French passenger named {name} writes: 'The driver was extremely discourteous and didn't greet me when I entered.' What is the best tone to use?",
            "scenario": "European courtesy complaint",
            "options": {
                "A": "Say: 'Drivers are not required to greet you. They just drive.'",
                "B": "Say: 'I apologize for the lack of courtesy, {name}. Professionalism and respect are very important to us. I will record this feedback to review the driver's service.'",
                "C": "Say: 'Maybe the driver was in a bad mood, let it go.'",
                "D": "Say: 'I will deactivate the driver immediately.'"
            },
            "answer": "B",
            "explanation": "European customers expect polite, structured, and formal customer service. Validate their expectation of courtesy and log the feedback formally.",
            "skill": "Tone & Courtesy"
        },
        {
            "text": "A customer in London writes: 'I was charged extra because the driver got stuck at a roundabout.' What is a 'roundabout'?",
            "scenario": "UK terminology",
            "options": {
                "A": "A circular intersection or traffic circle.",
                "B": "A dead end street.",
                "C": "A highway toll booth.",
                "D": "A construction zone."
            },
            "answer": "A",
            "explanation": "'Roundabout' is the British term for a circular road junction (traffic circle).",
            "skill": "UK English Vocabulary"
        },
        {
            "text": "A customer in Berlin says: 'The driver refused to take my dog. I am blind and this was a guide dog.' What is the correct policy?",
            "scenario": "Service animal policy in EU",
            "options": {
                "A": "Tell them drivers can choose whether to allow animals or not.",
                "B": "Under the law and Uber policy, service animals must be accommodated. Acknowledge this immediately, apologize, refund any cancellation fee, and escalate to the compliance team.",
                "C": "Tell them to book a special animal ride and pay extra.",
                "D": "Ask them to prove their blindness first."
            },
            "answer": "B",
            "explanation": "Service animal accommodation is a legal requirement in Europe (e.g. UK Equality Act). Refusal of a guide dog is a severe policy violation and must be escalated.",
            "skill": "Policy & Legal Compliance"
        },
        {
            "text": "A European customer messages: 'I'm queueing for a taxi because my Uber never showed up.' What does 'queueing' mean?",
            "scenario": "UK slang",
            "options": {
                "A": "Waiting in a line.",
                "B": "Paying with cash.",
                "C": "Calling the police.",
                "D": "Writing a review."
            },
            "answer": "A",
            "explanation": "'Queueing' means waiting in a line. In this situation, check the driver's location and issue a refund/credit if the driver cancelled incorrectly.",
            "skill": "UK English Vocabulary"
        },
        {
            "text": "A customer from {city} writes: 'I am on holiday and the driver refused to put my heavy cases in the bonnet.' What is wrong with the customer's request?",
            "scenario": "Car parts vocabulary check",
            "options": {
                "A": "Heavy cases belong in the boot (trunk), not the bonnet (hood), which covers the engine.",
                "B": "Passengers must carry all bags on their laps.",
                "C": "Uber does not allow heavy luggage.",
                "D": "The bonnet is the passenger seat."
            },
            "answer": "A",
            "explanation": "In UK/EU, 'bonnet' is the car hood (covering the engine). Luggage goes in the 'boot' (trunk). Politely clarify if there was a language/parts confusion.",
            "skill": "Vehicle Terminology"
        },
        {
            "text": "A customer from the Netherlands writes: 'Your driver drove past the roundabout and took a petrol station exit.' What does 'petrol' mean?",
            "scenario": "EU vocabulary",
            "options": {
                "A": "Diesel engine oil.",
                "B": "Gasoline (gas).",
                "C": "Electric charging station.",
                "D": "A restaurant."
            },
            "answer": "B",
            "explanation": "'Petrol' is the British/European term for gasoline.",
            "skill": "Language Differences"
        },
        {
            "text": "A customer named {name} from {city} writes: 'I received a bill for a toll road, but the driver didn't tell me this route had tolls.' How do you structure your explanation?",
            "scenario": "Structured billing response",
            "options": {
                "A": "Write a short sentence: 'Tolls are added automatically. Bye.'",
                "B": "Provide a structured, polite breakdown: 1. Confirm the trip ID; 2. Explain how toll fees are calculated and added; 3. Apologize for the lack of communication from the driver.",
                "C": "Tell them to contact the toll authority directly.",
                "D": "Offer a full refund of the entire fare to avoid any argument."
            },
            "answer": "B",
            "explanation": "European customers value clear, structured explanations (often numbered or bulleted) that detail the 'why' behind charges.",
            "skill": "Structured Writing"
        }
    ]
    
    random.seed(43)
    id_counter = 1
    for i in range(20):
        for template in templates:
            name = random.choice(EU_NAMES)
            city = random.choice(CITIES[5:10])
            price = random.choice(AMOUNTS[6:12])
            item = random.choice(ITEMS)
            ride_id = random.randint(100000, 999999)
            
            q_text = template["text"].format(name=name, city=city, price=price, item=item, id=ride_id)
            opts = {}
            for key, val in template["options"].items():
                opts[key] = val.format(name=name, city=city, price=price, item=item, id=ride_id)
                
            questions.append(make_question(
                q_id=id_counter,
                question=q_text,
                scenario=template["scenario"],
                options=opts,
                answer=template["answer"],
                explanation=template["explanation"].format(name=name, price=price),
                skill=template["skill"]
            ))
            id_counter += 1
            if len(questions) >= 200:
                break
        if len(questions) >= 200:
            break
            
    while len(questions) < 200:
        name = random.choice(EU_NAMES)
        city = random.choice(CITIES[5:8])
        questions.append(make_question(
            q_id=id_counter,
            question=f"A customer from {city} named {name} asks: 'Can you confirm if my credit card details are stored securely?' Under privacy rules, what must you do?",
            scenario="European privacy query",
            options={
                "A": "Tell them we don't know and they should contact their bank.",
                "B": "Say: 'Hello {name}. I can confirm that your payment details are fully encrypted and secure in accordance with GDPR regulations. We do not store raw card numbers on our customer support side.'",
                "C": "Send them a screenshot of their account settings showing their full card number.",
                "D": "Ignore the message as it is not about a ride."
            },
            answer="B",
            explanation="Assure the customer of data security using professional language. Never share raw card numbers.",
            skill="Privacy & Trust"
        ))
        id_counter += 1
        
    return questions

# 3. EAST ASIA CUSTOMERS DATA GENERATION (Respectful, Face-Saving, Apologies, Patience)
def generate_east_asia_questions():
    questions = []
    
    templates = [
        {
            "text": "A Japanese customer named {name} writes: 'I apologize for causing any trouble, but the driver missed my pickup spot and I had to walk in the rain.' What is the best tone to respond with?",
            "scenario": "Japanese customer politeness handling",
            "options": {
                "A": "Say: 'It's fine, at least you got your ride eventually.'",
                "B": "Say: 'Thank you for your message. I am deeply sorry for the inconvenience and discomfort you experienced due to the missed pickup. We have refunded your fare as a gesture of goodwill.'",
                "C": "Say: 'Why didn't you call the driver? It is your fault for not checking the GPS.'",
                "D": "Say: 'Okay. I will refund you {price}. Please rate us 5 stars.'"
            },
            "answer": "B",
            "explanation": "East Asian customers, especially from Japan, appreciate deep politeness, formal apologies, and sincere gestures when their service expectations are not met.",
            "skill": "Respectful Apology"
        },
        {
            "text": "An East Asian customer says: 'The driver was talking very loudly on his phone. It was slightly uncomfortable.' How do you address this complaint?",
            "scenario": "Indirect complaint handling",
            "options": {
                "A": "Ignore it because 'slightly uncomfortable' means it is not a big issue.",
                "B": "Acknowledge the feedback respectfully: 'Thank you for sharing your experience, {name}. We hold our drivers to high professional standards. I will pass your feedback to the review team to ensure a quiet environment.'",
                "C": "Deactivate the driver's phone permissions.",
                "D": "Tell the passenger they should have told the driver to shut up."
            },
            "answer": "B",
            "explanation": "East Asian customers often express dissatisfaction indirectly ('slightly uncomfortable' or 'a bit troubled'). Support agents must read between the lines and take complaints seriously.",
            "skill": "Reading Indirect Signals"
        },
        {
            "text": "A customer in Seoul named {name} has been charged a cancellation fee. They write: 'I arrived at the pin but the driver left. Please review this.' How should you decline a refund if the driver waited the full 5 minutes?",
            "scenario": "Delivering negative news politely",
            "options": {
                "A": "Say: 'We cannot refund you. The driver waited 5 minutes. You were late.'",
                "B": "Say: 'While I understand this is disappointing, {name}, our system shows the driver waited at the pickup location for the required 5 minutes. To be fair to the driver's time, we are unable to refund this fee. Thank you for understanding.'",
                "C": "Say: 'No refund. Rules are rules.'",
                "D": "Say: 'Please check your watch. You were late.'"
            },
            "answer": "B",
            "explanation": "When delivering negative news to East Asian clients, maintain high politeness, provide the reasoning clearly, and close with appreciation for their understanding to maintain harmony.",
            "skill": "Polite Refusals"
        },
        {
            "text": "A customer from Singapore named {name} writes: 'The driver didn't want to follow my GPS route and went the long way, very sian.' What does 'sian' mean in Singlish?",
            "scenario": "Singapore English understanding",
            "options": {
                "A": "Happy and excited.",
                "B": "Bored, frustrated, or tired. You should check the route for fare inflation and apologize for the annoyance.",
                "C": "Fast and efficient.",
                "D": "Cheated by price."
            },
            "answer": "B",
            "explanation": "'Sian' is a Singlish term expressing boredom, frustration, or exhaustion. Acknowledging this mood and validating their frustration is key.",
            "skill": "Local Slang Comprehension"
        },
        {
            "text": "Why should you avoid using a customer's first name immediately in communication with traditional East Asian clients, unless they invite it?",
            "scenario": "Cultural naming conventions",
            "options": {
                "A": "Because first names are secret in Asia.",
                "B": "Using first names immediately can be perceived as overly familiar or disrespectful. Addressing them as Mr./Ms. [Last Name] is safer and highly professional.",
                "C": "Because their names are too hard to pronounce.",
                "D": "It doesn't matter, everyone prefers first names globally."
            },
            "answer": "B",
            "explanation": "In many Asian cultures (Japan, South Korea, China), addressing someone by their first name on first contact can seem informal. Mr./Ms. or using full names respectfully is preferred.",
            "skill": "Address Protocol"
        },
        {
            "text": "A customer from Tokyo writes: 'I left my {item} in the vehicle. The driver is not picking up the phone. I am deeply concerned.' What is the best way to reassure them?",
            "scenario": "High anxiety lost item",
            "options": {
                "A": "Tell them to wait. The driver will call when they are free.",
                "B": "Say: 'I understand your concern, {name}. Please be assured that we will do our absolute best to contact the driver and secure your {item}. I will keep you updated every step of the way.'",
                "C": "Tell them to buy a replacement.",
                "D": "Explain that we are not responsible for lost items."
            },
            "answer": "B",
            "explanation": "Providing calm, structural reassurance and taking ownership of the search helps reduce the customer's anxiety and builds trust.",
            "skill": "Reassurance & Trust"
        }
    ]
    
    random.seed(44)
    id_counter = 1
    for i in range(20):
        for template in templates:
            name = random.choice(EAST_ASIA_NAMES)
            city = random.choice(CITIES[10:12])
            price = random.choice(AMOUNTS[:6])
            item = random.choice(ITEMS)
            ride_id = random.randint(100000, 999999)
            
            q_text = template["text"].format(name=name, city=city, price=price, item=item, id=ride_id)
            opts = {}
            for key, val in template["options"].items():
                opts[key] = val.format(name=name, city=city, price=price, item=item, id=ride_id)
                
            questions.append(make_question(
                q_id=id_counter,
                question=q_text,
                scenario=template["scenario"],
                options=opts,
                answer=template["answer"],
                explanation=template["explanation"].format(name=name, price=price),
                skill=template["skill"]
            ))
            id_counter += 1
            if len(questions) >= 200:
                break
        if len(questions) >= 200:
            break
            
    while len(questions) < 200:
        name = random.choice(EAST_ASIA_NAMES)
        city = random.choice(CITIES[10:12])
        questions.append(make_question(
            q_id=id_counter,
            question=f"A customer from {city} named {name} writes: 'I think there was a small error in my billing. It is not an issue, but I wanted to report it.' How do you react?",
            scenario="Minor error reporting",
            options={
                "A": "Since they said 'not an issue', close the ticket immediately.",
                "B": "Say: 'Thank you for your honesty and patience, Mr./Ms. {name}. Let me review the billing immediately. I will correct any discrepancy and send you the details.'",
                "C": "Tell them that we don't fix small errors under $1.",
                "D": "Ask them to submit a formal letter of complaint."
            },
            answer="B",
            explanation="East Asian customers appreciate thoroughness and honesty. Even minor reported errors should be addressed with full attention and respect.",
            skill="Attention to Detail"
        ))
        id_counter += 1
        
    return questions

# 4. AFRICA CUSTOMERS DATA GENERATION (Warm, Relational, Cash & Mobile Money)
def generate_africa_questions():
    questions = []
    
    templates = [
        {
            "text": "A customer in Nairobi named {name} messages: 'I tried paying for the ride using M-Pesa but the transaction failed. The driver is refusing to let me leave the vehicle.' How do you handle this high-stakes situation?",
            "scenario": "M-Pesa payment failure in Kenya",
            "options": {
                "A": "Tell the passenger to call the police themselves and close the chat.",
                "B": "Say: 'I am sorry to hear this, {name}. Please stay safe. I am contacting the driver immediately to resolve this and authorize the cash-out. Please tell the driver that Uber is resolving it now.'",
                "C": "Tell them to wait for 24 hours for the transaction to clear.",
                "D": "Explain that M-Pesa is a third-party app and not our problem."
            },
            "answer": "B",
            "explanation": "Mobile money (like M-Pesa in Kenya) is a primary payment option. A failed transaction causing a dispute in the car requires immediate driver outreach and calming support.",
            "skill": "High-Urgency Payment Resolution"
        },
        {
            "text": "A South African customer named {name} writes: 'The driver took a route that felt very unsafe. I am shaken up.' How do you address their safety concern?",
            "scenario": "Safety concern during route in SA",
            "options": {
                "A": "Explain that the driver was just avoiding traffic.",
                "B": "Say: 'I am very sorry to hear this, {name}. Your safety is our top priority. Let me review this route and pass this report directly to our dedicated Safety Team for investigation. Are you currently in a safe place?'",
                "C": "Tell them to write a review of the route on Google Maps.",
                "D": "Offer them a {price} discount on their next ride and close the chat."
            },
            "answer": "B",
            "explanation": "Safety concerns in South Africa must be treated with high empathy and immediate escalation to the Safety Team. Always check if the user is currently safe.",
            "skill": "Safety Protocols"
        },
        {
            "text": "A Nigerian client named {name} starts their message with: 'Good day. I hope this find you well. I want to report a fare issue.' What cultural element is important here?",
            "scenario": "African greeting etiquette",
            "options": {
                "A": "Greetings are wastes of time; ignore it and go straight to the refund.",
                "B": "African customers value warm, respectful greetings and relational check-ins. You should reply: 'Good day, {name}. I hope you are doing well too. Let me help you with that fare issue right away.'",
                "C": "Tell them not to send greetings because we have strict handling time metrics.",
                "D": "Answer with a short 'Hi. What is the issue?'"
            },
            "answer": "B",
            "explanation": "In many African cultures (e.g. Nigeria, Ghana), starting with a warm and polite greeting is expected. Mirroring this warmth builds rapport.",
            "skill": "Relational Tone & Warmth"
        },
        {
            "text": "A driver in Lagos writes: 'The rider didn't have cash and said they would transfer the money, but I haven't received it yet.' How do you assist?",
            "scenario": "Lagos Cash/Transfer dispute",
            "options": {
                "A": "Tell the driver to search for the passenger and collect the money.",
                "B": "Say: 'Hello. I understand this is frustrating. Let me look into this trip. We will verify the payment status and credit your driver wallet for the unpaid fare directly.'",
                "C": "Deactivate the rider's account immediately without checking.",
                "D": "Tell the driver that cash transfers are at their own risk."
            },
            "answer": "B",
            "explanation": "Direct bank transfers are common in Nigeria when cash is low. If a transfer fails, support should verify the ride details and ensure the driver is compensated according to policy.",
            "skill": "Driver Compensation"
        },
        {
            "text": "A passenger in Johannesburg says: 'My driver demanded that I pay extra cash for petrol because of the load shedding traffic.' What is the correct action?",
            "scenario": "Load shedding cash extortion",
            "options": {
                "A": "Tell them to pay because load shedding is difficult for everyone.",
                "B": "Apologize and explain that drivers must never demand extra cash. Refund the extra fee if they paid, and log a warning on the driver's profile.",
                "C": "Tell them to report the driver to the traffic police.",
                "D": "Ignore the report."
            },
            "answer": "B",
            "explanation": "Load shedding in SA causes traffic delays, but drivers demanding extra cash violates policy. Empathize with the rider, refund, and report the driver.",
            "skill": "Policy Violations"
        }
    ]
    
    random.seed(45)
    id_counter = 1
    for i in range(40):
        for template in templates:
            name = random.choice(AFRICA_NAMES)
            city = random.choice(CITIES[12:])
            price = random.choice(AMOUNTS[12:])
            item = random.choice(ITEMS)
            ride_id = random.randint(100000, 999999)
            
            q_text = template["text"].format(name=name, city=city, price=price, item=item, id=ride_id)
            opts = {}
            for key, val in template["options"].items():
                opts[key] = val.format(name=name, city=city, price=price, item=item, id=ride_id)
                
            questions.append(make_question(
                q_id=id_counter,
                question=q_text,
                scenario=template["scenario"],
                options=opts,
                answer=template["answer"],
                explanation=template["explanation"].format(name=name, price=price),
                skill=template["skill"]
            ))
            id_counter += 1
            if len(questions) >= 200:
                break
        if len(questions) >= 200:
            break
            
    while len(questions) < 200:
        name = random.choice(AFRICA_NAMES)
        city = random.choice(CITIES[12:])
        questions.append(make_question(
            q_id=id_counter,
            question=f"A rider in {city} named {name} asks: 'The driver cancelled the trip because I had cash. Why is this happening?' What is the correct response?",
            scenario="Cash ride cancellation",
            options={
                "A": "Tell them cash is not supported in their city anymore.",
                "B": "Say: 'Good day, {name}. I apologize for this experience. Drivers should accept cash rides if that option is selected. I have waived any cancellation fee and flagged this on the driver's account for review.'",
                "C": "Tell them cash rides are always cancelled.",
                "D": "Suggest they buy a credit card."
            },
            answer="B",
            explanation="Waive the fee and log the driver behavior. Cash is a critical payment option in these markets.",
            skill="Fee Waiver & Policy"
        ))
        id_counter += 1
        
    return questions

# 5. UBER SCENARIOS (Cleaning Fees, Service Animals, Lost Items, Route Disputes, Driver issues)
def generate_uber_scenarios():
    questions = []
    
    templates = [
        {
            "text": "A rider claims: 'I left my {item} in the vehicle yesterday. The driver is demanding cash to return it to me.' What is Uber's policy?",
            "scenario": "Lost item extortion",
            "options": {
                "A": "Tell the rider they must pay the driver whatever cash they want.",
                "B": "Explain that while Uber has a standard return fee that goes to the driver for their time, demanding extra cash is a policy violation. We will coordinate the return and warn the driver.",
                "C": "Tell them to report the driver for theft immediately.",
                "D": "Say that we do not interfere in lost items."
            },
            "answer": "B",
            "explanation": "Drivers are entitled to a standard return fee (e.g. $15) to cover their fuel and time, but extorting passengers for extra cash is prohibited. Support must mediate.",
            "skill": "Lost Item Policy"
        },
        {
            "text": "A driver messages: 'The passenger threw up in my backseat. I need a cleaning fee.' What documentation is mandatory to process this?",
            "scenario": "Cleaning fee documentation",
            "options": {
                "A": "Just the driver's word is enough.",
                "B": "Clear photos of the mess and a valid cleaning receipt or invoice from a professional cleaner detailing the service.",
                "C": "A copy of the driver's driver's license.",
                "D": "A police report."
            },
            "answer": "B",
            "explanation": "To charge a rider a cleaning fee (up to $150), the driver must submit clear photos of the mess and a valid professional cleaning invoice within 3 days.",
            "skill": "Documentation Verification"
        },
        {
            "text": "A rider writes: 'My driver took a very long route to my destination, costing me {price} more than the upfront estimate.' What is the review protocol?",
            "scenario": "Upfront fare adjustment",
            "options": {
                "A": "If the route was significantly longer due to driver error (not traffic), adjust the fare back to the upfront estimate and refund the difference.",
                "B": "Tell them the estimate is just an estimate, they must pay.",
                "C": "Refund the entire ride cost to keep the CSAT high.",
                "D": "Tell them to walk next time."
            },
            "answer": "A",
            "explanation": "Compare the actual GPS route with the planned route. If the driver made a clear error or took a detour without passenger consent, refund the difference.",
            "skill": "Fare Adjustment & Map Review"
        },
        {
            "text": "A driver complains: 'The passenger's child was only 3 years old and they didn't have a car seat, so I cancelled. I want a cancellation fee.' What is the policy?",
            "scenario": "Child seat safety cancellation",
            "options": {
                "A": "Tell the driver they should have driven anyway.",
                "B": "Support the driver's safety decision. Waive any impact on the driver's rating/rate and credit them a cancellation fee. Safety is our top priority.",
                "C": "Tell the driver they are suspended for refusing a child.",
                "D": "Ignore the ticket."
            },
            "answer": "B",
            "explanation": "Uber policy supports drivers who refuse rides due to lack of required child safety seats. The driver is eligible for a cancellation fee.",
            "skill": "Safety Policies"
        },
        {
            "text": "A rider says: 'My driver brought a friend who was sitting in the front seat. I felt extremely uncomfortable.' How do you handle this security concern?",
            "scenario": "Unauthorised co-rider",
            "options": {
                "A": "Tell the rider that ride-sharing allows drivers to bring friends.",
                "B": "Acknowledge the safety concern immediately. Explain that co-riders are strictly prohibited. Escalate to the safety and driver compliance teams for driver warning/deactivation.",
                "C": "Suggest the rider make friends with the co-rider.",
                "D": "Refund the ride and do nothing else."
            },
            "answer": "B",
            "explanation": "Uber policy strictly prohibits co-riders (anyone other than the driver and riders) in the vehicle. This is a safety violation and must be escalated.",
            "skill": "Safety Escalation"
        }
    ]
    
    random.seed(46)
    id_counter = 1
    for i in range(40):
        for template in templates:
            name = random.choice(USA_NAMES)
            city = random.choice(CITIES)
            price = random.choice(AMOUNTS[:6])
            item = random.choice(ITEMS)
            ride_id = random.randint(100000, 999999)
            
            q_text = template["text"].format(name=name, city=city, price=price, item=item, id=ride_id)
            opts = {}
            for key, val in template["options"].items():
                opts[key] = val.format(name=name, city=city, price=price, item=item, id=ride_id)
                
            questions.append(make_question(
                q_id=id_counter,
                question=q_text,
                scenario=template["scenario"],
                options=opts,
                answer=template["answer"],
                explanation=template["explanation"].format(name=name, price=price),
                skill=template["skill"]
            ))
            id_counter += 1
            if len(questions) >= 200:
                break
        if len(questions) >= 200:
            break
            
    while len(questions) < 200:
        name = random.choice(USA_NAMES)
        city = random.choice(CITIES)
        questions.append(make_question(
            q_id=id_counter,
            question=f"A rider in {city} asks: 'Can I travel with my cat in a standard Uber ride?' What is the pet policy?",
            scenario="Pet policy query",
            options={
                "A": "No, pets are never allowed.",
                "B": "Yes, standard rides always allow pets.",
                "C": "Pets are at the driver's discretion unless it is a service animal. For guaranteed pet travel, passengers should book an 'Uber Pet' ride.",
                "D": "Only dogs are allowed, cats are banned."
            },
            answer="C",
            explanation="Service animals must be allowed. Other pets are at the driver's discretion unless booking an Uber Pet ride.",
            skill="Uber Policies"
        ))
        id_counter += 1
        
    return questions

# 6. EMPATHY TRAINING (Active Listening, Validating, Positive Phrasing)
def generate_empathy_questions():
    questions = []
    
    templates = [
        {
            "text": "A customer writes: 'I am so stressed. I left my passport in your cab and my flight is in 3 hours.' Which response shows the best active listening and empathy?",
            "scenario": "Stressful lost passport",
            "options": {
                "A": "We are not responsible for left items. Please fill a form.",
                "B": "I understand how incredibly stressful this must be, especially with your flight leaving soon. Let me contact the driver immediately to help locate your passport.",
                "C": "Relax, passport can be remade at the embassy.",
                "D": "Why did you forget your passport? That is very careless."
            },
            "answer": "B",
            "explanation": "Active empathy involves validating the customer's specific emotion ('stressful') and urgency ('flight leaving soon'), and taking immediate action.",
            "skill": "Active Listening & Reassurance"
        },
        {
            "text": "A customer is complaining about a double payment: 'This app is stealing my money!' How do you frame the response using positive phrasing?",
            "scenario": "Double charge positive framing",
            "options": {
                "A": "We cannot refund you until we check the banks. Do not accuse us of stealing.",
                "B": "Let's get this resolved for you. I will check your payment history right now and ensure any extra charges are reversed to your account immediately.",
                "C": "You are wrong. It is just a temporary hold.",
                "D": "Please wait for 3 days and don't message us again."
            },
            "answer": "B",
            "explanation": "Positive framing focuses on resolution, action, and assistance, rather than defensiveness or negative rules.",
            "skill": "Positive Framing"
        },
        {
            "text": "Which of these phrases is considered 'Robotic/Scripted' and should be avoided in personalized live chat support?",
            "scenario": "Avoiding robotic phrases",
            "options": {
                "A": "I'll check that for you right now.",
                "B": "I am sorry for the inconvenience caused. Your satisfaction is our top priority. Please wait while I pull up your details.",
                "C": "Let's look at the trip map together to see what happened.",
                "D": "I understand you're disappointed with the route."
            },
            "answer": "B",
            "explanation": "Generic apologies like 'sorry for the inconvenience caused' sound robotic and impersonal in live chat. Personalized, conversational language is much better.",
            "skill": "Conversational Tone"
        },
        {
            "text": "A rider writes: 'The driver yelled at me and made me feel unsafe.' What is the best initial empathy statement?",
            "scenario": "Safety complaint empathy",
            "options": {
                "A": "I am sorry the driver was in a bad mood.",
                "B": "I am deeply sorry to hear about this experience. Feeling safe during a ride is absolutely essential, and I want to assure you we are taking this very seriously.",
                "C": "Please rate the driver 1 star and report him.",
                "D": "Did you say something to make him angry?"
            },
            "answer": "B",
            "explanation": "For safety issues, validate the customer's feeling of safety, apologize sincerely, and assure them of serious action.",
            "skill": "Safety Empathy"
        },
        {
            "text": "A passenger named {name} says: 'The app crashed during my ride and I couldn't see the price.' How do you show accountability?",
            "scenario": "App crash accountability",
            "options": {
                "A": "It is your phone's fault. Upgrade your device.",
                "B": "I apologize for the app crashing during your ride, {name}. I know how frustrating it is to not see your fare. Let me look up the exact fare details for you right now.",
                "C": "We don't guarantee app uptime. Read the terms of service.",
                "D": "Wait for the receipt to email you."
            },
            "answer": "B",
            "explanation": "Accountability means taking responsibility for the service failure (the app crashing) and moving directly to a solution.",
            "skill": "Accountability"
        }
    ]
    
    random.seed(47)
    id_counter = 1
    for i in range(40):
        for template in templates:
            name = random.choice(USA_NAMES)
            price = random.choice(AMOUNTS[:6])
            item = random.choice(ITEMS)
            ride_id = random.randint(100000, 999999)
            
            q_text = template["text"].format(name=name, price=price, item=item, id=ride_id)
            opts = {}
            for key, val in template["options"].items():
                opts[key] = val.format(name=name, price=price, item=item, id=ride_id)
                
            questions.append(make_question(
                q_id=id_counter,
                question=q_text,
                scenario=template["scenario"],
                options=opts,
                answer=template["answer"],
                explanation=template["explanation"].format(name=name, price=price),
                skill=template["skill"]
            ))
            id_counter += 1
            if len(questions) >= 200:
                break
        if len(questions) >= 200:
            break
            
    while len(questions) < 200:
        name = random.choice(USA_NAMES)
        questions.append(make_question(
            q_id=id_counter,
            question=f"A customer named {name} writes: 'I was charged for a ride I never took. I feel cheated.' What is the best empathy response?",
            scenario="Fraud allegation empathy",
            options={
                "A": "We didn't cheat you. Please check your bank card.",
                "B": "I understand how upsetting it is to see a charge for a ride you didn't take, {name}. Let's get this investigated and resolved for you immediately.",
                "C": "That is standard banking hold. Do not worry.",
                "D": "We do not refund unauthorized rides."
            },
            answer="B",
            explanation="Acknowledge the customer's feeling of being upset, and promise an immediate investigation.",
            skill="Empathy & Reassurance"
        ))
        id_counter += 1
        
    return questions

# 7. ESCALATION TRAINING (Safety, Threats, Abuse, Account Suspension)
def generate_escalation_questions():
    questions = []
    
    templates = [
        {
            "text": "A rider messages: 'I was in a car crash. The driver hit another car. I am bleeding.' What is your immediate action?",
            "scenario": "Severe accident report",
            "options": {
                "A": "Tell the rider to ask the driver for insurance details.",
                "B": "Immediately escalate to the Critical Incident Safety Team (L2 Safety), verify if emergency services are on site, and freeze the driver's account.",
                "C": "Tell them to wait for 24 hours and we will call them.",
                "D": "Offer a refund for the ride and close the ticket."
            },
            "answer": "B",
            "explanation": "Severe safety incidents involving injury must be escalated to the Critical Incident Safety Team immediately. Check safety status first.",
            "skill": "Critical Safety Escalation"
        },
        {
            "text": "A passenger writes: 'The driver touched my leg on purpose and made inappropriate comments. I am calling the media.' What protocol is followed?",
            "scenario": "Physical harassment report",
            "options": {
                "A": "Tell them it was probably an accident and close the chat.",
                "B": "Apologize, deactivate the driver immediately, and escalate the case to the Safety and legal response team as a priority safety incident.",
                "C": "Offer them a free coupon to not contact the media.",
                "D": "Ask them for video proof of the touch."
            },
            "answer": "B",
            "explanation": "Sexual harassment and physical safety violations are zero-tolerance issues. Driver deactivation and escalation to specialized Safety/Legal teams are mandatory.",
            "skill": "Harassment Protocol"
        },
        {
            "text": "A rider says: 'If you don't refund my {price} immediately, I am going to sue your company and contact my lawyer.' How do you respond to legal threats?",
            "scenario": "Legal action threat",
            "options": {
                "A": "Tell them: 'Go ahead, we have many lawyers.'",
                "B": "Acknowledge the dispute. Remain professional. Avoid arguing. State the final policy decision clearly and transfer the chat to the Legal Escalations Team.",
                "C": "Apologize and give a full refund instantly to avoid a lawsuit.",
                "D": "Disconnect the chat immediately without responding."
            },
            "answer": "B",
            "explanation": "When legal action is threatened, remain calm, do not argue, state the policy, and escalate the ticket to the Legal Escalations Team.",
            "skill": "Legal Threat Handling"
        },
        {
            "text": "A user is using abusive language in chat: 'You guys are f***ing idiots. Solve my issue now!' What is the professional boundary protocol?",
            "scenario": "Abusive customer handling",
            "options": {
                "A": "Abuse them back using the same language.",
                "B": "Politely warn the customer: 'I want to help you, but I must ask you to maintain a professional tone. If the abusive language continues, I will have to end this chat session.'",
                "C": "Disconnect the chat instantly without warning.",
                "D": "Ignore the abuse and continue apologizing."
            },
            "answer": "B",
            "explanation": "Set clear, professional boundaries. Warn the customer politely before terminating the chat for abusive behavior.",
            "skill": "Boundary Setting & Tone Control"
        },
        {
            "text": "A driver messages: 'The rider was racially abusive towards me and kicked my car.' What is the driver support action?",
            "scenario": "Discrimination and vandalism report",
            "options": {
                "A": "Tell the driver to clean the car and ignore the comments.",
                "B": "Acknowledge the distress, reassure the driver that discrimination is not tolerated, block the rider from matching with this driver, and escalate to the compliance team to suspend the rider's account.",
                "C": "Tell them to report the rider to their local community leader.",
                "D": "Suspend the driver's account."
            },
            "answer": "B",
            "explanation": "Discrimination and vehicle vandalism violate Uber's community guidelines. Empathize with the driver, block matching, and escalate to compliance for rider suspension.",
            "skill": "Driver Protection & Compliance"
        }
    ]
    
    random.seed(48)
    id_counter = 1
    for i in range(40):
        for template in templates:
            name = random.choice(USA_NAMES)
            price = random.choice(AMOUNTS[:6])
            item = random.choice(ITEMS)
            ride_id = random.randint(100000, 999999)
            
            q_text = template["text"].format(name=name, price=price, item=item, id=ride_id)
            opts = {}
            for key, val in template["options"].items():
                opts[key] = val.format(name=name, price=price, item=item, id=ride_id)
                
            questions.append(make_question(
                q_id=id_counter,
                question=q_text,
                scenario=template["scenario"],
                options=opts,
                answer=template["answer"],
                explanation=template["explanation"].format(name=name, price=price),
                skill=template["skill"]
            ))
            id_counter += 1
            if len(questions) >= 200:
                break
        if len(questions) >= 200:
            break
            
    while len(questions) < 200:
        name = random.choice(USA_NAMES)
        questions.append(make_question(
            q_id=id_counter,
            question=f"A rider named {name} writes: 'I left my wallet in the car and the driver is refusing to return it. He said he threw it out of the window.' What category is this?",
            scenario="Driver theft allegation",
            options={
                "A": "Standard lost item request.",
                "B": "Serious driver compliance escalation (theft/property destruction). Transfer to the Priority Incident Team.",
                "C": "Billing dispute.",
                "D": "Ignore request."
            },
            answer="B",
            explanation="Allegations of intentional property damage or theft by drivers must be escalated to the compliance team for review and account lock.",
            skill="Priority Escalations"
        ))
        id_counter += 1
        
    return questions

# 8. PROFESSIONAL VOCABULARY (SLA, CSAT, Metrics, Active Voice, Formality)
def generate_vocabulary_questions():
    questions = []
    
    templates = [
        {
            "text": "What does 'SLA' stand for in customer service operations?",
            "scenario": "Customer service metric definitions",
            "options": {
                "A": "System Level Agreement.",
                "B": "Service Level Agreement (the time window in which support is expected to respond or resolve an issue).",
                "C": "Service Logic Analysis.",
                "D": "Standard Level Assessment."
            },
            "answer": "B",
            "explanation": "SLA (Service Level Agreement) defines the agreed-upon time standards for responding to and resolving customer tickets.",
            "skill": "Support Terminology"
        },
        {
            "text": "What is 'CSAT' and how is it measured?",
            "scenario": "Customer Satisfaction Metric",
            "options": {
                "A": "Customer Service Action Time, measured in minutes.",
                "B": "Customer Satisfaction score, measured through post-interaction customer surveys (usually out of 5 stars or percentage).",
                "C": "Customer Security and Trust score.",
                "D": "Company Service Assessment Test."
            },
            "answer": "B",
            "explanation": "CSAT (Customer Satisfaction) is a crucial metric reflecting how satisfied customers are with the support they received.",
            "skill": "Customer Service Metrics"
        },
        {
            "text": "Which of these is written in the 'Active Voice', which is preferred in US customer communications?",
            "scenario": "Active vs. Passive voice",
            "options": {
                "A": "Your refund was processed by our team.",
                "B": "We processed your refund.",
                "C": "A process of refunding has been initiated.",
                "D": "Your account has been credited."
            },
            "answer": "B",
            "explanation": "Active voice ('We processed your refund') is direct, confident, and shorter than passive voice ('Your refund was processed by us').",
            "skill": "Grammatical Structure"
        },
        {
            "text": "Instead of saying 'You must upload your document', which professional alternative should you use to sound collaborative?",
            "scenario": "Polite instruction phrasing",
            "options": {
                "A": "Do it now or your account will close.",
                "B": "Please upload your document so we can activate your account.",
                "C": "Document upload is requested from your side.",
                "D": "You have to send us the papers."
            },
            "answer": "B",
            "explanation": "Using 'Please upload...' or 'I suggest uploading...' sounds polite and collaborative, rather than commanding ('you must').",
            "skill": "Collaborative Phrasing"
        },
        {
            "text": "What does 'FCR' stand for and why is it important?",
            "scenario": "First Contact Resolution metric",
            "options": {
                "A": "First Contact Resolution (solving the customer's problem in their very first interaction without transfers or follow-ups).",
                "B": "Final Customer Response.",
                "C": "Frequently Customer Route.",
                "D": "First Chat Review."
            },
            "answer": "A",
            "explanation": "FCR (First Contact Resolution) measures the ability of support to resolve issues immediately, which is a major driver of high CSAT.",
            "skill": "Service Quality Metrics"
        }
    ]
    
    random.seed(49)
    id_counter = 1
    for i in range(40):
        for template in templates:
            name = random.choice(USA_NAMES)
            price = random.choice(AMOUNTS[:6])
            item = random.choice(ITEMS)
            ride_id = random.randint(100000, 999999)
            
            q_text = template["text"].format(name=name, price=price, item=item, id=ride_id)
            opts = {}
            for key, val in template["options"].items():
                opts[key] = val.format(name=name, price=price, item=item, id=ride_id)
                
            questions.append(make_question(
                q_id=id_counter,
                question=q_text,
                scenario=template["scenario"],
                options=opts,
                answer=template["answer"],
                explanation=template["explanation"].format(name=name, price=price),
                skill=template["skill"]
            ))
            id_counter += 1
            if len(questions) >= 200:
                break
        if len(questions) >= 200:
            break
            
    while len(questions) < 200:
        questions.append(make_question(
            q_id=id_counter,
            question=f"What is 'AHT' in contact center operations and how does it relate to chat?",
            scenario="Average Handling Time metric",
            options={
                "A": "Account Holder Transfer, the time to transfer a bank account.",
                "B": "Average Handling Time (the total duration spent typing and resolving a single customer chat). Managing AHT efficiently while ensuring high quality is critical.",
                "C": "Annual Holiday Time.",
                "D": "All Hour Tracking."
            },
            answer="B",
            explanation="AHT (Average Handling Time) measures efficiency. Lowering AHT without compromising service quality is key for agents.",
            skill="Efficiency Metrics"
        ))
        id_counter += 1
        
    return questions

# 9. SOFT SKILLS
def generate_soft_skills():
    questions = []
    templates = [
        {
            "text": "A rider named {name} writes: 'I am so frustrated! I have been waiting for my driver for 15 minutes in the heat. Your service is terrible.' What is the best soft skill response?",
            "scenario": "Handling customer frustration and wait time",
            "options": {
                "A": "I understand your frustration, {name}. I apologize for the delay. Let me check the driver's current status and see how we can get this resolved for you right away.",
                "B": "Please do not use that tone. The driver is stuck in traffic. Wait for some more time.",
                "C": "The ride is only {price} so please do not worry. It is normal to wait in peak hours.",
                "D": "I can cancel your ride if you want, but you will pay a fee."
            },
            "answer": "A",
            "explanation": "Active empathy, sincere apology for the wait time, and taking immediate ownership of the check represents the best soft skill behavior. Never admonish the customer's tone.",
            "skill": "Patience & Empathy"
        },
        {
            "text": "You must inform a customer that their request for a refund of a {price} fare has been denied because the trip was completed successfully. How do you deliver this bad news professionally?",
            "scenario": "Delivering negative news",
            "options": {
                "A": "Your refund is denied. The driver completed the ride. Case closed.",
                "B": "I understand this isn't the outcome you hoped for, {name}. After reviewing the trip details, we verified the route was completed successfully. Therefore, we are unable to process a refund. Thank you for your understanding.",
                "C": "We cannot give you {price} because that would be a loss for our driver. Please pay.",
                "D": "You completed the trip so why are you asking for a refund? That is not allowed."
            },
            "answer": "B",
            "explanation": "Delivering bad news requires validation of feelings, transparency of decision-making, clear policy stating, and closing with professional courtesy.",
            "skill": "Diplomacy & Tact"
        },
        {
            "text": "A driver messages: 'The passenger was extremely rude to me, slamming my doors and yelling.' What soft skill is critical here?",
            "scenario": "De-escalating driver issues",
            "options": {
                "A": "Acknowledge the driver's distress: 'I am sorry to hear this, {driver}. Safety and respect are important to us. Let me log this on the rider's profile and ensure you aren't matched with them again.'",
                "B": "Tell the driver to report it to the police and don't accept passengers who look rude.",
                "C": "Tell them slamming doors is normal and they shouldn't worry about it.",
                "D": "Ignore the ticket as it is a passenger rating dispute."
            },
            "answer": "A",
            "explanation": "Drivers are our partners. Validating their feelings, reassuring them of safety rules, blocking matches, and noting the rider profile shows high-quality driver support.",
            "skill": "Partner De-escalation"
        },
        {
            "text": "A customer says: 'The app shows my driver is 5 minutes away, but he is going in the wrong direction. I need to get to {location} immediately.' How do you show accountability?",
            "scenario": "App GPS error support",
            "options": {
                "A": "Say: 'Let me look into this, {name}. I will contact the driver to verify their direction and ensure they are heading your way to {location} now.'",
                "B": "Say: 'The GPS has a delay. Please wait for the driver to turn around.'",
                "C": "Say: 'You should cancel the ride and book another one.'",
                "D": "Say: 'The driver knows what he is doing, please do not interfere.'"
            },
            "answer": "A",
            "explanation": "Accountability means taking charge, offering to verify with the driver directly, and giving the customer an active timeline.",
            "skill": "Accountability & Solution"
        },
        {
            "text": "Which of these displays a 'Collaborative and Positive Tone' instead of a demanding one?",
            "scenario": "Tone adjustment check",
            "options": {
                "A": "You must verify your email or I will close the chat.",
                "B": "To help secure your account, could you please verify your registered email address? I'll be happy to assist you once that is confirmed.",
                "C": "Verify your email now.",
                "D": "It is our policy that you send email details first."
            },
            "answer": "B",
            "explanation": "Using collaborative requests ('could you please...') and stating the positive reason ('to help secure your account...') improves CSAT significantly.",
            "skill": "Positive Tone"
        }
    ]
    random.seed(50)
    id_counter = 1
    for i in range(40):
        for template in templates:
            name = random.choice(USA_NAMES)
            driver = random.choice(DRIVER_NAMES)
            city = random.choice(CITIES)
            price = random.choice(AMOUNTS)
            location = random.choice(["the office", "the station", "the airport", "my hotel"])
            q_text = template["text"].format(name=name, driver=driver, city=city, price=price, location=location)
            opts = {}
            for key, val in template["options"].items():
                opts[key] = val.format(name=name, driver=driver, city=city, price=price, location=location)
            questions.append(make_question(
                q_id=id_counter,
                question=q_text,
                scenario=template["scenario"],
                options=opts,
                answer=template["answer"],
                explanation=template["explanation"],
                skill=template["skill"]
            ))
            id_counter += 1
            if len(questions) >= 200:
                break
        if len(questions) >= 200:
            break
    while len(questions) < 200:
        name = random.choice(USA_NAMES)
        questions.append(make_question(
            q_id=id_counter,
            question=f"A rider named {name} writes: 'I had a terrible experience with my driver. I will never use your app again!' What soft skill is most important here?",
            scenario="Handling user attrition warning",
            options={
                "A": "Tell them they are free to use other apps.",
                "B": "Acknowledge the severity: 'I am deeply sorry you had such a bad experience, {name}. This is definitely not the standard we expect. Please tell me what happened so I can make this right.'",
                "C": "Offer a $2 coupon without checking what happened.",
                "D": "Tell them that we have millions of users so it's fine."
            },
            answer="B",
            explanation="Customer retention requires serious empathy, active inquiry, and demonstrating that the company cares about individual experiences.",
            skill="Customer Retention & Empathy"
        ))
        id_counter += 1
    return questions

# 10. ACTIVE READING
def generate_active_reading():
    questions = []
    templates = [
        {
            "text": "A customer sends a long message: 'I was on my way to my wedding anniversary dinner at {location} around 8 PM. The driver Marcus was nice but got lost near the highway. Also, I think I dropped my gold watch in the backseat. I need to get it back immediately because it was a gift.' What is the most critical/urgent issue to address first?",
            "scenario": "Identifying core issue in verbose message",
            "options": {
                "A": "The driver getting lost on the highway.",
                "B": "The wedding anniversary dinner.",
                "C": "The lost gold watch in the backseat (urgent lost item recovery).",
                "D": "The nice behavior of Driver Marcus."
            },
            "answer": "C",
            "explanation": "Active reading requires distinguishing between background details (anniversary, nice driver, wrong route) and the urgent, actionable issue (a high-value lost item: a gold watch).",
            "skill": "Core Issue Identification"
        },
        {
            "text": "A user writes: 'My card was charged {price} for a ride in {city} yesterday, but I was at home sleeping! I didn't authorize this! This is fraud! Lock my account!' What is the customer's emotional subtext and requested action?",
            "scenario": "Reading emotional state & goal",
            "options": {
                "A": "The user is calm and wants a receipt.",
                "B": "The user is highly anxious/angry about fraud, and wants their account secured and the charge investigated.",
                "C": "The user is happy and wants to book another ride.",
                "D": "The user is testing our system."
            },
            "answer": "B",
            "explanation": "Active reading involves recognizing the emotional state (highly anxious/angry, using exclamation marks) and the explicit request (unauthorized charge check and account security).",
            "skill": "Emotion & Goal Identification"
        },
        {
            "text": "A passenger messages: 'I requested a ride to the airport for my daughter named Emily. She is waiting near the Starbucks with a blue suitcase. The driver Carlos drove past without picking her up.' What are the key details for the driver search?",
            "scenario": "Extracting pickup details",
            "options": {
                "A": "The passenger is the writer, waiting inside Starbucks.",
                "B": "The passenger is Emily, waiting near Starbucks with a blue suitcase.",
                "C": "The passenger is Carlos, waiting at the airport.",
                "D": "The daughter has no luggage."
            },
            "answer": "B",
            "explanation": "Active reading requires identifying that the account holder is not the passenger. The passenger is Emily, located near Starbucks with a blue suitcase.",
            "skill": "Detail Extraction"
        },
        {
            "text": "A rider messages: 'I got into the car and it smelled like smoke. I asked the driver to roll down the windows, but he refused. Then he took a longer route which cost me {price} more than the upfront fare.' What are the two distinct issues here?",
            "scenario": "Analyzing multi-issue complaints",
            "options": {
                "A": "Smell of smoke and driver's nice rating.",
                "B": "Vehicle cleanliness/driver service issue (smoke and windows) AND a billing route dispute (overcharge).",
                "C": "The app glitching and the weather.",
                "D": "There is only one issue: the route detour."
            },
            "answer": "B",
            "explanation": "The rider has complained about driver quality/behavior (refusing to open windows in a smoky car) and a financial discrepancy (route detour overcharge). Both must be addressed in your response.",
            "skill": "Multi-issue Analysis"
        },
        {
            "text": "A customer writes: 'I need to dispute my fare for trip #{id}. I was charged {price} for a cancellation fee, but the driver never arrived at the terminal.' What is the primary data you must pull up first?",
            "scenario": "Action mapping from text",
            "options": {
                "A": "The customer's email subscription history.",
                "B": "The GPS log and status of trip #{id} to verify if the driver reached the pickup pin.",
                "C": "The driver's vehicle registration papers.",
                "D": "A refund button."
            },
            "answer": "B",
            "explanation": "Active reading maps the user's issue directly to the first support step: pulling up trip #{id} and checking the GPS logs to see if the driver waited at the correct spot.",
            "skill": "Action Mapping"
        }
    ]
    random.seed(51)
    id_counter = 1
    for i in range(40):
        for template in templates:
            name = random.choice(USA_NAMES)
            city = random.choice(CITIES)
            price = random.choice(AMOUNTS)
            location = random.choice(["the Hilton Hotel", "the Grand Theater", "the Central Plaza", "the Science Museum"])
            ride_id = random.randint(100000, 999999)
            q_text = template["text"].format(name=name, city=city, price=price, location=location, id=ride_id)
            opts = {}
            for key, val in template["options"].items():
                opts[key] = val.format(name=name, city=city, price=price, location=location, id=ride_id)
            questions.append(make_question(
                q_id=id_counter,
                question=q_text,
                scenario=template["scenario"],
                options=opts,
                answer=template["answer"],
                explanation=template["explanation"],
                skill=template["skill"]
            ))
            id_counter += 1
            if len(questions) >= 200:
                break
        if len(questions) >= 200:
            break
    while len(questions) < 200:
        questions.append(make_question(
            q_id=id_counter,
            question="A customer writes: 'The driver Marcus didn't follow my instructions. I told him to take the third exit on the roundabout but he took the second one. Then he got angry when I corrected him.' What is the core behavior complaint?",
            scenario="Identifying behavior core",
            options={
                "A": "The driver did not know the GPS coordinates.",
                "B": "The driver was angry and dismissive when corrected about a route decision.",
                "C": "The driver drove too fast.",
                "D": "The roundabout was closed."
            },
            answer="B",
            explanation="Active reading identifies that the emotional core of the complaint is the driver's anger and attitude when corrected by the rider.",
            skill="Behavior Core Identification"
        ))
        id_counter += 1
    return questions

# 11. PARAPHRASING
def generate_paraphrasing():
    questions = []
    templates = [
        {
            "text": "A rider named {name} writes: 'I requested a ride but the driver sat in his car down the street, never moved, and then cancelled the ride and I was charged {price} for no reason.' What is the best paraphrase of this issue to start your response?",
            "scenario": "Paraphrasing a cancellation dispute",
            "options": {
                "A": "If I understand correctly, {name}, you were charged a {price} fee after the driver cancelled without attempting to pick you up. Let me check this for you.",
                "B": "So you are saying our driver was lazy and didn't move. Let me refund your {price}.",
                "C": "To clarify, you want a free ride because the driver cancelled the trip.",
                "D": "You were charged {price} because the driver waited down the street."
            },
            "answer": "A",
            "explanation": "A professional paraphrase captures the core action (incorrect cancellation charge) and the cause (driver did not move) politely, validating the customer's issue.",
            "skill": "Summarizing Issue"
        },
        {
            "text": "A passenger says: 'The driver refused to open the trunk for my suitcases and forced me to cram them into the back seat. My bags got scratched in the process.' What is the best paraphrase?",
            "scenario": "Paraphrasing baggage incident",
            "options": {
                "A": "You are complaining because your suitcases got scratched in the cabin.",
                "B": "If I have this right, the driver did not assist with the trunk, forcing you to load your luggage in the passenger area, which caused damage to your bags. Let's look into this.",
                "C": "You want the driver to buy you new luggage because they were scratched.",
                "D": "So the driver didn't want to open the car door for you."
            },
            "answer": "B",
            "explanation": "Paraphrasing should accurately capture the sequence of events (no trunk access, cabin loading, damage) in a professional, objective tone.",
            "skill": "Objective Restatement"
        },
        {
            "text": "A customer in {city} writes: 'My credit card was charged twice for trip #{id}. One charge is {price} and the other is {price}. Please fix this glitched billing.' What is the best paraphrase?",
            "scenario": "Paraphrasing duplicate charges",
            "options": {
                "A": "To clarify, you're seeing duplicate billing charges for trip #{id} on your credit card. Let me check the payment logs right now.",
                "B": "So the app glitched and took twice your money. I will refund {price}.",
                "C": "You want me to delete trip #{id} because you paid twice.",
                "D": "You were charged twice because your card failed the first time."
            },
            "answer": "A",
            "explanation": "A clean billing paraphrase acknowledges the double charge on trip #{id} and moves immediately to the resolution action.",
            "skill": "Billing Paraphrase"
        },
        {
            "text": "A passenger writes: 'The driver took a very long route because he said the highway was closed. But my friends took the highway 10 minutes later and it was open. I want a refund for the extra distance.' What is the best paraphrase?",
            "scenario": "Paraphrasing detour complaint",
            "options": {
                "A": "If I understand correctly, you believe the driver took an unnecessarily long route and incorrectly claimed the highway was closed, resulting in a higher fare. Let me review the map.",
                "B": "So you are calling our driver a liar because your friends took the highway. Let me check.",
                "C": "You want a refund because your friends arrived faster than you.",
                "D": "The driver took a longer route because the highway was closed, so the fare is correct."
            },
            "answer": "A",
            "explanation": "Paraphrasing a detour dispute should summarize the customer's perspective (unnecessary detour, incorrect claim of closure, overcharge) without taking a defensive stance or calling names.",
            "skill": "Conflict Paraphrasing"
        },
        {
            "text": "A driver messages: 'The passenger threw up on my seat and when I asked for their details to clean it, they ran away.' What is the best paraphrase to reassure the driver?",
            "scenario": "Paraphrasing driver mess report",
            "options": {
                "A": "So the rider messed your car and ran away. Please clean it.",
                "B": "Thank you for reporting this. If I understand correctly, a passenger caused mess damage in your vehicle and left without providing details. Let me help you file the cleaning claim.",
                "C": "To clarify, you want us to search for the passenger and force them to clean your car.",
                "D": "You need money because the passenger was sick."
            },
            "answer": "B",
            "explanation": "For drivers, paraphrasing confirms the incident (mess damage) and the critical detail (passenger left) while directing them immediately to the correct policy action (filing a claim).",
            "skill": "Partner Support Paraphrase"
        }
    ]
    random.seed(52)
    id_counter = 1
    for i in range(40):
        for template in templates:
            name = random.choice(USA_NAMES)
            city = random.choice(CITIES)
            price = random.choice(AMOUNTS)
            ride_id = random.randint(100000, 999999)
            q_text = template["text"].format(name=name, city=city, price=price, id=ride_id)
            opts = {}
            for key, val in template["options"].items():
                opts[key] = val.format(name=name, city=city, price=price, id=ride_id)
            questions.append(make_question(
                q_id=id_counter,
                question=q_text,
                scenario=template["scenario"],
                options=opts,
                answer=template["answer"],
                explanation=template["explanation"],
                skill=template["skill"]
            ))
            id_counter += 1
            if len(questions) >= 200:
                break
        if len(questions) >= 200:
            break
    while len(questions) < 200:
        questions.append(make_question(
            q_id=id_counter,
            question="A customer writes: 'My driver Marcus was talking on his phone through the Bluetooth speaker for the entire ride, discussing personal issues. I could barely hear myself think.' What is the best paraphrase?",
            scenario="Paraphrasing distraction complaint",
            options={
                "A": "If I understand correctly, the driver was distracted by a phone conversation on the speaker throughout the ride, making it uncomfortable. Let me log this feedback.",
                "B": "So the driver Marcus talks too much on Bluetooth. I will warn him.",
                "C": "You want a refund because the car Bluetooth was too loud.",
                "D": "The driver was discussing personal issues on Bluetooth."
            },
            answer="A",
            explanation="A professional paraphrase restates the user's issue (distracted driver, Bluetooth call, discomfort) neutrally and sets up the support action.",
            skill="Distraction Paraphrasing"
        ))
        id_counter += 1
    return questions

# -------------------------------------------------------------
# MAIN GENERATION PROCESS
# -------------------------------------------------------------

def main():
    generators = {
        "usa_customers.json": generate_usa_questions,
        "europe_customers.json": generate_europe_questions,
        "east_asia_customers.json": generate_east_asia_questions,
        "africa_customers.json": generate_africa_questions,
        "uber_scenarios.json": generate_uber_scenarios,
        "empathy_training.json": generate_empathy_questions,
        "escalation_training.json": generate_escalation_questions,
        "professional_vocabulary.json": generate_vocabulary_questions,
        "soft_skills.json": generate_soft_skills,
        "active_reading.json": generate_active_reading,
        "paraphrasing.json": generate_paraphrasing
    }
    
    for filename, generator_func in generators.items():
        filepath = os.path.join(TEST_FOLDER, filename)
        print(f"Generating questions for {filename}...")
        questions = generator_func()
        
        # Verify count
        count = len(questions)
        print(f"Generated {count} questions for {filename}.")
        
        # Write to JSON
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)
            
    print("All JSON question files generated successfully!")

if __name__ == "__main__":
    main()
