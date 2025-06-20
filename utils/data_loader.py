import pandas as pd


def load_common_data():
    return pd.DataFrame({
        "Total_People_Onboard": [242],
        "Passengers": [230],
        "Crew": [12],
        "Death_Toll_Reported": [265],
        "Confirmed_Deaths": [241],
        "Survivors": [1],
        "Altitude_at_Crash_Feet": [425],
        "Captain_Flight_Hours": [8200],
        "Co_Pilot_Flight_Hours": [1100],
        "Required_Hours_for_Commander": [1500],
        "NDRF_Teams_Deployed": [6],
        "Bodies_Handed_Over": [6],
        "Assistance_Centers_Count": [4],
        "Airport_Helplines_Count": [3],
        "DNA_Control_Room_Helplines_Count": [2],
        "Days_for_DNA_Matching": [3]
    })
