def test_get_especie(client, setup_database):
    response = client.get("/especie/")
    assert response.status_code == 200


def test_post_especie(client, setup_database):
    response = client.post("/especie/")
    assert response.status_code == 200
