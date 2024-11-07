import streamlit as st
from src.SQLdb.sql_query_engine import insert_data


ROLES = ["Admin", "User"]

def registration_form():
    with st.form("Registration Form", clear_on_submit=True):
        st.write("Registration Form")
        
        # User inputs
        full_name = st.text_input(label="Full Name")
        email = st.text_input(label="Email")
        is_active = st.toggle(label="Active User", value=False)
        username = st.text_input("UserName")
        password = st.text_input("Password", type="password")
        roles = st.selectbox("Role", ROLES)
        
        # Form submission button
        submit_button = st.form_submit_button("Submit", use_container_width=True)
        
        # Validate inputs and submit
        if submit_button:
            if not full_name:
                st.warning("Full name is required")
            if not email:
                st.warning("Email is required")
            if not username:
                st.warning("Username is required")
            if not password:
                st.warning("Password is required")

            # Only proceed if all fields are filled
            if full_name and email and username and password:
                # Prepare SQL query with parameterization to avoid SQL injection
                query = f"""
                    INSERT INTO User_Table (Name, Email, IsActive, UserName, Password, Role) 
                    VALUES ('{str(full_name)}', '{str(email)}', {int(is_active)}, '{str(username)}', '{str(password)}', '{str(roles)}');
                """
                # st.write("Executing query:", query)  # This line is just for debugging
                
                # Insert data and handle the result
                result = insert_data(query)
                
                if result.get('rows_affected', 0) > 0:
                    st.info("User Registration Details Inserted successfully!")
                else:
                    st.error("An error occurred during registration.")

# Run the registration form function
registration_form()

# with st.form("Registraion Form",clear_on_submit=True):
#     with  st.container():
#         st.write("Registraion Form")
#         full_name = st.text_input(label="Full Name")
#         Email = st.text_input(label="Email")
#         # st.radio("Active User",["NO","YES"],index=None)
#         IsActive = st.toggle(label="Active User")
#         username = st.text_input("UserName")
#         password = st.text_input("Password",type="password")
#         roles = st.selectbox("Role",ROLES)
        
        
#         st.form_submit_button("Submit",use_container_width=True)

#         if st.form_submit_button:
#             if full_name == "":
#                 st.warning(" Full name is required")
#             if Email == "":
#                 st.warning("Email is required")   
#             if username == "":
#                 st.warning("usename is required")
#             if password == "":
#                 st.warning("Password is required")


#             if full_name != "" and Email != "" and username != "" and password != "":
#                 query = f"Insert INTO User_Table (Name,Email,IsActive,UserName,Password,Role) VALUES ('{str(full_name)}','{str(Email)}',{int(0)},'{str(username)}','{str(password)}','{str(roles)}');"
#                 print(query)
#                 rslt= insert_data(query)
#                 print(rslt)
                
#                 if rslt['rows_affected'] > 0:
#                     st.info("User Registration Details Inserted successful !!")
                  
