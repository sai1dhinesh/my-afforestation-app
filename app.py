import streamlit as st

# Define a SpeciesProfile class
class SpeciesProfile:
    def __init__(self, name, co2_absorption_per_tree, water_needed_per_tree, growth_rate):
        self.name = name
        self.co2_absorption_per_tree = co2_absorption_per_tree  # kg/year
        self.water_needed_per_tree = water_needed_per_tree  # liters/year
        self.growth_rate = growth_rate  # percentage survival rate

# Default species data
DEFAULT_SPECIES_PROFILES = {
    "Neem": SpeciesProfile("Neem", 400, 288.96, 90),
    "Teak": SpeciesProfile("Teak", 250, 500.0, 80),
    "Banyan": SpeciesProfile("Banyan", 350, 600.0, 85),
}

st.title("🌱 Afforestation Impact Calculator")

# Input section
species = st.selectbox("Choose a tree species:", list(DEFAULT_SPECIES_PROFILES.keys()))
num_trees = st.number_input("Enter number of trees:", min_value=1, step=1)

# Calculate impact
if st.button("Calculate Impact"):
    profile = DEFAULT_SPECIES_PROFILES[species]
    total_co2 = num_trees * profile.co2_absorption_per_tree
    total_water = num_trees * profile.water_needed_per_tree
    
    st.success(f"🌍 By planting {num_trees} {species} trees:")
    st.write(f"- Estimated CO₂ absorbed per year: **{total_co2} kg**")
    st.write(f"- Water required per year: **{total_water} liters**")
    st.write(f"- Average survival rate: **{profile.growth_rate}%**")
