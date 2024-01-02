from contextlib import contextmanager

import streamlit as st
import streamlit.components.v1 as components

from next_page import next_page
from terms_of_service import terms_of_service_modal


class Modal:

    def __init__(self, title, key, padding=20, max_width=None):
        self.title = title
        self.padding = padding
        self.max_width = max_width
        self.key = key

    def is_open(self):
        return st.session_state.get(f'{self.key}-opened', False)

    def open(self):
        st.session_state[f'{self.key}-opened'] = True
        st.experimental_rerun()

    def close(self, rerun=True):
        st.session_state[f'{self.key}-opened'] = False
        if rerun:
            st.experimental_rerun()

    @contextmanager
    def container(self):
        if self.max_width:
            max_width = str(self.max_width) + "px"
        else:
            max_width = 'unset'

        st.markdown(
            f"""
            <style>
            div[data-modal-container='true'][key='{self.key}'] {{
                position: absolute;
                padding: 40px;
                width: 75vw !important;
                left: 12.5%;
                top: 10%;
                z-index: 1001;
                direction: rtl;
            }}

            div[data-modal-container='true'][key='{self.key}'] > div:first-child {{
                margin: auto;
            }}

            div[data-modal-container='true'][key='{self.key}'] h1 a {{
                display: none
            }}

            div[data-modal-container='true'][key='{self.key}']::before {{
                    position: fixed;
                    content: ' ';
                    left: 0;
                    right: 0;
                    top: 0;
                    bottom: 0;
                    z-index: 1000;
                    background-color: rgba(0, 0, 0, 0.5);
            }}
            div[data-modal-container='true'][key='{self.key}'] > div:first-child {{
                max-width: {max_width};
            }}

            div[data-modal-container='true'][key='{self.key}'] > div:first-child > div:first-child {{
                width: unset !important;
                background-color: #fff;
                padding: {self.padding}px;
                margin-top: {2*self.padding}px;
                margin-left: -{self.padding}px;
                margin-right: -{self.padding}px;
                margin-bottom: -{2*self.padding}px;
                z-index: 1001;
                border-radius: 5px;
            }}
            div[data-modal-container='true'][key='{self.key}'] > div > div:nth-child(2)  {{
                z-index: 1003;
                position: absolute;
            }}
            div[data-modal-container='true'][key='{self.key}'] > div > div:nth-child(2) > div {{
                text-align: right;
                padding-right: {self.padding}px;
                max-width: {max_width};
            }}

            div[data-modal-container='true'][key='{self.key}'] > div > div:nth-child(2) > div > button {{
                right: 0;
                margin-top: {2*self.padding + 14}px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        with st.container():
            _container = st.container()

            st.markdown(
                """
                <style>

                    btn:nth-of-type(1)
                    {
                        display: none!important;
                    }
                    p:nth-of-type(1)
                    {
                        direction: rtl;
                    }
                </style>
                """, unsafe_allow_html=True
            )
            terms_of_service_modal()
            if self.title:
                _container.markdown(
                    f"<h2>{self.title}</h2>", unsafe_allow_html=True)

            close_ = st.button("המשך", on_click=next_page, args=(3,), key=f"{self.key}-close")

            if close_:
                self.close()

        components.html(
            f"""
            <script>
            // STREAMLIT-MODAL-IFRAME-{self.key} <- Don't remove this comment. It's used to find our iframe
            const iframes = parent.document.body.getElementsByTagName('iframe');
            let container
            for(const iframe of iframes)
            {{
            if (iframe.srcdoc.indexOf("STREAMLIT-MODAL-IFRAME-{self.key}") !== -1) {{
                container = iframe.parentNode.previousSibling;
                container.setAttribute('data-modal-container', 'true');
                container.setAttribute('key', '{self.key}');
            }}
            }}
            </script>
            """,
            height=0, width=0
        )

        with _container:
            yield _container


# keep compatible with old api

_default_modal = Modal('', key='streamlit-modal-default')




