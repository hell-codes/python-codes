age= int(input("Enter patient's age:"))
severity= input("Enter symptom severity (severe/mild):").strip().lower()
if age>60 and severity=="severe":
    ward = "Emergency ward"
elif age>60 and severity=="mild":
    ward = "General ward"
elif age<=60 and severity=="severe":
    ward = "Special Observation ward"
else:
    ward = "OPD Consultation"
    print("\n-----HOSPITAL TRIAGE TESULT-----")
    print(f"Age: {age}")
    print(f"Symptoms:{severity}")
    print(f"Assigned: {ward}")
