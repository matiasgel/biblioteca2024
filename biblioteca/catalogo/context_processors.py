from django.urls import reverse

links = [
    {"label": "Catálogo", "href": reverse("catalogo"), "icon": "bi bi-house-door"},
    {"label": "Logout", "href": reverse("logout"), "icon": "bi bi-door-closed"},
]


def navbar(request):
    def add_active(link):
        copy = link.copy()

        if copy["href"] == "/":
            copy["active"] = request.path == "/"
        else:
            copy["active"] = request.path.startswith(copy.get("href", ""))

        return copy

    return {"links": map(add_active, links)}