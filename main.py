import json
import time

import requests
import streamlit as st
from streamlit.components.v1 import html

from modal import Modal

from next_page import next_page, stop_timer
from start_timer import start_timer

LAYOUT = (1, 8, 1)


def landing_page():
    start_timer(1)
    st.markdown(
        """
        <style>

            h1:nth-of-type(1)
            {
                // text-align: center;
                direction: rtl;
            }
            p:nth-of-type(1), p:nth-of-type(2)
            {
                direction: rtl;
                color:#660066;
                text-align: center;
                font-size: 20px;
            }
        </style>
        """, unsafe_allow_html=True
    )
    desc_1 = "לפני כל סמסטר ולקראת פתיחת חלונות הזמן לבניית מערכת, אנו מוצאים את עצמנו כל שנה משקיעים זמן רב במעבר על קורסי הבחירה השונים כדי לבנות את מערכת השעות האידיאלית."
    with st.columns(LAYOUT)[1]:
        st.write(desc_1)
        st.markdown(
            "<p>תחסוך לך זמן ותבנה עבורך <u>מערכת אידיאלית במהירות ובקלות</u> בהתאם לתחומי העניין שלך, מטלות מועדפות, חובת נוכחות בקורסים ושעות נוחות.</p>",
            unsafe_allow_html=True)
        st.button("המשך", on_click=next_page, args=(1,))


def description_page():
    start_timer(2)
    desc = f"""<p dir="RTL" style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;text-align:justify;font-size:15px;line-height:150%;'><span style="font-size: 16px; line-height: 150%;  color: rgb(102, 0, 102);">לאחר הורדת האפליקציה, ההתחברות אליה תעשה דרך <u>חשבון המשתמש שלך</u> בפייסבוק, גוגל או אפל. בהמשך לכך עליך להזין את שם המוסד האקדמי בו את/ה לומד/ת, החוג/הפקולטה, פרטי גיליון הציונים, גיל, כתובת, תחומי העניין שלך במסגרת התחום אותו את/ה לומד/ת, מטלות מועדפות בקורס ומגבלות אישיות (לרבות עבודה, התנדבויות, ילדים וחיי משפחה).&nbsp;</span></p>
<p dir="RTL" style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;text-align:justify;font-size:15px;line-height:150%;'><span style="font-size: 16px; line-height: 150%;  color: rgb(102, 0, 102);">בהתאם לנתונים שהזנת לאפליקציה ומידע נוסף מפרופיל המשתמש שבאמצעותו התחברת לאפליקציה, יוצגו בעבורך מספר אפשרויות של מערכות שעות אשר לוקחות בחשבון את כלל הנתונים.</span></p>
<p dir="RTL" style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;text-align:justify;font-size:15px;font-family:"Calibri",sans-serif;line-height:150%;'><span style="color: rgb(102, 0, 102);"><strong><span style="font-size: 16px; line-height: 150%; ">כל שנותר לך הוא רק לבחור את מערכת השעות המתאימה ביותר עבורך!&nbsp;</span></strong></span></p>
<ul style="list-style-type: undefined;margin-left:0cmundefined;">
    <li style="color: rgb(102, 0, 102);"><span style="line-height: 150%;   font-size: 12pt;">האפליקציה <u>מעודכנת בזמן אמת</u> בהתאם להיצע הקורסים העדכני ביותר בכל מוסדות הלימוד האקדמיים בישראל, אך היא אינה ספק שירותים רשמי מטעם המוסדות האקדמיים.&nbsp;</span></li>
    <li style="color: rgb(102, 0, 102);"><span style="line-height: 150%;   font-size: 12pt;">השימוש באפליקציה הוא <u>ללא תשלום</u>, כאשר לאורך שנת הלימודים נשתמש במידע שמסרת לנו כדי להציע לך שירותים שונים בתשלום מטעמנו או מטעם שותפינו העסקיים.&nbsp;</span></li>
    <li style="color: rgb(102, 0, 102);"><span style="line-height: 150%;   font-size: 12pt; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">לפני הורדת האפליקציה יש לקרוא את תנאי השימוש ומדיניות הפרטיות שלה.</span></li>
</ul> """
    modal = Modal("תנאי שימוש", key="terms-of-service")
    if modal.is_open():
        with modal.container():
            stop_timer(2)
    with st.columns(LAYOUT)[1]:
        st.title("קצת על האפליקציה")
        st.markdown(desc, unsafe_allow_html=True)

        open_modal = st.button("למעבר לתנאי השימוש")
        if open_modal:
            modal.open()

    st.markdown(
        """
        <style>

            h1:nth-of-type(1)
            {
                text-align: center;
                direction: rtl;
            }
            p:nth-of-type(1)
            {
                direction: rtl;
            }
            li{
                direction: rtl;
                padding: 0!important;
                text-align: right;
            } 
        </style>
        """, unsafe_allow_html=True
    )


def _finish(accepted: bool):
    st.session_state.app_installed = accepted

    time_taken = time.time() - st.session_state[f"page_4_timer"]
    st.session_state[f"page_4_time_taken"] = time_taken

    project_id = "law-experiment"
    collection_name = "summaries"

    url = f"https://firestore.googleapis.com/v1/projects/{project_id}/databases/(default)/documents/{collection_name}"
    data = {
        "page_1_timing": {"doubleValue": st.session_state[f"page_1_time_taken"]},
        "page_2_timing": {"doubleValue": st.session_state[f"page_2_time_taken"]},
        "page_3_timing": {"doubleValue": st.session_state[f"page_3_time_taken"]},
        "page_4_timing": {"doubleValue": st.session_state[f"page_4_time_taken"]},
        "terms_of_service": {"booleanValue": st.session_state.terms_of_service},
        "terms_of_service_num": {"integerValue": st.session_state.terms_of_service_num},
        "app_installed": {"booleanValue": st.session_state.app_installed},
        "location_access": {"stringValue": st.session_state.get("location_access", "none")},
        "contact_access": {"stringValue": st.session_state.get("contact_access", "none")},
        "camera_access": {"stringValue": st.session_state.get("camera_access", "none")},
        "cookies": {"stringValue": st.session_state.get("cookies", "none")},
        "advertisements": {"booleanValue": st.session_state.get("advertisements", False)},
    }
    headers = {
        "Content-Type": "application/json",
    }
    print("sending")
    res = requests.post(url, data=json.dumps({"fields": data}), headers=headers)
    print("sent")
    print(res.json())
    st.session_state.submitted = True


def app_installation():
    start_timer(4)
    st.title("התקנת האפליקציה")
    cols = st.columns(5)
    if st.session_state.get("submitted") is None:
        st.session_state.submitted = False
    with cols[2]:
        if st.session_state.submitted:
            url = "https://docs.google.com/forms/d/e/1FAIpQLSfxkrlEbibzw1v1gl_uhBFSPTBrnAP3ccCgCEqBzKF4nEfZGA/viewform?usp=sf_link"
            st.markdown(f"<a href='{url}'>לחצו כאן להמשך</a>", unsafe_allow_html=True)
        else:
            print("Meir")
            st.button("התקנת האפליקציה", on_click=_finish, args=(True,))
            st.button("אינני מעוניין להמשיך", on_click=_finish, args=(False,))





    st.markdown(
        """
        <style>

            h1:nth-of-type(1)
            {
                text-align: center;
                direction: rtl;
            }
            button{
                direction: rtl;
                text-align: right;
            }

        </style>
        """, unsafe_allow_html=True
    )


def get_page(page_num: int) -> callable:
    if page_num == 1:
        return landing_page
    elif page_num == 2:
        return description_page
    else:
        return app_installation


if __name__ == '__main__':
    st.set_page_config(layout='wide', )
    streamlit_style = """
    			<style>
    			@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap');

    			html, body, [class*="css"], h1, div, p, label, button  {
    			font-family: 'Heebo', sans-serif;
    			}
    			// prevents from scrolling when clicking
    			*, ::before, ::after {
                    box-sizing: inherit;
                }
                h1:nth-of-type(1), img:nth-of-type(1){
                    text-align: center;
                    direction: rtl;
                }
        </style>"""
    st.markdown(streamlit_style, unsafe_allow_html=True)
    st.title("SchedI – לבניית מערכת שעות בשניות! ")
    cols = st.columns(3)
    with cols[1]:
        st.image("logo.jpeg", width=300)
    get_page(st.session_state.get("page_num", 1))()
