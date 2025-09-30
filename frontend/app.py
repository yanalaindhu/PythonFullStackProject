# app.py 
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"   

st.set_page_config(page_title="📓 Daily Journal", layout="centered")
st.title("📓 Daily Journal Web App")
def show_error(res):
    try:
        data = res.json()
        msg = data.get("detail", "Unknown error")
    except ValueError: 
        msg = res.text if res.text else "No response from server"
    st.error(f"❌ {msg}")

# ---------------- Sidebar Menu ----------------
menu = ["Users", "Journal Entries"]
choice = st.sidebar.selectbox("Navigate", menu)

# ---------------- USERS ----------------
if choice == "Users":
    st.header("👤 Manage Users")

    # Create user
    with st.form("create_user"):
        st.subheader("Add New User")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Create User")
        if submitted:
            res = requests.post(f"{API_URL}/users", json={
                "username": username,
                "email": email,
                "password": password
            })
            if res.status_code == 200:
                st.success("✅ User created successfully!")
            else:
                show_error(res)

    # Display all users
    st.subheader("All Users")
    res = requests.get(f"{API_URL}/users")
    if res.status_code == 200:
        users = res.json().get("users", [])
        if users:
            for u in users:
                with st.expander(f"👤 {u['username']} (ID: {u['user_id']})"):
                    st.write(f"📧 {u['email']}")

                    # Update user
                    new_username = st.text_input(f"Update Username {u['user_id']}", value=u['username'])
                    new_email = st.text_input(f"Update Email {u['user_id']}", value=u['email'])
                    new_password = st.text_input(f"New Password {u['user_id']}", type="password")

                    if st.button(f"Update User {u['user_id']}"):
                        res_update = requests.put(f"{API_URL}/users/{u['user_id']}", json={
                            "username": new_username,
                            "email": new_email,
                            "password": new_password if new_password else None
                        })
                        if res_update.status_code == 200:
                            st.success("✅ User updated successfully!")
                        else:
                            show_error(res_update)

                    # Delete user
                    if st.button(f"Delete User {u['user_id']}"):
                        res_delete = requests.delete(f"{API_URL}/users/{u['user_id']}")
                        if res_delete.status_code == 200:
                            st.success("🗑️ User deleted successfully!")
                        else:
                            show_error(res_delete)
        else:
            st.info("No users found.")
    else:
        show_error(res)

# ---------------- JOURNAL ENTRIES ----------------
elif choice == "Journal Entries":
    st.header("📝 Manage Journal Entries")

    # Select user
    user_id = st.number_input("Enter User ID", min_value=1, step=1)

    if user_id:
        # Create entry
        with st.form("create_entry"):
            st.subheader("Add New Entry")
            title = st.text_input("Title")
            content = st.text_area("Content")
            submitted = st.form_submit_button("Add Entry")
            if submitted:
                res = requests.post(f"{API_URL}/entries", json={
                    "user_id": user_id,
                    "title": title,
                    "content": content
                })
                if res.status_code == 200:
                    st.success("✅ Entry added successfully!")
                else:
                    show_error(res)

        # Show entries
        st.subheader("Previous Entries")
        res = requests.get(f"{API_URL}/entries/{user_id}")
        if res.status_code == 200:
            entries = res.json().get("entries", [])
            if entries:
                for e in entries:
                    with st.expander(f"📌 {e['title']} (ID: {e['entry_id']})"):
                        st.write(e["content"])
                        st.caption(f"Created at: {e['created_at']}")

                        # Update entry
                        new_title = st.text_input(f"Update Title {e['entry_id']}", value=e['title'])
                        new_content = st.text_area(f"Update Content {e['entry_id']}", value=e['content'])
                        if st.button(f"Update Entry {e['entry_id']}"):
                            res_update = requests.put(f"{API_URL}/entries/{e['entry_id']}", json={
                                "title": new_title,
                                "content": new_content
                            })
                            if res_update.status_code == 200:
                                st.success("✅ Entry updated successfully!")
                            else:
                                show_error(res_update)

                        # Delete entry
                        if st.button(f"Delete Entry {e['entry_id']}"):
                            res_delete = requests.delete(f"{API_URL}/entries/{e['entry_id']}")
                            if res_delete.status_code == 200:
                                st.success("🗑️ Entry deleted successfully!")
                            else:
                                show_error(res_delete)
            else:
                st.info("No entries for this user.")
        else:
            show_error(res)
