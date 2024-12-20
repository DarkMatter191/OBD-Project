import random
import json
import os

# Base engine data provided
base_data = {
    "OBD Volts": "13 V",
    "Calculated Engine Load": "28.63%",
    "Coolant Temperature": "206.6 °F",
    "Short Term Fuel Trim (STFT) Bank 1": "2.34%",
    "Long Term Fuel Trim (LTFT) Bank 1": "1.56%",
    "Manifold Absolute Pressure (MAP)": "8.11 psi",
    "Engine RPM": "831 rpm",
    "Speed": "0 km/h",
    "Timing Advance": "6 °",
    "Intake Air Temperature": "127.4 °F",
    "Mass Air Flow (MAF) Rate": "3.4 g/sec",
    "Throttle Position": "22.75%",
    "Oxygen Sensor 1 Voltage (Bank 1)": "0.79 V",
    "Oxygen Sensor 1 Trim (Bank 1)": "2.34%",
    "Oxygen Sensor 2 Voltage (Bank 1)": "0.11 V",
    "Oxygen Sensor 2 Trim (Bank 1)": "%",
    "Distance Traveled with MIL On": "497 km",
    "EVAP Purge": "23%",
    "Number of Warm-Ups Since Codes Cleared": "255",
    "Distance Traveled Since Codes Cleared": "44,265 km",
    "Barometric Pressure": "14.5 psi",
    "Catalytic Converter Temperature (Bank 1 Sensor 1)": "933.8 °F",
    "ECU Voltage": "14.09 V",
    "Absolute Load Value": "30.59%",
    "Fuel/Air Commanded Ratio": "14.63",
    "Relative Throttle Position": "10%",
    "Ambient Air Temperature": "71.6 °F",
    "Absolute Throttle Position B": "22%",
    "Absolute Throttle Position D": "20%",
    "Absolute Throttle Position E": "10%",
    "Throttle Actuator": "14%",
    "Intake Air Temperature B1S1": "127.4 °F",
    "Intake Air Temperature B1S2": "141.8 °F",
    "Intake Air Temperature B1S3": "93.2 °F",
    "Intake Air Temperature B2S1": "N/A",
    "Intake Air Temperature B2S2": "N/A",
    "Intake Air Temperature B2S3": "N/A",
    "Fuel Level Input": "51%",
    "Reset Trip": "(Empty)",
    "Average Fuel Consumption": "∞ L/100 km (error reading)",
    "Average Fuel Consumption (Total)": "∞ L/100 km (error reading)",
    "Average Fuel Consumption (10 sec)": "∞ L/100 km (error reading)",
    "Average Speed": "0 km/h",
    "Calculated Boost": "-6.22 psi",
    "Instant Fuel Consumption": "∞ L/100 km (error reading)",
    "Instant Fuel Rate": "0.32 gal/h",
    "Distance to Empty": "[Empty]",
    "Distance Traveled": "0 km",
    "Total Distance Traveled": "0 km",
    "Engine RPM x1000": "0.8 rpm",
    "Free Space in Fuel Tank": "24.5 gallons",
    "Fuel Economizer (Based on Throttle Position)": "1",
    "Fuel Level Input (V)": "25.5 gallons",
    "Fuel Used": "0.01 gallons",
    "Total Fuel Used": "0.01 gallons",
    "Fuel Used Price": "0.03 $",
    "Total Fuel Used Price": "0.02 $",
    "Power (Fuel)": "4.81 hp",
    "Power from MAF": "4.38 hp",
    "Vehicle Acceleration": "0 g",
    "Elapsed Time Since Engine Start": "276 seconds",
    "Knock Retard": "0°",
    "ATF Temperature (var.1)": "158 °F",
    "ATF Temperature (var.2)": "158 °F",
    "ATF Temperature (var.3)": "158 °F",
    "ATF Temperature (var.4)": "158 °F",
    "ATF Temperature (var.5)": "158 °F",
    "A/C High Pressure": "197.96 psi",
    "H2OS Sensor": "794.22 mV",
    "Misfire Cyl 1 History": "0",
    "Misfire Cyl 2 History": "0",
    "Misfire Cyl 3 History": "0",
    "Misfire Cyl 4 History": "0",
    "Misfire Cyl 5 History": "0",
    "Misfire Cyl 6 History": "0",
    "Misfire Cyl 7 History": "0",
    "Misfire Cyl 8 History": "0",
    "Misfire Cyl 1 Current": "0",
    "Misfire Cyl 2 Current": "0",
    "Misfire Cyl 3 Current": "0",
    "Misfire Cyl 4 Current": "0",
    "Misfire Cyl 5 Current": "0",
    "Misfire Cyl 6 Current": "0",
    "Misfire Cyl 7 Current": "0",
    "Misfire Cyl 8 Current": "0",
    "Transmission Fluid Temperature (7E2)": "70°F",
    "Current Gear var.2": "1",
    "Current Gear var.3": "0",
    "EGR Duty Cycle": "0%",
    "EGR V": "0 V",
    "Air Conditioning High Side Pressure": "175.74 psi",
    "Engine Oil Pressure": "0 psi",
    "Engine Oil Temperature": "210.2 °F",
    "ATF Temperature (var.6)": "167°F",
    "E85 (Alcohol) Content in Fuel": "9.8%",
    "Odometer (engine unit)": "99,483.17 km",
    "Catalytic Converter Temperature (Bank 1 Sensor 1)": "933.8°F",
    "Barometric Pressure": "14.5 psi",
    "Number of Warm-Ups Since Codes Cleared": "255"
}

# Function to vary all engine data points meaningfully
def vary_all_data(base_data):
    varied_data = {}
    for key, value in base_data.items():
        if "°F" in value:
            # Vary temperature values between 50°F and 250°F
            varied_data[key] = f"{random.uniform(50, 250):.1f} °F"
        elif "%" in value:
            # Vary percentage values between -20% and 100%
            varied_data[key] = f"{random.uniform(-20, 100):.2f}%"
        elif "psi" in value:
            # Vary pressure values between 5 psi and 300 psi
            varied_data[key] = f"{random.uniform(5, 300):.2f} psi"
        elif "V" in value:
            # Vary voltage values between 0 V and 14 V
            varied_data[key] = f"{random.uniform(0, 14):.2f} V"
        elif "rpm" in value:
            # Vary RPM values between 500 rpm and 7000 rpm
            varied_data[key] = f"{random.randint(500, 7000)} rpm"
        elif "km/h" in value:
            # Vary speed between 0 km/h and 200 km/h
            varied_data[key] = f"{random.randint(0, 200)} km/h"
        elif "km" in value and "km/h" not in key:
            # Vary distance between 0 km and 500,000 km
            varied_data[key] = f"{random.randint(0, 500000)} km"
        elif "gal/h" in value or "g/sec" in value:
            # Vary flow rates between 0 and 50 units
            unit = value.split()[-1]
            varied_data[key] = f"{random.uniform(0, 50):.2f} {unit}"
        elif "°" in value:
            # Vary angle values between -10° and 40°
            varied_data[key] = f"{random.uniform(-10, 40):.1f} °"
        elif "hp" in value:
            # Vary horsepower between 0 hp and 400 hp
            varied_data[key] = f"{random.uniform(0, 400):.2f} hp"
        elif "gallons" in value:
            # Vary gallons between 0 and 30 gallons
            varied_data[key] = f"{random.uniform(0, 30):.2f} gallons"
        elif "seconds" in value:
            # Vary time between 0 and 10,000 seconds
            varied_data[key] = f"{random.randint(0, 10000)} seconds"
        elif "mV" in value:
            # Vary millivolts between 0 mV and 1000 mV
            varied_data[key] = f"{random.uniform(0, 1000):.2f} mV"
        elif "g" in value and "gal/h" not in key and "g/sec" not in key:
            # Vary acceleration between -1 g and 1 g
            varied_data[key] = f"{random.uniform(-1, 1):.2f} g"
        elif "N/A" in value or "(Empty)" in value or "[Empty]" in value:
            # Keep empty or N/A values as is
            varied_data[key] = value
        elif value.replace('.', '', 1).isdigit():
            # Vary numeric values
            varied_data[key] = f"{random.uniform(0, 1000):.2f}"
        else:
            # Keep other values as is
            varied_data[key] = value
    return varied_data

# Function to generate user inputs and AI model responses based on the varied data
def generate_conversation(varied_data):
    conversations = []
    
    # System message instructions for formatting and interpretation
    system_message = (
        "You are a car diagnostics assistant. The following OBD data is provided as an example. "
        "When given actual data, carefully review it without making immediate assumptions. "
        "Consider that multiple readings could point to one underlying problem. "
        "In your initial answer, identify only the single most critical issue and explicitly state it as such. "
        "If the user requests more detail later, provide the next two most critical issues. "
        "Keep responses short, concise, and no more than a few sentences. "
        "If asked for mechanical help or factual verification, clarify that you rely on your own data rather than these samples."
    )
    
    # User provides the varied OBD-II data and describes symptoms
    user_symptoms = []
    if float(varied_data.get("Coolant Temperature", "0").split()[0]) > 230:
        user_symptoms.append("My car is overheating.")
    if float(varied_data.get("Short Term Fuel Trim (STFT) Bank 1", "0%").strip('%')) > 10:
        user_symptoms.append("I'm noticing poor fuel economy.")
    misfires = [i for i in range(1, 9) if float(varied_data.get(f"Misfire Cyl {i} Current", "0")) > 0]
    if misfires:
        user_symptoms.append("My engine is shaking.")
    if float(varied_data.get("OBD Volts", "0 V").split()[0]) < 12:
        user_symptoms.append("My car's electrical systems are acting up.")
    if int(varied_data.get("Engine RPM", "0 rpm").split()[0]) > 4000:
        user_symptoms.append("My engine revs high without acceleration.")
    if float(varied_data.get("Engine Oil Pressure", "0 psi").split()[0]) < 20:
        user_symptoms.append("The oil pressure warning light is on.")

    # Combine symptoms into a single user input
    if user_symptoms:
        user_input = " ".join(user_symptoms)
    else:
        user_input = "My car is not performing well."

    # Analyze the data to find potential issues (but only present one initially)
    potential_issues = []
    if "My car is overheating." in user_input:
        potential_issues.append("High coolant temperature suggests engine overheating.")
    if "I'm noticing poor fuel economy." in user_input:
        potential_issues.append("High fuel trim values indicate a rich fuel mixture.")
    if "My engine is shaking." in user_input:
        potential_issues.append("Engine misfires detected.")
    if "My car's electrical systems are acting up." in user_input:
        potential_issues.append("Low battery voltage or electrical issue detected.")
    if "My engine revs high without acceleration." in user_input:
        potential_issues.append("Possible idle control or vacuum leak issue.")
    if "The oil pressure warning light is on." in user_input:
        potential_issues.append("Low engine oil pressure warning.")

    # Choose the single most critical issue to present
    if potential_issues:
        most_critical_issue = potential_issues[0]
        assistant_response = (
            f"{most_critical_issue} This is the most critical issue. "
            "Please note that I rely on my own data, not these examples, for accurate information."
        )
    else:
        assistant_response = (
            "No immediate critical issues detected from the provided data. "
            "This is the most critical assessment I can make now, but I rely on my own data for accuracy."
        )

    # Construct the initial conversation with system, user, and assistant
    # Construct the initial conversation with system, user, and assistant
    conversations.append({
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": f"User Data: {json.dumps(varied_data)}\nUser Input: {user_input}"},
            {"role": "assistant", "content": assistant_response}
        ]
    })


    # Generate follow-up interactions (unchanged, but could be refined)
    num_follow_ups = random.randint(1, 4)
    follow_up_options = [
        ("What should I do next?", "It's best to address the identified issue promptly. Consult a qualified mechanic."),
        ("Can I keep driving?", "It's not advisable to continue driving if a critical issue is identified. Get professional help soon."),
        ("Could it be something else?", "Yes, multiple data points may indicate an underlying issue. Further diagnostics are needed."),
        ("How urgent is this?", "You should consider it urgent and seek help before more damage occurs."),
        ("Can I fix this myself?", "While simple checks can be done at home, professional diagnostic tools and expertise are recommended.")
    ]

    for _ in range(num_follow_ups):
        user_follow_up, ai_follow_up = random.choice(follow_up_options)
        follow_up_prompt = f"User Input: '{user_follow_up}'\n\nAssistant:"
        follow_up_completion = ai_follow_up

        conversations.append({
            "messages": [
                {"role": "user", "content": user_follow_up},
                {"role": "assistant", "content": ai_follow_up}
            ]
        })

    return conversations


# Generate the dataset with 100 entries
entries = []

for _ in range(100):
    # Vary all engine data
    varied_data = vary_all_data(base_data)
    
    # Generate conversation based on varied data
    conversation = generate_conversation(varied_data)
    
    # Append conversation entries to the dataset
    entries.extend(conversation)

# Save the dataset to a JSONL file
with open('tuning.jsonl', 'w') as file:
    for entry in entries:
        json.dump(entry, file)
        file.write('\n')


print("Saving file to:", os.getcwd())
