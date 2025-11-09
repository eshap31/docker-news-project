from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
from managing_scripts import *
from configurations import LoadEnvVar
from configurations import LoadConfigVariables
from data_filtering import SearchManager

app = FastAPI()

config_var_loader = LoadConfigVariables()
env_var_loader = LoadEnvVar()
template = Jinja2Templates(directory=env_var_loader.load_env_variable("TEMPLATES_DIR"))

mongo_db_mgr = MongoManager()
mongo_db_mgr.initialize()
search_mgr = SearchManager(mongo_db_mgr)


@app.get('/')
def index(req: Request):
    print(f"request: {req}")
    return template.TemplateResponse(
        name="index.html",
        context={"request": req}
    )


@app.get('/get-source')
def index(req: Request):
    requested_val = req.query_params['src']
    # TODO search and return relevant entries
    filtered_results = search_mgr.get_results(requested_val)
    print(f"found {len(filtered_results)} filtered results for {requested_val}: {filtered_results}")
    return filtered_results


if __name__ == "__main__":
    uvicorn.run("main:app")
