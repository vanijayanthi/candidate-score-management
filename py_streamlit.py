import streamlit as st
import pandas as pd
import os

FILENAME = "candidate_scores.csv"

st.title("📊 Candidate Score Management System")

# ---------------- CREATE CSV ----------------
def create_csv():
    if os.path.exists(FILENAME):
        st.warning("CSV file already exists")
        return

    data = {
        "candidate_no": [
            "001","002","003","004","005",
            "006","007","008","009","010",
            "011","012","013","014","015",
            "016","017","018","019","020"
        ],
        "candidate_name": [
            "Vani","Shiva","Kumaran","Arjun","Priya",
            "Rahul","Sneha","Karthik","Anitha","Suresh",
            "Meena","Vikram","Divya","Ramesh","Pooja",
            "Ajay","Nithya","Sanjay","Lavanya","Manoj"
        ],
        "python_score": [
            6,4,7,8,9,
            5,6,7,8,6,
            9,7,6,5,8,
            7,9,6,8,7
        ],
        "sql_score": [
            8,6,9,7,8,
            6,7,8,9,6,
            8,7,6,5,9,
            8,9,7,6,8
        ],
        "databricks_score": [
            6,7,8,7,9,
            6,7,8,9,6,
            8,7,6,5,9,
            8,9,7,6,8
        ],
        "pyspark_score": [
            4,8,7,6,9,
            5,6,7,8,6,
            8,7,6,5,9,
            8,9,7,6,8
        ],
        "remarks": [
            "Good","Average","Good","Very Good","Excellent",
            "Average","Good","Good","Excellent","Average",
            "Very Good","Good","Average","Needs Improvement","Excellent",
            "Good","Excellent","Good","Very Good","Good"
        ],
        "grade": [
            "B","C","B","A","A",
            "C","B","B","A","C",
            "A","B","C","D","A",
            "B","A","B","A","B"
        ]
    }

    df = pd.DataFrame(data)
    df.to_csv(FILENAME, index=False)
    st.success("CSV file with 20 records created successfully")

# ---------------- READ CSV ----------------
def load_data():
    if os.path.exists(FILENAME):
        return pd.read_csv(FILENAME)
    else:
        return pd.DataFrame()

# ---------------- SIDEBAR MENU ----------------
menu = st.sidebar.selectbox(
    "Choose an option",
    ["Create CSV", "Insert Record", "Display Records", "Update Record", "Delete Record"]
)

# ---------------- CREATE ----------------
if menu == "Create CSV":
    if st.button("Create CSV File"):
        create_csv()

# ---------------- INSERT ----------------
elif menu == "Insert Record":
    st.subheader("➕ Insert New Candidate")

    df = load_data()

    candidate_no = st.text_input("Candidate Number")
    candidate_name = st.text_input("Candidate Name")
    python_score = st.number_input("Python Score", 0, 10)
    sql_score = st.number_input("SQL Score", 0, 10)
    databricks_score = st.number_input("Databricks Score", 0, 10)
    pyspark_score = st.number_input("PySpark Score", 0, 10)
    remarks = st.text_input("Remarks")
    grade = st.text_input("Grade")

    if st.button("Insert Record"):
        if candidate_no in df["candidate_no"].values:
            st.error("Candidate number already exists")
        else:
            new_row = {
                "candidate_no": candidate_no,
                "candidate_name": candidate_name,
                "python_score": python_score,
                "sql_score": sql_score,
                "databricks_score": databricks_score,
                "pyspark_score": pyspark_score,
                "remarks": remarks,
                "grade": grade
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(FILENAME, index=False)
            st.success("Record inserted successfully")

# ---------------- DISPLAY ----------------
elif menu == "Display Records":
    st.subheader("📄 Candidate Records")
    df = load_data()
    st.dataframe(df)

# ---------------- UPDATE ----------------
elif menu == "Update Record":
    st.subheader("✏️ Update Candidate")

    df = load_data()

    if df.empty:
        st.warning("No data available")
    else:
        candidate_no = st.selectbox(
            "Select Candidate Number",
            df["candidate_no"].tolist()
        )

        new_python_score = st.number_input("New Python Score", 0, 10)
        new_grade = st.text_input("New Grade")

        if st.button("Update Record"):
            df.loc[df["candidate_no"] == candidate_no, "python_score"] = new_python_score
            df.loc[df["candidate_no"] == candidate_no, "grade"] = new_grade
            df.to_csv(FILENAME, index=False)
            st.success("✅ Record updated successfully")


# ---------------- DELETE ----------------
elif menu == "Delete Record":
    st.subheader("🗑️ Delete Candidate")

    df = load_data()

    if df.empty:
        st.warning("No data available")
    else:
        candidate_no = st.selectbox(
            "Select Candidate Number to Delete",
            df["candidate_no"].tolist()
        )

        if st.button("Delete Record"):
            df = df[df["candidate_no"] != candidate_no]
            df.to_csv(FILENAME, index=False)
            st.success("✅ Record deleted successfully")
