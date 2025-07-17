import streamlit as st

# Corrected select_technology function without energy
def select_technology(land, inCost, om_cost, temp):
    if land < 0 or inCost < 0 or om_cost < 0:
        return "Invalid input: Parameters cannot be negative"
    
    technology = "None"
    
    if land >= 0.5:
        if temp > 20 and inCost <= 60:
            technology = "WSP"
        else:
            technology = "Root Zone"
    elif land >= 0.25:
        if 50 <= inCost <= 80 and 2 <= om_cost <= 5 and temp >= 10:
            technology = "Trickling Filter"
        elif 40 <= inCost <= 60 and 2 <= om_cost <= 3.5 and temp > 15:
            technology = "UASB"
        elif 40 <= inCost <= 60 and 1.5 <= om_cost <= 3:
            technology = "Aerated Lagoon"
    elif land >= 0.13:
        if 80 <= inCost <= 200 and 2 <= om_cost <= 2.5:
            technology = "DTS/DEWATS"
        elif 80 <= inCost <= 170 and 6 <= om_cost <= 10:
            technology = "ASP"
        elif 90 <= inCost <= 200 and 7 <= om_cost <= 12:
            technology = "EA"
    elif land >= 0.1:
        if 150 <= inCost <= 300 and 10 <= om_cost <= 20:
            technology = "SBR"
        elif 80 <= inCost <= 170 and 6 <= om_cost <= 10:
            technology = "ASP"
        elif 90 <= inCost <= 200 and 7 <= om_cost <= 12:
            technology = "EA"
    else:  # land < 0.1
        if 170 <= inCost <= 230 and 8 <= om_cost <= 12:
            technology = "MBBR"
    
    return technology

# Dictionary for technology details
technology_details = {
    "WSP": "Waste Stabilization Ponds (WSP): Low-cost, natural treatment. Needs large land and warm climate.",
    "Root Zone": "Root Zone: Plant-based filtration system. Suitable for semi-urban/rural areas, moderate land.",
    "DTS/DEWATS": "Decentralized Treatment Systems (DTS/DEWATS): Small footprint, simple operation, low energy.",
    "Aerated Lagoon": "Aerated Lagoon: Uses mechanical aeration, needs moderate land and cost.",
    "UASB": "UASB (Upflow Anaerobic Sludge Blanket): Effective in warm climates, low energy and cost.",
    "SBR": "SBR (Sequencing Batch Reactor): Compact, automated, suitable for urban areas with limited land.",
    "ASP": "ASP (Activated Sludge Process): Common in cities, moderate cost, higher land and energy needs.",
    "EA": "Extended Aeration: Variation of ASP with longer retention time. Reliable and robust.",
    "MBBR": "MBBR (Moving Bed Biofilm Reactor): Advanced, space-efficient, moderate O&M and capex.",
    "Trickling Filter": "Trickling Filter: Biological filter, low O&M, suitable for moderate climates.",
    "None": "No suitable technology found for the given parameters."
}

# Streamlit app
st.title("Wastewater Treatment Technology Selector")
st.write("Enter the parameters below to identify the suitable wastewater treatment technology.")

# Input fields (excluding energy)
land = st.number_input("Land Requirement (ha/MLD)", min_value=0.0, max_value=2.0, value=0.5, step=0.01)
inCost = st.number_input("Installation Cost (lakh/MLD)", min_value=30.0, max_value=300.0, value=100.0, step=1.0)
om_cost = st.number_input("O&M Cost (lakh/MLD per year)", min_value=0.0, max_value=50.0, value=5.0, step=0.1)
temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=20.0, step=1.0)

# Button to trigger selection
if st.button("Identify Technology"):
    result = select_technology(land, inCost, om_cost, temp)
    if result == "None":
        st.error("No suitable technology found for the given parameters.")
    elif result.startswith("Invalid"):
        st.error(result)
    else:
        st.success(f"Recommended Technology: **{result}**")
        st.info(technology_details[result])

    