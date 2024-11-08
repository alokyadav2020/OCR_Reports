import streamlit as st 
from src.pipeline.google_storage import create_bucket_and_folder
from src.SQLdb.sql_query_engine import insert_data,fetch_all
import pandas as pd


st.set_page_config(
    page_title="Project",
    layout="wide",
    menu_items={
              'Get Help': 'https://www.extremelycoolapp.com/help',
              'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
})

@st.dialog("Create Project")
def Project_Title():

    with st.form("Create Projetc",clear_on_submit=True):
        # st.write("Create Project")

        project_name= st.text_input(label="Project Name").replace(" ","-").lower()
        project_description = st.text_area(label="Project Description")
              
        user_id = st.session_state.user_id
        save_button = st.form_submit_button(label="Submit",use_container_width=True)

        if save_button:

            if not project_name:
                st.warning("Project Name is required !!")

            if project_name:
                Bucke_folder_path = create_bucket_and_folder(bucket_name=str(project_name),folder_name="pdf_folder")

                print(Bucke_folder_path)

                if Bucke_folder_path is not None:


                    query = f""" INSERT INTO ORG_Title(Title_Name, Description, Org_File_Path, Id_user)

                                VALUES('{str(project_name)}', '{str(project_description)}', '{str(Bucke_folder_path)}', {int(user_id)})

                            """
                    

                    result = insert_data(query)
                    
                    if result.get('rows_affected', 0) > 0:
                        st.info("Project details saved successfully!")
                        project_name = ""
                        project_description = ""
                        Bucke_folder_path = ""
                        st.rerun()
                    else:
                        st.error("An error occurred during project creation.")

                else:
                    st.write("Project not saved Please try agian with different name")        



def display_projects():
    st.write("Project Details")
    user_id = st.session_state.user_id
    columns = ["Project Name", "Description", "Project Path"]
    query = f"SELECT Title_Name, Description, Org_File_Path  FROM MORdb.ORG_Title where Id_user = {int(user_id)};"
    result = fetch_all(query)
    if result:
        df = pd.DataFrame(data=result,columns=columns)
        st.dataframe(df,use_container_width=True,selection_mode="single-row",hide_index=True)


            


with st.container():

    if st.button("Create New Project"):
     Project_Title()
    #  st.rerun()

with st.container(border=True):
    display_projects()




# st.write(st.session_state.role)
# st.write(st.session_state.user_id)
# st.write(st.session_state.user_email)
