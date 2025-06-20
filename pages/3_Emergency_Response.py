import streamlit as st
from utils.data_loader import load_common_data


df = load_common_data()
st.title("🧯 Emergency Response")

st.markdown("""
**Responding Units**:  
- 6 NDRF teams  
- Fire engines, ambulances, and police units  
- DNA sampling initiated—**6 bodies matched**, **3-day matching window**

**Support Infrastructure**:  
- Assistance centers in Ahmedabad, Mumbai, Delhi & Gatwick  
- 3 airport helplines  
- 2 DNA control helplines
""")

st.image("assets/images/emergency_resources.png", caption="Emergency Response Breakdown")

st.image("assets/images/dna_processing_pie.png", caption="DNA Processing Progress")
