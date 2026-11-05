import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.patches import Patch

# Folders

base_path = r"/home/pedro/Data"

# Only systems used in the article
systems = {
    "System1": "S1",
    "System2": "S2",
    "System3": "S3"
}

# Start dates

start_dates = {
    "System1": "2026-04-01",
    "System2": "2026-04-10",
    "System3": "2026-03-24"
}

# Analysis window
# 59 days in hours

MAX_DAYS = 59
MAX_HOURS = MAX_DAYS * 24

# Figure

plt.figure(figsize=(18, 4.5))

# Process each system

for idx, (user, system_name) in enumerate(systems.items()):

    folder_path = Path(base_path) / user

    # Search only events.csv
    csv_files = list(
        folder_path.rglob("events.csv")
    )

    dfs = []

    # Read files

    for file in csv_files:

        try:

            temp_df = pd.read_csv(
                file,
                sep=None,
                engine="python"
            )

            temp_df.columns = (
                temp_df.columns.str.strip()
            )

            # UNIX timestamp in seconds
            temp_df["Time"] = pd.to_datetime(
                temp_df["Time"],
                unit="s"
            )

            dfs.append(temp_df)

        except Exception as e:

            print(f"Error reading {file}")
            print(e)

    # Skip if no data
    if len(dfs) == 0:
        continue

    # Merge data

    df = pd.concat(
        dfs,
        ignore_index=True
    )

    # Sort by time

    df = df.sort_values(
        "Time"
    ).reset_index(drop=True)

    # Map states

    df["Status"] = df["Event Type"].map({
        "ONLINE": 1,
        "OFFLINE": 0
    })

    # Remove consecutive duplicates

    df = df[
        df["Status"].shift() != df["Status"]
    ].reset_index(drop=True)

    # Initial timestamp

    start_time = pd.Timestamp(
        start_dates[user]
    )

    end_time = start_time + pd.Timedelta(days=MAX_DAYS)

    # Filter analysis window
    df = df[
        (df["Time"] >= start_time) &
        (df["Time"] <= end_time)
    ].reset_index(drop=True)

    # Skip if empty
    if len(df) < 2:
        continue

    # Create intervals

    intervals = []

    for i in range(len(df) - 1):

        start = df.loc[i, "Time"]
        end = df.loc[i + 1, "Time"]

        status = df.loc[i, "Status"]

        duration = end - start

        intervals.append({
            "start": start,
            "end": end,
            "status": status,
            "duration": duration
        })

    intervals_df = pd.DataFrame(intervals)

    # Extend last state to end of window

    last_start = df.iloc[-1]["Time"]

    last_status = df.iloc[-1]["Status"]

    if last_start < end_time:

        intervals_df.loc[len(intervals_df)] = {
            "start": last_start,
            "end": end_time,
            "status": last_status,
            "duration": end_time - last_start
        }

    # Metrics

    online_intervals = intervals_df[
        intervals_df["status"] == 1
    ]

    offline_intervals = intervals_df[
        intervals_df["status"] == 0
    ]

    # Total times

    total_online = online_intervals[
        "duration"
    ].sum()

    total_offline = offline_intervals[
        "duration"
    ].sum()

    total_time = (
        total_online + total_offline
    )

    # Availability

    availability = (
        total_online / total_time
    ) * 100

    # Counts

    num_failures = len(
        offline_intervals
    )

    num_recoveries = len(
        online_intervals
    )

    if num_failures > 0:

        mtbf = (
            total_online / num_failures
        )

    else:

        mtbf = pd.Timedelta(0)


    if num_failures > 0:

        mttr = (
            total_offline / num_failures
        )

    else:

        mttr = pd.Timedelta(0)

    # Maximum durations

    max_online = online_intervals[
        "duration"
    ].max()

    max_offline = offline_intervals[
        "duration"
    ].max()

    # Mean durations

    mean_online = online_intervals[
        "duration"
    ].mean()

    mean_offline = offline_intervals[
        "duration"
    ].mean()

    # Convert to hours

    total_online_h = (
        total_online.total_seconds() / 3600
    )

    total_offline_h = (
        total_offline.total_seconds() / 3600
    )

    mtbf_h = (
        mtbf.total_seconds() / 3600
    )

    mttr_h = (
        mttr.total_seconds() / 3600
    )

    max_online_h = (
        max_online.total_seconds() / 3600
    )

    max_offline_h = (
        max_offline.total_seconds() / 3600
    )

    mean_online_h = (
        mean_online.total_seconds() / 3600
    )

    mean_offline_h = (
        mean_offline.total_seconds() / 3600
    )

    # Print results

    print("\n===================================")
    print(f"STATISTICS - {system_name}")
    print("===================================")

    print(f"Total analyzed time: {MAX_DAYS} days")

    print(
        f"Total ONLINE time: "
        f"{total_online_h:.2f} h"
    )

    print(
        f"Total OFFLINE time: "
        f"{total_offline_h:.2f} h"
    )

    print(
        f"Availability: "
        f"{availability:.2f}%"
    )

    print(
        f"Number of failures: "
        f"{num_failures}"
    )

    print(
        f"Number of recoveries: "
        f"{num_recoveries}"
    )

    print(
        f"MTBF: "
        f"{mtbf_h:.2f} h"
    )

    print(
        f"MTTR: "
        f"{mttr_h:.2f} h"
    )

    print(
        f"Maximum ONLINE duration: "
        f"{max_online_h:.2f} h"
    )

    print(
        f"Maximum OFFLINE duration: "
        f"{max_offline_h:.2f} h"
    )

    print(
        f"Mean ONLINE duration: "
        f"{mean_online_h:.2f} h"
    )

    print(
        f"Mean OFFLINE duration: "
        f"{mean_offline_h:.2f} h"
    )
    
    # Plot timeline

    t0 = intervals_df["start"].min()

    for _, row in intervals_df.iterrows():

        start_hours = (
            (row["start"] - t0)
            .total_seconds() / 3600
        )

        duration_hours = (
            row["duration"]
            .total_seconds() / 3600
        )

        color = (
            "#658D1B"
            if row["status"] == 1
            else "#BA0C2F"
        )

        plt.barh(
            y=idx,
            width=duration_hours,
            left=start_hours,
            height=0.55,
            color=color
        )

plt.xlabel("Time (h)", fontsize=22)

plt.yticks(
    range(len(systems)),
    systems.values(),
    rotation=90,
    va="center",
    fontsize=22
)

plt.gca().invert_yaxis()

tick_step = 200

ticks = list(
    range(0, MAX_HOURS + 1, tick_step)
)

labels = [
    f"{t}"
    for t in ticks
]

plt.xticks(
    ticks,
    labels,
    fontsize=20
)

plt.xlim(0, MAX_HOURS)

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.5
)

legend_elements = [
    Patch(
        facecolor="#658D1B",
        label="ONLINE"
    ),
    Patch(
        facecolor="#BA0C2F",
        label="OFFLINE"
    )
]

plt.tight_layout()

plt.show()
