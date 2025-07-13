#inputs are land,capex,o&m cost,energy availability,temp
import streamlit as st

st.title("Wastewater Treatment Technology Selector")

st.write("Enter the parameters below to identify the suitable wastewater treatment technology.")

#taking inputs
land = st.number_input("Land Requirement (ha/MLD)", min_value=0.0, max_value=2.0, value=0.5, step=0.01)
inCost = st.number_input("Installation Cost (lakh/MLD)",min_value=30,max_value=300,value=100,step = 1)
om_cost = st.number_input("O&M Cost (lakh/MLD per year)",min_value=0.0, max_value=50.0, value=5.0, step=0.1)
energy = st.number_input("Energy Consumption",min_value=0,max_value=250,value=0,step = 1)
temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=20.0, step=1.0)


def select_technology(land, inCost, om_cost, energy, temp):
    # Input validation
    if land < 0 or inCost < 0 or om_cost < 0 or energy < 0:
        return "Invalid input: Parameters cannot be negative"
    
    technology = "None"
    
    # Energy = 0 (WSP, Root Zone, DTS/DEWATS)
    if energy == 0:
        if land < 0.5:
            technology = "DTS/DEWATS"
        else:  # land >= 0.5
            if temp > 20 and inCost <= 60:
                technology = "WSP"
            else:
                technology = "Root Zone"
    
    # Energy < 150 (Aerated Lagoon, UASB)
    elif energy < 150:
        if energy <= 15:
            if temp >= 15:
                technology = "UASB"
            else:
                technology = "None"
        else:
            technology = "Aerated Lagoon"
    
    # Energy >= 150 (ASP, EA, SBR, MBBR, Trickling Filter)
    else:
        if land <= 0.05:
            if 170 <= inCost <= 230 and 8 <= om_cost <= 12:
                technology = "MBBR"
        elif land <= 0.25:  # Combined SBR, ASP, EA checks
            if 150 <= inCost <= 300 and 10 <= om_cost <= 20 and land <= 0.15:
                technology = "SBR"
            elif 80 <= inCost <= 170 and 6 <= om_cost <= 10:
                technology = "ASP"
            elif 90 <= inCost <= 200 and 7 <= om_cost <= 12:
                technology = "EA"
        else:  # land > 0.25
            if 50 <= inCost <= 80 and 2 <= om_cost <= 5 and temp >= 10:
                technology = "Trickling Filter"
            else:
                technology = "None"
    
    return technology


# Button to trigger the calculation
if st.button("Identify Technology"):
    result = select_technology(land,inCost,om_cost,energy,temp)
    if result == "None":
        st.error("No suitable technology found for the given parameters.")
    elif result.startswith("Invalid"):
        st.error(result)
    else:
        st.success(f"Recommended Technology: **{result}**")   
