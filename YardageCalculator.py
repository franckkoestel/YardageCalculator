import streamlit as st
import math

def calculate_total_width_each_panel(width, fullness, side_returns, overlap, panel_type):
    if panel_type == "PAIR":
        total_width = ((width / 2) * fullness) + 6 + side_returns + overlap
    else:
        total_width = (width * fullness) + 6 + side_returns + overlap
    return total_width

def calculate_number_of_fabric_width(total_width_each_panel, fabric_width, panel_type):
    number_of_widths = total_width_each_panel / fabric_width
    if panel_type == "PAIR":
        number_of_widths *= 2
    return number_of_widths

def calculate_cut_height(height, bottom_hem, liner):
    if liner == "YES":
        cut_height = height + bottom_hem + 2
    else:
        cut_height = height + bottom_hem + 12
    return cut_height

def calculate_width_each_side(number_of_fabric_widths, panel_type):
    if panel_type == "PAIR":
        width_each_side = math.ceil(number_of_fabric_widths * 2) / 2
    else:
        width_each_side = math.ceil(number_of_fabric_widths)
    return width_each_side

def calculate_yardage(cut_height, width_each_side, panel_type):
    if panel_type == "PAIR":
        yardage = (cut_height * width_each_side / 36) * 2
    else:
        yardage = cut_height * width_each_side / 36
    return yardage

def main():
    st.title("Drapery Yardage Calculator")

    # Initialize session state for yardage calculations if not already present
    if 'yardages' not in st.session_state:
        st.session_state.yardages = []

    # Select the number of Custom Drapes
    num_drapes = st.number_input("Select the number of Custom Drapes", min_value=1, max_value=50, value=1, step=1)

    for drape_num in range(1, num_drapes + 1):
        st.header(f"Custom Drapes #{drape_num}")

        # Input variables
        width = st.number_input(f"Width of Custom Drapes #{drape_num}", min_value=0, value=72)
        width_fraction = st.selectbox(f"Width Fraction of Custom Drapes #{drape_num}", options=["0", "1/8", "1/4", "3/8", "1/2", "5/8", "3/4", "7/8"], index=0)
        width += eval(width_fraction) if width_fraction != "0" else 0

        height = st.number_input(f"Height of Custom Drapes #{drape_num}", min_value=0, value=90)
        height_fraction = st.selectbox(f"Height Fraction of Custom Drapes #{drape_num}", options=["0", "1/8", "1/4", "3/8", "1/2", "5/8", "3/4", "7/8"], index=0)
        height += eval(height_fraction) if height_fraction != "0" else 0

        fullness = st.number_input(f"Fullness of Custom Drapes #{drape_num}", min_value=0.0, value=2.5)
        side_returns = st.number_input(f"Side Returns of Custom Drapes #{drape_num}", min_value=0.0, value=3.5)
        overlap = st.number_input(f"Overlap of Custom Drapes #{drape_num}", min_value=0.0, value=3.5)
        bottom_hem = st.number_input(f"Bottom Hem of Custom Drapes #{drape_num}", min_value=0, value=10)
        fabric_width = st.number_input(f"Fabric Width of Custom Drapes #{drape_num}", min_value=0, value=54)
        vertical_repeat = st.number_input(f"Vertical Repeat of Custom Drapes #{drape_num}", min_value=0.0)
        panel_type = st.selectbox(f"Panel Type of Custom Drapes #{drape_num}", options=["PAIR", "SINGLE PANEL"])
        liner = st.selectbox(f"Liner for Custom Drapes #{drape_num}", options=["YES", "NO"])

        if st.button(f"Calculate Yardage for Custom Drapes #{drape_num}"):
            # Output variables calculation
            total_width_each_panel = calculate_total_width_each_panel(width, fullness, side_returns, overlap, panel_type)
            number_of_fabric_widths = calculate_number_of_fabric_width(total_width_each_panel, fabric_width, panel_type)
            cut_height = calculate_cut_height(height, bottom_hem, liner)
            width_each_side = calculate_width_each_side(number_of_fabric_widths, panel_type)
            yardage = calculate_yardage(cut_height, width_each_side, panel_type)

            # Display output
            st.write(f"Total Width Each Panel for Custom Drapes #{drape_num}: {total_width_each_panel:.2f}")
            st.write(f"Number of Fabric Widths for Custom Drapes #{drape_num}: {number_of_fabric_widths:.2f}")
            st.write(f"Cut Height for Custom Drapes #{drape_num}: {cut_height:.2f}")
            st.write(f"Width Each Side for Custom Drapes #{drape_num}: {width_each_side:.2f}")
            st.write(f"Yardage for Custom Drapes #{drape_num}: {yardage:.2f} yards")

            # Update session state with the new yardage
            if len(st.session_state.yardages) < drape_num:
                st.session_state.yardages.append(yardage)
            else:
                st.session_state.yardages[drape_num - 1] = yardage

    # Display total yardage for all drapes
    total_yardage_all_drapes = sum(st.session_state.yardages)
    st.header(f"Total Yardage for All Custom Drapes: {total_yardage_all_drapes:.2f} yards")

if __name__ == "__main__":
    main()
