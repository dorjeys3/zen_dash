from pages.custom_page.row_nine.customer_html import CustomHTMLData, CustomHTML2Data
from pages.table_page.row_nine.table import TableDataInfo
from zen_dash import Zen
from zen_dash.flex_data import FlexData
from zen_dash import instances as i
import uuid
from jinja2 import Template

prefix = "/backend/custom_page/row_nine"
flex = FlexData(fxFlex="50%", fxFlex_md="50%",
                fxFlex_sm="110%", fxFlex_xs="110%")



class IFrame(Zen):
    @staticmethod
    def full_url() -> str:
        return f"{prefix}/iframe"

    @staticmethod
    def url() -> str:
        return "/iframe"

    @staticmethod
    def view():
        return i.ReturnData(type=i.InstanceType.IFRAME,
                            iframe_data=i.IframeData(url="https://pepy.tech/project/zen_dash", height="500px", width="600px"), flex=i.FlexData(fxFlex='50%', fxFlex_md='100%', fxFlex_sm='100%')
                            )


class CustomHTML(Zen):
    @staticmethod
    def full_url() -> str:
        return f"{prefix}/custom_html"

    @staticmethod
    def url() -> str:
        return "/custom_html"

    @staticmethod
    def view():
        return i.ReturnData(type=i.InstanceType.CUSTOM_HTML,
                            custom_html_data=i.CustomHTML(
                                name="test", full_custom=False, html=CustomHTMLData, script= ".test{background-color:red}")
                            )


class FullCustomHTML(Zen):
    @staticmethod
    def full_url() -> str:
        return f"{prefix}/full_custom_html"

    @staticmethod
    def url() -> str:
        return "/full_custom_html"

    @staticmethod
    def view():
        return i.ReturnData(type=i.InstanceType.CUSTOM_HTML,
                            custom_html_data=i.CustomHTML(
                                name="test", full_custom=True, html=CustomHTML2Data)
                            )

