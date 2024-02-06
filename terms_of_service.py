import random

import streamlit as st
import codecs

from start_timer import start_timer

from next_page import next_page


def terms_of_service_modal():
    start_timer(3)
    st.markdown(
        """
        <style>

            h1:nth-of-type(1)
            {
                text-align: center;
                direction: rtl;
            }
            p
            {
                direction: rtl;
            }
            li{
                direction: rtl;
                padding: 0!important;
                text-align: right;
            }
            label{
                direction: rtl;
            }

            .stRadio{
                direction: rtl;
            }

        </style>
        """, unsafe_allow_html=True
    )

    terms_index = st.session_state.terms_of_service_num
    if terms_index != 3:
        st.title("תנאי השימוש")
    if st.session_state.terms_of_service_num == 1:
        _terms_of_service_1()
    elif st.session_state.terms_of_service_num == 2:
        _terms_of_service_2()
    else:
        _terms_of_service_3()

    cols = st.columns((4, 10, 4))
    with cols[1]:
        st.session_state.location_access = st.radio(label='אני נותן לאפליקציה "SchedI" גישה למיקום המכשיר שלי',
                                                    options=["בזמן השימוש באפליקציה", "רק הפעם",
                                                             "אין אישור"]) if terms_index == 2 else None
        st.session_state.contact_access = st.radio(label='אני נותן לאפליקציה "SchedI" גישה לאנשי הקשר שלי',
                                                   options=["בזמן השימוש באפליקציה", "רק הפעם",
                                                            "אין אישור"]) if terms_index == 2 else None
        st.session_state.camera_access = st.radio(label='אני נותן לאפליקציה "SchedI" גישה למצלמה שלי',
                                                  options=["בזמן השימוש באפליקציה", "רק הפעם",
                                                           "אין אישור"]) if terms_index == 2 else None
        st.session_state.cookies = st.radio(
            label='אנו משתמשים בקובצי Cookie כדי לאפשר לאתר שלנו לפעול כהלכה, להתאים אישית תוכן ומודעות וכמובן את לוח הסטודנט שלך. בנוסף, אנו משתפים מידע אודות השימוש שלך באתר שלנו עם שותפינו העסקיים.',
            options=["קבל את כל קבצי ה-Cookie", "בצע הגדרות אישיות של קובצי ה-Cookie",
                     "דחה הכל(במידה ולא תאשר את הקבצים הדבר יפגע באיכות השירות שתקבל)"]) if terms_index == 2 else None
        if st.session_state.get("advertisements") is None:
            st.session_state.advertisements = False
        st.session_state.advertisements = st.checkbox(
            "אני מעוניין שהאפליקציה תשלח לי הצעות פרסומיות אשר תואמות את העדפותיי") if terms_index == 2 else False
        if st.session_state.get("terms_of_service") is None:
            st.session_state.terms_of_service = False
        st.session_state.terms_of_service = st.checkbox("קראתי והסכמתי לתנאי השימוש")


def _terms_of_service_1():
    cols = st.columns((4, 10, 4))
    with cols[1]:
        st.markdown("""<style>
            li{
                white-space: normal!important;
            }
        </style>""", unsafe_allow_html=True)
        st.markdown("""
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">חשוב להקפיד לקרוא היטב את תנאי השימוש לפני השימוש באפליקציה, היות וכל שימוש כפוף למדיניות הפרטיות, תנאי השימוש והוראות הדין הרלוונטי. הגלישה והשימוש באפליקציה פירושם הסכמתכם לאמור בתנאי השימוש ובמסמך מדיניות הפרטיות, ואם קיים תנאי כלשהו במסמכים אלו שנוגדים את הסכמתכם, אתם מתבקשים להימנע מגלישה ושימוש.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">ההקדמה לתנאי השימוש היא חלק בלתי נפרד מהמסמך, ותנאי השימוש הם בבחינת הסכם משפטי מחייב בין כל גולש שמשתמש בשירות לבין בעלי השירות, כלומר, הוא אינו מהווה הסכם שפועל לטובת צד ג&apos; כלשהו.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">לשון רבים ויחיד.&nbsp;בכל מקום שבו תנאי השימוש נכתבים בלשון רבים, הוראות התנאים חלות גם על יחידים, ולהיפך.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">לשון זכר ונקבה.&nbsp;בכל מקום בתנאי השימוש, בו הנוסח נכתב בלשון זכר, התנאים חלים גם על נשים, והניסוח מופיע בלשון זכר רק מטעמי נוחות.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בשילוב עם מדיניות הפרטיות של האפליקציה, תנאי השימוש מהווים את הבסיס לגלישה ושימוש באפליקציה. כל שימוש באפליקציה באופן שאינו מצוין במפורש בתנאי שימוש אלה ומופיע בהם, מותנה וכפוף אף להסכמת המשתמשים למדיניות הפרטיות של האפליקציה, בנוסח המלא שלה, כפי שהוא מופיע במדיניות פרטיות של האפליקציה.</span></p>
<ol style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">השימוש באפליקציה יהיה כרוך במסירת פרטים אישיים. חשוב להבין שהחוק אינו מחייב את המשתמשים באפליקציה למסור את המידע האישי שלהם או את פרטיהם, ומסירת כל מידע אישי מתבצעת רק בהתאם לרצון חופשי והסכמה אישית.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מסירת פרטים חלקיים או שאינם נכונים היא התנהלות שעלולה למנוע את האפשרות להשתמש בחלק משירותי האפליקציה או להשלים את תהליך הרישום ובכך לפגוע באפשרות לקבל את השירות המוצע על ידי האפליקציה או לפגוע באיכות השירות הניתן, כמו גם פגיעה באפשרות ליצור קשר עם המשתמשים בהתאם לצורך.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="2">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">השימוש באפליקציה ללא תשלום. אולם, האפליקציה שומרת לעצמה את הזכות להציע למשתמש שירותים שונים בתשלום מטעמה או מטעם שותפיה העסקיים.&nbsp;</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">האפליקציה שומרת לעצמה את הזכות לגבות תשלומים עבור שימוש באפליקציה, בתנאי שגביית התשלומים תאושר מראש על ידי המשתמשים ותלווה בהודעה מוקדמת מראש.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="3">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מפעיל השירות רשאי לשנות, להסיר, למחוק, להוריד, לעדכן או להוסיף תנאי שימוש למסמך זה, בהתאם לשיקול דעתו הבלעדי, בזמנים שונים ובכפוף להוראות הדין.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">השימוש באפליקציה או במערכות המופיעות בה יהיה כפוף לתנאים החלים לאחר העדכונים, השינויים והתוספות, ולכן על המשתמשים לקרוא היטב את תנאי השימוש לפני השימוש באפליקציה.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="4">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">כדי להירשם לשימוש באפליקציה, יש לסמן את תיבות הסימון המתאימות ולהקליק על הכפתור לאישור. מילוי הפרטים האישיים וסימון התיבות הרלוונטיות בתהליך הבקשה, עם לחיצה על כפתור האישור בסיום, פירושה אישור המשתמשים שקראו את תנאי השימוש, הוראות תהליך ההרשמה ואת מסמך מדיניות הפרטיות, ושהם מסכימים לתנאים לאחר שקראו והבינו את כל האמור בהם.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">המשתמשים באפליקציה מצהירים שהם מודעים לכך שאחריותם היא לספק את כל המידע הנדרש כדי לקבל את המוצרים.&nbsp;</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="5">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:14pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">חל איסור על העלאת מידע או תכנים שיש בהם את המאפיינים הבאים:</span></p>
    </li>
</ol>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:14pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">שיבוש, הפרעה, הגבלה או מניעת השימוש באפליקציה הן לבעלי האפליקציה או למשתמשים אחרים;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מידע מעליב;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מידע פוגעני או שעלול להוות חומר פוגעני;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מידע משמיץ או וולגרי;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מידע שיש בו הוצאת דיבה;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">רישום צדדים שלישיים או פתיחת סיסמאות וחשבונות בשמם ועבורם;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">העלאה או פרסום מידע או תכנים שקריים, שאינם מדויקים; מטעים או מסולפים;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מידע שיש בו איומים;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מידע פורנוגרפי;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">או כל מידע אסור לשימוש או לפרסום.</span></p>
    </li>
</ul>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">חל איסור על העלאת מידע או תכנים שיש בהם בבחינת נזק לאפליקציה, למשתמשים בו, כמו למשל שורות קוד; תוכנות מזיקות; &apos;סוס טרויאני&apos;; החדרת וירוסים שונים; או כל תוכנה אחרת שיש בה על מנת לפגוע בהתנהלות התקינה של האפליקציה והשימוש בו, או ההתנהלות והשימוש באפליקציה למשתמשים אחרים, כמו גם נזק למשתמשים ולאפליקציה, או למחשבים ולציוד.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">חל איסור גם על עזרה או שידול לאחרים שמבקשים להתנהל או לבצע פעולה אסורה באפליקציה, מכל סוג שהוא, כולל הפעילויות האסורות המפורטות בתנאי השימוש.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">תכנים לעיל יוסרו מהאפליקציה ואף יש בהם כדי להביא להסרת חשבון המשתמש והפסקת ההתקשרות עימו.&nbsp;</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="6">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:14pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מבלי לגרוע מהאמור בסעיפי תנאי השימוש, החברה יכולה למנוע שימוש באפליקציה למשתמשים רשומים או שאינם רשומים, או לכלל הציבור, בכל אחד מהמקרים הבאים:</span></p>
    </li>
</ol>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:14pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">תנאי השימוש באפליקציה הופרו.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בוצע מחדל או פעילות שיש בהם פגיעה באפליקציה, בבעלי האפליקציה, במידע שמצוי בידי החברה; בציוד החברה; או במשתמשים אחרים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:14pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">המשתמשים מסרו פרטים חסרים, שגויים או שקריים.</span></p>
    </li>
</ul>
<ol style="margin-top:0;margin-bottom:0;" start="7">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:14pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">האפליקציה שומרת לעצמה את הזכות להסיר תוכן שהמשתמשים הזינו במסגרת הרישום לאפליקציה ואף להפסיק את ההתקשרות עם המשתמש במיידי וללא כל פירוט מצידה, בכל אחד מהמקרים הבאים:&nbsp;</span></p>
    </li>
</ol>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">המשתמש הפר את תנאי השימוש ומדיניות הפרטיות.&nbsp;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">המשתמש הכניס תוכן לא נכון, לא חוקי או פוגעני.&nbsp;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מכל סיבה נוספת שנראית לבעלי האפליקציה מהותית ופוגעת בשירות במפעיליו, במשתמש, בצדדים שלישיים ובמשתמשים אחרים.&nbsp;</span></p>
    </li>
</ul>
<ol style="margin-top:0;margin-bottom:0;" start="8">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">לנותן השירות יש את הזכות להפסיק חלק מפעילות האפליקציה או את כל הפעילות לפרק זמן קצר, זמני, ארוך או לתמיד, כולל הפסקת מתן שירותים, באופן חלקי או מלא, כמו גם הגבלת או הפחתת מתן השירותים, ללא הודעה מוקדמת מראש.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">הגבלת אחריות:</span></p>
    </li>
</ol>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בעלי האפליקציה אינם אחראים לנזקים ישירים או עקיפים מכל סוג שהוא, שייגרמו למשתמשים או למי מטעמם, בכל מקרה בו מידע אישי כלשהו יאבד או יגיע לגורמים עוינים, או שיתבצע בו שימוש כלשהו שאינו בהרשאה.</span></p>
    </li>
</ul>
<p dir="rtl" style="line-height:2.4;margin-right: 36pt;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><br></p>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בכל מקום בתנאי השימוש בו משתמע או נכתב במפורש שנותן השירות יחליט על ענין כלשהו, יבצע פעולה מסוימת או יקבע דבר מסוים, לנותן השירות מוקנית באופן מפורש או מכללא הסמכות, הזכות או שיקול הדעת הבלעדי לפעול, לבצע, או להחליט לא לפעול, בהתאם לשיקול דעתו הבלעדי מבלי שתחול עליו חובת הנמקה.</span></p>
    </li>
</ul>
<p dir="rtl" style="line-height:2.4;margin-right: 36pt;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">התנהלות נותן השירות לא תהיה ניתנת לערעור ותיחשב לסופית, באופן שלמשתמשים לא תהיה אפשרות לטעון נגד השירות, לתבוע אותו, או להביע דרישה הנוגעת לפעילותו או הימנעות מפעילות, כפי שנאמר.</span></p>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">המשתמשים באפליקציה מצהירים שלבעלי האפליקציה יש זכות והרשאה להשתמש במידע, כפי שמונח זה מוגדר במדיניות הפרטיות, בהתאם למדיניות הפרטיות. נותן השירות אינו אחראי לכל נזק מכל סוג שהוא, שנגרמו כתוצאה ממקרים שנובעים מהעברת הפרטים לספק, או כתוצאה ממקרים שאינם בשליטתו, או כתוצאה מאובדן המידע, או כתוצאה ממקרים שמוגדרים בבחינת כוח עליון.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">למרות שבעלי האפליקציה נוקטים בכל המאמצים לפרסום תכנים ומידע נכונים, אמינים ומדויקים, עדיין עשויים להופיע אי דיוקים או להתפרסם שגיאות בתכנים, כולל שיבוש במידע. בעלי האפליקציה אינם אחראים לשום נזק, משום סוג, שייגרם למשתמשים כתוצאה מפרסום התכנים והמידע.</span></p>
    </li>
</ul>
<p dir="rtl" style="line-height:2.4;margin-right: 36pt;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בכל מקרה בו המשתמשים אינם מרוצים מהאפליקציה, האפשרות הבלעדית והיחידה שעומדת לרשותם היא הפסקת השימוש באפליקציה.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="10">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">לבעלי האפליקציה יש את הזכות, בהתאם לשיקול דעתם הבלעדי, לבצע פעולות שדרוג, ריענון או תחזוקה לאפליקציה, כולל שינויי עיצוב או כל התנהלות אחרת שעשויה למנוע מהמשתמשים את הגישה לאפליקציה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">באפליקציה מופיעים קישורים שמפנים לאפליקציות חיצוניות, וחלק מהמידע המפורסם באפליקציה מבוסס על מידע שמגיע מצדדים שלישיים, כמו למשל ממוסדות אקדמיים.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בעלי האפליקציה אינם ערבים לכם שהמידע שנמצא אצל צדדים שלישיים הוא מדויק ואמין, והמשתמשים מצהירים שהם מודעים לעובדה זו ומבינים את השלכותיה. בעלי האפליקציה לא יימצאו אחראים לכל נזק מכל סוג שהוא שייגרם למשתמשים כתוצאה מהסתמכות על המידע המופיע באפליקציה.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="12">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בעלי האפליקציה יכולים לשלוח הודעות לכתובת הדואר האלקטרוני או לכתובת הדואר שהמשתמשים מסרו במהלך הרישום לאפליקציה והמשתמשים יכולים ליצור קשר עם בעלי האפליקציה בעמוד יצירת הקשר.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">כל הודעה שיש לשלוח מצד אחד שני, למעט אם צוין אחרת בתנאי השימוש, תתבצע באמצעות דואר האלקטרוני. אם ההודעה נשלחה לבעלי האפליקציה, היא תיחשב שנתקבלה רק אם בוצע אישור מסירה על קבלת ההודעה.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="13">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">הדין שחל על אפליקציה או על כל נושא ועניין שקשורים אליו, כולל תנאי שימוש אלה, וכל מקרה של סכסוך משפטי ישיר או עקיף לאפליקציה או לשימוש בו, הוא הדין הישראלי בלבד.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:14pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">הסמכות הבלעדית והייחודית לדון בכל סכסוך או מחלוקת משפטית, שקשורים באופן ישיר או עקיף לאפליקציה או לשימוש בו, היא הסמכות של בית המשפט המוסמך במחוז מרכז, ולא לכל ערכאה שיפוטית אחרת.</span></p>
<h1>מדיניות פרטיות</h1>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">יש לקרוא היטב את המסמך, שמתאר את מדיניות הפרטיות באפליקציה, שמהווה חלק בלתי נפרד ממסמך תנאי השימוש באפליקציה.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מדיניות הפרטיות, כפי שהיא מופיעה במסמך זה חלה על כל שימוש, גלישה או צפייה באפליקציה, בכל ומכל אמצעי תקשורת. בכל מקרה בו המשתמשים אינם מסכימים לתנאי מתנאי מדיניות הפרטיות, עליהם להפסיק מידית את השימוש או הגלישה באפליקציה.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">אופן הניסוח במדיניות הפרטיות מנוסח בלשון זכר רק מטעמי נוחות, אך הוא מופנה כלפי גברים ונשים. כמו כן, בכל מקום במסמך בו הניסוח נכתב בלשון יחיד, הוא מופנה גם כלפי רבים, ולהיפך.</span></p>
<ol style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:14pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">השירות שמוצע באמצעות האפליקציה, קרי בניית מערכת שעות מותאמת אישית, כרוך במסירת פרטים ומידע אישי (להלן: &quot;המידע&quot;), כמו למשל:</span></p>
    </li>
</ol>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">גיל.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">שם מלא.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">כתובת מגורים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">פרטי גיליון הציונים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">כתובת דואר אלקטרוני.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מגבלות אישיות (לרבות עבודה, התנדבויות, ילדים וחיי משפחה).</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">או כל מידע אישי או מזהה אחר.</span></p>
    </li>
</ul>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בהתאם לחוק, יודגש שהמשתמשים אינם חייבים למסור מידע ופרטים אישיים, ומסירת פרטים אלו תלויה רק ברצונם החופשי והסכמתם.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בהתאם, לא חלה על המשתמשים חובת הסכמה לאיסוף, מסירת או הפקת המידע שנמסר על ידם, ובכל פעם שהם משתמשים באפליקציה, הם מביעים את הסכמתם מרצונם לשימוש במלוא המידע, מסירתו או העברתו, כפי שמפורט במדיניות הפרטיות.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">יחד עם זאת, מסירת פרטים חלקיים, שגויים או שקריים, עלולה למנוע מהמשתמשים את האפשרות להשתמש בחלק משירותי האפליקציה או בכולם, או להשלים את תהליך הרישום, ובכך לפגוע באיכות השירות שהמשתמשים מקבלים.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="2">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">האיסוף של המידע נעשה כדי לבנות למשתמש את מערכת השעות האידיאלית עבורו אשר מותאמת לצרכיו האישיים בהתאם למידע שמסר.&nbsp;</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">כמו כן, המשתמשים באפליקציה מסכימים שבעלי האפליקציה יאספו את המידע ויפיקו אותו, כולל ביצוע שימוש בו, על מנת לאפשר שימוש באפליקציה, למטרות הבאות:</span></p>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בניית מערכת שעות.&nbsp;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">תיעדוף פרסומות.&nbsp;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">שיפור חווית השירות.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">יצירת התאמות אישיות.&nbsp;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">יצירת קשר.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">אימות פרטים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">שליחת עדכונים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">פניה וזיהוי.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מתן שירותים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">עיבוד מידע.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מחקר סטטיסטי ופילוח.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">פרסום ושיווק.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מטרות עסקיות.</span></p>
    </li>
</ul>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בעלי האפליקציה רשאים גם להשתמש במידע האישי למטרות גילוי, מסירה או מכירת המידע לצדדים שלישיים, בארץ או בחו&quot;ל.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="3">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:14pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">המשתמשים מביעים את הסכמתם לכך שבעלי האפליקציה יאספו את המידע האישי וישמרו אותו, כפי שהוא נמסר במהלך שימוש המשתמשים באפליקציה, בין אם המידע נמסר ישירות על ידי המשתמשים או התקבל בעקיפין. בין היתר, המידע שנאסף ונשמר כולל:</span></p>
    </li>
</ol>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:14pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">היסטוריית גלישה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">פרסומות שהמשתמשים נחשפו אליהן שמופיעות באפליקציה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מידע שהמשתמשים קראו באפליקציה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מיקום.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">צפייה בעמודים השונים באפליקציה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">או כל מידע אחר שנמסר על ידי המשתמשים.</span></p>
    </li>
</ul>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">כל המידע והפרטים האישיים, כפי שהם נמסרו על ידי המשתמשים, יישמרו במאגרי המידע של בעלי האפליקציה.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="4">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:14pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">לבעלי האפליקציה יש זכות להשתמש במידה ולהעביר אותו לצדדים שלישיים. לרבות שותפים עסקיים וספקי שירותים שונים, בהתאם לשיקול דעתם, בין היתר גם כדי למלא אחרי הוראות הדין, כולל:</span></p>
    </li>
</ol>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:14pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">החוקים והחקיקות;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">הפקודות והצווים;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">האמנות והתקנות;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">הוראות המינהל והוראות רשמיות;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">הנחיות או חוזרים של גופים רגולטוריים או שלטוניים שונים.</span></p>
    </li>
</ul>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מטרת העברת המידע לצדדים שלישיים תתבצע בכל מקרה שנוגע לאחד או יותר מהתרחישים הבאים:</span></p>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בקשה או תלונה הנוגעת לשימוש באפליקציה;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">טיפול בבעיות טכניות או בעיות אבטחה של השימוש באפליקציה או השימוש במערכותיו;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">סכסוכים משפטיים בין המשתמשים לבין בעלי האפליקציה, כדי להשיב על תביעות של צדדים שלישיים;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">כשהשימוש באפליקציה התבצע באופן שמנוגד להוראות כל דין, לתנאי השימוש או למטרות שיפור או שינוי האפליקציה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">הגנה על זכויות הקניין של המשתמשים באפליקציה או של בעלי האפליקציה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">הצעת שירותים נוספים למשתמשים מטעם אותם צדדים שלישיים במסגרת פרסום ממוקד באפליקציה.&nbsp;</span></p>
    </li>
</ul>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">המשתמשים מאשרים שלמטרות המפורטות במסמך מדיניות פרטיות זה, לבעלי האפליקציה יש זכות להעביר את המידע לצדדים שלישיים, וכי להם יש זכות לבצע שימוש במידע שקיבלו לאותן מטרות כפי שהן מפורטות בתנאי השימוש ובמדיניות הפרטיות, כמו גם לשמור את המידע במאגרי המידע שלהם. בעלי האפליקציה אינם אחראים לשום סוג של שימוש של צדדים שלישיים במידע.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="5">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">כחלק מהתפעול השוטף של אפליקציה נעשה שימוש ב&quot;עוגיות&quot;, שבין היתר משמשות להבנת העדפות המשתמש והתאמות אישיות, אימות פרטים אישיים, או איסוף מידע סטטיסטי. מובהר בזאת שיתכן שלא יתבקש אישור המשתמשים לפני השימוש, והמשתמשים רשאים בכל עת לנקות את &quot;העוגיות&quot; מהדפדפן שלהם, או להגדיר אותו באופן שיסרב לבצע שימוש ב&quot;עוגיות&quot;.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">אבל בעלי האפליקציה אינם מבטיחים שפעילויות אלו יאפשרו שימוש וגלישה תקינים באפליקציה, והם רשאים למנוע שירות או לחסום את השימוש באפליקציה במקרים בהם בוצעו פעולות כאמור.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="6">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">באפליקציה מופיעים קישורים שמפנים את המשתמשים לאפליקציות או אתרים שונים, כמו גם הצעות פרסום לרכישת מוצרים נוספים. מובהר שמדיניות הפרטיות כפי שהיא מפורטת במסמך זה חלה בנוגע לאפליקציה בלבד.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בעלי האפליקציה אינם אחראים למדיניות הפרטיות של אפליקציות חיצוניות, והכניסה אליהם באמצעות הקלקה על הקישורים היא באחריות הבלעדית של המשתמשים. בעלי האפליקציה אינם אחראים לשימוש או כניסה לאפליקציות אחרות, ומומלץ לקרוא בעיון את תנאי השימוש ומדיניות הפרטיות באפליקציות המקושרות לפני העברת פרטים אישיים או ביצוע פעולות שונות בהם.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="7">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">לאורך שנת הלימודים בעלי האפליקציה ישתמשו במידע שנמסר כדי להציע למשתמשים שירותים שונים בתשלום או שלא בתשלום מטעם בעלי האפליקציה או שותפיהם העסקיים או צדדים שלישיים אחרים.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">המשתמשים מאשרים שהם מסכימים לקבל דברי פרסומת כפי שמפורט בסעיף 30א&apos; לחוק התקשורת (בזק ושידורים), התשמ&quot;ב-1982 (להלן: &quot;חוק התקשורת&quot;), כמו גם לקבלת דיוורים ישירים בהתאם לחוק הגנת הפרטיות התשמ&quot;א-1981 (להלן: &quot;חוק הגנת הפרטיות) מבעלי האפליקציה ומהספקים.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מבלי לגרוע מכלליות האמור לעיל, המשתמשים באפליקציה מאשרים ומביעים את הסכמתם לקבלת כל מידע שיווקי כגון:</span></p>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">עדכונים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מבצעים והטבות.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מידע שיווקי ופרסומי.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">הצעות לרכישת שירותים או מוצרים מבעלי האפליקציה או מצדדים שלישיים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;padding:0pt 0pt 14pt 0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">סוגים שונים של דיוור ישיר.</span></p>
    </li>
</ul>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מידע שיווקי זה יכול להגיע אל המשתמשים באפליקציה כמודעות קופצות בתוך האפליקציה, בדואר האלקטרוני, במסרונים בטלפון הנייד, במערכת חיוג אוטומטי, בפקס, או בכל שיטת ואמצעי תקשורת אחר.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="8">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">זכויות במידע:&nbsp;</span></p>
    </li>
</ol>
<ul style="margin-top:0;margin-bottom:0;">
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">הזכות לעיין במידע המשתמש זכאי לעיין במידע שנאסף אודותיו, ששמור במאגרי המידע שלנו, ושמזוהה ומשויך אליו. אין אפשרות לעיין במידע שאינו מזוהה ומשויך.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">הזכות לתיקון מידע אם המשתמש מצא שהמידע שנשמר אודותיו אינו נכון, שלם, ברור או מעודכן, ניתן לפנות לבעלי האפליקציה בבקשה מפורטת לתיקון או מחיקה של המידע. למימוש זכויות אלו, ניתן לפנות לבעלי האפליקציה, באמצעות פרטי הקשר המופיעים בהמשך מסמך זה. בעלי האפליקציה יבחנו את הפנייה, וישיבו בהתאם למועדים הקבועים בחוק.&nbsp;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">הזכות לבטל הסכמה המשתמש זכאי, בכל עת, לבטל את הסכמתו לקבלת דיוור, בפניה מתאימה אל בעלי האפליקציה. לפירוט נוסף, ראה את הפרק העוסק בדיוור ישיר והודעות פרסומיות.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;font-family:'Noto Sans Symbols',sans-serif;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;" aria-level="1">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">זכויות נוספות בקשר למידע ייתכן שהמשתמש זכאי לזכויות נוספות, בקשר למידע אודותיו. לפניות בנושאים אלו, או בנושאים אחרים הקשורים למדיניות פרטיות זו, ניתן לפנות לבעלי האפליקציה באמצעות פרטי הקשר המופיעים בהמשך מסמך זה. בעלי האפליקציה יבדקו את הפניה וישיבו בהתאם.</span></p>
    </li>
</ul>
<ol style="margin-top:0;margin-bottom:0;" start="9">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">גם אם ימחק, יתוקן מידע, או תתקבל בקשתה בכל דרך אחרת, בעלי האפליקציה בכל מקרה יוסיפו וישמרו מידע שדרוש להם לשם ניהול השירות, לרבות מידע אשר דרוש להם להגנה ולשמירה על זכויותיהם המשפטיות, או לצורך עמידה בדרישות הרגולטוריות, מניעת הונאה או תרמית, ואכיפה של מדיניות פרטיות זו ותנאי השימוש באתרים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">מסירת המידע באפליקציה או איסופו במהלך השימוש באפליקציה, מתבצעים בתהליכים מאובטחים שמאפשרים הצפנת מידע שמועבר באינטרנט באופן שאינו מאפשר זיהוי או קריאה של המידע במהלך העברתו.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בעלי האפליקציה ינקטו בכל המאמצים לאבטח את המידע באפליקציה, בהתאם למקובל ולנהוג באפליקציות מסוג זה, אך אינם ערבים ואינם מבטיחים שמסדי הנתונים שלהם, כולל המידע האישי שנמסר על ידי המשתמשים, לא ייפרץ ושהמידע לא יגיע לצדדים שלישיים שאינם מורשים.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">כל עוד בעלי האפליקציה נוקטים באמצעים סבירים לאבטחת המידע, הם לא יימצאו אחראים לשום נזקים, מכל סוג שהוא, שייגרמו למשתמשים כתוצאה מפריצה לאפליקציה, למסדי הנתונים או למחשבים המפעילים אותו.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="11">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">לתשומת לב המשתמשים באפליקציה, השימוש באפליקציה או בתכנים שמפורסמים בו או בתכנים שמפורסמים באפליקציות אחרות שהאפליקציה מקשרת אליהם, עלול לחשוף אותם לסיכונים שכרוכים בשימוש באינטרנט, כולל חדירה לטלפון הנייד, למחשב, חשיפה לתוכנות זדוניות או לווירוסים, וכן הלאה.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">השימוש והגלישה באפליקציה או עיון בתכנים המפורסמים בו או בתכנים המפורסמים באפליקציות חיצוניות שהאפליקציה מקשרת אליהן, מתבצעת רק באחריות המשתמשים. בעלי האפליקציה ממליצים על התקנת תוכנות מספקות של אבטחה והגנה, לפני הכניסה לאפליקציה או ביצוע שימוש בה.</span></p>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בעלי האפליקציה לא ימצאו אחראים לנזקים מכל הסוגים, ישירים או עקיפים, שייגרמו למשתמשים כתוצאה משימוש באפליקציה.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="12">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">על מדיניות הפרטיות כפי שהיא מנוסחת במסמך זה, חל הדין הישראלי ויש לפרש אותה בהתאם. לבית המשפט המוסמך במחוז מרכז יש את הסמכות השיפוטית בכל נושא שנוגע למדיניות הפרטיות.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בכל מקרה בו בית המשפט המוסמך יקבע שהוראה כלשהיא מהוראות מדיניות הפרטיות מנוסחת באופן שאינו חוקי או תקף, או שכולה או חלקה אינה ניתנת לאכיפה, ובהתאם לקביעת בית המשפט המוסמך, אותה הוראה בלבד, או חלקה, בהתאם לעניין, תהיה בטלה, ולא יהיה בכך על מנת להשפיע על שאר הוראות מדיניות הפרטיות שיישארו בתוקף ויחייבו את המשתמשים.</span></p>
<ol style="margin-top:0;margin-bottom:0;" start="13">
    <li dir="rtl" style="list-style-type:decimal;font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;margin-left: -18pt;" aria-level="2">
        <p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">בעלי האפליקציה יכולים ועשויים לשנות, באופן של מחיקה, שינוי, הורדה, הסרה והוספה (להלן: &quot;השינוי&quot;), את מדיניות הפרטיות באפליקציה, מדי פעם ובהתאם לשיקול דעתם הבלעדי.</span></p>
    </li>
</ol>
<p dir="rtl" style="line-height:2.4;text-align: justify;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:David;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">השימוש באפליקציה או במערכותיה כפוף למדיניות הפרטיות החדשה בעקבות השינוי, ולכן יש לקרוא את המדיניות בכל פעם בה מתבצע שימוש באפליקציה.</span></p>
""", unsafe_allow_html=True)


def _terms_of_service_2():
    cols = st.columns((4, 10, 4))
    st.markdown("""<style>
                li{
                    white-space: normal!important;
                }
                span{
                    color: #660066!important;
                }
            </style>""", unsafe_allow_html=True)
    with cols[1]:
        st.markdown(""" <style type="text/css">
    .awlist1 {
        list-style: none;
        counter-reset: awlistcounter69_0
    }

    .awlist1>li:before {
        content: '('counter(awlistcounter69_0) ')';
        counter-increment: awlistcounter69_0
    }

    .awlist2 {
        list-style: none;
        counter-reset: awlistcounter14_0
    }

    .awlist2>li:before {
        content: counter(awlistcounter14_0) '.';
        counter-increment: awlistcounter14_0
    }

    .awlist3 {
        list-style: none;
        counter-reset: awlistcounter14_1
    }

    .awlist3>li:before {
        content: counter(awlistcounter14_0) '.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist4 {
        list-style: none;
        counter-reset: awlistcounter14_1 1
    }

    .awlist4>li:before {
        content: counter(awlistcounter14_0) '.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist5 {
        list-style: none;
        counter-reset: awlistcounter14_1 2
    }

    .awlist5>li:before {
        content: '1.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist6 {
        list-style: none;
        counter-reset: awlistcounter14_1 3
    }

    .awlist6>li:before {
        content: '1.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist7 {
        list-style: none;
        counter-reset: awlistcounter14_0 1
    }

    .awlist7>li:before {
        content: counter(awlistcounter14_0) '.';
        counter-increment: awlistcounter14_0
    }

    .awlist8 {
        list-style: none;
        counter-reset: awlistcounter14_1 1
    }

    .awlist8>li:before {
        content: '2.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist9 {
        list-style: none;
        counter-reset: awlistcounter14_1 2
    }

    .awlist9>li:before {
        content: '2.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist10 {
        list-style: none;
        counter-reset: awlistcounter14_0 2
    }

    .awlist10>li:before {
        content: counter(awlistcounter14_0) '.';
        counter-increment: awlistcounter14_0
    }

    .awlist11 {
        list-style: none;
        counter-reset: awlistcounter14_1 1
    }

    .awlist11>li:before {
        content: '3.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist12 {
        list-style: none;
        counter-reset: awlistcounter14_1 2
    }

    .awlist12>li:before {
        content: '3.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist13 {
        list-style: none;
        counter-reset: awlistcounter14_0 3
    }

    .awlist13>li:before {
        content: counter(awlistcounter14_0) '.';
        counter-increment: awlistcounter14_0
    }

    .awlist14 {
        list-style: none;
        counter-reset: awlistcounter14_1 2
    }

    .awlist14>li:before {
        content: '4.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist15 {
        list-style: none;
        counter-reset: awlistcounter14_0 4
    }

    .awlist15>li:before {
        content: counter(awlistcounter14_0) '.';
        counter-increment: awlistcounter14_0
    }

    .awlist16 {
        list-style: none;
        counter-reset: awlistcounter14_1
    }

    .awlist16>li:before {
        content: '5.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist17 {
        list-style: none;
        counter-reset: awlistcounter40_0
    }

    .awlist17>li:before {
        content: counter(awlistcounter40_0) '.';
        counter-increment: awlistcounter40_0
    }

    .awlist18 {
        list-style: none;
        counter-reset: awlistcounter40_0 1
    }

    .awlist18>li:before {
        content: counter(awlistcounter40_0) '.';
        counter-increment: awlistcounter40_0
    }

    .awlist19 {
        list-style: none;
        counter-reset: awlistcounter40_0 2
    }

    .awlist19>li:before {
        content: counter(awlistcounter40_0) '.';
        counter-increment: awlistcounter40_0
    }

    .awlist20 {
        list-style: none;
        counter-reset: awlistcounter40_0 3
    }

    .awlist20>li:before {
        content: counter(awlistcounter40_0) '.';
        counter-increment: awlistcounter40_0
    }

    .awlist21 {
        list-style: none;
        counter-reset: awlistcounter40_1
    }

    .awlist21>li:before {
        content: counter(awlistcounter40_0) '.'counter(awlistcounter40_1) '.';
        counter-increment: awlistcounter40_1
    }

    .awlist22 {
        list-style: none;
        counter-reset: awlistcounter40_1 1
    }

    .awlist22>li:before {
        content: '4.'counter(awlistcounter40_1) '.';
        counter-increment: awlistcounter40_1
    }

    .awlist23 {
        list-style: none;
        counter-reset: awlistcounter40_1 2
    }

    .awlist23>li:before {
        content: '4.'counter(awlistcounter40_1) '.';
        counter-increment: awlistcounter40_1
    }
</style>
<div dir="rtl">
    <p dir="rtl" style="margin-top:0pt; margin-bottom:8pt; text-align:center; line-height:150%; font-size:12pt;"><br></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">חשוב להקפיד לקרוא היטב את תנאי השימוש לפני השימוש באפליקציה, היות וכל שימוש כפוף למדיניות הפרטיות, תנאי השימוש והוראות הדין הרלוונטי. הגלישה והשימוש באפליקציה פירושם הסכמתכם לאמור בתנאי השימוש ובמסמך מדיניות הפרטיות, ואם קיים תנאי כלשהו במסמכים אלו שנוגדים את הסכמתכם, אתם מתבקשים להימנע מגלישה ושימוש</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">ההקדמה לתנאי השימוש היא חלק בלתי נפרד מהמסמך, ותנאי השימוש הם בבחינת הסכם משפטי מחייב בין כל גולש שמשתמש בשירות לבין בעלי השירות, כלומר, הוא אינו מהווה הסכם שפועל לטובת צד ג&apos; כלשהו</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><strong><span style="font-family:David;">לשון רבים ויחיד.</span></strong><span style="font-family:David; font-weight:bold;" dir="ltr">&nbsp;</span><span style="font-family:David;">בכל מקום שבו תנאי השימוש נכתבים בלשון רבים, הוראות התנאים חלות גם על יחידים, ולהי</span><span style="font-family:David;">פך</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><strong><span style="font-family:David;">לשון זכר ונקבה.</span></strong><span style="font-family:David; font-weight:bold;" dir="ltr">&nbsp;</span><span style="font-family:David;">בכל מקום בתנאי השימוש, בו הנוסח נכתב בלשון זכר, התנאים חלים גם על נשים, והניסוח מופיע בלשון זכר רק מטעמי נוחות</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><strong><span style="font-family:David;">הכותרות הראשיות והמשניות של תנאי השימוש.</span></strong><span style="font-family:David; font-weight:bold;" dir="ltr">&nbsp;</span><span style="font-family:David;">מופיעות לשם ניווט קל בתנאי השימוש, ואינם מהווים פרשנויות</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><strong><span style="font-family:David; letter-spacing:-0.25pt;">שימוש באפליקציה ותנאי המדיניות</span></strong></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בשילוב עם מדיניות הפרטיות של האפליקציה, תנאי השימוש מהווים את הבסיס לגלישה ושימוש באפליקציה. כל שימוש באפליקציה באופן שאינו מצוין במפורש בתנאי שימוש אלה ומופיע בהם, מותנה וכפוף אף להסכמת המשתמשים למדיניות הפרטיות של האפליקציה, בנוסח המלא שלה, כפי שהוא מופיע במדיניות פרטיות של האפליקציה</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:32.29pt; text-align:justify; line-height:normal; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">מסירת מידע ופרטים אישיים<svg height="39.2" id="Icons_Baseball_M" width="39.2" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M73.387 85.453 63.947 57.8 63.947 33.749C63.9498 31.5951 62.2059 29.8468 60.052 29.844 60.0487 29.844 60.0453 29.844 60.042 29.844L48.42 29.844C47.7117 29.8252 47.0138 30.0173 46.415 30.396L39.375 34.622 33.038 28.283 33.706 27.614C35.1536 26.1873 36.7539 24.9243 38.478 23.848 41.1716 22.1188 43.6634 20.0939 45.907 17.811L53.907 9.811 53.981 9.728C55.4278 8.11008 55.2891 5.62561 53.6712 4.17878 53.5808 4.09787 53.4866 4.02119 53.389 3.949 52.7289 3.36175 51.8831 3.02576 51 3 49.9352 2.96802 48.9098 3.40399 48.194 4.193L40.194 12.193C38.0401 14.3727 36.098 16.7521 34.394 19.299 33.2159 21.0841 31.877 22.7578 30.394 24.299L29.451 25.244C29.0061 25.0772 28.5341 24.9944 28.059 25 27.0628 25.0129 26.1155 25.4336 25.438 26.164 24.6778 26.9198 24.2576 27.9522 24.274 29.024 24.2875 29.4255 24.3655 29.8223 24.505 30.199L22.7 32.011C21.9206 32.7918 21.9206 34.0562 22.7 34.837L23.186 35.323 23.186 35.323C23.5605 35.6987 24.0695 35.9093 24.6 35.908L24.6 35.908C25.1308 35.9092 25.6401 35.6978 26.014 35.321L27.56 33.771 36.091 42.3C36.8058 43.0484 37.7971 43.4697 38.832 43.465 39.5404 43.4834 40.2382 43.2909 40.837 42.912L43.786 41.143 43.786 41.143 43.806 41.131 46.548 39.485 46.548 57.9 37.108 85.55C36.2459 88.1199 37.6303 90.902 40.2002 91.7641 40.2121 91.7681 40.224 91.7721 40.236 91.776 40.7253 91.91 41.2289 91.9852 41.736 92 43.8261 92.012 45.6897 90.6858 46.363 88.707L55.285 62.546C55.291 62.531 55.299 62.531 55.304 62.546L64.231 88.717C64.9066 90.6913 66.7683 92.0131 68.855 92 69.3621 91.9853 69.8656 91.9104 70.355 91.777L70.486 91.735C72.9618 90.7373 74.233 87.9846 73.387 85.453ZM36.025 20.453C37.6627 17.9997 39.5316 15.7089 41.606 13.612L49.668 5.543C50.0121 5.17713 50.4982 4.97895 51 5 52.0806 4.97599 52.976 5.83248 53 6.91303 53.0006 6.94202 53.0006 6.97101 53 7 52.9671 7.52349 52.7752 8.02446 52.45 8.436L44.493 16.4C42.3437 18.5921 39.9531 20.5338 37.367 22.188 35.5338 23.3363 33.8317 24.6816 32.291 26.2L31.624 26.869 31.138 26.383 31.806 25.713C33.3714 24.0927 34.7837 22.3312 36.025 20.451ZM24.6 33.91 24.6 33.91 24.114 33.424 25.662 31.873 26.149 32.359ZM69.8 89.853C69.4905 89.9359 69.173 89.9852 68.853 90 67.6169 90.0181 66.5112 89.2343 66.119 88.062L56.242 59.1C56.063 58.5775 55.4943 58.2991 54.9718 58.4782 54.6796 58.5783 54.4501 58.8078 54.35 59.1L44.475 88.052C44.0845 89.2287 42.9767 90.0169 41.737 90 41.4188 89.9857 41.1031 89.9378 40.795 89.857 39.2886 89.3374 38.486 87.6974 39 86.189L48.492 58.389C48.5271 58.2849 48.545 58.1758 48.545 58.066L48.545 38.271 50.161 37.295C50.6338 37.0095 50.7855 36.3948 50.5 35.922 50.2145 35.4492 49.5998 35.2975 49.127 35.583L42.806 39.4 39.77 41.223C39.7407 41.2408 39.7123 41.2602 39.685 41.281 39.4235 41.4212 39.1282 41.486 38.832 41.468 38.3278 41.4707 37.8459 41.2605 37.505 40.889L26.821 30.2C26.4784 29.8856 26.2805 29.4439 26.274 28.979 26.2686 28.437 26.4889 27.9172 26.882 27.544 27.1964 27.2036 27.6367 27.007 28.1 27 28.6259 26.9953 29.1311 27.2042 29.5 27.579L38.507 36.588C38.8316 36.9125 39.3355 36.9744 39.729 36.738L47.477 32.088C47.5065 32.0709 47.5349 32.0518 47.562 32.031 47.8235 31.8908 48.1188 31.826 48.415 31.844L60.042 31.844C61.0706 31.8205 61.9235 32.6354 61.947 33.664 61.9477 33.6927 61.9477 33.7213 61.947 33.75L61.947 57.967C61.9465 58.0769 61.9645 58.186 62 58.29L71.489 86.09C71.9705 87.5917 71.242 89.2147 69.8 89.853Z">&nbsp;<path d="M48.4 21.006C48.4 24.872 51.534 28.006 55.4 28.006 59.266 28.006 62.4 24.872 62.4 21.006 62.4 17.14 59.266 14.006 55.4 14.006 51.534 14.006 48.4 17.14 48.4 21.006ZM55.4 16.006C58.1614 16.006 60.4 18.2446 60.4 21.006 60.4 23.7674 58.1614 26.006 55.4 26.006 52.6386 26.006 50.4 23.7674 50.4 21.006 50.4006 18.2438 52.6378 16.0039 55.4 16Z">&nbsp;</path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">השימוש באפליקציה יהיה כרוך&nbsp;</span><u><span style="font-family:David;">במסירת פרטים אישיים</span></u><span style="font-family:David;">. חשוב להבין שהחוק אינו מחייב את המשתמשים באפליקציה למסור את המידע האישי שלהם או את פרטיהם, ומסירת כל מידע אישי מתבצעת רק בהתאם לרצון חופשי והסכמה אישית</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><u><span style="font-family:David;">מסירת פרטים חלקיים או שאינם נכונים</span></u><span style="font-family:David;">&nbsp;היא התנהלות שעלולה למנוע את האפשרות להשתמש בחלק משירותי האפליקציה או להשלים את תהליך הרישום ובכך לפגוע באפשרות לקבל את השירות המוצע על ידי האפליקציה או לפגוע באיכות השירות הניתן, כמו גם פגיעה באפשרות ליצור קשר עם המשתמשים בהתאם לצורך</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="2" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:32.29pt; text-align:justify; line-height:normal; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">גביית תשלומים<svg height="49.6" id="Icons_Transfer1_LTR_M" width="49.6" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M54.789 35.931 83.883 30.146 85.018 35.931 87.056 35.931 85.456 27.794 44.63 35.911C44.576 35.922 44.576 35.931 44.63 35.931Z">&nbsp;<path d="M74.435 20.877 76.677 26.477 78.677 26.077 75.548 18.255 32.379 35.912C32.353 35.922 32.354 35.931 32.379 35.931L37.614 35.931Z">&nbsp;<path d="M22.821 38.331 22.821 70.331 93.233 70.331 93.233 38.331ZM91.233 68.331 24.821 68.331 24.821 40.331 91.233 40.331Z">&nbsp;<path d="M58.027 61.531C61.209 61.531 63.788 58.307 63.788 54.331 63.788 50.355 61.209 47.131 58.027 47.131 54.845 47.131 52.266 50.355 52.266 54.331 52.266 58.307 54.846 61.531 58.027 61.531ZM58.027 49.131C60.066 49.131 61.788 51.513 61.788 54.331 61.788 57.149 60.066 59.531 58.027 59.531 55.988 59.531 54.266 57.149 54.266 54.331 54.266 51.513 55.989 49.13 58.027 49.13Z">&nbsp;<path d="M37.357 57.668C39.1986 58.0347 40.9888 56.8391 41.3556 54.9975 41.7223 53.1559 40.5267 51.3657 38.6851 50.9989 36.8434 50.6322 35.0532 51.8278 34.6865 53.6694 34.599 54.1087 34.5992 54.5608 34.687 55 34.958 56.3461 36.0107 57.398 37.357 57.668ZM38.024 52.932C38.7972 52.932 39.424 53.5588 39.424 54.332 39.424 55.1052 38.7972 55.732 38.024 55.732 37.2508 55.732 36.624 55.1052 36.624 54.332 36.624 53.5588 37.2508 52.932 38.024 52.932Z">&nbsp;<path d="M77.363 57.668C79.2045 58.0353 80.9951 56.8402 81.3624 54.9987 81.7297 53.1573 80.5346 51.3667 78.6931 50.9994 76.8516 50.632 75.0611 51.8271 74.6937 53.6686 74.6061 54.1081 74.6062 54.5606 74.694 55 74.9649 56.3458 76.0171 57.3976 77.363 57.668ZM78.031 52.932C78.8042 52.932 79.431 53.5588 79.431 54.332 79.431 55.1052 78.8042 55.732 78.031 55.732 77.2578 55.732 76.631 55.1052 76.631 54.332 76.631 53.5588 77.2578 52.932 78.031 52.932Z">&nbsp;<path d="M86.032 65.533 88.432 63.133 88.432 45.533 86.032 43.133 30.823 43.133 27.623 46.333 27.623 62.333 30.823 65.533ZM29.622 47.16 31.651 45.131 85.2 45.131 86.428 46.36 86.428 62.3 85.2 63.533 31.651 63.533 29.622 61.5Z">&nbsp;</path>
                                        </path>
                                    </path>
                                </path>
                            </path>
                        </path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">השימוש באפליקציה&nbsp;</span><u><span style="font-family:David;">ללא תשלום</span></u><span style="font-family:David;">. אולם, האפליקציה שומרת לעצמה את הזכות להציע למשתמש שירותים שונים בתשלום מטעמה או מטעם שותפיה העסקיים.&nbsp;</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">האפליקציה שומרת לעצמה את הזכות לגבות תשלומים עבור שימוש באפליקציה, בתנאי שגביית התשלומים תאושר מראש על ידי המשתמשים ותלווה בהודעה מוקדמת מראש</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="3" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:32.29pt; text-align:justify; line-height:normal; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">שינויים, תוספות ועדכונים בהגדרות תנאי השימוש <svg height="32" id="Icons_SingleGear_M" width="32" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M23.6 61.717 21.1 69.217 26.8 74.917 34.3 72.417C36.2897 73.5299 38.4045 74.4027 40.6 75.017L44.1 82.017 52.1 82.017 55.6 75.017C57.7698 74.4205 59.8537 73.5466 61.8 72.417L69.3 74.917 75 69.217 72.5 61.717C73.6124 59.7271 74.4852 57.6123 75.1 55.417L82.1 51.917 82.1 43.917 75 40.517C74.403 38.3473 73.5291 36.2635 72.4 34.317L74.9 26.817 69.2 21.117 61.7 23.617C59.7103 22.5041 57.5955 21.6313 55.4 21.017L52 14 44 14 40.5 21C38.3302 21.5965 36.2463 22.4704 34.3 23.6L26.8 21.1 21.1 26.8 23.6 34.3C22.4876 36.2899 21.6148 38.4047 21 40.6L14 44 14 52 21 55.5C21.5956 57.6755 22.4695 59.7651 23.6 61.717ZM16 45.264 21.874 42.41 22.691 42.01 22.93 41.134C23.5041 39.0905 24.3174 37.1219 25.353 35.269L25.774 34.503 25.498 33.673 23.388 27.344 27.341 23.39 33.668 25.5 34.523 25.785 35.303 25.333C37.0998 24.29 39.0237 23.4833 41.027 22.933L41.89 22.698 42.29 21.898 45.238 16 50.75 16 53.6 21.88 54 22.696 54.876 22.935C56.9187 23.51 58.8866 24.3236 60.739 25.359L61.506 25.781 62.336 25.504 68.663 23.394 72.616 27.348 70.506 33.677 70.221 34.532 70.673 35.311C71.7165 37.1082 72.5232 39.0329 73.073 41.037L73.314 41.92 74.139 42.315 80.1 45.172 80.1 50.679 74.205 53.627 73.405 54.027 73.17 54.889C72.5957 56.9324 71.7824 58.901 70.747 60.754L70.326 61.52 70.602 62.35 72.712 68.679 68.759 72.633 62.432 70.523 61.577 70.238 60.797 70.69C59 71.7332 57.0757 72.5399 55.072 73.09L54.21 73.325 53.81 74.125 50.862 80.025 45.338 80.025 42.391 74.125 41.991 73.325 41.128 73.09C39.0856 72.515 37.118 71.7014 35.266 70.666L34.499 70.244 33.669 70.521 27.342 72.631 23.389 68.677 25.5 62.35 25.784 61.495 25.333 60.715C24.2892 58.9179 23.4825 56.9933 22.933 54.989L22.697 54.127 21.897 53.727 16 50.779Z">&nbsp;<path d="M48 60.017C54.6274 60.017 60 54.6444 60 48.017 60 41.3896 54.6274 36.017 48 36.017 41.3726 36.017 36 41.3896 36 48.017 36.0209 54.6358 41.3812 59.9961 48 60.017ZM48 38.01C53.5228 38.01 58 42.4872 58 48.01 58 53.5328 53.5228 58.01 48 58.01 42.4772 58.01 38 53.5328 38 48.01 38.0072 42.4901 42.4801 38.0172 48 38.01Z">&nbsp;</path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">מפעיל השירות רשאי&nbsp;</span><u><span style="font-family:David;">לשנות, להסיר, למחוק, להוריד, לעדכן או להוסיף תנאי שימוש</span></u><span style="font-family:David;">&nbsp;למסמך זה, בהתאם לשיקול דעתו הבלעדי, בזמנים שונים ובכפוף להוראות הדין</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">השימוש באפליקציה או במערכות המופיעות בה יהיה כפוף לתנאים החלים לאחר העדכונים, השינויים והתוספות, ולכן&nbsp;</span><u><span style="font-family:David;">על המשתמשים לקרוא היטב את תנאי השימוש לפני השימוש באפליקציה</span></u><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="4" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:32.29pt; text-align:justify; line-height:normal; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">רישום לאפליקציה &nbsp;<svg height="38.4" id="Icons_Clipboard1_LTR_M" width="38.4" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<path d="M45 20C46.933 20 48.5 18.433 48.5 16.5 48.5 14.567 46.933 13 45 13L44.9 13C42.9974 13.034 41.4788 14.5972 41.5 16.5 41.5033 18.4316 43.0684 19.9967 45 20ZM44.934 15 45 15C45.8284 15 46.5 15.6716 46.4999 16.5001 46.4999 17.3285 45.8283 18 44.9999 18 44.1714 18 43.4999 17.3284 43.4999 16.4999 43.4999 16.4953 43.5 16.4906 43.5 16.486 43.4872 15.6803 44.1283 15.0159 44.934 15Z">&nbsp;<path d="M45 52.482 45 52 23 52 23 54 43.485 54 45 52.482Z">&nbsp;<path d="M23 66 39.177 66 39.841 64 23 64 23 66Z">&nbsp;<path d="M57.457 40 23 40 23 42 55.461 42 57.457 40Z">&nbsp;<path d="M83.241 21.689C82.3585 20.7838 80.9093 20.7655 80.0041 21.648 80.0027 21.6493 80.0014 21.6507 80 21.652L79.963 21.689 45.624 56.1 42 67.02 52.97 63.4 87.262 28.982C88.1647 28.1893 88.2542 26.8151 87.462 25.912ZM45.435 63.021 47.2 57.7C48.4518 56.6222 50.3404 56.7632 51.4182 58.0151 52.3362 59.0814 52.387 60.6434 51.54 61.767L46.004 63.594ZM52.685 56.433C51.8425 55.5969 50.728 55.0909 49.544 55.007L76.044 28.452 80.513 32.922 54.1 59.435C53.9868 58.3016 53.4872 57.2416 52.685 56.433ZM85.94 27.481 85.891 27.524 85.845 27.571 81.925 31.505 77.456 27.037 81.4 23.082C81.4532 23.0293 81.5251 22.9998 81.6 23 81.6848 23.0005 81.7655 23.0368 81.822 23.1L85.969 27.253C86.0171 27.3257 86.0048 27.4227 85.94 27.481Z">&nbsp;<path d="M75 45.541 73 47.548 73 84C73 85.1046 72.1046 86 71 86L19 86C17.8954 86 17 85.1046 17 84L17 18.979C17 17.8744 17.8954 16.979 19 16.979L30 16.979 30 27 60 27 60 16.979 71 16.979C72.1046 16.979 73 17.8744 73 18.979L73 24.428 75 22.428 75 18.979C75 16.7699 73.2091 14.979 71 14.979L56 14.979 56 12.979C55.9961 10.2192 53.7598 7.98286 51 7.979L39 7.979C36.2399 7.98231 34.0033 10.2189 34 12.979L34 14.979 19 14.979C16.792 14.9818 15.0028 16.771 15 18.979L15 84C15 86.2091 16.7909 88 19 88L71 88C73.2091 88 75 86.2091 75 84ZM32 16.979 36 16.979 36 12.979C36 11.3221 37.3431 9.979 39 9.979L51 9.979C52.6569 9.979 54 11.3221 54 12.979L54 16.979 58 16.979 58 25 32 25Z">&nbsp;</path>
                                </path>
                            </path>
                        </path>
                    </path>
                </path></svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">כדי להירשם לשימוש באפליקציה, יש לסמן את תיבות הסימון המתאימות ולהקליק על הכפתור לאישור. מילוי הפרטים האישיים וסימון התיבות הרלוונטיות בתהליך הבקשה, עם לחיצה על כפתור האישור בסיום, פירושה אישור המשתמשים שקראו את תנאי השימוש, הוראות תהליך ההרשמה ואת מסמך מדיניות הפרטיות, ושהם מסכימים לתנאים לאחר שקראו והבינו את כל האמור בהם</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">המשתמשים באפליקציה מצהירים שהם מודעים לכך שאחריותם היא לספק את כל המידע הנדרש כדי לקבל את המוצרים.&nbsp;</span></p>
    <ol start="5" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:32.29pt; text-align:justify; line-height:normal; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">שימוש פוגעני בתכני האפליקציה <svg height="34.4" id="Icons_NoPhones_M" width="34.4" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M53 11C53.5523 11 54 10.5523 54 10 54 9.44771 53.5523 9 53 9L44 9C43.4477 9 43 9.44771 43 10 43 10.5523 43.4477 11 44 11Z">&nbsp;<path d="M87.707 10.707 86.293 9.293 8.293 87.293 9.707 88.707 23 75.414 23 90.025C23.0038 91.128 23.897 92.0212 25 92.025L71 92.025C72.1027 92.0206 72.9956 91.1277 73 90.025L73 25.411ZM30 68.413 66 32.413 66 80.022 30 80.022ZM71 90.026 25 90.026 25 73.414 28 70.414 28 82.022 68 82.022 68 30.411 71 27.411Z">&nbsp;<path d="M25 6 71 6 71 18.969 73 16.969 73 6C72.9962 4.89703 72.103 4.00384 71 4L25 4C23.8968 4.00329 23.0033 4.8968 23 6L23 66.97 25 64.97Z">&nbsp;<path d="M68.003 21.969 68.003 16.005 68.003 14.005 66.003 14.005 30.001 14.005 28.001 14.005 28.001 16.005 28.001 61.971 30.001 59.971 30.001 16.005 66.003 16.005 66.003 23.969 68.003 21.969Z">&nbsp;</path>
                            </path>
                        </path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">חל&nbsp;</span><u><span style="font-family:David;">איסור על העלאת מידע או תכנים</span></u><span style="font-family:David;">&nbsp;שיש בהם את המאפיינים הבאים</span><span style="font-family:David;" dir="ltr">:</span></p>
    <ul type="disc" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:14pt; margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">שיבוש, הפרעה, הגבלה או מניעת השימוש באפליקציה הן לבעלי האפליקציה או למשתמשים אחרים</span><span style="font-family:David; font-size:12pt;" dir="ltr">;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">מידע מעליב</span><span style="font-family:David; font-size:12pt;" dir="ltr">;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">מידע פוגעני או שעלול להוות חומר פוגעני</span><span style="font-family:David; font-size:12pt;" dir="ltr">;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">מידע משמיץ או וולגרי</span><span style="font-family:David; font-size:12pt;" dir="ltr">;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">מידע שיש בו הוצאת דיבה</span><span style="font-family:David; font-size:12pt;" dir="ltr">;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">רישום צדדים שלישיים או פתיחת סיסמאות וחשבונות בשמם ועבורם</span><span style="font-family:David; font-size:12pt;" dir="ltr">;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">העלאה או פרסום מידע או תכנים שקריים, שאינם מדויקים; מטעים או מסולפים</span><span style="font-family:David; font-size:12pt;" dir="ltr">;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">מידע שיש בו איומים</span><span style="font-family:David; font-size:12pt;" dir="ltr">;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">מידע פורנוגרפי</span><span style="font-family:David; font-size:12pt;" dir="ltr">;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; margin-bottom:14pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">או כל מידע אסור לשימוש או לפרסום</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
    </ul>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">חל&nbsp;</span><u><span style="font-family:David;">איסור על העלאת מידע או תכנים שיש בהם בבחינת נזק</span></u><span style="font-family:David;">&nbsp;לאפליקציה, למשתמשים בו, כמו למשל שורות קוד; תוכנות מזיקות; &apos;סוס טרויאני&apos;; החדרת וירוסים שונים; או כל תוכנה אחרת שיש בה על מנת לפגוע בהתנהלות התקינה של האפליקציה והשימוש בו, או ההתנהלות והשימוש באפליקציה למשתמשים אחרים, כמו גם נזק למשתמשים ולאפליקציה, או למחשבים ולציוד</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">חל&nbsp;</span><u><span style="font-family:David;">איסור גם על עזרה או שידול</span></u><span style="font-family:David;">&nbsp;לאחרים שמבקשים להתנהל או לבצע פעולה אסורה באפליקציה, מכל סוג שהוא, כולל הפעילויות האסורות המפורטות בתנאי השימוש</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">תכנים לעיל&nbsp;</span><u><span style="font-family:David;">יוסרו מהאפליקציה</span></u><span style="font-family:David;">&nbsp;ואף יש בהם כדי להביא להסרת חשבון המשתמש והפסקת ההתקשרות עימו.&nbsp;</span></p>
    <ol start="6" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:32.29pt; text-align:justify; line-height:normal; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">מניעת השימוש באפליקציה <svg height="38.4" id="Icons_NoSign_M" width="38.4" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M48 10C27.0071 9.99393 9.98408 27.0071 9.978 48 9.97193 68.9929 26.9851 86.0159 47.978 86.022 68.9709 86.0281 85.9939 69.0149 86 48.022 86 48.0183 86 48.0147 86 48.011 86.0116 27.0297 69.0123 10.0116 48.031 10 48.0207 10 48.0103 9.99999 48 10ZM48 84.021C28.1266 84.0321 12.007 67.9305 11.996 48.057 11.9908 38.8387 15.5238 29.9699 21.866 23.28L72.729 74.143C66.0597 80.4881 57.2054 84.025 48 84.021ZM74.143 72.729 23.28 21.866C37.7093 8.20441 60.4814 8.82674 74.143 23.256 87.2797 37.1308 87.2797 58.8542 74.143 72.729Z">&nbsp;</path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">מבלי לגרוע מהאמור בסעיפי תנאי השימוש, החברה יכולה&nbsp;</span><u><span style="font-family:David;">למנוע שימוש באפליקציה</span></u><span style="font-family:David;">&nbsp;למשתמשים רשומים או שאינם רשומים, או לכלל הציבור, בכל אחד מהמקרים הבאים</span><span style="font-family:David;" dir="ltr">:</span></p>
    <ul type="disc" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:14pt; margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">תנאי השימוש באפליקציה הופרו</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">בוצע מחדל או פעילות שיש בהם פגיעה באפליקציה, בבעלי האפליקציה, במידע שמצוי בידי החברה; בציוד החברה; או במשתמשים אחרים.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">המשתמשים מסרו פרטים חסרים, שגויים או שקריים</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
    </ul>
    <ol start="7" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:32.29pt; text-align:justify; line-height:normal; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold; background-color:#ffffff;">הסרת תכני המשתמש וסיום התקשרות<svg height="34.4" id="Icons_NoPhones_M" width="34.4" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M53 11C53.5523 11 54 10.5523 54 10 54 9.44771 53.5523 9 53 9L44 9C43.4477 9 43 9.44771 43 10 43 10.5523 43.4477 11 44 11Z">&nbsp;<path d="M87.707 10.707 86.293 9.293 8.293 87.293 9.707 88.707 23 75.414 23 90.025C23.0038 91.128 23.897 92.0212 25 92.025L71 92.025C72.1027 92.0206 72.9956 91.1277 73 90.025L73 25.411ZM30 68.413 66 32.413 66 80.022 30 80.022ZM71 90.026 25 90.026 25 73.414 28 70.414 28 82.022 68 82.022 68 30.411 71 27.411Z">&nbsp;<path d="M25 6 71 6 71 18.969 73 16.969 73 6C72.9962 4.89703 72.103 4.00384 71 4L25 4C23.8968 4.00329 23.0033 4.8968 23 6L23 66.97 25 64.97Z">&nbsp;<path d="M68.003 21.969 68.003 16.005 68.003 14.005 66.003 14.005 30.001 14.005 28.001 14.005 28.001 16.005 28.001 61.971 30.001 59.971 30.001 16.005 66.003 16.005 66.003 23.969 68.003 21.969Z">&nbsp;</path>
                            </path>
                        </path>
                    </path>
                </g>&nbsp;</svg><svg height="38.4" id="Icons_NoSign_M" width="38.4" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M48 10C27.0071 9.99393 9.98408 27.0071 9.978 48 9.97193 68.9929 26.9851 86.0159 47.978 86.022 68.9709 86.0281 85.9939 69.0149 86 48.022 86 48.0183 86 48.0147 86 48.011 86.0116 27.0297 69.0123 10.0116 48.031 10 48.0207 10 48.0103 9.99999 48 10ZM48 84.021C28.1266 84.0321 12.007 67.9305 11.996 48.057 11.9908 38.8387 15.5238 29.9699 21.866 23.28L72.729 74.143C66.0597 80.4881 57.2054 84.025 48 84.021ZM74.143 72.729 23.28 21.866C37.7093 8.20441 60.4814 8.82674 74.143 23.256 87.2797 37.1308 87.2797 58.8542 74.143 72.729Z">&nbsp;</path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">האפליקציה שומרת לעצמה את הזכות&nbsp;</span><u><span style="font-family:David;">להסיר תוכן</span></u><span style="font-family:David;">&nbsp;שהמשתמשים הזינו במסגרת הרישום לאפליקציה ואף&nbsp;</span><u><span style="font-family:David;">להפסיק את ההתקשרות</span></u><span style="font-family:David;">&nbsp;עם המשתמש במיידי וללא כל פירוט מצידה.</span></p>
    <ol start="8" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:32.29pt; text-align:justify; line-height:normal; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">הפסקת פעילות האפליקציה<svg height="40" id="Icons_RaisedHand_M" width="40" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M25.445 76.939C26.484 78.4389 27.042 80.2194 27.045 82.044L27.054 88 29.054 88 29.046 82.04C29.0437 79.8069 28.3595 77.6277 27.085 75.794L25.491 73.494C23.2848 70.3151 22.1017 66.5385 22.1 62.669L22.1 28.192C22.0575 26.0969 23.5965 24.3046 25.674 24.03 27.8553 23.8135 29.7991 25.4063 30.0156 27.5876 30.0285 27.7173 30.0349 27.8476 30.035 27.978 30.0385 28.1415 30.0832 28.3014 30.165 28.443L30.165 47C30.165 47.5523 30.6127 48 31.165 48 31.7173 48 32.165 47.5523 32.165 47L32.165 18.145C32.1294 16.0604 33.6679 14.2828 35.736 14.019 37.9196 13.8031 39.8648 15.3981 40.0807 17.5817 40.0934 17.7098 40.0998 17.8383 40.1 17.967L40.1 47C40.1 47.5523 40.5477 48 41.1 48 41.6523 48 42.1 47.5523 42.1 47L42.1 12.146C42.0648 10.061 43.6035 8.28325 45.672 8.019 47.8561 7.8025 49.8021 9.39754 50.0186 11.5816 50.0314 11.7104 50.0378 11.8396 50.038 11.969L50.038 47C50.038 47.5523 50.4857 48 51.038 48 51.5903 48 52.038 47.5523 52.038 47L52.038 18.272C52.0781 18.168 52.0988 18.0575 52.099 17.946 51.9754 16.8104 52.4304 15.6887 53.31 14.96 56.529 12.63 60.035 14.897 60.035 17.967L60.035 57C60.0367 57.5523 60.4858 57.9986 61.038 57.997 61.494 57.9956 61.8913 57.6859 62.004 57.244L66.509 39.312C66.9272 37.2578 68.8208 35.8449 70.909 36.029 72.0249 36.1607 73.0314 36.7629 73.675 37.684 74.3177 38.5987 74.546 39.7416 74.304 40.833L68.283 67.67C68.0961 68.5032 67.623 69.2446 66.946 69.765L55.427 78.615C55.1812 78.8042 55.0371 79.0968 55.037 79.407L55.037 88 57.037 88 57.037 79.9 68.165 71.35C69.2125 70.5449 69.9446 69.3981 70.234 68.109L76.255 41.27C76.9737 38.0527 74.9481 34.862 71.7308 34.1433 71.5406 34.1008 71.3484 34.0677 71.155 34.044 68.0551 33.7354 65.2179 35.8042 64.564 38.85L62.055 48.836C62.045 48.879 62.036 48.878 62.036 48.836L62.036 18.22C62.049 14.8744 59.4054 12.1219 56.062 12 54.5715 12.0029 53.1365 12.5662 52.042 13.578L52.042 12.178C52.0856 9.12819 49.873 6.51353 46.858 6.052 43.5866 5.61956 40.584 7.92103 40.1515 11.1925 40.1175 11.4499 40.1003 11.7093 40.1 11.969L40.1 13.522C39.0021 12.5353 37.5761 11.9927 36.1 12 32.779 12.152 30.1668 14.8925 30.174 18.217L30.174 23.646C30.145 23.619 30.119 23.588 30.09 23.562 28.8383 22.4313 27.1691 21.8787 25.49 22.039 22.3875 22.4161 20.0654 25.0669 20.1 28.192L20.1 62.669C20.1 66.9465 21.4062 71.1221 23.844 74.637Z">&nbsp;</path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">לנותן השירות יש את הזכות להפסיק חלק מפעילות האפליקציה או את כל הפעילות לפרק זמן קצר, זמני, ארוך או לתמיד, כולל הפסקת מתן שירותים, באופן חלקי או מלא, כמו גם הגבלת או הפחתת מתן השירותים, ללא הודעה מוקדמת מראש</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="9" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:32.29pt; text-align:justify; line-height:normal; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">הגבלת אחריות<span style="font-family:Arial; font-size:11pt; font-weight:normal; letter-spacing:normal;" dir="ltr">&nbsp;</span><img src="data:image/jpeg;base64,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" width="51" height="40" alt="הגבלת אחריות בהסכם שמירה וביטוח רכוש"></li>
    </ol>
    <ul type="circle" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:30.2pt; text-align:justify; line-height:normal; padding-right:5.8pt; font-family:serif; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בעלי האפליקציה&nbsp;</span><u><span style="font-family:David;">אינם אחראים</span></u><span style="font-family:David;">&nbsp;לנזקים ישירים או עקיפים מכל סוג שהוא, שייגרמו למשתמשים או למי מטעמם, בכל מקרה בו מידע אישי כלשהו יאבד או יגיע לגורמים עוינים, או שיתבצע בו שימוש כלשהו שאינו בהרשאה</span><span style="font-family:David;" dir="ltr">.</span></li>
    </ul>
    <p dir="rtl" style="margin-top:0pt; margin-right:36pt; margin-bottom:0pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">&nbsp;</span></p>
    <ul type="circle" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:30.2pt; text-align:justify; line-height:normal; padding-right:5.8pt; font-family:serif; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בכל מקום בתנאי השימוש בו משתמע או נכתב במפורש שנותן השירות יחליט על ענין כלשהו, יבצע פעולה מסוימת או יקבע דבר מסוים, לנותן השירות מוקנית באופן מפורש או מכללא הסמכות, הזכות או שיקול הדעת הבלעדי לפעול, לבצע, או להחליט לא לפעול, בהתאם לשיקול דעתו הבלעדי מבלי שתחול עליו חובת הנמקה</span><span style="font-family:David;" dir="ltr">.</span></li>
    </ul>
    <p dir="rtl" style="margin-top:0pt; margin-right:36pt; margin-bottom:0pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">התנהלות נותן השירות לא תהיה ניתנת לערעור ותיחשב לסופית, באופן שלמשתמשים לא תהיה אפשרות לטעון נגד השירות, לתבוע אותו, או להביע דרישה הנוגעת לפעילותו או הימנעות מפעילות, כפי שנאמר</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:0pt; margin-right:36pt; margin-bottom:0pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;" dir="ltr">&nbsp;</span></p>
    <ul type="circle" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:30.2pt; text-align:justify; line-height:normal; padding-right:5.8pt; font-family:serif; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">המשתמשים באפליקציה מצהירים שלבעלי האפליקציה יש&nbsp;</span><u><span style="font-family:David;">זכות והרשאה להשתמש במידע</span></u><span style="font-family:David;">, כפי שמונח זה מוגדר במדיניות הפרטיות, בהתאם למדיניות הפרטיות</span><span style="font-family:David;" dir="ltr">.</span><span style="font-family:David;">&nbsp;נותן השירות&nbsp;</span><span style="font-family:David;">אינו אחראי לכל נזק מכל סוג שהוא, שנגרמו כתוצאה ממקרים שנובעים מהעברת הפרטים לספק, או כתוצאה ממקרים שאינם בשליטתו, או כתוצאה מאובדן המידע, או כתוצאה ממקרים שמוגדרים בבחינת כוח עליון</span><span style="font-family:David;" dir="ltr">.</span></li>
    </ul>
    <p dir="rtl" style="margin-top:0pt; margin-right:36pt; margin-bottom:0pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;" dir="ltr">&nbsp;</span></p>
    <ul type="circle" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:30.2pt; text-align:justify; line-height:normal; padding-right:5.8pt; font-family:serif; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">למרות שבעלי האפליקציה נוקטים בכל המאמצים לפרסום תכנים ומידע נכונים, אמינים ומדויקים, עדיין&nbsp;</span><u><span style="font-family:David;">עשויים להופיע אי דיוקים או להתפרסם שגיאות בתכנים</span></u><span style="font-family:David;">, כולל שיבוש במידע. בעלי האפליקציה אינם אחראים לשום נזק, משום סוג, שייגרם למשתמשים כתוצאה מפרסום התכנים והמידע</span><span style="font-family:David;" dir="ltr">.</span></li>
    </ul>
    <p dir="rtl" style="margin-top:0pt; margin-right:36pt; margin-bottom:0pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בכל מקרה בו המשתמשים אינם מרוצים מהאפליקציה, האפשרות הבלעדית והיחידה שעומדת לרשותם היא&nbsp;</span><u><span style="font-family:David;">הפסקת השימוש באפליקציה</span></u><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="10" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:36pt; text-align:justify; line-height:normal; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">שינויים ושדרוגים באפליקציה<svg height="29.6" id="Icons_RollerPaintTool_M" width="29.6" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M89.317 44.866 51.133 6.683C49.571 5.12147 47.039 5.12147 45.477 6.683L42.648 9.511 41.235 8.1C39.2808 6.15128 36.1182 6.15128 34.164 8.1L25.415 16.849C24.0055 18.258 23.5674 20.3695 24.3 22.223L37.213 54.813C37.6535 55.9253 37.391 57.1931 36.545 58.039L32.039 62.545 30.627 61.13C29.4555 59.9589 27.5565 59.9589 26.385 61.13L5.879 81.636C4.70733 82.8075 4.70717 84.707 5.87864 85.8786 5.87876 85.8788 5.87888 85.8789 5.879 85.879L10.121 90.121C11.2925 91.2927 13.192 91.2928 14.3636 90.1214 14.3638 90.1212 14.3639 90.1211 14.364 90.121L34.87 69.615C36.0411 68.4435 36.0411 66.5445 34.87 65.373L33.456 63.959 37.962 59.453C39.372 58.043 39.8094 55.9299 39.075 54.076L26.162 21.487C25.7208 20.3746 25.9829 19.1063 26.829 18.26L35.578 9.511C36.7495 8.33933 38.649 8.33917 39.8206 9.51064 39.8208 9.51076 39.8209 9.51088 39.821 9.511L41.234 10.925 38.406 13.754C36.8439 15.3161 36.8438 17.8487 38.4059 19.4109 38.4059 19.4109 38.4059 19.411 38.406 19.411L76.589 57.594C78.1511 59.1561 80.6837 59.1562 82.2458 57.5941 82.2459 57.5941 82.2459 57.5941 82.246 57.594L89.317 50.523C90.8791 48.9609 90.8792 46.4283 89.3171 44.8661 89.3171 44.8661 89.317 44.8661 89.317 44.866ZM33.456 68.2 12.95 88.707C12.5597 89.0977 11.9265 89.0981 11.5358 88.7078 11.5355 88.7075 11.5353 88.7073 11.535 88.707L7.293 84.464C6.90262 84.0735 6.90262 83.4405 7.293 83.05L27.8 62.544C28.1905 62.1536 28.8235 62.1536 29.214 62.544L33.457 66.787C33.8474 67.1775 33.8474 67.8105 33.457 68.201ZM87.9 49.109 80.832 56.18C80.051 56.9608 78.785 56.9608 78.004 56.18L39.82 18C39.0392 17.219 39.0392 15.953 39.82 15.172L46.891 8.1C47.672 7.31924 48.938 7.31924 49.719 8.1L87.9 46.281C88.6808 47.062 88.6808 48.328 87.9 49.109Z">&nbsp;</path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">לבעלי האפליקציה יש את הזכות, בהתאם לשיקול דעתם הבלעדי, לבצע פעולות שדרוג, ריענון או תחזוקה לאפליקציה, כולל שינויי עיצוב או כל התנהלות אחרת שעשויה למנוע מהמשתמשים את הגישה לאפליקציה</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="11" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:36pt; text-align:justify; line-height:normal; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">קישורים באפליקציה ומידע שמגיע מצדדים שלישיים<svg height="24.8" id="Icons_Link_M" width="24.8" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<path d="M42.565 48.215C37.9544 50.4224 32.4534 49.4867 28.832 45.879L21.137 38.184C16.4258 33.4765 16.4228 25.8412 21.1302 21.13 25.8377 16.4188 33.473 16.4158 38.1842 21.1232 38.1865 21.1255 38.1887 21.1277 38.191 21.13L45.891 28.83C49.4992 32.4511 50.435 37.9525 48.227 42.563L49.718 44.054C52.6786 38.5816 51.6955 31.8147 47.3 27.411L39.6 19.716C34.0327 14.3036 25.132 14.4291 19.7195 19.9964 14.4134 25.4543 14.415 34.1439 19.723 39.6L27.423 47.3C31.8256 51.6942 38.5914 52.6754 44.061 49.713Z">&nbsp;<path d="M76.291 56.4 68.6 48.707C64.1955 44.3165 57.4323 43.3356 51.962 46.294L53.452 47.785C58.0616 45.5681 63.5686 46.5048 67.186 50.121L74.88 57.821C79.6504 62.4684 79.7502 70.1031 75.1028 74.8735 70.4553 79.644 62.8207 79.7437 58.0502 75.0963 57.9738 75.0219 57.8984 74.9464 57.824 74.87L50.124 67.17C46.5158 63.5489 45.58 58.0475 47.788 53.437L46.3 51.951C43.3404 57.4209 44.3209 64.1847 48.712 68.589L56.412 76.289C61.9042 81.7784 70.8066 81.7762 76.296 76.284 81.7854 70.7918 81.7832 61.8894 76.291 56.4Z">&nbsp;<path d="M58.614 59.607C58.3488 59.6069 58.0945 59.5015 57.907 59.314L36.694 38.1C36.2967 37.7163 36.2857 37.0833 36.6694 36.686 37.0531 36.2887 37.6862 36.2777 38.0834 36.6614 38.0918 36.6695 38.1 36.6777 38.108 36.686L59.321 57.9C59.7115 58.2906 59.7114 58.9237 59.3208 59.3142 59.1333 59.5016 58.8791 59.6069 58.614 59.607Z">&nbsp;</path>
                    </path>
                </path></svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">באפליקציה מופיעים קישורים שמפנים לאפליקציות חיצוניות, וחלק מהמידע המפורסם באפליקציה מבוסס&nbsp;</span><u><span style="font-family:David;">על מידע שמגיע מצדדים שלישיים</span></u><span style="font-family:David;">, כמו למשל ממוסדות אקדמיים</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בעלי האפליקציה&nbsp;</span><u><span style="font-family:David;">אינם ערבים</span></u><span style="font-family:David;">&nbsp;לכם שהמידע שנמצא אצל צדדים שלישיים הוא מדויק ואמין, והמשתמשים מצהירים שהם מודעים לעובדה זו ומבינים את השלכותיה. בעלי האפליקציה&nbsp;</span><u><span style="font-family:David;">לא יימצאו אחראים</span></u><span style="font-family:David;">&nbsp;לכל נזק מכל סוג שהוא שייגרם למשתמשים כתוצאה מהסתמכות על המידע המופיע באפליקציה</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="12" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:36pt; text-align:justify; line-height:normal; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">משלוח הודעות<svg height="31.2" id="Icons_Email_M" width="31.2" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M73 25.776 73 16 61.493 16 48 4.7 34.507 16 23 16 23 25.776 10 36.529 10 90 86 90 86 36.529ZM73 28.376 83.516 37.076 73 47.586ZM48 7.305 58.378 16 37.622 16ZM25 18 71 18 71 49.586 58.948 61.638C52.6188 56.3138 43.3772 56.3138 37.048 61.638L25 49.586ZM23 28.372 23 47.586 12.484 37.07ZM12.017 39.431 35.586 63 12.017 86.569C12.0131 86.5729 12.0067 86.5728 12.0029 86.5689 12.0011 86.567 12 86.5646 12 86.562L12 39.438C12.0001 39.4325 12.0046 39.4281 12.0101 39.4281 12.0127 39.4282 12.0152 39.4292 12.017 39.431ZM13.438 88C13.4325 87.9999 13.4281 87.9954 13.4281 87.9899 13.4282 87.9873 13.4292 87.9848 13.431 87.983L37.394 64.021C43.2551 58.1722 52.7449 58.1722 58.606 64.021L82.569 87.983C82.5729 87.9869 82.5728 87.9933 82.5689 87.9971 82.567 87.9989 82.5646 88 82.562 88ZM83.983 86.569 60.414 63 83.983 39.431C83.9869 39.4271 83.9933 39.4272 83.9971 39.4311 83.9989 39.433 84 39.4354 84 39.438L84 86.562C83.9999 86.5675 83.9954 86.5719 83.9899 86.5719 83.9873 86.5718 83.9848 86.5708 83.983 86.569Z">&nbsp;<path d="M45.733 50.807C46.4836 50.935 47.2436 50.9995 48.005 51 50.0569 51.0021 52.0797 50.5142 53.905 49.577 54.4148 49.3646 54.6559 48.7791 54.4435 48.2693 54.2311 47.7595 53.6457 47.5184 53.1359 47.7308 53.0889 47.7504 53.0435 47.7735 53 47.8 47.5887 50.5614 40.9635 48.4132 38.2021 43.0019 35.4407 37.5906 37.5889 30.9654 43.0002 28.204 44.7767 27.2974 46.7663 26.8909 48.756 27.028 54.6117 27.5358 59.0817 32.4789 59 38.356L59 41C59 41.5523 58.5523 42 58 42L57.363 42C55.5062 41.9978 54.0017 40.4928 54 38.636L54 38C54.0117 34.6747 51.3254 31.9696 48.0001 31.9579 44.6749 31.9463 41.9697 34.6325 41.9581 37.9578 41.9464 41.2831 44.6327 43.9882 47.9579 43.9999 49.8944 44.0066 51.716 43.0816 52.853 41.514 53.8328 43.0589 55.5336 43.9964 57.363 44L58 44C59.6569 44 61 42.6569 61 41L61 38.356C61.0809 31.4251 55.7941 25.609 48.887 25.03 41.7265 24.5056 35.4966 29.8852 34.9722 37.0458 34.4835 43.7185 39.1393 49.6724 45.733 50.807ZM48 42C45.7909 42 44 40.2091 44 38 44 35.7909 45.7909 34 48 34 50.2091 34 52 35.7909 52 38 52 40.2091 50.2091 42 48 42Z">&nbsp;</path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בעלי האפליקציה יכולים לשלוח הודעות לכתובת הדואר האלקטרוני או לכתובת הדואר שהמשתמשים מסרו במהלך הרישום לאפליקציה</span><span style="font-family:David;" dir="ltr">&nbsp;</span><span style="font-family:David;">והמשתמשים יכולים ליצור קשר עם בעלי האפליקציה בעמוד יצירת הקשר</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">כל הודעה שיש לשלוח מצד אחד שני, למעט אם צוין אחרת בתנאי השימוש, תתבצע באמצעות דואר האלקטרוני</span><span style="font-family:David;" dir="ltr">.</span><span style="font-family:David;">&nbsp;</span><span style="font-family:David;">אם ההודעה נשלחה לבעלי האפליקציה, היא תיחשב שנתקבלה רק אם בוצע אישור מסירה על קבלת ההודעה</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="13" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:36pt; text-align:justify; line-height:normal; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">התניית שיפוט <svg height="40.8" id="Icons_Gavel_M" width="40.8" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M68.083 32.749C69.2545 33.9207 71.154 33.9208 72.3256 32.7494 72.3258 32.7492 72.3259 32.7491 72.326 32.749L76.569 28.506 56.063 8 51.82 12.243C50.6489 13.4145 50.6489 15.3135 51.82 16.485L28.485 39.82C27.3135 38.6489 25.4145 38.6489 24.243 39.82L20 44.063 40.506 64.569 44.749 60.326C45.9207 59.1545 45.9208 57.255 44.7494 56.0834 44.7492 56.0832 44.7491 56.0831 44.749 56.083L53.588 47.245 80.528 74.185C82.0509 75.7082 84.5202 75.7085 86.0434 74.1856 86.0436 74.1854 86.0438 74.1852 86.044 74.185L86.185 74.044C87.7082 72.5211 87.7085 70.0518 86.1856 68.5286 86.1854 68.5284 86.1852 68.5282 86.185 68.528L59.244 41.588ZM53.234 13.657 56.063 10.828 73.74 28.506 70.912 31.334C70.5217 31.7247 69.8885 31.7251 69.4978 31.3348 69.4975 31.3345 69.4973 31.3343 69.497 31.334L68.083 29.92 68.083 29.92 53.941 15.778 53.941 15.778 53.234 15.071C52.8436 14.6805 52.8436 14.0475 53.234 13.657ZM43.334 58.912 40.506 61.74 22.828 44.063 25.657 41.234C26.0475 40.8436 26.6805 40.8436 27.071 41.234L28.485 42.648 28.485 42.648 41.921 56.083 41.921 56.083 43.335 57.5C43.724 57.8903 43.724 58.5217 43.335 58.912ZM43.334 54.669 29.9 41.234 53.234 17.9 53.234 17.9 66.669 31.334ZM84.771 69.943C85.5133 70.6847 85.5137 71.8877 84.772 72.63 84.7717 72.6303 84.7713 72.6307 84.771 72.631L84.631 72.771C83.889 73.513 82.686 73.513 81.944 72.771L55 45.83 57.83 43Z">&nbsp;<path d="M11.9 88 44.1 88C46.2528 87.9972 47.9972 86.2528 48 84.1L48 83.9C47.9972 81.7472 46.2528 80.0028 44.1 80L42 80 42 75 14 75 14 80 11.9 80C9.74723 80.0028 8.00275 81.7472 8 83.9L8 84.1C8.00275 86.2528 9.74723 87.9972 11.9 88ZM16 77 40 77 40 80 16 80ZM10 83.9C10 82.8507 10.8507 82 11.9 82L44.1 82C45.1493 82 46 82.8507 46 83.9L46 84.1C46 85.1493 45.1493 86 44.1 86L11.9 86C10.8507 86 10 85.1493 10 84.1Z">&nbsp;</path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">הדין שחל על אפליקציה</span><span style="font-family:David;" dir="ltr">&nbsp;</span><span style="font-family:David;">או על כל נושא ועניין שקשורים אליו, כולל תנאי שימוש אלה, וכל מקרה של סכסוך משפטי ישיר או עקיף לאפליקציה או לשימוש בו, הוא&nbsp;</span><u><span style="font-family:David;">הדין הישראלי בלבד</span></u><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">הסמכות הבלעדית והייחודית לדון בכל סכסוך או מחלוקת משפטית, שקשורים באופן ישיר או עקיף לאפליקציה או לשימוש בו, היא הסמכות של בית המשפט המוסמך&nbsp;</span><u><span style="font-family:David;">במחוז מרכז</span></u><span style="font-family:David;">, ולא לכל ערכאה שיפוטית אחרת</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="ltr" style="margin-top:0pt; margin-bottom:8pt; text-align:left; line-height:108%; font-size:12pt;"><br style="page-break-before:always; clear:both;"></p>
    <p dir="rtl" style="margin-top:12pt; margin-bottom:0pt; text-align:center; page-break-inside:avoid; page-break-after:avoid; line-height:108%; font-size:16pt;"><strong><u><span style="font-family:'Times New Roman';">מדיניות הפרטיות</span></u></strong></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">יש לקרוא היטב את המסמך, שמתאר את מדיניות הפרטיות באפליקציה, שמהווה חלק בלתי נפרד ממסמך תנאי השימוש</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">מדיניות הפרטיות, כפי שהיא מופיעה במסמך זה חלה על כל שימוש, גלישה או צפייה באפליקציה, בכל ומכל אמצעי תקשורת. בכל מקרה בו המשתמשים אינם מסכימים לתנאי מתנאי מדיניות הפרטיות, עליהם להפסיק מידית את השימוש או הגלישה באפליקציה</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">אופן הניסוח במדיניות הפרטיות מנוסח בלשון זכר רק מטעמי נוחות, אך הוא מופנה כלפי גברים ונשים. כמו כן, בכל מקום במסמך בו הניסוח נכתב בלשון יחיד, הוא מופנה גם כלפי רבים, ולהיפך</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:14.29pt; text-align:justify; line-height:normal; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt; background-color:#ffffff;">מסירת פרטים אישיים <svg height="36" id="Icons_AddressBook_RTL_M" width="36" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M17 15 17 80.963C17.0077 83.7286 19.2534 85.9658 22.019 85.963L79 85.963 79 10 22.019 10C19.2533 9.99723 17.0077 12.2344 17 15ZM77 83.961 69.739 83.961 69.739 12 77 12ZM19 15C19.0066 13.3385 20.3575 11.9961 22.019 12L67.739 12 67.739 83.961 22.019 83.961C20.3575 83.9649 19.0066 82.6225 19 80.961Z">&nbsp;<path d="M52.054 39.135C52.0755 34.8907 48.6524 31.4326 44.4081 31.4111 40.1638 31.3896 36.7057 34.8127 36.6842 39.057 36.6627 43.3013 40.0858 46.7594 44.3301 46.7809 44.3434 46.781 44.3567 46.781 44.37 46.781 48.5994 46.7954 52.0396 43.3784 52.054 39.1491 52.054 39.1444 52.054 39.1397 52.054 39.135ZM50.054 39.135C50.0755 42.2747 47.5478 44.8373 44.4081 44.8589 41.2685 44.8804 38.7058 42.3527 38.6843 39.213 38.6627 36.0733 41.1905 33.5107 44.3301 33.4891 44.3434 33.489 44.3567 33.489 44.37 33.489 47.4971 33.4823 50.0397 36.0079 50.054 39.135Z">&nbsp;<path d="M29 56.326 29 63.972 59.739 63.972 59.739 56.326C59.714 55.1266 59.1484 54.0027 58.2 53.268 54.1587 50.3779 49.3374 48.7785 44.37 48.68 42.2213 48.6861 40.0852 49.0096 38.031 49.64 35.3155 50.3359 32.7672 51.5696 30.537 53.268 29.5879 54.0019 29.0226 55.1265 29 56.326ZM31 56.326C31.0234 55.7397 31.3072 55.1945 31.774 54.839 33.7968 53.3002 36.1098 52.1862 38.574 51.564 40.4534 50.986 42.4077 50.6882 44.374 50.68 46.3439 50.7168 48.3002 51.0161 50.191 51.57 52.6256 52.2771 54.9242 53.3878 56.991 54.856 57.4427 55.2141 57.7173 55.7502 57.744 56.326L57.744 61.972 31 61.972Z">&nbsp;</path>
                        </path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">השירות שמוצע באמצעות האפליקציה, קרי בניית מערכת שעות מותאמת אישית, כרוך&nbsp;</span><u><span style="font-family:David;">במסירת פרטים ומידע אישי&nbsp;</span></u><span style="font-family:David;">(להלן: &quot;המידע&quot;), כמו למשל</span><span style="font-family:David;" dir="ltr">:</span></p>
    <ul type="disc" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:14pt; margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">גיל</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">שם מלא</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">כתובת מגורים</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">פרטי גיליון הציונים.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">כתובת דואר אלקטרוני</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">מגבלות אישיות (לרבות עבודה, התנדבויות, ילדים וחיי משפחה).</span></li>
        <li dir="rtl" style="margin-right:27.6pt; margin-bottom:14pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">או כל מידע אישי או מזהה אחר</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
    </ul>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בהתאם לחוק, יודגש שהמשתמשים אינם חייבים למסור מידע ופרטים אישיים, ומסירת פרטים אלו תלויה רק&nbsp;</span><u><span style="font-family:David;">ברצונם החופשי והסכמתם</span></u><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בהתאם, לא חלה על המשתמשים חובת הסכמה לאיסוף, מסירת או הפקת המידע שנמסר על ידם, ובכל פעם שהם משתמשים באפליקציה, הם מביעים את הסכמתם מרצונם לשימוש במלוא המידע, מסירתו או העברתו, כפי שמפורט במדיניות הפרטיות</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">יחד עם זאת, מסירת פרטים חלקיים, שגויים או שקריים, עלולה למנוע מהמשתמשים את האפשרות להשתמש בחלק משירותי האפליקציה או בכולם, או להשלים את תהליך הרישום, ובכך לפגוע באיכות השירות שהמשתמשים מקבלים</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="2" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:12pt; margin-right:14.29pt; page-break-inside:avoid; page-break-after:avoid; line-height:108%; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold;">מטרת איסוף המידע<span style="font-weight:normal;">&nbsp;</span><svg height="34.4" id="Icons_Bullseye_M" width="34.4" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M75.6 31C85.8442 47.0984 81.0984 68.4533 65 78.6974 48.9016 88.9416 27.5467 84.1958 17.3026 68.0974 7.0584 51.999 11.8042 30.6442 27.9026 20.4 39.2198 13.1983 53.6827 13.1983 65 20.4L65 18.054C47.6092 7.81304 25.2091 13.6092 14.9682 31 4.72722 48.3908 10.5233 70.7909 27.9142 81.0318 45.305 91.2728 67.705 85.4767 77.946 68.0858 84.6848 56.6422 84.6848 42.4436 77.946 31Z">&nbsp;<path d="M60.035 30.307C49.4146 22.8114 34.7286 25.3446 27.2331 35.965 19.7375 46.5854 22.2706 61.2714 32.8911 68.7669 43.5115 76.2625 58.1974 73.7294 65.693 63.1089 71.4357 54.9722 71.4357 44.1018 65.693 35.965L64.257 37.4C70.9573 47.2245 68.4245 60.6205 58.6 67.3208 48.7755 74.021 35.3795 71.4883 28.6792 61.6638 21.979 51.8392 24.5117 38.4433 34.3362 31.743 41.6542 26.7522 51.282 26.7522 58.6 31.743Z">&nbsp;<path d="M46.5 41C47.338 41.0003 48.1714 41.1246 48.973 41.369L50.534 39.809C45.1763 37.5756 39.0226 40.1083 36.7892 45.466 34.5559 50.8237 37.0886 56.9774 42.4462 59.2108 47.8039 61.4441 53.9576 58.9114 56.191 53.5538 57.2698 50.9658 57.2698 48.054 56.191 45.466L54.631 47.027C55.9968 51.5183 53.463 56.2665 48.9717 57.6323 44.4804 58.9981 39.7322 56.4643 38.3664 51.973 37.0006 47.4817 39.5344 42.7335 44.0257 41.3677 44.8278 41.1238 45.6616 40.9999 46.5 41Z">&nbsp;<path d="M87.924 17.617C87.7691 17.2434 87.4044 16.9999 87 17L79 17 79 9C78.9999 8.44771 78.5521 8.0001 77.9998 8.00021 77.7347 8.00027 77.4805 8.10558 77.293 8.293L68.293 17.293C68.1055 17.4805 68.0001 17.7348 68 18L68 26.586 45.793 48.793C45.3957 49.1767 45.3847 49.8097 45.7684 50.207 46.1521 50.6043 46.7852 50.6153 47.1824 50.2316 47.1908 50.2235 47.199 50.2153 47.207 50.207L69.414 28 78 28C78.2652 27.9999 78.5195 27.8946 78.707 27.707L87.707 18.707C87.9932 18.421 88.0788 17.9908 87.924 17.617ZM70 18.414 76.983 11.431C76.992 11.422 77 11.425 77 11.438L77 17.586 70 24.586ZM77.586 26 71.414 26 78.414 19 84.562 19C84.575 19 84.578 19.008 84.569 19.017Z">&nbsp;</path>
                            </path>
                        </path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">האיסוף של המידע נעשה&nbsp;</span><u><span style="font-family:David;">כדי לבנות למשתמש את מערכת השעות האידיאלית</span></u><span style="font-family:David;">&nbsp;עבורו אשר מותאמת לצרכיו האישיים בהתאם למידע שמסר.&nbsp;</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">כמו כן, המשתמשים באפליקציה מסכימים שבעלי האפליקציה יאספו את המידע ויפיקו אותו, כולל ביצוע עיבוד של המידע ויצירת פרופילים, על מנת לאפשר שימוש באפליקציה, למטרות הבאות</span><span style="font-family:David;" dir="ltr">:</span></p>
    <ul type="disc" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:14pt; margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">בניית מערכת שעות.&nbsp;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">תיעדוף פרסומות.&nbsp;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">שיפור חווית השירות.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">יצירת התאמות אישיות.&nbsp;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">יצירת קשר</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">אימות פרטים</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">שליחת עדכונים</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">פניה וזיהוי</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">מתן שירותים</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">עיבוד מידע</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">מחקר סטטיסטי ופילוח</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">פרסום ושיווק</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; margin-bottom:14pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">מטרות עסקיות</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
    </ul>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בעלי האפליקציה רשאים גם להשתמש במידע האישי למטרות גילוי, מסירה או מכירת המידע לצדדים שלישיים, בארץ או בחו&quot;ל.</span></p>
    <ol start="3" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:12pt; margin-right:14.29pt; page-break-inside:avoid; page-break-after:avoid; line-height:108%; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold;">שמירה ואיסוף של מידע המשתמש<span style="font-weight:normal;">&nbsp;</span><svg height="38.4" id="Icons_Computer_M" width="38.4" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M9 25.006 7 25.006 7 59.018 55 59.018 55 25.006 9 25.006ZM53 57.018 9 57.018 9 27.006 53 27.006Z">&nbsp;<path d="M56 20 6 20C3.7936 20.0066 2.00659 21.7936 2 24L2 60.019C2.00714 62.2252 3.79382 64.0119 6 64.019L26 64.019 26 72.019 16 72.019 16 74.019 46 74.019 46 72.019 36 72.019 36 64.019 56 64.019C58.2062 64.0119 59.9929 62.2252 60 60.019L60 24.005C59.9962 21.7966 58.2084 20.0066 56 20ZM34 72.023 28 72.023 28 64.023 34 64.023ZM58 60.023C58 61.1276 57.1046 62.023 56 62.023L6 62.023C4.89543 62.023 4 61.1276 4 60.023L4 24.005C4 22.9004 4.89543 22.005 6 22.005L56 22.005C57.1046 22.005 58 22.9004 58 24.005Z">&nbsp;<path d="M90 20 70 20C67.7909 20 66 21.7909 66 24L66 70C66 72.2091 67.7909 74 70 74L90 74C92.2091 74 94 72.2091 94 70L94 24C94 21.7909 92.2091 20 90 20ZM92 70C92 71.1046 91.1046 72 90 72L70 72C68.8954 72 68 71.1046 68 70L68 24C68 22.8954 68.8954 22 70 22L90 22C91.1046 22 92 22.8954 92 24Z">&nbsp;</path>
                        </path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">המשתמשים&nbsp;</span><u><span style="font-family:David;">מביעים את הסכמתם לכך שבעלי האפליקציה יאספו את המידע האישי וישמרו אותו</span></u><span style="font-family:David;">, כפי שהוא נמסר במהלך שימוש המשתמשים באפליקציה, בין אם המידע נמסר ישירות על ידי המשתמשים או התקבל בעקיפין. בין היתר, המידע שנאסף ונשמר כולל</span><span style="font-family:David;" dir="ltr">:</span></p>
    <ul type="disc" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:14pt; margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">היסטוריית גלישה</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">פרסומות שהמשתמשים נחשפו אליהן שמופיעות באפליקציה</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">מידע שהמשתמשים קראו באפליקציה</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">מיקום</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">צפייה בעמודים השונים באפליקציה</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; margin-bottom:14pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">או כל מידע אחר שנמסר על ידי המשתמשים</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
    </ul>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">כל המידע והפרטים האישיים, כפי שהם נמסרו על ידי המשתמשים,&nbsp;</span><u><span style="font-family:David;">יישמרו במאגרי המידע של בעלי האפליקציה</span></u><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="4" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:12pt; margin-right:14.29pt; page-break-inside:avoid; page-break-after:avoid; line-height:108%; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold;">העברת מידע לצדדים שלישיים<span style="font-weight:normal;">&nbsp;</span><svg height="44.8" id="Icons_CycleWithPeople_M" width="44.8" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M54.1 71C54.1 70.5 54 70 54 69.5 54 69.3 54 69.2 54 69L42 69C42 69.2 42 69.3 42 69.5 42 70 42 70.5 41.9 71L54.1 71Z">&nbsp;<path d="M32.9 55.4 38.5 45.7C37.9 45.4 37.4 45 36.8 44.6L31 54.7C31.7 54.9 32.3 55.1 32.9 55.4Z">&nbsp;<path d="M64.2 55 58.2 44.6C57.7 45 57.1 45.3 56.5 45.7L62.3 55.8C62.9 55.5 63.6 55.2 64.2 55Z">&nbsp;<path d="M26.5 57C19.6 57 14 62.6 14 69.5 14 76.4 19.6 82 26.5 82 33.4 82 39 76.4 39 69.5 39 62.6 33.4 57 26.5 57ZM20.5 78.1C20.8 74.8 23.8 72.3 27.1 72.6 30 72.9 32.3 75.2 32.6 78.1 28.9 80.6 24.1 80.6 20.5 78.1ZM23.7 67.8C23.7 66.3 24.9 65 26.5 65 28 65 29.3 66.2 29.3 67.8 29.3 69.3 28.1 70.6 26.5 70.6 25 70.6 23.7 69.3 23.7 67.8ZM34.3 76.5C33.7 74.2 32 72.2 29.8 71.2 31.7 69.4 31.8 66.4 30 64.4 28.2 62.5 25.2 62.4 23.2 64.2 21.3 66 21.2 69 23 71 23.1 71.1 23.2 71.2 23.2 71.2 21 72.2 19.3 74.1 18.7 76.5 14.8 72.2 15.1 65.6 19.4 61.7 23.7 57.8 30.3 58.1 34.2 62.4 37.9 66.4 37.9 72.5 34.3 76.5Z">&nbsp;<path d="M69.5 57C62.6 57 57 62.6 57 69.5 57 76.4 62.6 82 69.5 82 76.4 82 82 76.4 82 69.5 82 62.6 76.4 57 69.5 57ZM63.5 78.1C63.8 74.8 66.8 72.3 70.1 72.6 73 72.9 75.3 75.2 75.6 78.1 71.9 80.6 67.1 80.6 63.5 78.1ZM66.7 67.8C66.7 66.3 67.9 65 69.5 65 71 65 72.3 66.2 72.3 67.8 72.3 69.3 71.1 70.6 69.5 70.6 68 70.6 66.7 69.3 66.7 67.8ZM77.3 76.5C76.7 74.2 75 72.2 72.8 71.2 74.7 69.4 74.8 66.4 73 64.4 71.2 62.5 68.2 62.4 66.2 64.2 64.2 66 64.2 69 66 71 66.1 71.1 66.2 71.2 66.2 71.2 64 72.2 62.3 74.1 61.7 76.5 57.8 72.2 58.1 65.6 62.4 61.7 66.7 57.8 73.3 58.1 77.2 62.4 80.9 66.4 80.9 72.5 77.3 76.5Z">&nbsp;<path d="M47.5 14C38.9 14 32 20.9 32 29.5 32 38.1 38.9 45 47.5 45 56.1 45 63 38.1 63 29.5 63 20.9 56.1 14 47.5 14ZM39.6 40.4C39.9 36 43.7 32.8 48.1 33.1 52 33.4 55.1 36.5 55.4 40.4 50.7 43.9 44.3 43.9 39.6 40.4ZM43.7 27.3C43.7 25.2 45.4 23.5 47.5 23.5 49.6 23.5 51.3 25.2 51.3 27.3 51.3 29.4 49.6 31.1 47.5 31.1 45.4 31.1 43.7 29.4 43.7 27.3L43.7 27.3ZM57.2 38.7C56.5 35.5 54.2 32.9 51.2 31.8 53.7 29.8 54 26.2 52 23.7 50 21.2 46.4 20.9 43.9 22.9 41.4 24.9 41 28.5 43 31 43.2 31.3 43.5 31.6 43.8 31.8 40.7 33 38.5 35.7 37.8 38.9 32.6 33.6 32.7 25 38.1 19.8 43.5 14.6 52 14.7 57.2 20.1 62.3 25.3 62.3 33.7 57.2 38.9 57.2 38.9 57.2 38.8 57.2 38.7Z">&nbsp;</path>
                                    </path>
                                </path>
                            </path>
                        </path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">לבעלי האפליקציה יש&nbsp;</span><u><span style="font-family:David;">זכות להשתמש במידה ולהעביר אותו לצדדים שלישיים</span></u><span style="font-family:David;">. לרבות שותפים עסקיים וספקי שירותים שונים, בהתאם לשיקול דעתם, בין היתר גם כדי למלא אחרי הוראות הדין, כולל</span><span style="font-family:David;" dir="ltr">:</span></p>
    <div style="margin-top:14pt; margin-right:18pt; background-color:#ffffff;">
        <p dir="rtl" style="margin-top:0pt; margin-right:18pt; margin-bottom:0pt; text-indent:-18pt; text-align:justify; line-height:normal; font-size:12pt;"><span style="font-family:Wingdings;"></span><span style="width:9.08pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span style="font-family:David;">החוקים והחקיקות</span><span style="font-family:David;" dir="ltr">;</span></p>
    </div>
    <div style="margin-right:18pt; background-color:#ffffff;">
        <p dir="rtl" style="margin-top:0pt; margin-right:18pt; margin-bottom:0pt; text-indent:-18pt; text-align:justify; line-height:normal; font-size:12pt;"><span style="font-family:Wingdings;"></span><span style="width:9.08pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span style="font-family:David;">הפקודות והצווים</span><span style="font-family:David;" dir="ltr">;</span></p>
    </div>
    <div style="margin-right:18pt; background-color:#ffffff;">
        <p dir="rtl" style="margin-top:0pt; margin-right:18pt; margin-bottom:0pt; text-indent:-18pt; text-align:justify; line-height:normal; font-size:12pt;"><span style="font-family:Wingdings;"></span><span style="width:9.08pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span style="font-family:David;">האמנות והתקנות</span><span style="font-family:David;" dir="ltr">;</span></p>
    </div>
    <div style="margin-right:18pt; background-color:#ffffff;">
        <p dir="rtl" style="margin-top:0pt; margin-right:18pt; margin-bottom:0pt; text-indent:-18pt; text-align:justify; line-height:normal; font-size:12pt;"><span style="font-family:Wingdings;"></span><span style="width:9.08pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span style="font-family:David;">הוראות המינהל והוראות רשמיות</span><span style="font-family:David;" dir="ltr">;</span></p>
    </div>
    <div style="margin-right:18pt; margin-bottom:14pt; background-color:#ffffff;">
        <p dir="rtl" style="margin-top:0pt; margin-right:18pt; margin-bottom:0pt; text-indent:-18pt; text-align:justify; line-height:normal; font-size:12pt;"><span style="font-family:Wingdings;"></span><span style="width:9.08pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span style="font-family:David;">הנחיות או חוזרים של גופים רגולטוריים או שלטוניים שונים</span><span style="font-family:David;" dir="ltr">.</span></p>
    </div>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><u><span style="font-family:David;">מטרת העברת המידע לצדדים שלישיים</span></u><span style="font-family:David;">&nbsp;תתבצע בכל מקרה שנוגע לאחד או יותר מהתרחישים הבאים</span><span style="font-family:David;" dir="ltr">:</span></p>
    <ul type="disc" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:14pt; margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">בקשה או תלונה הנוגעת לשימוש באפליקציה</span><span style="font-family:David; font-size:12pt;" dir="ltr">;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">טיפול בבעיות טכניות או בעיות אבטחה של השימוש באפליקציה או השימוש במערכותיו</span><span style="font-family:David; font-size:12pt;" dir="ltr">;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">סכסוכים משפטיים בין המשתמשים לבין בעלי האפליקציה, כדי להשיב על תביעות של צדדים שלישיים</span><span style="font-family:David; font-size:12pt;" dir="ltr">;</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">כשהשימוש באפליקציה התבצע באופן שמנוגד להוראות כל דין, לתנאי השימוש או למטרות שיפור או שינוי האפליקציה</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">הגנה על זכויות הקניין של המשתמשים באפליקציה או של בעלי האפליקציה</span><span style="font-family:David; font-size:12pt;" dir="ltr">.</span></li>
        <li dir="rtl" style="margin-right:27.6pt; text-align:justify; line-height:normal; padding-right:8.4pt; font-family:serif; font-size:10pt; background-color:#ffffff;"><span style="font-family:David; font-size:12pt;">הצעת שירותים נוספים למשתמשים מטעם אותם צדדים שלישיים במסגרת פרסום ממוקד באפליקציה.&nbsp;</span>
            <ol start="5" type="1" style="margin-right:0pt; margin-left:0pt; padding-right:0pt;">
                <li dir="rtl" style="margin-right:-21.71pt; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold; background-color:#ffffff;"><span style="letter-spacing:-0.25pt;">השימוש באפליקציה על ידי צדדים שלישיים&nbsp;</span></li>
            </ol>
        </li>
    </ul>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">המשתמשים מאשרים שלמטרות המפורטות במסמך מדיניות פרטיות זה, לבעלי האפליקציה יש זכות להעביר את המידע לצדדים שלישיים, וכי להם יש זכות לבצע שימוש במידע שקיבלו לאותן מטרות כפי שהן מפורטות בתנאי השימוש ובמדיניות הפרטיות, כמו גם לשמור את המידע במאגרי המידע שלהם. בעלי האפליקציה אינם אחראים לשום סוג של שימוש של צדדים שלישיים במידע</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="6" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:12pt; margin-right:14.29pt; page-break-inside:avoid; page-break-after:avoid; line-height:108%; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold;">שימוש בעוגיות <span dir="ltr">(Cookies)</span><span style="font-weight:normal;">&nbsp; &nbsp; &nbsp;</span><svg height="46.4" id="Icons_GingerbreadCookie_M" width="46.4" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M75.3105 70.0027C73.7842 69.2537 72.6191 68.7361 71.6836 68.3201 69.9191 67.6483 68.2808 66.6832 66.8379 65.4656 65.0186 63.9207 63.4215 62.1319 62.0917 60.15 61.1824 57.8731 60.8725 55.4009 61.1917 52.97L72.8217 47.9234 75.7417 46.6534 75.9317 46.5734C79.7299 44.9233 81.4713 40.5065 79.8212 36.7082 78.1771 32.9239 73.7845 31.1789 69.9917 32.8034 69.9817 32.8034 69.9717 32.8134 69.9617 32.8134L66.9517 34.1234 57.83 38.0788C57.8253 38.081 57.8198 38.0789 57.8177 38.0743 57.816 38.0707 57.8168 38.0666 57.8195 38.0638 60.5153 35.2406 61.9986 31.4741 61.9516 27.5708 61.8559 19.2871 55.0631 12.6493 46.7794 12.745 38.5639 12.8399 31.9536 19.5262 31.9526 27.7422 31.9505 31.5875 33.4317 35.2855 36.0877 38.0662 36.0912 38.0699 36.091 38.0757 36.0873 38.0792 36.0848 38.0816 36.081 38.0824 36.0777 38.0811L26.9509 34.124 23.9409 32.814C23.9309 32.814 23.9209 32.804 23.9109 32.804 20.1042 31.1736 15.6965 32.9378 14.066 36.7445 12.4416 40.5373 14.1866 44.9299 17.9709 46.574L18.1609 46.654 21.0809 47.924 32.7137 52.9718C33.0411 55.5549 32.6707 58.1785 31.6411 60.57 30.3768 62.3875 28.8819 64.033 27.1937 65.4653 25.7508 66.683 24.1125 67.6482 22.348 68.32 21.4125 68.736 20.2474 69.2536 18.7211 70.0026 16.5433 71.07 15.4427 72.7965 15.6211 74.8639 15.9211 78.3268 19.8545 82.0172 24.7711 83.4489 25.7901 83.7515 26.8468 83.908 27.9097 83.9137L27.9107 83.9137C33.1138 83.9137 36.5396 80.0407 39.0416 77.2125 39.4296 76.7741 43.226 72.1525 47.0151 67.5302 50.8039 72.152 54.6003 76.7741 54.9885 77.2125 57.4904 80.0407 60.9162 83.9137 66.1193 83.9137L66.1203 83.9137C67.1836 83.9081 68.2407 83.7516 69.26 83.449 74.177 82.0173 78.1106 78.3269 78.41 74.864 78.5889 72.7966 77.4883 71.07 75.3105 70.0027ZM77.5305 36.6392C79.2133 39.1742 78.5224 42.5934 75.9874 44.2762 75.898 44.3355 75.8068 44.3923 75.7141 44.4463 71.7795 42.717 70.1988 39.4917 70.8927 34.6063 72.4762 33.9451 74.2808 34.0836 75.7448 34.9787 76.461 35.3857 77.0723 35.9543 77.53 36.6392ZM16.3937 36.6073C16.8571 35.924 17.4738 35.3586 18.1946 34.956 19.6531 34.0808 21.4407 33.9508 23.0104 34.606 23.7033 39.4901 22.1236 42.7149 18.1921 44.4444 15.5629 42.9152 14.6713 39.5442 16.2005 36.915 16.2614 36.8103 16.3257 36.7077 16.3933 36.6073ZM27.9105 81.9138C27.0366 81.908 26.168 81.7784 25.3305 81.5288 20.8159 80.2141 17.8097 76.9563 17.6136 74.6917 17.5502 73.4494 18.299 72.3092 19.4643 71.8738 22.0516 72.4377 24.385 73.8285 26.1119 75.8359 27.6405 77.5146 28.6852 79.5764 29.1346 81.8019 29.1357 81.8073 29.1322 81.8126 29.1268 81.8137 29.1266 81.8137 29.1263 81.8138 29.1261 81.8138 28.724 81.8779 28.3176 81.9113 27.9105 81.9138ZM56.4868 75.887C56.314 75.6917 55.0547 74.1819 48.5626 66.2622 48.0724 65.6646 47.2819 65.4026 46.5318 65.5892 46.1032 65.7001 45.722 65.9466 45.4449 66.2919 38.9713 74.1883 37.7162 75.6934 37.5435 75.8884 35.8021 77.8568 33.746 80.1734 31.0779 81.2717 31.0728 81.2738 31.0669 81.2714 31.0648 81.2663 31.0646 81.2657 31.0644 81.2651 31.0643 81.2645 30.5281 78.746 29.3351 76.4143 27.6064 74.5059 26.1133 72.8104 24.2526 71.4783 22.1664 70.6112 22.1546 70.6064 22.1547 70.5982 22.1664 70.593 22.5208 70.433 22.8586 70.2817 23.165 70.1455 25.0969 69.3981 26.8915 68.3354 28.4756 67.0007 30.2949 65.4585 31.9064 63.6868 33.27 61.73L33.5012 61.3044C34.6545 58.6017 35.0677 55.6408 34.6982 52.7256 34.6062 52.0252 34.156 51.4232 33.51 51.1372L20.5211 45.5C20.5162 45.4974 20.5143 45.4914 20.5169 45.4865 20.5177 45.4851 20.5188 45.4838 20.5201 45.4829 23.8795 43.4079 25.4439 40.0137 25.1164 35.5229 25.116 35.5174 25.1202 35.5126 25.1257 35.5123 25.1272 35.5122 25.1286 35.5124 25.1299 35.5129L35.3236 39.9345C36.3382 40.3745 37.5173 39.9087 37.9572 38.8941 37.9791 38.8436 37.9989 38.7922 38.0166 38.7401 38.2386 37.9756 38.0207 37.1509 37.4501 36.5958 32.5505 31.3478 32.8329 23.1215 38.0809 18.2219 43.3289 13.3222 51.5552 13.6046 56.4549 18.8527 61.1138 23.8429 61.119 31.5868 56.4666 36.5832 55.9295 37.1678 55.7157 37.98 55.8956 38.7532 56.2588 39.7976 57.4 40.3498 58.4444 39.9866 58.4914 39.9703 58.5377 39.9522 58.5833 39.9324L68.7722 35.513C68.7774 35.5111 68.7831 35.5137 68.7851 35.5188 68.7856 35.5202 68.7858 35.5216 68.7857 35.523 68.4577 40.0138 70.0221 43.408 73.3819 45.483 73.3865 45.4861 73.3876 45.4923 73.3845 45.4969 73.3836 45.4982 73.3823 45.4993 73.3809 45.5001L60.3955 51.1359C59.7457 51.4255 59.2942 52.0333 59.2045 52.7391 58.8484 55.4835 59.1967 58.2734 60.2166 60.8461L60.443 61.2826C61.8756 63.4154 63.5963 65.3398 65.5563 67.001 67.1474 68.3404 68.9498 69.4066 70.89 70.156 71.1692 70.28 71.4782 70.4183 71.8026 70.5646 71.8143 70.5698 71.8143 70.5781 71.8026 70.5828 69.6893 71.4488 67.8048 72.7914 66.2961 74.5059 64.5798 76.4014 63.391 78.7141 62.8486 81.213 62.8474 81.2184 62.842 81.2218 62.8366 81.2205 62.8361 81.2204 62.8355 81.2202 62.835 81.22 60.225 80.1024 58.2031 77.8271 56.4868 75.887ZM76.4176 74.6914C76.2216 76.9563 73.2155 80.2141 68.7006 81.5288 67.8629 81.7784 66.9941 81.908 66.1201 81.9138 65.6705 81.9119 65.2219 81.8724 64.7789 81.7959 64.7734 81.7951 64.7697 81.79 64.7705 81.7845 64.7705 81.7843 64.7706 81.7842 64.7706 81.784 65.2222 79.5653 66.2655 77.51 67.79 75.8359 69.5364 73.8023 71.9054 72.4022 74.5291 71.853 75.7136 72.2818 76.4797 73.4332 76.4176 74.6914Z">&nbsp;<path d="M54.373 29.8506C53.8964 29.5727 53.2847 29.7338 53.0068 30.2104 53.0065 30.2109 53.0062 30.2114 53.0059 30.2119 51.0619 33.555 46.7758 34.6892 43.4327 32.7452 42.3891 32.1384 41.5202 31.2722 40.9102 30.2305 40.6205 29.7603 40.0045 29.6139 39.5343 29.9036 39.0784 30.1845 38.9246 30.7746 39.1855 31.2422 41.6982 35.532 47.2127 36.9726 51.5025 34.4599 52.8412 33.6758 53.9545 32.559 54.7344 31.2178 55.0121 30.7405 54.8503 30.1284 54.373 29.8506Z">&nbsp;</path>
                    </path>
                </g>&nbsp;</svg><span style="font-weight:normal;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span style="font-weight:normal;" dir="ltr">&nbsp;&nbsp;</span></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">כחלק מהתפעול השוטף של אפליקציה נעשה שימוש ב&quot;עוגיות&quot;, שבין היתר משמשות להבנת העדפות המשתמש והתאמות אישיות, אימות פרטים אישיים, או איסוף מידע סטטיסטי. מובהר בזאת שיתכן שלא יתבקש אישור המשתמשים לפני השימוש.&nbsp;</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">המשתמשים רשאים בכל עת לנקות את &quot;העוגיות&quot; מהדפדפן שלהם, או להגדיר אותו באופן שיסרב לבצע שימוש ב&quot;עוגיות&quot;</span><span style="font-family:David;" dir="ltr">.</span><span style="font-family:David;">&nbsp;אולם&nbsp;</span><span style="font-family:David;">בעלי האפליקציה&nbsp;</span><u><span style="font-family:David;">אינם מבטיחים שפעילויות אלו יאפשרו שימוש וגלישה תקינים באפליקציה</span></u><span style="font-family:David;">, והם רשאים למנוע שירות או לחסום את השימוש באפליקציה במקרים בהם בוצעו פעולות כאמור</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="7" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:12pt; margin-right:14.29pt; page-break-inside:avoid; page-break-after:avoid; line-height:108%; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold;"><a name="_Hlk156325664">קישורים לאפליקציות אחרות<span style="font-weight:normal;">&nbsp;</span></a><svg height="32" id="Icons_Link_M" width="32" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<path d="M42.565 48.215C37.9544 50.4224 32.4534 49.4867 28.832 45.879L21.137 38.184C16.4258 33.4765 16.4228 25.8412 21.1302 21.13 25.8377 16.4188 33.473 16.4158 38.1842 21.1232 38.1865 21.1255 38.1887 21.1277 38.191 21.13L45.891 28.83C49.4992 32.4511 50.435 37.9525 48.227 42.563L49.718 44.054C52.6786 38.5816 51.6955 31.8147 47.3 27.411L39.6 19.716C34.0327 14.3036 25.132 14.4291 19.7195 19.9964 14.4134 25.4543 14.415 34.1439 19.723 39.6L27.423 47.3C31.8256 51.6942 38.5914 52.6754 44.061 49.713Z">&nbsp;<path d="M76.291 56.4 68.6 48.707C64.1955 44.3165 57.4323 43.3356 51.962 46.294L53.452 47.785C58.0616 45.5681 63.5686 46.5048 67.186 50.121L74.88 57.821C79.6504 62.4684 79.7502 70.1031 75.1028 74.8735 70.4553 79.644 62.8207 79.7437 58.0502 75.0963 57.9738 75.0219 57.8984 74.9464 57.824 74.87L50.124 67.17C46.5158 63.5489 45.58 58.0475 47.788 53.437L46.3 51.951C43.3404 57.4209 44.3209 64.1847 48.712 68.589L56.412 76.289C61.9042 81.7784 70.8066 81.7762 76.296 76.284 81.7854 70.7918 81.7832 61.8894 76.291 56.4Z">&nbsp;<path d="M58.614 59.607C58.3488 59.6069 58.0945 59.5015 57.907 59.314L36.694 38.1C36.2967 37.7163 36.2857 37.0833 36.6694 36.686 37.0531 36.2887 37.6862 36.2777 38.0834 36.6614 38.0918 36.6695 38.1 36.6777 38.108 36.686L59.321 57.9C59.7115 58.2906 59.7114 58.9237 59.3208 59.3142 59.1333 59.5016 58.8791 59.6069 58.614 59.607Z">&nbsp;</path>
                    </path>
                </path></svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">באפליקציה מופיעים קישורים שמפנים את המשתמשים לאפליקציות או אתרים שונים, כמו גם הצעות פרסום לרכישת מוצרים נוספים. מובהר שמדיניות הפרטיות כפי שהיא מפורטת במסמך זה חלה בנוגע לאפליקציה בלבד</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><u><span style="font-family:David;">בעלי האפליקציה אינם אחראים למדיניות הפרטיות של אפליקציות חיצוניות</span></u><span style="font-family:David;">, והכניסה אליהם באמצעות הקלקה על הקישורים היא באחריות הבלעדית של המשתמשים. בעלי האפליקציה אינם אחראים לשימוש או כניסה לאפליקציות אחרות, ומומלץ לקרוא בעיון את תנאי השימוש ומדיניות הפרטיות באפליקציות המקושרות לפני העברת פרטים אישיים או ביצוע פעולות שונות בהם</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="8" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:12pt; margin-right:14.29pt; page-break-inside:avoid; page-break-after:avoid; line-height:108%; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold; letter-spacing:-0.25pt;"><span style="letter-spacing:normal;">דיוור ישיר והודעות פרסומיות</span><span style="font-weight:normal;">&nbsp;</span><img src="data:image/png;base64,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" width="63" height="56" alt="אנטי ספאם - אבטחת המידע שלכם עם צעד אחד קדימה | IT-START"></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">לאורך שנת הלימודים בעלי האפליקציה ישתמשו במידע שנמסר כדי להציע למשתמשים שירותים שונים בתשלום או שלא בתשלום מטעם בעלי האפליקציה או שותפיהם העסקיים או צדדים שלישיים אחרים.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">המשתמשים מאשרים שהם&nbsp;</span><u><span style="font-family:David;">מסכימים לקבל דברי פרסומת</span></u><span style="font-family:David;">&nbsp;כפי שמפורט בסעיף 30א&apos; לחוק התקשורת (בזק ושידורים), התשמ&quot;ב-1982 (להלן: &quot;חוק התקשורת&quot;), כמו גם&nbsp;</span><u><span style="font-family:David;">לקבלת דיוורים ישירים</span></u><span style="font-family:David;">&nbsp;בהתאם לחוק הגנת הפרטיות התשמ&quot;א-1981 (להלן: &quot;חוק הגנת הפרטיות) מבעלי האפליקציה ומהספקים</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">מבלי לגרוע מכלליות האמור לעיל, המשתמשים באפליקציה מאשרים ומביעים את הסכמתם לקבלת כל מידע שיווקי כגון</span><span style="font-family:David;" dir="ltr">:</span></p>
    <div style="margin-top:14pt; margin-right:18pt; background-color:#ffffff;">
        <p dir="rtl" style="margin-top:0pt; margin-right:18pt; margin-bottom:0pt; text-indent:-18pt; text-align:justify; line-height:normal; font-size:12pt;"><span style="font-family:Wingdings; font-size:16pt;"></span><span style="width:7.3pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp; &nbsp;</span><span style="font-family:David;">עדכונים</span><span style="font-family:David;" dir="ltr">.</span></p>
    </div>
    <div style="margin-right:18pt; background-color:#ffffff;">
        <p dir="rtl" style="margin-top:0pt; margin-right:18pt; margin-bottom:0pt; text-indent:-18pt; text-align:justify; line-height:normal; font-size:12pt;"><span style="font-family:Wingdings; font-size:16pt;"></span><span style="width:7.3pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp; &nbsp;</span><span style="font-family:David;">מבצעים והטבות</span><span style="font-family:David;" dir="ltr">.</span></p>
    </div>
    <div style="margin-right:18pt; background-color:#ffffff;">
        <p dir="rtl" style="margin-top:0pt; margin-right:18pt; margin-bottom:0pt; text-indent:-18pt; text-align:justify; line-height:normal; font-size:12pt;"><span style="font-family:Wingdings; font-size:16pt;"></span><span style="width:7.3pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp; &nbsp;</span><span style="font-family:David;">מידע שיווקי ופרסומי</span><span style="font-family:David;" dir="ltr">.</span></p>
    </div>
    <div style="margin-right:18pt; background-color:#ffffff;">
        <p dir="rtl" style="margin-top:0pt; margin-right:18pt; margin-bottom:0pt; text-indent:-18pt; text-align:justify; line-height:normal; font-size:12pt;"><span style="font-family:Wingdings; font-size:16pt;"></span><span style="width:7.3pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp; &nbsp;</span><span style="font-family:David;">הצעות לרכישת שירותים או מוצרים מבעלי האפליקציה או מצדדים שלישיים</span><span style="font-family:David;" dir="ltr">.</span></p>
    </div>
    <div style="margin-right:18pt; margin-bottom:14pt; background-color:#ffffff;">
        <p dir="rtl" style="margin-top:0pt; margin-right:18pt; margin-bottom:0pt; text-indent:-18pt; text-align:justify; line-height:normal; font-size:12pt;"><span style="font-family:Wingdings; font-size:16pt;"></span><span style="width:7.3pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp; &nbsp;</span><span style="font-family:David;">סוגים שונים של דיוור ישיר</span><span style="font-family:David;" dir="ltr">.</span></p>
    </div>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">מידע שיווקי זה יכול להגיע אל המשתמשים באפליקציה כמודעות קופצות בתוך האפליקציה, בדואר האלקטרוני, במסרונים בטלפון הנייד, במערכת חיוג אוטומטי, בפקס, או בכל שיטת ואמצעי תקשורת אחר</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="9" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:12pt; margin-right:14.29pt; page-break-inside:avoid; page-break-after:avoid; line-height:108%; padding-right:3.71pt; font-family:David; font-size:12pt; font-weight:bold;">הזכויות שלך במידע<span style="font-weight:normal;">&nbsp;</span><svg height="42.4" id="Icons_WeightsUneven_M" width="42.4" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M21.5 68.729C28.509 68.729 34 65.554 34 61.5L34 60.5 29.9 60.5 23 33.856 45.146 24.774C45.5203 25.1563 45.9674 25.4596 46.461 25.666 46.6379 25.7343 46.8193 25.7901 47.004 25.833L47.004 81 40 81C37.7909 81 36 82.7909 36 85L38 85C38 83.8954 38.8954 83 40 83L56 83C57.1046 83 58 83.8954 58 85L60 85C60 82.7909 58.2091 81 56 81L49 81 49 25.833C49.1759 25.7923 49.3489 25.7402 49.518 25.677 51.0243 25.0592 52.0058 23.59 52 21.962L72.572 13.525 66.1 38.5 62 38.5 62 39.5C62 43.554 67.491 46.729 74.5 46.729 81.509 46.729 87 43.554 87 39.5L87 38.5 82.9 38.5 76.058 12.1 78.106 11.259C78.6112 11.0358 78.8398 10.4454 78.6167 9.9402 78.402 9.45426 77.8449 9.22098 77.348 9.409L51.466 20.019C50.9363 19.0771 50.046 18.3915 49 18.12L49 9C49 8.44771 48.5523 8 48 8 47.4477 8 47 8.44771 47 9L47 18.122C44.9273 18.5786 43.6171 20.629 44.0737 22.7017 44.097 22.8076 44.1248 22.9125 44.157 23.016L17.088 34.116C16.5769 34.3256 16.3324 34.9099 16.542 35.421 16.7516 35.9321 17.3359 36.1766 17.847 35.967L19.647 35.228 13.1 60.5 9 60.5 9 61.5C9 65.554 14.491 68.729 21.5 68.729ZM84.8 40.5C83.833 42.875 79.509 44.729 74.5 44.729 69.491 44.729 65.169 42.875 64.2 40.5ZM80.84 38.5 68.162 38.5 74.49 14.093C74.49 14.0875 74.4945 14.083 74.5 14.083 74.5055 14.083 74.51 14.0875 74.51 14.093ZM47.24 20.125C47.4574 20.0386 47.6882 19.9909 47.922 19.984 47.9477 19.9908 47.9737 19.9962 48 20 48.03 20 48.056 19.985 48.085 19.983 49.1821 20.0381 50.0268 20.9721 49.9718 22.0692 49.9167 23.1663 48.9827 24.0111 47.8856 23.956 46.7884 23.9009 45.9437 22.9669 45.9988 21.8698 46.0376 21.0959 46.5224 20.415 47.241 20.125ZM21.51 36.093 27.838 60.5 15.162 60.5 21.49 36.093C21.49 36.0875 21.4945 36.083 21.5 36.083 21.5055 36.083 21.51 36.0875 21.51 36.093ZM31.8 62.5C30.833 64.875 26.509 66.729 21.5 66.729 16.491 66.729 12.169 64.875 11.2 62.5Z">&nbsp;</path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><u><span style="font-family:David;">הזכות לעיין במידע</span></u><span style="font-family:David;">&nbsp;המשתמש זכאי לעיין במידע שנאסף אודותיו, ששמור במאגרי המידע שלנו, ושמזוהה ומשויך אליו. אין אפשרות לעיין במידע שאינו מזוהה ומשויך.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><u><span style="font-family:David;">הזכות לתיקון מידע</span></u><span style="font-family:David;">&nbsp;אם המשתמש מצא שהמידע שנשמר אודותיו אינו נכון, שלם, ברור או מעודכן, ניתן לפנות לבעלי האפליקציה בבקשה מפורטת לתיקון או מחיקה של המידע. למימוש זכויות אלו, ניתן לפנות לבעלי האפליקציה, באמצעות פרטי הקשר המופיעים בהמשך מסמך זה. בעלי האפליקציה יבחנו את הפנייה, וישיבו בהתאם למועדים הקבועים בחוק.&nbsp;</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><u><span style="font-family:David;">הזכות לבטל הסכמה</span></u><span style="font-family:David;">&nbsp;המשתמש זכאי, בכל עת, לבטל את הסכמתו לקבלת דיוור, בפניה מתאימה אל בעלי האפליקציה. לפירוט נוסף, ראה את הפרק העוסק בדיוור ישיר והודעות פרסומיות.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><u><span style="font-family:David;">זכויות נוספות בקשר למידע</span></u><span style="font-family:David;">&nbsp;ייתכן שהמשתמש זכאי לזכויות נוספות, בקשר למידע אודותיו. לפניות בנושאים אלו, או בנושאים אחרים הקשורים למדיניות פרטיות זו, ניתן לפנות לבעלי האפליקציה באמצעות פרטי הקשר המופיעים בהמשך מסמך זה. בעלי האפליקציה יבדקו את הפניה וישיבו בהתאם.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">גם אם ימחק, יתוקן מידע, או תתקבל בקשתה בכל דרך אחרת, בעלי האפליקציה בכל מקרה יוסיפו וישמרו מידע שדרוש להם לשם ניהול השירות, לרבות מידע אשר דרוש להם להגנה ולשמירה על זכויותיהם המשפטיות, או לצורך עמידה בדרישות הרגולטוריות, מניעת הונאה או תרמית, ואכיפה של מדיניות פרטיות זו ותנאי השימוש באתרים.</span></p>
    <ol start="10" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:12pt; margin-right:18pt; page-break-inside:avoid; page-break-after:avoid; line-height:108%; font-family:David; font-size:12pt; font-weight:bold;">אבטחת מידע<span style="font-weight:normal;">&nbsp;&nbsp;</span><svg height="36" id="Icons_Unlock_M" width="36" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M20 47.512 20 85.523 48 87.523 76 85.523 76 47.512 69 47.012 63 46.612 48 45.512 34 46.539 34 29.006C34 21.274 40.268 15.006 48 15.006 55.732 15.006 62 21.274 62 29.006L62 36 69 36 69.029 29.031C69.029 17.4187 59.6153 8.005 48.003 8.005 36.3907 8.005 26.977 17.4187 26.977 29.031L26.977 47.014ZM28.976 29.031C28.976 18.5232 37.4942 10.005 48.002 10.005 58.5098 10.005 67.028 18.5232 67.028 29.031L67 34 64 34 64 29.006C64 20.1694 56.8366 13.006 48 13.006 39.1634 13.006 32 20.1694 32 29.006L32 46.679 28.975 46.879ZM33.147 48.607 48 47.517 62.867 48.608 68.858 49.008 74 49.375 74 83.661 48 85.519 22 83.661 22 49.375 27.134 49.008Z">&nbsp;<path d="M45 71.89 45 77.521 51 77.521 51 71.866C53.4176 70.6668 54.9617 68.2164 55 65.518 54.9738 61.6521 51.8185 58.5394 47.9526 58.5657 44.0867 58.5919 40.9741 61.7471 41.0003 65.613 41.0186 68.2995 42.5727 70.7386 45 71.89ZM48 60.516C50.7598 60.5199 52.9961 62.7562 53 65.516 52.9564 67.6436 51.6247 69.5313 49.635 70.286L49 70.537 49 75.521 47 75.521 47 70.508 46.328 70.275C43.7151 69.3349 42.359 66.4546 43.2991 63.8417 44.0133 61.8568 45.8905 60.5287 48 60.516Z">&nbsp;</path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">מסירת המידע באפליקציה או איסופו במהלך השימוש באפליקציה, מתבצעים&nbsp;</span><u><span style="font-family:David;">בתהליכים מאובטחים שמאפשרים הצפנת מידע</span></u><span style="font-family:David;">&nbsp;שמועבר באינטרנט באופן שאינו מאפשר זיהוי או קריאה של המידע במהלך העברתו</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בעלי האפליקציה&nbsp;</span><u><span style="font-family:David;">ינקטו בכל המאמצים לאבטח את המידע באפליקציה</span></u><span style="font-family:David;">, בהתאם למקובל ולנהוג באפליקציות מסוג זה, אך אינם ערבים ואינם מבטיחים שמסדי הנתונים שלהם, כולל המידע האישי שנמסר על ידי המשתמשים, לא ייפרץ ושהמידע לא יגיע לצדדים שלישיים שאינם מורשים</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">כל עוד בעלי האפליקציה נוקטים באמצעים סבירים לאבטחת המידע, הם לא יימצאו אחראים לשום נזקים, מכל סוג שהוא, שייגרמו למשתמשים כתוצאה מפריצה לאפליקציה, למסדי הנתונים או למחשבים המפעילים אותו</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="11" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:12pt; margin-right:18pt; page-break-inside:avoid; page-break-after:avoid; line-height:108%; font-family:David; font-size:12pt; font-weight:bold;">חשיפה לסיכונים והגבלת אחריות<svg height="34.4" id="Icons_BioHazard_M" width="34.4" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M51.16 63.52C51.1261 64.7978 51.415 66.0635 52 67.2 56.6312 65.228 59.333 60.3639 58.56 55.39 57.2971 55.512 56.0791 55.9225 55 56.59 55.0647 57.1582 55.0647 57.7318 55 58.3 54.6106 60.5464 53.1886 62.4795 51.16 63.52Z">&nbsp;<path d="M36.7 55.27C35.8564 60.4577 38.7836 65.5218 43.7 67.38 43.7328 67.3113 43.7695 67.2445 43.81 67.18 44.3421 66.1263 44.6389 64.9697 44.68 63.79 42.5964 62.8985 41.0524 61.0804 40.51 58.88L40.54 58.88C40.2856 58.0178 40.2041 57.1138 40.3 56.22 39.189 55.6308 37.9571 55.3058 36.7 55.27Z">&nbsp;<path d="M42.35 49.68C42.8133 50.1118 43.3231 50.4908 43.87 50.81 46.3311 49.2546 49.4855 49.3295 51.87 51 52.9853 50.3971 53.9495 49.5492 54.69 48.52 50.7759 45.2921 45.1617 45.1599 41.1 48.2 41.4605 48.7382 41.8797 49.2346 42.35 49.68Z">&nbsp;<path d="M53.62 70.73C50.5245 68.2923 49.3396 64.1452 50.68 60.44L49.9 60C48.6659 60.8439 47.0274 60.7913 45.85 59.87L45.21 60.23C45.6058 61.2919 45.8057 62.4168 45.8 63.55 45.7916 64.9665 45.449 66.3609 44.8 67.62 44.1758 68.8829 43.2607 69.9796 42.13 70.82 40.4793 72.0806 38.4462 72.7371 36.37 72.68 34.4016 72.6425 32.4961 71.9799 30.9291 70.7879 30.8521 70.7293 30.8462 70.7359 30.916 70.8031 32.7922 72.6091 35.2049 73.7558 37.79 74.07 41.5174 74.552 45.2597 73.2947 47.94 70.66 50.0873 72.7825 52.9273 74.0605 55.94 74.26L57.34 74.26C58.7773 74.1489 60.188 73.8114 61.52 73.26 62.7674 72.7051 63.9215 71.9605 64.9412 71.0527 64.9733 71.024 64.9684 71.0161 64.93 71.0356 63.94 71.5501 62.9183 72.001 61.871 72.3856 59.0158 73.226 55.9299 72.6068 53.62 70.73Z">&nbsp;<path d="M68.55 59.5C67.7139 55.2376 64.6626 51.7477 60.55 50.35 60.3 50.26 60.05 50.19 59.8 50.11 61.4994 43.7019 57.8231 37.0981 51.4811 35.1665 51.3763 35.1346 51.3734 35.1429 51.4744 35.1855 56.1812 37.1716 58.3867 42.5972 56.4006 47.304 55.1613 50.2409 52.4971 52.3328 49.35 52.84L49.35 54.12C50.561 54.689 51.3386 55.902 51.35 57.24L51.35 57.48 52.09 57.89C54.5508 54.7641 58.7317 53.5569 62.48 54.89 64.2417 55.5139 65.7655 56.6708 66.84 58.2 67.7378 59.4723 68.3064 60.9473 68.4949 62.4931 68.557 63.0693 68.571 63.6497 68.5367 64.2283 68.5359 64.2338 68.5397 64.239 68.5452 64.2398 68.5507 64.2406 68.5559 64.2368 68.5567 64.2313 68.6746 63.7214 68.7493 63.2025 68.78 62.68 68.8189 62.125 68.805 61.53 68.805 61.53 68.805 61.53 68.795 61.3 68.78 61.04 68.7377 60.5221 68.6608 60.0076 68.55 59.5Z">&nbsp;<path d="M38.45 54.48C40.4795 54.9084 42.2988 56.0247 43.6 57.64L44.44 57.17C44.4614 55.84 45.237 54.6377 46.44 54.07L46.44 52.8C44.6308 52.5011 42.9561 51.6568 41.64 50.38 40.0694 48.9514 39.0828 46.9924 38.87 44.88 38.4427 40.29 40.4836 37.1208 44.4335 35.1872 44.4793 35.1648 44.4767 35.1572 44.4272 35.1689 43.2117 35.5126 42.0621 36.0567 41.0258 36.7789 40.184 37.349 39.425 38.0325 38.77 38.81 36.071 41.862 35.0631 46.0547 36.08 50 31.4854 51.2185 28.0092 54.9831 27.16 59.66 27.06 60.17 26.98 60.86 26.95 61.17 26.9072 61.6657 26.9072 62.1643 26.95 62.66 26.9743 62.8751 26.99 63.01 27.04 63.32 27.11 63.8047 27.1965 64.2817 27.2776 64.7646 27.2948 64.8667 27.3036 64.866 27.2976 64.7626 27.2753 64.3947 27.234 63.5935 27.2599 63.0649 27.5103 57.964 31.8484 54.0319 36.9492 54.2823 37.4541 54.3071 37.956 54.3732 38.45 54.48Z">&nbsp;<path d="M51.41 12C50.3111 10.0836 47.8667 9.42084 45.9503 10.5197 45.3342 10.873 44.8233 11.3839 44.47 12L5.38 80C4.27543 81.9132 4.93093 84.3595 6.8441 85.4641 7.45209 85.8151 8.14176 85.9999 8.8438 86L87.0264 86C89.2355 85.9997 91.0262 84.2086 91.0259 81.9995 91.0258 81.2975 90.841 80.6079 90.49 80ZM87 84 8.8438 84C7.73923 83.9999 6.84386 83.1044 6.84394 81.9999 6.84397 81.6475 6.93706 81.3015 7.1138 80.9967L46.205 12.9949C46.3817 12.687 46.6371 12.4316 46.945 12.2549 47.2461 12.0803 47.5881 11.9886 47.9362 11.9892 48.6546 11.9898 49.3181 12.3739 49.6762 12.9967L88.7579 81C89.3103 81.9565 88.9826 83.1797 88.0261 83.7321 87.7144 83.9121 87.3599 84.0047 87 84Z">&nbsp;</path>
                                        </path>
                                    </path>
                                </path>
                            </path>
                        </path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">לתשומת לב המשתמשים באפליקציה, השימוש באפליקציה או בתכנים שמפורסמים בו או בתכנים שמפורסמים באפליקציות אחרות שהאפליקציה מקשרת אליהם,&nbsp;</span><u><span style="font-family:David;">עלול לחשוף אותם לסיכונים שכרוכים בשימוש באינטרנט</span></u><span style="font-family:David;">, כולל חדירה לטלפון הנייד, למחשב, חשיפה לתוכנות זדוניות או לווירוסים, וכן הלאה</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">השימוש והגלישה באפליקציה או עיון בתכנים המפורסמים בו או בתכנים המפורסמים באפליקציות חיצוניות שהאפליקציה מקשרת אליהן, מתבצעת רק באחריות המשתמשים. בעלי האפליקציה&nbsp;</span><u><span style="font-family:David;">ממליצים על התקנת תוכנות מספקות של אבטחה והגנה</span></u><span style="font-family:David;">, לפני הכניסה לאפליקציה או ביצוע שימוש בה</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בעלי האפליקציה&nbsp;</span><u><span style="font-family:David;">לא ימצאו אחראים לנזקים</span></u><span style="font-family:David;">&nbsp;מכל הסוגים, ישירים או עקיפים, שייגרמו למשתמשים כתוצאה משימוש באפליקציה</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="12" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:12pt; margin-right:18pt; page-break-inside:avoid; page-break-after:avoid; line-height:108%; font-family:David; font-size:12pt; font-weight:bold;">התניית שיפוט<span style="font-weight:normal;">&nbsp;</span><svg height="40.8" id="Icons_Gavel_M" width="40.8" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M68.083 32.749C69.2545 33.9207 71.154 33.9208 72.3256 32.7494 72.3258 32.7492 72.3259 32.7491 72.326 32.749L76.569 28.506 56.063 8 51.82 12.243C50.6489 13.4145 50.6489 15.3135 51.82 16.485L28.485 39.82C27.3135 38.6489 25.4145 38.6489 24.243 39.82L20 44.063 40.506 64.569 44.749 60.326C45.9207 59.1545 45.9208 57.255 44.7494 56.0834 44.7492 56.0832 44.7491 56.0831 44.749 56.083L53.588 47.245 80.528 74.185C82.0509 75.7082 84.5202 75.7085 86.0434 74.1856 86.0436 74.1854 86.0438 74.1852 86.044 74.185L86.185 74.044C87.7082 72.5211 87.7085 70.0518 86.1856 68.5286 86.1854 68.5284 86.1852 68.5282 86.185 68.528L59.244 41.588ZM53.234 13.657 56.063 10.828 73.74 28.506 70.912 31.334C70.5217 31.7247 69.8885 31.7251 69.4978 31.3348 69.4975 31.3345 69.4973 31.3343 69.497 31.334L68.083 29.92 68.083 29.92 53.941 15.778 53.941 15.778 53.234 15.071C52.8436 14.6805 52.8436 14.0475 53.234 13.657ZM43.334 58.912 40.506 61.74 22.828 44.063 25.657 41.234C26.0475 40.8436 26.6805 40.8436 27.071 41.234L28.485 42.648 28.485 42.648 41.921 56.083 41.921 56.083 43.335 57.5C43.724 57.8903 43.724 58.5217 43.335 58.912ZM43.334 54.669 29.9 41.234 53.234 17.9 53.234 17.9 66.669 31.334ZM84.771 69.943C85.5133 70.6847 85.5137 71.8877 84.772 72.63 84.7717 72.6303 84.7713 72.6307 84.771 72.631L84.631 72.771C83.889 73.513 82.686 73.513 81.944 72.771L55 45.83 57.83 43Z">&nbsp;<path d="M11.9 88 44.1 88C46.2528 87.9972 47.9972 86.2528 48 84.1L48 83.9C47.9972 81.7472 46.2528 80.0028 44.1 80L42 80 42 75 14 75 14 80 11.9 80C9.74723 80.0028 8.00275 81.7472 8 83.9L8 84.1C8.00275 86.2528 9.74723 87.9972 11.9 88ZM16 77 40 77 40 80 16 80ZM10 83.9C10 82.8507 10.8507 82 11.9 82L44.1 82C45.1493 82 46 82.8507 46 83.9L46 84.1C46 85.1493 45.1493 86 44.1 86L11.9 86C10.8507 86 10 85.1493 10 84.1Z">&nbsp;</path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">על מדיניות הפרטיות כפי שהיא מנוסחת במסמך זה,&nbsp;</span><u><span style="font-family:David;">חל הדין הישראלי</span></u><span style="font-family:David;">&nbsp;ויש לפרש אותה בהתאם. לבית המשפט המוסמך&nbsp;</span><u><span style="font-family:David;">במחוז מרכז</span></u><span style="font-family:David;">&nbsp;יש את הסמכות השיפוטית בכל נושא שנוגע למדיניות הפרטיות</span><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בכל מקרה בו בית המשפט המוסמך יקבע שהוראה כלשהיא מהוראות מדיניות הפרטיות מנוסחת באופן שאינו חוקי או תקף, או שכולה או חלקה אינה ניתנת לאכיפה, ובהתאם לקביעת בית המשפט המוסמך, אותה הוראה בלבד, או חלקה, בהתאם לעניין, תהיה בטלה, ולא יהיה בכך על מנת להשפיע על שאר הוראות מדיניות הפרטיות שיישארו בתוקף ויחייבו את המשתמשים</span><span style="font-family:David;" dir="ltr">.</span></p>
    <ol start="13" type="1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-top:12pt; margin-right:18pt; page-break-inside:avoid; page-break-after:avoid; line-height:108%; font-family:David; font-size:12pt; font-weight:bold;">שינוי ועדכון בהגדרות מדיניות הפרטיות<span style="font-weight:normal;">&nbsp;</span><svg height="34.4" id="Icons_SingleGear_M" width="34.4" xmlns="http://www.w3.org/2000/svg" style="overflow:hidden;" xmlns:xlink="http://www.w3.org/1999/xlink">&nbsp;<g id="Icons">&nbsp;<path d="M23.6 61.717 21.1 69.217 26.8 74.917 34.3 72.417C36.2897 73.5299 38.4045 74.4027 40.6 75.017L44.1 82.017 52.1 82.017 55.6 75.017C57.7698 74.4205 59.8537 73.5466 61.8 72.417L69.3 74.917 75 69.217 72.5 61.717C73.6124 59.7271 74.4852 57.6123 75.1 55.417L82.1 51.917 82.1 43.917 75 40.517C74.403 38.3473 73.5291 36.2635 72.4 34.317L74.9 26.817 69.2 21.117 61.7 23.617C59.7103 22.5041 57.5955 21.6313 55.4 21.017L52 14 44 14 40.5 21C38.3302 21.5965 36.2463 22.4704 34.3 23.6L26.8 21.1 21.1 26.8 23.6 34.3C22.4876 36.2899 21.6148 38.4047 21 40.6L14 44 14 52 21 55.5C21.5956 57.6755 22.4695 59.7651 23.6 61.717ZM16 45.264 21.874 42.41 22.691 42.01 22.93 41.134C23.5041 39.0905 24.3174 37.1219 25.353 35.269L25.774 34.503 25.498 33.673 23.388 27.344 27.341 23.39 33.668 25.5 34.523 25.785 35.303 25.333C37.0998 24.29 39.0237 23.4833 41.027 22.933L41.89 22.698 42.29 21.898 45.238 16 50.75 16 53.6 21.88 54 22.696 54.876 22.935C56.9187 23.51 58.8866 24.3236 60.739 25.359L61.506 25.781 62.336 25.504 68.663 23.394 72.616 27.348 70.506 33.677 70.221 34.532 70.673 35.311C71.7165 37.1082 72.5232 39.0329 73.073 41.037L73.314 41.92 74.139 42.315 80.1 45.172 80.1 50.679 74.205 53.627 73.405 54.027 73.17 54.889C72.5957 56.9324 71.7824 58.901 70.747 60.754L70.326 61.52 70.602 62.35 72.712 68.679 68.759 72.633 62.432 70.523 61.577 70.238 60.797 70.69C59 71.7332 57.0757 72.5399 55.072 73.09L54.21 73.325 53.81 74.125 50.862 80.025 45.338 80.025 42.391 74.125 41.991 73.325 41.128 73.09C39.0856 72.515 37.118 71.7014 35.266 70.666L34.499 70.244 33.669 70.521 27.342 72.631 23.389 68.677 25.5 62.35 25.784 61.495 25.333 60.715C24.2892 58.9179 23.4825 56.9933 22.933 54.989L22.697 54.127 21.897 53.727 16 50.779Z">&nbsp;<path d="M48 60.017C54.6274 60.017 60 54.6444 60 48.017 60 41.3896 54.6274 36.017 48 36.017 41.3726 36.017 36 41.3896 36 48.017 36.0209 54.6358 41.3812 59.9961 48 60.017ZM48 38.01C53.5228 38.01 58 42.4872 58 48.01 58 53.5328 53.5228 58.01 48 58.01 42.4772 58.01 38 53.5328 38 48.01 38.0072 42.4901 42.4801 38.0172 48 38.01Z">&nbsp;</path>
                    </path>
                </g>&nbsp;</svg></li>
    </ol>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">בעלי האפליקציה יכולים ועשויים לשנות, באופן של מחיקה, שינוי, הורדה, הסרה והוספה (להלן: &quot;השינוי&quot;), את מדיניות הפרטיות באפליקציה, מדי פעם ו</span><u><span style="font-family:David;">בהתאם לשיקול דעתם הבלעדי</span></u><span style="font-family:David;" dir="ltr">.</span></p>
    <p dir="rtl" style="margin-top:14pt; margin-bottom:14pt; text-align:justify; line-height:normal; font-size:12pt; background-color:#ffffff;"><span style="font-family:David;">השימוש באפליקציה או במערכותיה&nbsp;</span><u><span style="font-family:David;">כפוף למדיניות הפרטיות החדשה בעקבות השינוי</span></u><span style="font-family:David;">, ולכן יש לקרוא את המדיניות בכל פעם בה מתבצע שימוש באפליקציה</span><span style="font-family:David;" dir="ltr">.</span><span style="font-family:David;">&nbsp;</span><span style="font-family:David;">על משתמשי האפליקציה חלה האחריות להכיר את ההסכמים המעודכנים ולקרוא את ההסכמים מעת לעת.&nbsp;</span></p>
    
</div>
""",
                    unsafe_allow_html=True)


def _terms_of_service_3():
    cols = st.columns((4, 10, 4))
    with cols[1]:
        st.markdown("""
        <style type="text/css">
    .awlist1 {
        list-style: none;
        counter-reset: awlistcounter69_0
    }

    .awlist1>li:before {
        content: '('counter(awlistcounter69_0) ')';
        counter-increment: awlistcounter69_0
    }

    .awlist2 {
        list-style: none;
        counter-reset: awlistcounter14_0
    }

    .awlist2>li:before {
        content: counter(awlistcounter14_0) '.';
        counter-increment: awlistcounter14_0
    }

    .awlist3 {
        list-style: none;
        counter-reset: awlistcounter14_1
    }

    .awlist3>li:before {
        content: counter(awlistcounter14_0) '.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist4 {
        list-style: none;
        counter-reset: awlistcounter14_1 1
    }

    .awlist4>li:before {
        content: counter(awlistcounter14_0) '.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist5 {
        list-style: none;
        counter-reset: awlistcounter14_1 2
    }

    .awlist5>li:before {
        content: '1.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist6 {
        list-style: none;
        counter-reset: awlistcounter14_1 3
    }

    .awlist6>li:before {
        content: '1.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist7 {
        list-style: none;
        counter-reset: awlistcounter14_0 1
    }

    .awlist7>li:before {
        content: counter(awlistcounter14_0) '.';
        counter-increment: awlistcounter14_0
    }

    .awlist8 {
        list-style: none;
        counter-reset: awlistcounter14_1 1
    }

    .awlist8>li:before {
        content: '2.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist9 {
        list-style: none;
        counter-reset: awlistcounter14_1 2
    }

    .awlist9>li:before {
        content: '2.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist10 {
        list-style: none;
        counter-reset: awlistcounter14_0 2
    }

    .awlist10>li:before {
        content: counter(awlistcounter14_0) '.';
        counter-increment: awlistcounter14_0
    }

    .awlist11 {
        list-style: none;
        counter-reset: awlistcounter14_1 1
    }

    .awlist11>li:before {
        content: '3.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist12 {
        list-style: none;
        counter-reset: awlistcounter14_1 2
    }

    .awlist12>li:before {
        content: '3.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist13 {
        list-style: none;
        counter-reset: awlistcounter14_0 3
    }

    .awlist13>li:before {
        content: counter(awlistcounter14_0) '.';
        counter-increment: awlistcounter14_0
    }

    .awlist14 {
        list-style: none;
        counter-reset: awlistcounter14_1 2
    }

    .awlist14>li:before {
        content: '4.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist15 {
        list-style: none;
        counter-reset: awlistcounter14_0 4
    }

    .awlist15>li:before {
        content: counter(awlistcounter14_0) '.';
        counter-increment: awlistcounter14_0
    }

    .awlist16 {
        list-style: none;
        counter-reset: awlistcounter14_1
    }

    .awlist16>li:before {
        content: '5.'counter(awlistcounter14_1) '.';
        counter-increment: awlistcounter14_1
    }

    .awlist17 {
        list-style: none;
        counter-reset: awlistcounter40_0
    }

    .awlist17>li:before {
        content: counter(awlistcounter40_0) '.';
        counter-increment: awlistcounter40_0
    }

    .awlist18 {
        list-style: none;
        counter-reset: awlistcounter40_0 1
    }

    .awlist18>li:before {
        content: counter(awlistcounter40_0) '.';
        counter-increment: awlistcounter40_0
    }

    .awlist19 {
        list-style: none;
        counter-reset: awlistcounter40_0 2
    }

    .awlist19>li:before {
        content: counter(awlistcounter40_0) '.';
        counter-increment: awlistcounter40_0
    }

    .awlist20 {
        list-style: none;
        counter-reset: awlistcounter40_0 3
    }

    .awlist20>li:before {
        content: counter(awlistcounter40_0) '.';
        counter-increment: awlistcounter40_0
    }

    .awlist21 {
        list-style: none;
        counter-reset: awlistcounter40_1
    }

    .awlist21>li:before {
        content: counter(awlistcounter40_0) '.'counter(awlistcounter40_1) '.';
        counter-increment: awlistcounter40_1
    }

    .awlist22 {
        list-style: none;
        counter-reset: awlistcounter40_1 1
    }

    .awlist22>li:before {
        content: '4.'counter(awlistcounter40_1) '.';
        counter-increment: awlistcounter40_1
    }

    .awlist23 {
        list-style: none;
        counter-reset: awlistcounter40_1 2
    }

    .awlist23>li:before {
        content: '4.'counter(awlistcounter40_1) '.';
        counter-increment: awlistcounter40_1
    }
</style>
<div dir="rtl">
    <p dir="rtl" style="margin-top:0pt; margin-bottom:8pt; text-align:center; line-height:150%; font-size:12pt;"><img src="data:image/png;base64,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" width="536" height="260" alt=""></p>
    <p dir="rtl" style="margin-top:0pt; margin-bottom:8pt; text-align:justify; line-height:150%; font-size:12pt;"><span style="font-family:David;">משתמשים יקרים,</span></p>
    <p dir="rtl" style="margin-top:0pt; margin-bottom:8pt; text-align:justify; line-height:150%; font-size:12pt;"><span style="font-family:David;">המדד שמוצג לעיל משקף את&nbsp;</span><u><span style="font-family:David;">מידת ההגנה של האפליקציה על מידע המשתמש</span></u><span style="font-family:David;">&nbsp;בהתאם לארבע קטגוריות. כל קטגוריה מייצגת סיכון אחר אפשרי למידע המשתמש בהחלטה לבצע שימוש באפליקציה ומנוקדת בהתאם.</span><span style="font-family:David;">&nbsp;&nbsp;</span></p>
    <p dir="rtl" style="margin-top:0pt; margin-bottom:8pt; text-align:justify; line-height:150%; font-size:12pt;"><span style="font-family:David;">הקטגוריות ותתי הקטגוריות, הינן:</span><span style="font-family:David;">&nbsp;&nbsp;</span></p>
    <ol type="1" class="awlist1" style="margin:0pt; padding-right:0pt;">
        <li dir="rtl" style="margin-right:36pt; text-indent:-18pt; text-align:justify; line-height:150%; font-family:David; font-size:12pt;"><span style="width:4.64pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp;</span><strong>הודעה אפקטיבית</strong>: כוללת את מטרת השימוש במידע, מידת השקיפות של האפליקציה, נגישות ההסכמים, מתן אפשרות להעדפות פרטיות והפניות להסכמים אחרים.</li>
        <li dir="rtl" style="margin-right:36pt; text-indent:-18pt; text-align:justify; line-height:150%; font-family:David; font-size:12pt;"><span style="width:4.64pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp;</span><strong>הגנת מידע המשתמש</strong>: כוללת ביצוע עיבוד של המידע וקבלת החלטות אוטומטיות, פרופיילינג, מעקב אחר מידע המשתמש, העברת מידע לצדדים שלישיים ומתן זכויות בסיסיות למשתמשים.</li>
        <li dir="rtl" style="margin-right:36pt; text-indent:-18pt; text-align:justify; line-height:150%; font-family:David; font-size:12pt;"><span style="width:4.64pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp;</span><strong>אבטחת מידע המשתמש</strong>: עד כמה האפליקציה משתמשת באמצעי מיגון ואבטחה כדי למנוע פריצות אבטחה, מתקפות סייבר, סחר במידע, גניבת זהות המשתמש ועוד.</li>
        <li dir="rtl" style="margin-right:36pt; margin-bottom:8pt; text-indent:-18pt; text-align:justify; line-height:150%; font-family:David; font-size:12pt;"><span style="width:4.64pt; font:7pt 'Times New Roman'; display:inline-block;">&nbsp; &nbsp;</span><strong>זכויות צרכניות וחוזיות</strong>: הקטגוריה כוללת סעיף הסרת תוכן, סעיף סיום התקשרות, שינוי החוזה בצורה חד צדדית, הגבלת אחריות והגבלת פעולות משפטיות לרבות ברירת דין, ברירת מקום שיפוט ותנאי בוררות.</li>
    </ol>
    <p dir="rtl" style="margin-top:0pt; margin-bottom:8pt; text-align:justify; line-height:150%; font-size:12pt;"><span style="font-family:David;">הניקוד של האפליקציה ניתן על סמך שאלון אותו מילא&nbsp;</span><u><span style="font-family:David;">קצין הציות של האפליקציה</span></u><span style="font-family:David;">. תשובות החברה לשאלון וגם תנאי השימוש ומדיניות הפרטיות מצורפים לנוחיותכם. באמצעות השאלון ניתן לגבש החלטה מודעת ומושכלת האם להוריד את האפליקציה, מאחר וניתן להבין באמצעותו&nbsp;</span><strong><span style="font-family:David;">עד כמה הסיכונים השונים למידע מתממשים ביחס לחברה הספציפית</span></strong><span style="font-family:David;">.</span></p>
</div>
        """, unsafe_allow_html=True)

        with open("terms_of_service.html", "r", encoding='utf-8') as f:
            if not st.session_state.get("downloaded_terms_of_service"):
                st.session_state.downloaded_terms_of_service = False
            if st.download_button("למעבר לתנאי השימוש ומדיניות הפרטיות",
                                  data=f,
                                  file_name="תנאי שימוש.html"):
                st.session_state.downloaded_terms_of_service = True
            if st.session_state.downloaded_terms_of_service:
                print("Downloaded")

        with open("quiz.html", "r", encoding='utf-8') as f:
            if not st.session_state.get("downloaded_quiz"):
                st.session_state.downloaded_quiz = False
            if st.download_button("למעבר לשאלון גילוי נאות",
                                  data=f,
                                  file_name="שאלון פרטיות.html"):
                st.session_state.downloaded_quiz = True
            if st.session_state.downloaded_quiz:
                print("Downloaded")
