import os
import requests
import zipfile


COMET_API_KEY='eLh0cH1J7CmpKR7x153LqCTZN'
#COMET_PROJECT='docker-example'
#COMET_WORKSPACE='packt'
COMET_API_KEY = os.environ.get("COMET_API_KEY")
COMET_WORKSPACE = os.environ.get("COMET_WORKSPACE")
#COMET_PROJECT = os.environ.get("COMET_PROJECT")

base_project = "diamonds"
models = ["model", "color-feature-label-encoder","clarity-feature-label-encoder","scaler", "label-encoder"]
output_dir = "models"

for model_name in models:
    model_name = f"{base_project}-{model_name}"
    url = f"https://www.comet.ml/api/rest/v2/registry-model/details?workspaceName={COMET_WORKSPACE}&modelName={model_name}"
    headers = {"Authorization": f"{COMET_API_KEY}"}


    response = requests.get(url, headers=headers)
    model_details = response.json()

    
    
    for version in model_details['versions']:
        for stage in version['stages']:
            if stage == 'production':
                model_version = version['version']
                
                link = f"https://www.comet.ml/api/rest/v2/registry-model/item/download?workspaceName={COMET_WORKSPACE}&modelName={model_name}&version={model_version}"
                path = f"{output_dir}/model.zip"
                model_resp = requests.get(link, headers=headers)
                with open(path, 'wb') as f:
                    f.write(model_resp.content)
                
                with zipfile.ZipFile(path,"r") as zip_ref:
                    zip_ref.extractall(output_dir)
                
                os.remove(path)
                break
