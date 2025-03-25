import requests

token = "sf5pu2u2cl40jgs5dg30o2bkr2"
project_id = "67410"
model = "object-detection-model-1"
image_filename = "images"

headers = {"X-Auth-token": token, "Content-Type": "application/octet-stream"}
for i in range(0, 876):
    with open(f"images/road{i}.png", 'rb') as handle:
        r = requests.post('https://platform.sentisight.ai/api/predict/{}/{}/'.format(project_id,model), headers=headers, data=handle)

    if r.status_code == 200:
        print(r.text)
    else:
        print('Error occured with REST API.')
        print('Status code: {}'.format(r.status_code))
        print('Error message: ' + r.text)
