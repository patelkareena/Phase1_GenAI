import pandas as pd

# Load the CSV file
df = pd.read_csv("Construction_Data_PM_Tasks_All_Projects.csv")
#1
# Count the number of rows where OverDue is True
num_overdue = len(df[df["OverDue"] == True])

# Print the result
print(f"Number of overdue tasks: {num_overdue}")

#2
# Group the data by task group and report status
grouped = df.groupby(["Task Group", "Report Status"])["Status"].count()

# Report the total number of open and closed tasks by each task group
for task_group in df["Task Group"].unique():
    try:
        open_tasks = grouped[task_group]["Open"]
    except KeyError:
        open_tasks = 0
    try:
        closed_tasks = grouped[task_group]["Closed"]
    except KeyError:
        closed_tasks = 0
    print(f"Task Group: {task_group}")
    print(f"Total number of open tasks: {open_tasks}")
    print(f"Total number of closed tasks: {closed_tasks}")

#4
# Filter for overdue tasks
import matplotlib.pyplot as plt

# Filter for overdue tasks
overdue_tasks = df[df["OverDue"] == True]

# Group the data by project and count the number of overdue tasks
grouped = overdue_tasks.groupby("project")["Report Status"].count()

# Create a bar chart of the total number of overdue tasks by project
plt.bar(grouped.index, grouped.values)
plt.xlabel("Project")
plt.ylabel("Number of Overdue Tasks")
plt.title("Total Number of Overdue Tasks by Project")

plt.savefig("overdue_tasks.png")
plt.close()

#3
import matplotlib.pyplot as plt
open_tasks = df[df["Report Status"] == "Open"]
closed_tasks = df[df["Report Status"] == "Closed"]

# Group the data by task group and report status
open_grouped = open_tasks.groupby("Task Group")["Report Status"].count()
closed_grouped = closed_tasks.groupby("Task Group")["Report Status"].count()

# Create a bar chart of the total number of open and closed tasks by each Task Group
fig, ax = plt.subplots()
ax.bar(open_grouped.index, open_grouped.values, label="Open")
ax.bar(closed_grouped.index, closed_grouped.values, bottom=open_grouped.values, label="Closed")
ax.set_xlabel("Task Group")
ax.set_ylabel("Number of Tasks")
ax.set_title("Total Number of Open and Closed Tasks by Task Group")
ax.legend()
plt.savefig("open_and_closed_tasks.png")
plt.close()
