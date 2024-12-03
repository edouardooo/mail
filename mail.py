import streamlit as st
import yagmail
import schedule
import time
from threading import Thread

# Configuration du compte email
SENDER_EMAIL = "hackercestpasbienmonpetit@gmail.com"
SENDER_PASSWORD = "chehcheh"

# Fonction pour envoyer un email
def send_email(receiver, subject, message):
    try:
        yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
        yag.send(to=receiver, subject=subject, contents=message)
        st.write(f"Email envoyé à {receiver}")
    except Exception as e:
        st.error(f"Erreur lors de l'envoi : {e}")

# Gestion des tâches récurrentes
def schedule_emails(receiver, subject, message):
    def task():
        send_email(receiver, subject, message)
    
    schedule.every(10).minutes.do(task)

    # Boucle pour exécuter les tâches planifiées
    while True:
        schedule.run_pending()
        time.sleep(1)

# Interface utilisateur Streamlit
st.title("Envoi d'Emails Automatisés et Récurrents")

receiver = st.text_input("jumonbeshel@hotmail.com")
subject = st.text_input("on ne vole pas les comptes des gens")
message = st.text_area("tu recevras ce mail tréééééés souvent")

if st.button("Programmer un envoi toutes les 10 minutes"):
    st.write("Envoi récurrent programmé.")
    # Démarrer le thread pour l'envoi récurrent
    thread = Thread(target=schedule_emails, args=(receiver, subject, message), daemon=True)
    thread.start()

if st.button("Envoyer une fois"):
    send_email(receiver, subject, message)
