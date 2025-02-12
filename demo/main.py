from typing import Optional
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pkg_resources
from pages.box_page import BOXPAGE
from zen_dash import sidebar as s
from zen_dash import page as p
from zen_dash import scripts as sc
from pydantic import BaseConfig
from fastapi.middleware.gzip import GZipMiddleware

from pages.input_page import INPUTZENPAGE
from pages.chart_page import CHARTPAGE
from pages.table_page import TABLEPAGE
from pages.custom_page import CUSTOMPAGE

from pages.input_page import row_one as iro
from pages.input_page import row_three as irt
from pages.input_page import row_four as irf
from pages.input_page import row_five as irfi
from pages.input_page import row_six as irs
from pages.input_page import row_seven as irse
from pages.input_page import row_ten as irte

from pages.table_page import row_two as trt
from pages.table_page import row_nine as trn

from pages.chart_page import row_two as crt
from pages.chart_page import row_eight as cre

from pages.box_page import row_one as bro

from pages.custom_page import row_nine as crn

import filters as f
from filters import view as fv
BaseConfig.arbitrary_types_allowed = True  # change #1

app = FastAPI()
app.include_router(f.router)
app.include_router(iro.router)
app.include_router(irt.router)
app.include_router(irf.router)
app.include_router(irfi.router)
app.include_router(irs.router)
app.include_router(irse.router)
app.include_router(irte.router)
app.include_router(trn.router)
app.include_router(trt.router)
app.include_router(crt.router)
app.include_router(cre.router)
app.include_router(bro.router)
app.include_router(crn.router)

app.add_middleware(GZipMiddleware, minimum_size=1000)


# Could be any dot-separated package/module name or a "Requirement"
# resource_package = 'zen_dash'
# resource_path = '/'.join(('templates', 'temp_file'))  # Do not use os.path.join()
# template = pkg_resources.resource_string(resource_package, resource_path)

folder = pkg_resources.resource_filename('zen_dash', 'static/')
templates = Jinja2Templates(directory=folder)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request, res: Response):
    tr = templates.TemplateResponse("index.html", {"request": request})
    tr.set_cookie("retry_count", "5")
    tr.set_cookie("show_right_sidebar","true")
    return tr


@app.get("/backend/title")
async def title():
    return 'Demo'


@app.post("/backend/document")
async def save_doc(request: Request):
    print(await request.json())
    return "yes"


@app.post("/backend/scripts", response_model=sc.CustomScripts)
async def scripts(request: Request):
    return sc.CustomScripts(scripts=[
        sc.CustomScript(
            url="https://code.jquery.com/jquery-3.6.1.min.js", type=sc.Style.JS),
        sc.CustomScript(
            url="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js", type=sc.Style.JS),
        sc.CustomScript(
            url="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.min.css", type=sc.Style.LINK, rel=sc.Rel.STYLESHEET),
        sc.CustomScript(
            url="https://cdn.datatables.net/1.13.1/js/jquery.dataTables.min.js", type=sc.Style.JS, defer=False),
        sc.CustomScript(
            url="https://cdn.datatables.net/responsive/2.4.0/css/responsive.dataTables.min.css", type=sc.Style.LINK, rel=sc.Rel.STYLESHEET),
        sc.CustomScript(
            url="https://cdn.datatables.net/responsive/2.4.0/js/dataTables.responsive.min.js", type=sc.Style.JS, defer=False
        )

    ])


@app.get("/backend/sidebar", response_model=s.Sidebar)
async def sidebar():
    x =  s.Sidebar(tabs=[
        s.SidebarTab(label=INPUTZENPAGE.name, icon=INPUTZENPAGE.icon),
        s.SidebarGroup(name="Data", subtabs=[
            s.SidebarTab(label=TABLEPAGE.name, icon=TABLEPAGE.icon),
            s.SidebarTab(label=CHARTPAGE.name, icon=CHARTPAGE.icon),
            s.SidebarTab(label=BOXPAGE.name, icon=BOXPAGE.icon),
            s.SidebarTab(label=CUSTOMPAGE.name, icon=CUSTOMPAGE.icon)
        ])],
        filters=[
        s.FilterInfo(url=fv.SingleFilterGlobal.full_url()),
        s.FilterInfo(
            url=fv.SingleFilterServerGlobal.full_url())]
    )
    print(x)
    return x



@app.get("/backend/sidebar2", response_model=s.Sidebar)
async def sidebar():
    x =  s.Sidebar(tabs=[
        s.SidebarTab(label=INPUTZENPAGE.name, icon=INPUTZENPAGE.icon),
        ],
        filters=[
        s.FilterInfo(url=fv.SingleFilterGlobal.full_url()),
        s.FilterInfo(
            url=fv.SingleFilterServerGlobal.full_url())]
    )
    print(x)
    return x


# fxFlex_md: Optional[str] = "40%"
# fxFlex_lt_md: Optional[str] = "100%"


@app.get("/backend/page_detail", response_model=p.Page)
async def page_detail(fragment: Optional[str]):
    if fragment == "page_0":
        return INPUTZENPAGE.page
    elif fragment == "page_1_0":
        return TABLEPAGE.page
    elif fragment == "page_1_1":
        return CHARTPAGE.page
    elif fragment == "page_1_2":
        return BOXPAGE.page
    elif fragment == "page_1_3":
        return CUSTOMPAGE.page
   
   

app.mount("/", StaticFiles(directory=folder), name="static")
