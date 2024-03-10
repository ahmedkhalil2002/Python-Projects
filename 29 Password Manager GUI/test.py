new_data = {
    "face": {
        "email": "ahmed khalil",
        "password": "20101874"
    },
    "whats": {
        "email": "khalil",
        "password": "01874"
    }
}

for key, value in new_data.items():
    print(key)
    print(value["email"])
    print()