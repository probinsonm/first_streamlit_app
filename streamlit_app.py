import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Arquitectura de Base de Datos')

streamlit.header('Aplicación de Gestión de Clientes')

streamlit.text('📔 Módulo de Gestion de Clientes')

  
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * FROM fruit_load_list")
#my_data_rows = my_cur.fetchall() 

streamlit.header("Obtener la lista de clientes:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM cliente")
    return my_cur.fetchall()
 
if streamlit.button('Desplegar la lista'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
#streamlit.stop()

def  insert_row_snowflake(new_id, new_name,new_addr):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("INSERT INTO Cliente VALUES ("+new_id+",'"+new_name+"','"+new_addr+"')")
    return "Se agrego a " + new_name
    
streamlit.header("Ingresar nuevo Cliente:")
add_id = streamlit.text_input('Identificacion:','10')
add_name = streamlit.text_input('Nombre Completo:','John Doe')
add_addr = streamlit.text_input('Dirección','Provincia/Distrito/Calle')
if streamlit.button('Agregar nuevo cliente'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  streamlit.text(insert_row_snowflake(add_id,add_name,add_addr))

#streamlit.write('Thanks for adding',add_my_fruit)
#my_cur.execute("INSERT INTO fruit_load_list VALUES ('from streamlit')")
