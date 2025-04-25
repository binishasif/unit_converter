import streamlit as st

# Conversion logic
def convert_units(value: float, unit_from: str, unit_to: str):
    conversions = {
        ("kilometers", "meters"): value * 1000,
        ("meters", "kilometers"): value * 0.001,
        ("kilograms", "grams"): value * 1000,
        ("grams", "kilograms"): value * 0.001
    }
    return conversions.get((unit_from, unit_to), "Conversion not supported")

# Streamlit App
def main():
    st.set_page_config(page_title="Unit Converter", page_icon="🔄")
    
    st.title("🔄 Unit Converter")
    st.markdown("""
        <style>
            .stApp {
                background-color: #f5f7fa;
            }
            .big-font {
                font-size:20px !important;
            }
        </style>
    """, unsafe_allow_html=True)

    st.write("Welcome to the simple and easy Unit Converter!")

    value = st.number_input("Enter the value you want to convert", min_value=0.0, step=0.1)
    
    units = ["meters", "kilometers", "grams", "kilograms"]
    
    unit_from = st.selectbox("Select the unit to convert **from**:", units)
    unit_to = st.selectbox("Select the unit to convert **to**:", units)

    if st.button("Convert"):
        result = convert_units(value, unit_from, unit_to)
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"✅ {value} {unit_from} is equal to {result} {unit_to}")

if __name__ == "__main__":
    main()
