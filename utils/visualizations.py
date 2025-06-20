import matplotlib.pyplot as plt
import os

output_dir = os.path.join(os.path.dirname(__file__), "../assets/images")
os.makedirs(output_dir, exist_ok=True)


def save_charts(df):
    # Casualty Bar
    plt.figure(figsize=(8, 6))
    plt.bar(["Total Onboard", "Passengers", "Crew", "Deaths", "Survivors", "Reported Toll"],
            [df["Total_People_Onboard"][0], df["Passengers"][0], df["Crew"][0],
             df["Confirmed_Deaths"][0], df["Survivors"][0], df["Death_Toll_Reported"][0]],
            color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"])
    plt.title("Casualty Metrics")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "casualty_metrics.png"))
    plt.close()

    # Pilot Experience
    plt.figure(figsize=(6, 4))
    plt.bar(["Captain", "Co-Pilot", "Required Cmdr Hrs"],
            [df["Captain_Flight_Hours"][0], df["Co_Pilot_Flight_Hours"][0], df["Required_Hours_for_Commander"][0]],
            color=["#1f77b4", "#ff7f0e", "#2ca02c"])
    plt.title("Pilot Experience")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "pilot_experience.png"))
    plt.close()

    # Survivor Pie
    plt.figure(figsize=(6, 6))
    plt.pie([df["Confirmed_Deaths"][0], df["Survivors"][0]],
            labels=["Deaths", "Survivors"],
            colors=["#d62728", "#9467bd"], autopct="%1.1f%%", explode=(0, 0.1))
    plt.savefig(os.path.join(output_dir, "casualty_pie.png"))
    plt.close()

    # Emergency Resources Bar Chart
    plt.figure(figsize=(8, 6))
    plt.bar(
        ["NDRF Teams", "Assistance Centers", "Airport Helplines", "DNA Helplines"],
        [
            df["NDRF_Teams_Deployed"][0],
            df["Assistance_Centers_Count"][0],
            df["Airport_Helplines_Count"][0],
            df["DNA_Control_Room_Helplines_Count"][0]
        ],
        color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"],
        edgecolor="black"
    )
    plt.title("Emergency Resource Deployment")
    plt.ylabel("Count")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "emergency_resources.png"))
    plt.close()

    # DNA Processing Progress Pie Chart
    plt.figure(figsize=(6, 6))
    processed = df["Bodies_Handed_Over"][0]
    remaining = df["Confirmed_Deaths"][0] - processed

    plt.pie(
        [processed, remaining],
        labels=["Bodies Handed Over", "Remaining for DNA Match"],
        colors=["#9467bd", "#8c564b"],
        explode=(0.1, 0),
        autopct="%1.1f%%",
        shadow=True,
        startangle=90
    )
    plt.title("DNA Processing Progress")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "dna_processing_pie.png"))
    plt.close()

