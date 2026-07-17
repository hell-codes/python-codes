# Smart Home Thermostat
temperature = float(input("Enter temperature (°C): "))
humidity = float(input("Enter humidity (%): "))
eco_mode = input("Is Eco Mode ON? (Yes/No): ").strip().lower()
ac_status = "AC OFF"

if eco_mode == "yes":
    if temperature >= 30:
        if temperature >= 35 and humidity >= 70:
            ac_status = "AC ON (High Power)"
        elif 28 <= temperature < 35 and humidity >= 50:
            ac_status = "AC ON (Normal Power)"
        else:
            ac_status = "AC OFF"
    else: