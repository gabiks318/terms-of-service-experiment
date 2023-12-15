import json
import random
import time
import uuid

import requests
import streamlit as st


def start_timer(page_num: int):
    st.session_state[f"page_{page_num}_timer"] = time.time()


def next_page(page_num: int):
    time_taken = time.time() - st.session_state[f"page_{page_num}_timer"]
    st.session_state[f"page_{page_num}_time_taken"] = time_taken
    print(f"Page {page_num} took {time_taken} seconds")
    st.session_state.page_num = page_num + 1


def landing_page():
    start_timer(1)
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
        </style>
        """, unsafe_allow_html=True
    )
    desc = "לפני תחילת שנת הלימודים החדשה ולקראת פתיחת חלונות הזמן לבניית מערכת, אנו מוצאים את עצמנו כל שנה משקיעים זמן רב במעבר על קורסי הבחירה השונים כדי לבנות את מערכת השעות האידיאלית. תכנונידע תחסוך לך זמן ותבנה עבורך מערכת אידיאלית במהירות ובקלות בהתאם לתחומי העניין שלך, מטלות מועדפות, חובת נוכחות בקורסים ושעות נוחות."
    start_timer(0)
    st.title("תכנונידע – לבניית מערכת שעות בשניות!")
    cols = st.columns((4, 10, 4))
    with cols[1]:
        st.write(desc)
        st.button("המשך", on_click=next_page, args=(1,))


def description_page():
    start_timer(2)

    initial_desc = "לאחר הורדת האפליקציה, ההתחברות אליה תעשה דרך חשבון המשתמש שלך בפייסבוק, גוגל או אפל. בהמשך לכך עליך להזין את שם המוסד האקדמי בו את/ה לומד/ת, החוג/הפקולטה, פרטי גיליון הציונים, גיל, כתובת, תחומי העניין שלך במסגרת התחום אותו את/ה לומד/ת, מטלות מועדפות בקורס ומגבלות אישיות (לרבות עבודה, התנדבויות, ילדים וחיי משפחה). בהתאם לנתונים שהזנת לאפליקציה ומידע נוסף מפרופיל המשתמש שבאמצעותו התחברת לאפליקציה, יוצגו בעבורך מספר אפשרויות של מערכות שעות אשר לוקחות בחשבון את כלל הנתונים. כל שנותר לך הוא רק לבחור את מערכת השעות המתאימה ביותר עבורך.  "

    desc = f"""
        {initial_desc}
        - האפליקציה מעודכנת בזמן אמת בהתאם להיצע הקורסים העדכני ביותר בכל מוסדות הלימוד האקדמיים בישראל, אך היא אינה ספק שירותים רשמי מטעם המוסדות האקדמיים. 
        - השימוש באפליקציה הוא ללא תשלום, כאשר לאורך שנת הלימודים נשתמש במידע שמסרת לנו כדי להציע לך שירותים שונים בתשלום מטעמנו או מטעם שותפינו העסקיים. 
    """
    st.title("קצת על האפליקציה")
    cols = st.columns((4, 10, 4))
    with cols[1]:
        st.markdown(desc)
        st.button("המשך", on_click=next_page, args=(2,))
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


def _terms_of_service_1():
    # st.markdown(
    #     """
    #     <style>
    #
    #         h1:nth-of-type(1)
    #         {
    #             text-align: center;
    #             direction: rtl;
    #         }
    #         p
    #         {
    #             direction: rtl;
    #         }
    #         li{
    #             direction: rtl;
    #             padding: 0!important;
    #             text-align: right;
    #         }
    #         label{
    #             direction: rtl;
    #         }
    #
    #     </style>
    #     """, unsafe_allow_html=True
    # )
    st.title("תנאי שימוש")
    cols = st.columns((4, 10, 4))
    with cols[1]:
        st.markdown("""
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">חשוב להקפיד לקרוא היטב את תנאי השימוש לפני השימוש באפליקציה, היות וכל שימוש כפוף למדיניות הפרטיות, תנאי השימוש והוראות הדין הרלוונטי. הגלישה והשימוש באפליקציה פירושם הסכמתכם לאמור בתנאי השימוש ובמסמך מדיניות הפרטיות, ואם קיים תנאי כלשהו במסמכים אלו שנוגדים את הסכמתכם, אתם מתבקשים להימנע מגלישה ושימוש.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">ההקדמה לתנאי השימוש היא חלק בלתי נפרד מהמסמך, ותנאי השימוש הם בבחינת הסכם משפטי מחייב בין כל גולש שמשתמש בשירות לבין בעלי השירות, כלומר, הוא אינו מהווה הסכם שפועל לטובת צד ג&apos; כלשהו.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">לשון רבים ויחיד.&nbsp;</span></strong><span style="font-size:12pt;">בכל מקום שבו תנאי השימוש נכתבים בלשון רבים, הוראות התנאים חלות גם על יחידים, ולהיפך.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">לשון זכר ונקבה.&nbsp;</span></strong><span style="font-size:12pt;">בכל מקום בתנאי השימוש, בו הנוסח נכתב בלשון זכר, התנאים חלים גם על נשים, והניסוח מופיע בלשון זכר רק מטעמי נוחות.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">הכותרות הראשיות והמשניות של תנאי השימוש.&nbsp;</span></strong><span style="font-size:12pt;">מופיעות לשם ניווט קל בתנאי השימוש, ואינם מהווים פרשנויות.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">שימוש באפליקציה ותנאי המדיניות</span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בשילוב עם מדיניות הפרטיות של האפליקציה, תנאי השימוש מהווים את הבסיס לגלישה ושימוש באפליקציה. כל שימוש באפליקציה באופן שאינו מצוין במפורש בתנאי שימוש אלה ומופיע בהם, מותנה וכפוף אף להסכמת המשתמשים למדיניות הפרטיות של האפליקציה, בנוסח המלא שלה, כפי שהוא מופיע במדיניות פרטיות של האפליקציה.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">מסירת מידע ופרטים אישיים</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="בייסבול קו מיתאר" src="https://lh7-us.googleusercontent.com/-pUgLihGJ3KFDt6Db6KsnUd-KRrwX75YiQgA62OYRlzAl20EcUhb-2mbdZ8_zl1egSl4fbgpmEDF-UW6G54N_FdrhjbRx3p7hJgv1_47uj6RWbeI-Nr2TScdBjjMEU1bqZrkLXOkzFIJlOOvuux5TJv1YkBEpJ4K" width="39" height="39"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">השימוש באפליקציה יהיה כרוך&nbsp;</span><u><span style="font-size:12pt;">במסירת פרטים אישיים</span></u><span style="font-size:12pt;">. חשוב להבין שהחוק אינו מחייב את המשתמשים באפליקציה למסור את המידע האישי שלהם או את פרטיהם, ומסירת כל מידע אישי מתבצעת רק בהתאם לרצון חופשי והסכמה אישית.</span></p>
<p dir="rtl" style="text-align: justify;"><u><span style="font-size:12pt;">מסירת פרטים חלקיים או שאינם נכונים</span></u><span style="font-size:12pt;">&nbsp;היא התנהלות שעלולה למנוע את האפשרות להשתמש בחלק משירותי האפליקציה או להשלים את תהליך הרישום ובכך לפגוע באפשרות לקבל את השירות המוצע על ידי האפליקציה או לפגוע באיכות השירות הניתן, כמו גם פגיעה באפשרות ליצור קשר עם המשתמשים בהתאם לצורך.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">גביית תשלומים</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="העברה1 קו מיתאר" src="https://lh7-us.googleusercontent.com/19a6ssAjrcpUSYEGVqekOtrpUR9nDOFxY8qu3Y621yCn2zfnpVndBVa76f0T-wxH5e2lMjA8kq0s_qn7gGURi50TQOKKFImnfUKPpA34EujrVDyrQ-lG4PmGV1OjYW3jwbiXg1WSrpIDTEjLMMbbNZYuYP93z3s5" width="50" height="50"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">השימוש באפליקציה&nbsp;</span><u><span style="font-size:12pt;">ללא תשלום</span></u><span style="font-size:12pt;">. אולם, האפליקציה שומרת לעצמה את הזכות להציע למשתמש שירותים שונים בתשלום מטעמה או מטעם שותפיה העסקיים.&nbsp;</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">האפליקציה שומרת לעצמה את הזכות לגבות תשלומים עבור שימוש באפליקציה, בתנאי שגביית התשלומים תאושר מראש על ידי המשתמשים ותלווה בהודעה מוקדמת מראש.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">שינויים, תוספות ועדכונים בהגדרות תנאי השימוש&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="גלגל שיניים יחיד קו מיתאר" src="https://lh7-us.googleusercontent.com/gZSnA4w9szlTyJxiHOfJ3olUSNmFcKLHaGp0iU_MZ_I15vLrVdN_HHmqmEGRwDQBv49QXT0Ne5TCWq4G_TephgEedx1zAgsrJP12m4rMXmLWH6eiD-1Bll4mHLIaMemDZrhjCXjM1GID_B-KD9qGEoEWzVoZE92_" width="32" height="32"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מפעיל השירות רשאי&nbsp;</span><u><span style="font-size:12pt;">לשנות, להסיר, למחוק, להוריד, לעדכן או להוסיף תנאי שימוש</span></u><span style="font-size:12pt;">&nbsp;למסמך זה, בהתאם לשיקול דעתו הבלעדי, בזמנים שונים ובכפוף להוראות הדין.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">השימוש באפליקציה או במערכות המופיעות בה יהיה כפוף לתנאים החלים לאחר העדכונים, השינויים והתוספות, ולכן&nbsp;</span><u><span style="font-size:12pt;">על המשתמשים לקרוא היטב את תנאי השימוש לפני השימוש באפליקציה</span></u><span style="font-size:12pt;">.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">רישום לאפליקציה &nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="לוח קו מיתאר" src="https://lh7-us.googleusercontent.com/y63HBezwKCe5Xuiy-YR1It8rBSrK6r5tHrLwoBW1aqnMnzuHs8KDhbKwt_ZiuwJhVfaMrxsRg-DCsPDL_T5q67OcsAexRVHciCawDeazsVpt9bo7aq2AeJLYQWslTqfLhtg5AorbddOUJExARs-aNBgZopK2QNLd" width="38" height="38"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">כדי להירשם לשימוש באפליקציה, יש לסמן את תיבות הסימון המתאימות ולהקליק על הכפתור לאישור. מילוי הפרטים האישיים וסימון התיבות הרלוונטיות בתהליך הבקשה, עם לחיצה על כפתור האישור בסיום, פירושה אישור המשתמשים שקראו את תנאי השימוש, הוראות תהליך ההרשמה ואת מסמך מדיניות הפרטיות, ושהם מסכימים לתנאים לאחר שקראו והבינו את כל האמור בהם.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">המשתמשים באפליקציה מצהירים שהם מודעים לכך שאחריותם היא לספק את כל המידע הנדרש כדי לקבל את המוצרים.&nbsp;</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">שימוש פוגעני בתכני האפליקציה&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="אסור להשתמש בטלפון קו מיתאר" src="https://lh7-us.googleusercontent.com/WM18PWqoyjM6MByqXg1C7R6JYIhTxF0kpuLLwHM1c0JSkxbypEMBHfdAe0ip765aOUqdSntgxQJGtgR4AjeW0lW_FWZriiWsRhhjPSa6lHrv5eqf1FbQLWjY5GvvlHmJ3PwCCrwkQ96dMcKCmDO0QJcU8HxycGss" width="34" height="34"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">חל&nbsp;</span><u><span style="font-size:12pt;">איסור על העלאת מידע או תכנים</span></u><span style="font-size:12pt;">&nbsp;שיש בהם את המאפיינים הבאים:</span></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">שיבוש, הפרעה, הגבלה או מניעת השימוש באפליקציה הן לבעלי האפליקציה או למשתמשים אחרים;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מידע מעליב;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מידע פוגעני או שעלול להוות חומר פוגעני;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מידע משמיץ או וולגרי;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מידע שיש בו הוצאת דיבה;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">רישום צדדים שלישיים או פתיחת סיסמאות וחשבונות בשמם ועבורם;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">העלאה או פרסום מידע או תכנים שקריים, שאינם מדויקים; מטעים או מסולפים;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מידע שיש בו איומים;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מידע פורנוגרפי;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">או כל מידע אסור לשימוש או לפרסום.</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">חל&nbsp;</span><u><span style="font-size:12pt;">איסור על העלאת מידע או תכנים שיש בהם בבחינת נזק</span></u><span style="font-size:12pt;">&nbsp;לאפליקציה, למשתמשים בו, כמו למשל שורות קוד; תוכנות מזיקות; &apos;סוס טרויאני&apos;; החדרת וירוסים שונים; או כל תוכנה אחרת שיש בה על מנת לפגוע בהתנהלות התקינה של האפליקציה והשימוש בו, או ההתנהלות והשימוש באפליקציה למשתמשים אחרים, כמו גם נזק למשתמשים ולאפליקציה, או למחשבים ולציוד.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">חל&nbsp;</span><u><span style="font-size:12pt;">איסור גם על עזרה או שידול</span></u><span style="font-size:12pt;">&nbsp;לאחרים שמבקשים להתנהל או לבצע פעולה אסורה באפליקציה, מכל סוג שהוא, כולל הפעילויות האסורות המפורטות בתנאי השימוש.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">תכנים לעיל&nbsp;</span><u><span style="font-size:12pt;">יוסרו מהאפליקציה</span></u><span style="font-size:12pt;">&nbsp;ואף יש בהם כדי להביא להסרת חשבון המשתמש והפסקת ההתקשרות עימו.&nbsp;</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">מניעת השימוש באפליקציה&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="סימן איסור קו מיתאר" src="https://lh7-us.googleusercontent.com/z3wVDuxEGzuGBGMN0FshGwnvXIw2MPa5nGmkXAcOtUj_0O6_hfr9SCjJwYfK-lJyFbMqOBhtSHbHBy8GUNxVXg97zFoJPJnBydYTKRVyvK3FPuZe-9OoG0onvWzfkfqBwre-441d6zEhKwYQNkLrDKZJoclAP7sB" width="38" height="38"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מבלי לגרוע מהאמור בסעיפי תנאי השימוש, החברה יכולה&nbsp;</span><u><span style="font-size:12pt;">למנוע שימוש באפליקציה</span></u><span style="font-size:12pt;">&nbsp;למשתמשים רשומים או שאינם רשומים, או לכלל הציבור, בכל אחד מהמקרים הבאים:</span></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">תנאי השימוש באפליקציה הופרו.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בוצע מחדל או פעילות שיש בהם פגיעה באפליקציה, בבעלי האפליקציה, במידע שמצוי בידי החברה; בציוד החברה; או במשתמשים אחרים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">המשתמשים מסרו פרטים חסרים, שגויים או שקריים.</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">הסרת תכני המשתמש וסיום התקשרות</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="אסור להשתמש בטלפון קו מיתאר" src="https://lh7-us.googleusercontent.com/WM18PWqoyjM6MByqXg1C7R6JYIhTxF0kpuLLwHM1c0JSkxbypEMBHfdAe0ip765aOUqdSntgxQJGtgR4AjeW0lW_FWZriiWsRhhjPSa6lHrv5eqf1FbQLWjY5GvvlHmJ3PwCCrwkQ96dMcKCmDO0QJcU8HxycGss" width="34" height="34"></span></span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="סימן איסור קו מיתאר" src="https://lh7-us.googleusercontent.com/z3wVDuxEGzuGBGMN0FshGwnvXIw2MPa5nGmkXAcOtUj_0O6_hfr9SCjJwYfK-lJyFbMqOBhtSHbHBy8GUNxVXg97zFoJPJnBydYTKRVyvK3FPuZe-9OoG0onvWzfkfqBwre-441d6zEhKwYQNkLrDKZJoclAP7sB" width="38" height="38"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">האפליקציה שומרת לעצמה את הזכות&nbsp;</span><u><span style="font-size:12pt;">להסיר תוכן</span></u><span style="font-size:12pt;">&nbsp;שהמשתמשים הזינו במסגרת הרישום לאפליקציה ואף&nbsp;</span><u><span style="font-size:12pt;">להפסיק את ההתקשרות</span></u><span style="font-size:12pt;">&nbsp;עם המשתמש במיידי וללא כל פירוט מצידה, בכל אחד מהמקרים הבאים:&nbsp;</span></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">המשתמש הפר את תנאי השימוש ומדיניות הפרטיות.&nbsp;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">המשתמש הכניס תוכן לא נכון, לא חוקי או פוגעני.&nbsp;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מכל סיבה נוספת שנראית לבעלי האפליקציה מהותית ופוגעת בשירות במפעיליו, במשתמש, בצדדים שלישיים ובמשתמשים אחרים.&nbsp;</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">הפסקת פעילות האפליקציה</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="יד מורמת קו מיתאר" src="https://lh7-us.googleusercontent.com/AjZLCChtZVw1IT8XegObjtic5Fa1Zxzq-5eusDO3lP3LEtV-fwJv3KtawIThYSce_S605g3SZgigj4_ZMfEP3HXjPVfa6P9j9f6mYSTf9kfKueJ3vU30vsjOyTOJTjHSn_SrPi81P_2aQl1qFnmmqNnHmHLsSxJL" width="40" height="40"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">לנותן השירות יש את הזכות להפסיק חלק מפעילות האפליקציה או את כל הפעילות לפרק זמן קצר, זמני, ארוך או לתמיד, כולל הפסקת מתן שירותים, באופן חלקי או מלא, כמו גם הגבלת או הפחתת מתן השירותים, ללא הודעה מוקדמת מראש.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">הגבלת אחריות</span></strong><span style="font-size:11pt;">&nbsp;</span><span style="font-size:11pt;"><span style="border:none;"><img alt="הגבלת אחריות בהסכם שמירה וביטוח רכוש" src="https://lh7-us.googleusercontent.com/OPLxnAuAGUm_9r9cab1azf03cO7HzrmpmdpUAKDODMEAuyXQ17TIeYhf7019f0rOcRVZfYmAbr6heIRUkoEXWHf07fNH7L0jywbRApgn3AHeMZ_2yS_UVXALvEOaU0oIlYGJD8MoRBjOdho3SlnlgZSq7_XbilHu" width="52" height="41"></span></span></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בעלי האפליקציה&nbsp;</span><u><span style="font-size:12pt;">אינם אחראים</span></u><span style="font-size:12pt;">&nbsp;לנזקים ישירים או עקיפים מכל סוג שהוא, שייגרמו למשתמשים או למי מטעמם, בכל מקרה בו מידע אישי כלשהו יאבד או יגיע לגורמים עוינים, או שיתבצע בו שימוש כלשהו שאינו בהרשאה.</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><br></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בכל מקום בתנאי השימוש בו משתמע או נכתב במפורש שנותן השירות יחליט על ענין כלשהו, יבצע פעולה מסוימת או יקבע דבר מסוים, לנותן השירות מוקנית באופן מפורש או מכללא הסמכות, הזכות או שיקול הדעת הבלעדי לפעול, לבצע, או להחליט לא לפעול, בהתאם לשיקול דעתו הבלעדי מבלי שתחול עליו חובת הנמקה.</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">התנהלות נותן השירות לא תהיה ניתנת לערעור ותיחשב לסופית, באופן שלמשתמשים לא תהיה אפשרות לטעון נגד השירות, לתבוע אותו, או להביע דרישה הנוגעת לפעילותו או הימנעות מפעילות, כפי שנאמר.</span></p>
<p dir="rtl" style="text-align: justify;"><br></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">המשתמשים באפליקציה מצהירים שלבעלי האפליקציה יש&nbsp;</span><u><span style="font-size:12pt;">זכות והרשאה להשתמש במידע</span></u><span style="font-size:12pt;">, כפי שמונח זה מוגדר במדיניות הפרטיות, בהתאם למדיניות הפרטיות. נותן השירות אינו אחראי לכל נזק מכל סוג שהוא, שנגרמו כתוצאה ממקרים שנובעים מהעברת הפרטים לספק, או כתוצאה ממקרים שאינם בשליטתו, או כתוצאה מאובדן המידע, או כתוצאה ממקרים שמוגדרים בבחינת כוח עליון.</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><br></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">למרות שבעלי האפליקציה נוקטים בכל המאמצים לפרסום תכנים ומידע נכונים, אמינים ומדויקים, עדיין&nbsp;</span><u><span style="font-size:12pt;">עשויים להופיע אי דיוקים או להתפרסם שגיאות בתכנים</span></u><span style="font-size:12pt;">, כולל שיבוש במידע. בעלי האפליקציה אינם אחראים לשום נזק, משום סוג, שייגרם למשתמשים כתוצאה מפרסום התכנים והמידע.</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בכל מקרה בו המשתמשים אינם מרוצים מהאפליקציה, האפשרות הבלעדית והיחידה שעומדת לרשותם היא&nbsp;</span><u><span style="font-size:12pt;">הפסקת השימוש באפליקציה</span></u><span style="font-size:12pt;">.</span></p>
<p dir="rtl" style="text-align: justify;"><br></p>
<p dir="rtl" style="text-align: justify;"><br></p>
<p dir="rtl" style="text-align: justify;"><br></p>
<p dir="rtl" style="text-align: justify;"><br></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">שינויים ושדרוגים באפליקציה</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="רולר צבע קו מיתאר" src="https://lh7-us.googleusercontent.com/72NcO_oVxuLYO4VIhfWzCb5GUA9LYi42Sv_1NCt36dulr5LyBS0q7RiuHq9vWtyTau7SDkjJb4jjaO12gDoIS5RCOTs5k2Agc8sThVW0LzPiJKMZ0rocq_tEZ7KvpXyAU1g-F-Meqg7_prJmiwS2-eBDbSk6cDM8" width="30" height="30"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">לבעלי האפליקציה יש את הזכות, בהתאם לשיקול דעתם הבלעדי, לבצע פעולות שדרוג, ריענון או תחזוקה לאפליקציה, כולל שינויי עיצוב או כל התנהלות אחרת שעשויה למנוע מהמשתמשים את הגישה לאפליקציה.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">קישורים באפליקציה ומידע שמגיע מצדדים שלישיים</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="קישור קו מיתאר" src="https://lh7-us.googleusercontent.com/CF9NTw2QtWoFOh-fH34yRAGFaXGy6eLNDRyJYK3R4TMzK3_ZTZwhuukFex20icmKLH71c--h_FwD5QvOQ1DQ2CIiP65smELMgr1ma90Mh3-AFsYN-nZ_4ujM4uULdQiJe8hsBjlcWhlPbRgHJj71Y1j1Ks5uEj5N" width="25" height="25"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">באפליקציה מופיעים קישורים שמפנים לאפליקציות חיצוניות, וחלק מהמידע המפורסם באפליקציה מבוסס&nbsp;</span><u><span style="font-size:12pt;">על מידע שמגיע מצדדים שלישיים</span></u><span style="font-size:12pt;">, כמו למשל ממוסדות אקדמיים.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בעלי האפליקציה&nbsp;</span><u><span style="font-size:12pt;">אינם ערבים</span></u><span style="font-size:12pt;">&nbsp;לכם שהמידע שנמצא אצל צדדים שלישיים הוא מדויק ואמין, והמשתמשים מצהירים שהם מודעים לעובדה זו ומבינים את השלכותיה. בעלי האפליקציה&nbsp;</span><u><span style="font-size:12pt;">לא יימצאו אחראים</span></u><span style="font-size:12pt;">&nbsp;לכל נזק מכל סוג שהוא שייגרם למשתמשים כתוצאה מהסתמכות על המידע המופיע באפליקציה.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">משלוח הודעות</span></strong><span style="font-size:12pt;"><span style="border:none;"><img alt="דואר אלקטרוני קו מיתאר" src="https://lh7-us.googleusercontent.com/tBxPe5fFnaJod8A-M7XtuETdmzfvH-NvTt8FuDy-IOMeLLmDfkTN91mqWoOhVdPsUaicz9j9CIw20Zbd9IklDjq-JctH6YVtiqjnZo0zKuu9QfWuun2QWO5FJ6bfkmLAlCpU1IzNV1_BmPKhOZjKqQcgivcDkkRN" width="31" height="31"></span></span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בעלי האפליקציה יכולים לשלוח הודעות לכתובת הדואר האלקטרוני או לכתובת הדואר שהמשתמשים מסרו במהלך הרישום לאפליקציה והמשתמשים יכולים ליצור קשר עם בעלי האפליקציה בעמוד יצירת הקשר.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">כל הודעה שיש לשלוח מצד אחד שני, למעט אם צוין אחרת בתנאי השימוש, תתבצע באמצעות דואר האלקטרוני. אם ההודעה נשלחה לבעלי האפליקציה, היא תיחשב שנתקבלה רק אם בוצע אישור מסירה על קבלת ההודעה.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">התניית שיפוט&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="פטיש יושב-ראש קו מיתאר" src="https://lh7-us.googleusercontent.com/tQATvXMGZnUI63gASpJQKYFPRZ0aF9yKPMitKcUaPorudDfbpVdNIH_CfpC82R9EU6partXnNmLAho_CE0J1OwlEqeY1P4vwpX-KPOK6GB3-a5zmydS0O6yhX6Fk_M615kAwkwKh8QhjYKTMOIL3MyZ9ZGz4Kv6x" width="41" height="41"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">הדין שחל על אפליקציה או על כל נושא ועניין שקשורים אליו, כולל תנאי שימוש אלה, וכל מקרה של סכסוך משפטי ישיר או עקיף לאפליקציה או לשימוש בו, הוא&nbsp;</span><u><span style="font-size:12pt;">הדין הישראלי בלבד</span></u><span style="font-size:12pt;">.</span></p>
<p><span style="font-size:12pt;">הסמכות הבלעדית והייחודית לדון בכל סכסוך או מחלוקת משפטית, שקשורים באופן ישיר או עקיף לאפליקציה או לשימוש בו, היא הסמכות של בית המשפט המוסמך&nbsp;</span><u><span style="font-size:12pt;">במחוז מרכז</span></u><span style="font-size:12pt;">, ולא לכל ערכאה שיפוטית אחרת.</span></p>""",
                    unsafe_allow_html=True)


def _terms_of_service_2():

    st.title("תנאי שימוש")
    cols = st.columns((4, 10, 4))
    with cols[1]:
        st.markdown("""
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">יש לקרוא היטב את המסמך, שמתאר את מדיניות הפרטיות באפליקציה, שמהווה חלק בלתי נפרד ממסמך תנאי השימוש באפליקציה.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מדיניות הפרטיות, כפי שהיא מופיעה במסמך זה חלה על כל שימוש, גלישה או צפייה באפליקציה, בכל ומכל אמצעי תקשורת. בכל מקרה בו המשתמשים אינם מסכימים לתנאי מתנאי מדיניות הפרטיות, עליהם להפסיק מידית את השימוש או הגלישה באפליקציה.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">אופן הניסוח במדיניות הפרטיות מנוסח בלשון זכר רק מטעמי נוחות, אך הוא מופנה כלפי גברים ונשים. כמו כן, בכל מקום במסמך בו הניסוח נכתב בלשון יחיד, הוא מופנה גם כלפי רבים, ולהיפך.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">מסירת פרטים אישיים&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="פנקס כתובות קו מיתאר" src="https://lh7-us.googleusercontent.com/Y58NIr2HgrLraa1e5evFJ4v-d5ebFqqZ6JhEsU9fM7OxbizJj8jcv2saEsdjGvgm6XIDYfrb-L9dYss-CtxVN6w34aJQeiyJyjLjthkfBZPKAXlIrad_2WN6R21aOzUtIAafwfA0RK6pxERhB5oOJsBwOWkidbCt" width="36" height="36"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">השירות שמוצע באמצעות האפליקציה, קרי בניית מערכת שעות מותאמת אישית, כרוך&nbsp;</span><u><span style="font-size:12pt;">במסירת פרטים ומידע אישי&nbsp;</span></u><span style="font-size:12pt;">(להלן: &quot;המידע&quot;), כמו למשל:</span></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">גיל.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">שם מלא.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">כתובת מגורים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">פרטי גיליון הציונים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">כתובת דואר אלקטרוני.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מגבלות אישיות (לרבות עבודה, התנדבויות, ילדים וחיי משפחה).</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">או כל מידע אישי או מזהה אחר.</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בהתאם לחוק, יודגש שהמשתמשים אינם חייבים למסור מידע ופרטים אישיים, ומסירת פרטים אלו תלויה רק&nbsp;</span><u><span style="font-size:12pt;">ברצונם החופשי והסכמתם</span></u><span style="font-size:12pt;">.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בהתאם, לא חלה על המשתמשים חובת הסכמה לאיסוף, מסירת או הפקת המידע שנמסר על ידם, ובכל פעם שהם משתמשים באפליקציה, הם מביעים את הסכמתם מרצונם לשימוש במלוא המידע, מסירתו או העברתו, כפי שמפורט במדיניות הפרטיות.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">יחד עם זאת, מסירת פרטים חלקיים, שגויים או שקריים, עלולה למנוע מהמשתמשים את האפשרות להשתמש בחלק משירותי האפליקציה או בכולם, או להשלים את תהליך הרישום, ובכך לפגוע באיכות השירות שהמשתמשים מקבלים.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">מטרת איסוף המידע&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="פגיעה במטרה קו מיתאר" src="https://lh7-us.googleusercontent.com/G0aLQlvxn7yn53ll5sRwD8RLTc7JzqaFexKuT_2GR5bszULWq-S0RUKle6oq5rvzBm1_hRsNfkEtvnFfOmYxuo7goaKJXNuvegS4tUzkBBmKP-N7FMorRLgyXqShoP0EkYQ1HTa29T3fPN04_d_dXI36nYCZuqDF" width="34" height="34"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">האיסוף של המידע נעשה&nbsp;</span><u><span style="font-size:12pt;">כדי לבנות למשתמש את מערכת השעות האידיאלית</span></u><span style="font-size:12pt;">&nbsp;עבורו אשר מותאמת לצרכיו האישיים בהתאם למידע שמסר.&nbsp;</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">כמו כן, המשתמשים באפליקציה מסכימים שבעלי האפליקציה יאספו את המידע ויפיקו אותו, כולל ביצוע שימוש בו, על מנת לאפשר שימוש באפליקציה, למטרות הבאות:</span></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בניית מערכת שעות.&nbsp;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">תיעדוף פרסומות.&nbsp;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">שיפור חווית השירות.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">יצירת התאמות אישיות.&nbsp;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">יצירת קשר.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">אימות פרטים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">שליחת עדכונים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">פניה וזיהוי.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מתן שירותים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">עיבוד מידע.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מחקר סטטיסטי ופילוח.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">פרסום ושיווק.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מטרות עסקיות.</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בעלי האפליקציה רשאים גם להשתמש במידע האישי למטרות גילוי, מסירה או מכירת המידע לצדדים שלישיים, בארץ או בחו&quot;ל.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">שמירה ואיסוף של מידע המשתמש&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="מחשב קו מיתאר" src="https://lh7-us.googleusercontent.com/YNnPE7qw0UNedTNsbQMNnO7pssvn29CbeVAoBN3llZhCtSlyMmTvPJrQNVlISeJpZM1RrgbnROIalaZ0jgvphwSTdDVUVgCQZ9Zdu9NyIZq9rkd4qrZrE_Sm5l_40m1syjjQezX2EoPsc08jKcjUDvbWC5daHMjA" width="38" height="38"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">המשתמשים&nbsp;</span><u><span style="font-size:12pt;">מביעים את הסכמתם לכך שבעלי האפליקציה יאספו את המידע האישי וישמרו אותו</span></u><span style="font-size:12pt;">, כפי שהוא נמסר במהלך שימוש המשתמשים באפליקציה, בין אם המידע נמסר ישירות על ידי המשתמשים או התקבל בעקיפין. בין היתר, המידע שנאסף ונשמר כולל:</span></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">היסטוריית גלישה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">פרסומות שהמשתמשים נחשפו אליהן שמופיעות באפליקציה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מידע שהמשתמשים קראו באפליקציה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מיקום.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">צפייה בעמודים השונים באפליקציה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">או כל מידע אחר שנמסר על ידי המשתמשים.</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">כל המידע והפרטים האישיים, כפי שהם נמסרו על ידי המשתמשים,&nbsp;</span><u><span style="font-size:12pt;">יישמרו במאגרי המידע של בעלי האפליקציה</span></u><span style="font-size:12pt;">.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">העברת מידע לצדדים שלישיים&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="מחזור עם אנשים קו מיתאר" src="https://lh7-us.googleusercontent.com/7oIxKNqUsRR5y7x4Ao9IWO3P7xpEyYnqTSDGQ77csb9hdnptO1xvNYKJXTXz08wOC_GV2W3N-a8D4atHPMOR8NB185UAtdI0-dLio_s4Jej60IRtggB6JSy2ZZM331Zfc9wGAhICf0DBeg77q7hkuWUxzVxLxvyT" width="45" height="45"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">לבעלי האפליקציה יש&nbsp;</span><u><span style="font-size:12pt;">זכות להשתמש במידה ולהעביר אותו לצדדים שלישיים</span></u><span style="font-size:12pt;">. לרבות שותפים עסקיים וספקי שירותים שונים, בהתאם לשיקול דעתם, בין היתר גם כדי למלא אחרי הוראות הדין, כולל:</span></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">החוקים והחקיקות;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">הפקודות והצווים;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">האמנות והתקנות;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">הוראות המינהל והוראות רשמיות;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">הנחיות או חוזרים של גופים רגולטוריים או שלטוניים שונים.</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><u><span style="font-size:12pt;">מטרת העברת המידע לצדדים שלישיים</span></u><span style="font-size:12pt;">&nbsp;תתבצע בכל מקרה שנוגע לאחד או יותר מהתרחישים הבאים:</span></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בקשה או תלונה הנוגעת לשימוש באפליקציה;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">טיפול בבעיות טכניות או בעיות אבטחה של השימוש באפליקציה או השימוש במערכותיו;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">סכסוכים משפטיים בין המשתמשים לבין בעלי האפליקציה, כדי להשיב על תביעות של צדדים שלישיים;</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">כשהשימוש באפליקציה התבצע באופן שמנוגד להוראות כל דין, לתנאי השימוש או למטרות שיפור או שינוי האפליקציה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">הגנה על זכויות הקניין של המשתמשים באפליקציה או של בעלי האפליקציה.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:10pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">הצעת שירותים נוספים למשתמשים מטעם אותם צדדים שלישיים במסגרת פרסום ממוקד באפליקציה.&nbsp;</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">השימוש באפליקציה על ידי צדדים שלישיים&nbsp;</span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">המשתמשים מאשרים שלמטרות המפורטות במסמך מדיניות פרטיות זה, לבעלי האפליקציה יש זכות להעביר את המידע לצדדים שלישיים, וכי להם יש זכות לבצע שימוש במידע שקיבלו לאותן מטרות כפי שהן מפורטות בתנאי השימוש ובמדיניות הפרטיות, כמו גם לשמור את המידע במאגרי המידע שלהם. בעלי האפליקציה אינם אחראים לשום סוג של שימוש של צדדים שלישיים במידע.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">שימוש בעוגיות (Cookies) &nbsp; &nbsp;&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="עוגיית זנגביל קו מיתאר" src="https://lh7-us.googleusercontent.com/18tMLP9xs7gK7uXlqTKrS5FjwRwrr4FMyafdRVHy5J3GJbBbxKqbmvLnYltjvKuvQp-gz2DLeXXvbxCT3Ryyh4GiOBgIY_5RF4oaWNAQv6U2fYE8se8FJIM9oH8yDRQxBje7AfwNEulzSmO-kGOeXklQxOm6s4h2" width="46" height="46"></span></span></strong><strong><span style="font-size:12pt;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">כחלק מהתפעול השוטף של אפליקציה נעשה שימוש ב&quot;עוגיות&quot;, שבין היתר משמשות להבנת העדפות המשתמש והתאמות אישיות, אימות פרטים אישיים, או איסוף מידע סטטיסטי. מובהר בזאת שיתכן שלא יתבקש אישור המשתמשים לפני השימוש, והמשתמשים רשאים בכל עת לנקות את &quot;העוגיות&quot; מהדפדפן שלהם, או להגדיר אותו באופן שיסרב לבצע שימוש ב&quot;עוגיות&quot;.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">אבל בעלי האפליקציה&nbsp;</span><u><span style="font-size:12pt;">אינם מבטיחים שפעילויות אלו יאפשרו שימוש וגלישה תקינים באפליקציה</span></u><span style="font-size:12pt;">, והם רשאים למנוע שירות או לחסום את השימוש באפליקציה במקרים בהם בוצעו פעולות כאמור.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">קישורים לאפליקציות אחרות&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="קישור קו מיתאר" src="https://lh7-us.googleusercontent.com/CF9NTw2QtWoFOh-fH34yRAGFaXGy6eLNDRyJYK3R4TMzK3_ZTZwhuukFex20icmKLH71c--h_FwD5QvOQ1DQ2CIiP65smELMgr1ma90Mh3-AFsYN-nZ_4ujM4uULdQiJe8hsBjlcWhlPbRgHJj71Y1j1Ks5uEj5N" width="32" height="32"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">באפליקציה מופיעים קישורים שמפנים את המשתמשים לאפליקציות או אתרים שונים, כמו גם הצעות פרסום לרכישת מוצרים נוספים. מובהר שמדיניות הפרטיות כפי שהיא מפורטת במסמך זה חלה בנוגע לאפליקציה בלבד.</span></p>
<p dir="rtl" style="text-align: justify;"><u><span style="font-size:12pt;">בעלי האפליקציה אינם אחראים למדיניות הפרטיות של אפליקציות חיצוניות</span></u><span style="font-size:12pt;">, והכניסה אליהם באמצעות הקלקה על הקישורים היא באחריות הבלעדית של המשתמשים. בעלי האפליקציה אינם אחראים לשימוש או כניסה לאפליקציות אחרות, ומומלץ לקרוא בעיון את תנאי השימוש ומדיניות הפרטיות באפליקציות המקושרות לפני העברת פרטים אישיים או ביצוע פעולות שונות בהם.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">דיוור ישיר והודעות פרסומיות</span><strong><span style="font-size:12pt;">&nbsp;</span></strong><span style="font-size:11pt;"><span style="border:none;"><img alt="אנטי ספאם - אבטחת המידע שלכם עם צעד אחד קדימה | IT-START" src="https://lh7-us.googleusercontent.com/ZmBNuZkvKMEthB0Dfu6OIpx1Wqh4qK3SH9dIVd9jtQRRtgQ69LYB75Mv6qMf3EJK0PSPBQAEYfoJvIVfoOrf7PXnQwk9ugIi8lz96339cgGhIfXUEXLjj2daIp0ZVgK4yNZF67qw5P7uiMgTvUDZD1H72vXnNLwz" width="80" height="72"></span></span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">לאורך שנת הלימודים בעלי האפליקציה ישתמשו במידע שנמסר כדי להציע למשתמשים שירותים שונים בתשלום או שלא בתשלום מטעם בעלי האפליקציה או שותפיהם העסקיים או צדדים שלישיים אחרים.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">המשתמשים מאשרים שהם&nbsp;</span><u><span style="font-size:12pt;">מסכימים לקבל דברי פרסומת</span></u><span style="font-size:12pt;">&nbsp;כפי שמפורט בסעיף 30א&apos; לחוק התקשורת (בזק ושידורים), התשמ&quot;ב-1982 (להלן: &quot;חוק התקשורת&quot;), כמו גם&nbsp;</span><u><span style="font-size:12pt;">לקבלת דיוורים ישירים</span></u><span style="font-size:12pt;">&nbsp;בהתאם לחוק הגנת הפרטיות התשמ&quot;א-1981 (להלן: &quot;חוק הגנת הפרטיות) מבעלי האפליקציה ומהספקים.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מבלי לגרוע מכלליות האמור לעיל, המשתמשים באפליקציה מאשרים ומביעים את הסכמתם לקבלת כל מידע שיווקי כגון:</span></p>
<ul>
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">עדכונים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מבצעים והטבות.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מידע שיווקי ופרסומי.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">הצעות לרכישת שירותים או מוצרים מבעלי האפליקציה או מצדדים שלישיים.</span></p>
    </li>
    <li dir="rtl" style="list-style-type:disc;font-size:12pt;">
        <p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">סוגים שונים של דיוור ישיר.</span></p>
    </li>
</ul>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מידע שיווקי זה יכול להגיע אל המשתמשים באפליקציה כמודעות קופצות בתוך האפליקציה, בדואר האלקטרוני, במסרונים בטלפון הנייד, במערכת חיוג אוטומטי, בפקס, או בכל שיטת ואמצעי תקשורת אחר.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">הזכויות שלך במידע&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="הבדל במשקל קו מיתאר" src="https://lh7-us.googleusercontent.com/TEnJT8WTUYEVn-o_Rcm9Go5H9fgSnabu18qQ191wBZax9DdMks0OYw_Up0blnCkCjFoyLmwffkyd-Ma2X2lou2i8jfCLurDDrJ6d4Iv9owIAyQG6AhReM58Zp9QGPCc7vKRtDOW_SPJbIkP2JKaKrv-m5iVi3NWG" width="42" height="42"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><u><span style="font-size:12pt;">הזכות לעיין במידע</span></u><span style="font-size:12pt;">&nbsp;המשתמש זכאי לעיין במידע שנאסף אודותיו, ששמור במאגרי המידע שלנו, ושמזוהה ומשויך אליו. אין אפשרות לעיין במידע שאינו מזוהה ומשויך.</span></p>
<p dir="rtl" style="text-align: justify;"><u><span style="font-size:12pt;">הזכות לתיקון מידע</span></u><span style="font-size:12pt;">&nbsp;אם המשתמש מצא שהמידע שנשמר אודותיו אינו נכון, שלם, ברור או מעודכן, ניתן לפנות לבעלי האפליקציה בבקשה מפורטת לתיקון או מחיקה של המידע. למימוש זכויות אלו, ניתן לפנות לבעלי האפליקציה, באמצעות פרטי הקשר המופיעים בהמשך מסמך זה. בעלי האפליקציה יבחנו את הפנייה, וישיבו בהתאם למועדים הקבועים בחוק.&nbsp;</span></p>
<p dir="rtl" style="text-align: justify;"><u><span style="font-size:12pt;">הזכות לבטל הסכמה</span></u><span style="font-size:12pt;">&nbsp;המשתמש זכאי, בכל עת, לבטל את הסכמתו לקבלת דיוור, בפניה מתאימה אל בעלי האפליקציה. לפירוט נוסף, ראה את הפרק העוסק בדיוור ישיר והודעות פרסומיות.</span></p>
<p dir="rtl" style="text-align: justify;"><u><span style="font-size:12pt;">זכויות נוספות בקשר למידע</span></u><span style="font-size:12pt;">&nbsp;ייתכן שהמשתמש זכאי לזכויות נוספות, בקשר למידע אודותיו. לפניות בנושאים אלו, או בנושאים אחרים הקשורים למדיניות פרטיות זו, ניתן לפנות לבעלי האפליקציה באמצעות פרטי הקשר המופיעים בהמשך מסמך זה. בעלי האפליקציה יבדקו את הפניה וישיבו בהתאם.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">גם אם ימחק, יתוקן מידע, או תתקבל בקשתה בכל דרך אחרת, בעלי האפליקציה בכל מקרה יוסיפו וישמרו מידע שדרוש להם לשם ניהול השירות, לרבות מידע אשר דרוש להם להגנה ולשמירה על זכויותיהם המשפטיות, או לצורך עמידה בדרישות הרגולטוריות, מניעת הונאה או תרמית, ואכיפה של מדיניות פרטיות זו ותנאי השימוש באתרים.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">אבטחת מידע &nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="פתיחת מנעול קו מיתאר" src="https://lh7-us.googleusercontent.com/Er1IJ1Bk6iYwIdsrzYAzihfUwBe1baZU4eh50eUmr0nuJU3A97j3vRn3lhjGi_lyQr919LP61pDfk4zpJF-LuwJQrLuMjo5rLOhOTiScIUWFl4z9OQfa6zW4y0cHqn313uyQuJUiEvPfAo1c0nPFNDRBVzJwNv4-" width="36" height="36"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">מסירת המידע באפליקציה או איסופו במהלך השימוש באפליקציה, מתבצעים&nbsp;</span><u><span style="font-size:12pt;">בתהליכים מאובטחים שמאפשרים הצפנת מידע</span></u><span style="font-size:12pt;">&nbsp;שמועבר באינטרנט באופן שאינו מאפשר זיהוי או קריאה של המידע במהלך העברתו.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בעלי האפליקציה&nbsp;</span><u><span style="font-size:12pt;">ינקטו בכל המאמצים לאבטח את המידע באפליקציה</span></u><span style="font-size:12pt;">, בהתאם למקובל ולנהוג באפליקציות מסוג זה, אך אינם ערבים ואינם מבטיחים שמסדי הנתונים שלהם, כולל המידע האישי שנמסר על ידי המשתמשים, לא ייפרץ ושהמידע לא יגיע לצדדים שלישיים שאינם מורשים.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">כל עוד בעלי האפליקציה נוקטים באמצעים סבירים לאבטחת המידע, הם לא יימצאו אחראים לשום נזקים, מכל סוג שהוא, שייגרמו למשתמשים כתוצאה מפריצה לאפליקציה, למסדי הנתונים או למחשבים המפעילים אותו.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">חשיפה לסיכונים</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="סיכון ביולוגי קו מיתאר" src="https://lh7-us.googleusercontent.com/PFRm42wsOUy9jpJlUooJqMRPGVplMWOJxJ3JFjvgQSF25H4Z3_vL_CgpqMqKEy0s6H5KSbsgcxAWEPaeCwMqsEqMd9-UROBZ-shoHYlWbI9-6g1Cud8FCnQMuEFGhDYvqjfMUr2Sh7xQq6nREJ684WmLNNECvpUj" width="34" height="34"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">לתשומת לב המשתמשים באפליקציה, השימוש באפליקציה או בתכנים שמפורסמים בו או בתכנים שמפורסמים באפליקציות אחרות שהאפליקציה מקשרת אליהם,&nbsp;</span><u><span style="font-size:12pt;">עלול לחשוף אותם לסיכונים שכרוכים בשימוש באינטרנט</span></u><span style="font-size:12pt;">, כולל חדירה לטלפון הנייד, למחשב, חשיפה לתוכנות זדוניות או לווירוסים, וכן הלאה.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">השימוש והגלישה באפליקציה או עיון בתכנים המפורסמים בו או בתכנים המפורסמים באפליקציות חיצוניות שהאפליקציה מקשרת אליהן, מתבצעת רק באחריות המשתמשים. בעלי האפליקציה&nbsp;</span><u><span style="font-size:12pt;">ממליצים על התקנת תוכנות מספקות של אבטחה והגנה</span></u><span style="font-size:12pt;">, לפני הכניסה לאפליקציה או ביצוע שימוש בה.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בעלי האפליקציה&nbsp;</span><u><span style="font-size:12pt;">לא ימצאו אחראים לנזקים</span></u><span style="font-size:12pt;">&nbsp;מכל הסוגים, ישירים או עקיפים, שייגרמו למשתמשים כתוצאה משימוש באפליקציה.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">התניית שיפוט&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="פטיש יושב-ראש קו מיתאר" src="https://lh7-us.googleusercontent.com/tQATvXMGZnUI63gASpJQKYFPRZ0aF9yKPMitKcUaPorudDfbpVdNIH_CfpC82R9EU6partXnNmLAho_CE0J1OwlEqeY1P4vwpX-KPOK6GB3-a5zmydS0O6yhX6Fk_M615kAwkwKh8QhjYKTMOIL3MyZ9ZGz4Kv6x" width="41" height="41"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">על מדיניות הפרטיות כפי שהיא מנוסחת במסמך זה,&nbsp;</span><u><span style="font-size:12pt;">חל הדין הישראלי</span></u><span style="font-size:12pt;">&nbsp;ויש לפרש אותה בהתאם. לבית המשפט המוסמך&nbsp;</span><u><span style="font-size:12pt;">במחוז מרכז</span></u><span style="font-size:12pt;">&nbsp;יש את הסמכות השיפוטית בכל נושא שנוגע למדיניות הפרטיות.</span></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בכל מקרה בו בית המשפט המוסמך יקבע שהוראה כלשהיא מהוראות מדיניות הפרטיות מנוסחת באופן שאינו חוקי או תקף, או שכולה או חלקה אינה ניתנת לאכיפה, ובהתאם לקביעת בית המשפט המוסמך, אותה הוראה בלבד, או חלקה, בהתאם לעניין, תהיה בטלה, ולא יהיה בכך על מנת להשפיע על שאר הוראות מדיניות הפרטיות שיישארו בתוקף ויחייבו את המשתמשים.</span></p>
<h1 dir="rtl" style="text-align: right;"><strong><span style="font-size:12pt;">דרכי התקשרות&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="טלפון עם רמקול קו מיתאר" src="https://lh7-us.googleusercontent.com/Pqyvmy6svU2Z8loVdNcj4pWmxY6RVB-4k_PBlHSR2oy7Qg5s0AgqSXwh5RptHOQYryne6LKbhN5s91FHPzcTNjOziwBUzsoBeBJI4XMG3ESup06q6FzIr7jIk29h74Ohk3lvthZgUwrFoROEvnUdbiIgKbnSRhKO" width="43" height="43"></span></span></strong></h1>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">אופן ההתקשרות עם בעלי האפליקציה:&nbsp;</span><u><span style="font-size:12pt;">מייל</span></u><span style="font-size:12pt;">:&nbsp;</span><a href="mailto:barfargon@gmail.com"><u><span style="color:#0563c1;font-size:12pt;">barfargon@gmail.com</span></u></a><span style="font-size:12pt;">;&nbsp;</span><u><span style="font-size:12pt;">פלאפון</span></u><span style="font-size:12pt;">: 0508-447397.</span></p>
<p dir="rtl" style="text-align: justify;"><strong><span style="font-size:12pt;">שינוי ועדכון בהגדרות מדיניות הפרטיות&nbsp;</span></strong><strong><span style="font-size:12pt;"><span style="border:none;"><img alt="גלגל שיניים יחיד קו מיתאר" src="https://lh7-us.googleusercontent.com/gZSnA4w9szlTyJxiHOfJ3olUSNmFcKLHaGp0iU_MZ_I15vLrVdN_HHmqmEGRwDQBv49QXT0Ne5TCWq4G_TephgEedx1zAgsrJP12m4rMXmLWH6eiD-1Bll4mHLIaMemDZrhjCXjM1GID_B-KD9qGEoEWzVoZE92_" width="34" height="34"></span></span></strong></p>
<p dir="rtl" style="text-align: justify;"><span style="font-size:12pt;">בעלי האפליקציה יכולים ועשויים לשנות, באופן של מחיקה, שינוי, הורדה, הסרה והוספה (להלן: &quot;השינוי&quot;), את מדיניות הפרטיות באפליקציה, מדי פעם ובהתאם לשיקול דעתם הבלעדי.</span></p>
<p><span style="font-size:12pt;">השימוש באפליקציה או במערכותיה&nbsp;</span><u><span style="font-size:12pt;">כפוף למדיניות הפרטיות החדשה בעקבות השינוי</span></u><span style="font-size:12pt;">, ולכן יש לקרוא את המדיניות בכל פעם בה מתבצע שימוש באפליקציה.</span></p>""",
                    unsafe_allow_html=True)


def _terms_of_service_3():
    pass


def _display_terms_of_service():
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
    match st.session_state.terms_of_service_num:
        case 1:
            _terms_of_service_1()
        case 2:
            _terms_of_service_2()
        case 3:
            _terms_of_service_3()
    cols = st.columns((4, 10, 4))
    with cols[1]:
        st.session_state.location_access = st.radio(label='אני נותן לאפליקציה "תכנונידע" גישה למיקום המכשיר שלי',
                                                    options=["בזמן השימוש באפליקציה", "רק הפעם", "אין אישור"])
        st.session_state.contact_access = st.radio(label='אני נותן לאפליקציה "תכנונידע" גישה לאנשי הקשר שלי',
                                                    options=["בזמן השימוש באפליקציה", "רק הפעם", "אין אישור"])
        st.session_state.camera_access = st.radio(label='אני נותן לאפליקציה "תכנונידע" גישה למצלמה שלי',
                                                    options=["בזמן השימוש באפליקציה", "רק הפעם", "אין אישור"])
        st.session_state.cookies = st.radio(label='אנו משתמשים בקובצי Cookie כדי לאפשר לאתר שלנו לפעול כהלכה, להתאים אישית תוכן ומודעות וכמובן את לוח הסטודנט שלך. בנוסף, אנו משתפים מידע אודות השימוש שלך באתר שלנו עם שותפינו העסקיים.',
                                                    options=["קבל את כל קבצי ה-Cookie", "בצע הגדרות אישיות של קובצי ה-Cookie", "דחה הכל(במידה ולא תאשר את הקבצים הדבר יפגע באיכות השירות שתקבל)"])
        if st.session_state.get("advertisements") is None:
            st.session_state.advertisements = False
        st.session_state.advertisements = st.checkbox("אני מעוניין שהאפליקציה תשלח לי הצעות פרסומיות אשר תואמות את העדפותיי")
        if st.session_state.get("terms_of_service") is None:
            st.session_state.terms_of_service = False
        st.session_state.terms_of_service = st.checkbox("קראתי והסכמתי לתנאי השימוש")
        st.button("המשך", on_click=next_page, args=(3,))


def terms_of_service():
    start_timer(3)
    st.session_state.terms_of_service_num = random.randint(1, 3)
    _display_terms_of_service()


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
        "location_access": {"stringValue": st.session_state.location_access},
        "contact_access": {"stringValue": st.session_state.contact_access},
        "camera_access": {"stringValue": st.session_state.camera_access},
        "cookies": {"stringValue": st.session_state.cookies},
        "advertisements": {"booleanValue": st.session_state.advertisements},
    }
    headers = {
        "Content-Type": "application/json",
    }
    print("sending")
    res = requests.post(url, data=json.dumps({"fields": data}), headers=headers)
    print("sent")
    print(res.json())


def app_installation():
    start_timer(4)
    st.title("התקנת האפליקציה")
    cols = st.columns((4, 10, 4))
    with cols[1]:
        st.button("התקן את האפליקציה", on_click=_finish, args=(True,))
        st.button("המשך", on_click=_finish, args=(False,))

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
    match page_num:
        case 1:
            return landing_page
        case 2:
            return description_page
        case 3:
            return terms_of_service
        case 4:
            return app_installation


if __name__ == '__main__':
    st.set_page_config(layout='wide')
    get_page(st.session_state.get("page_num", 1))()
