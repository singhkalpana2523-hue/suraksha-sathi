import requests


BASE = 'http://127.0.0.1:8000'


def get_token(phone='9876543210', password='secret123'):
    # ensure user exists
    requests.post(
        f'{BASE}/auth/signup',
        json={'name': 'Test', 'phone': phone, 'password': password},
        timeout=10,
    )
    r = requests.post(f'{BASE}/auth/login', json={'phone': phone, 'password': password}, timeout=10)
    assert r.status_code in (200, 201)
    return r.json()['access_token']



def test_history_crud_flow():
    token = get_token()
    headers = {'Authorization': f'Bearer {token}'}

    # create
    cr = requests.post(
        f'{BASE}/history',
        json={'title': 'Test', 'question': 'Q?', 'answer': 'A.', 'category': 'Legal'},
        headers=headers,
        timeout=10,
    )
    assert cr.status_code in (200, 201)
    history_id = cr.json()['id']

    # list
    lr = requests.get(f'{BASE}/history?page=1&limit=10', headers=headers, timeout=10)
    assert lr.status_code == 200

    # get
    gr = requests.get(f'{BASE}/history/{history_id}', headers=headers, timeout=10)
    assert gr.status_code == 200

    # search
    sr = requests.get(f'{BASE}/history/search?q=Test', headers=headers, timeout=10)
    assert sr.status_code == 200

    # delete single
    dr = requests.delete(f'{BASE}/history/{history_id}', headers=headers, timeout=10)
    assert dr.status_code == 200

    # delete all
    dar = requests.delete(f'{BASE}/history', headers=headers, timeout=10)
    assert dar.status_code == 200

