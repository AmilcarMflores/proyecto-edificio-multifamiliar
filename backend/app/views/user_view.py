def render_user_list(users):
    return [
        {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "telephone": user.telephone,
            "role": user.role
        }
        for user in users
    ]

def render_user_detail(user):
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "telephone": user.telephone,
        "role": user.role
    }

