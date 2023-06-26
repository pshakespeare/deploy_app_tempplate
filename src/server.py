from flask import Flask, jsonify
from models.passthrough_handler import *



app = Flask(__name__)

@app.route('/', methods=['GET'])
def service_page():
    return jsonify({"message": "service"})


@app.route('/deploy', methods=['GET']) # TODO: Make this a POST to accept json_payload
def deploy():
    # request function to accept json body *
    ########################################
    payload = ''
    personal_access_token = config('ACCESS_TOKEN')

    conn = connect_to_azure_devops(person_access_token=personal_access_token,
                                org_url=ORG_URL)
    
    core_client = conn.clients.get_core_client()

    get_projects_response =  core_client.get_projects()

    tfs_projects = []
    for project in get_projects_response:
        if project.name in TFS_SELECTED_PROJECTS:
            tfs = TFSProject(name=project.name,
                                    id=project.id)
            tfs_projects.append(tfs)
    
    if payload == None or payload == '':
        payload = {
                    "templateParameters" : {"environment" : "drizzy-214345",
                                            "passthrough" : "Hello World"}
                  }

    deployment_res = post_params_to_firebird_k8s_deploy(personal_access_token=personal_access_token,
                                                        azure_url=f'{ORG_URL}/{tfs_projects[0].name}/_apis/pipelines/{PIPELINE_IDS["Firebird K8s Deploy"]}/runs?api-version=6.1-preview.1',
                                                        body=json.dumps(payload))

    return jsonify({"message" : deployment_res})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')