from django.http import JsonResponse
from django.shortcuts import render

from city.documents import OrganizationDocument


# Create your views here.
def organization_search_view(request):
    return render(request, "city_index.html")




def get_organizations_view(request):
    keywords = request.GET.get("keywords")
    radius = request.GET.get("radius")
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")
    day_of_week = request.GET.get("day_of_week")
    time = request.GET.get("time")


    search = OrganizationDocument.search()[:2000]

    if radius and lat and lon:
        search = search.filter("geo_distance", distance=f"{radius}m", location=[float(lon), float(lat)])

    if day_of_week and time:
        _hours, _minutes = time.split(":")
        minutes = int(_hours) * 60 + int(_minutes)
        # search = search.filter("range", **{f"d{day_of_week}__start": {"lte": minutes}})
        search = search.filter("term", **{f"d{day_of_week}__start__lte": minutes})
        search = search.filter("range", **{f"d{day_of_week}__finish": {"gte": minutes}})

    if keywords:
        search = search.query(
            "multi_match",
            query=keywords,
            fields=["title^3", "tags^2", "description^1"],
            fuzziness=1,
        )

    search = search.sort("-rating", "-type")

    def _get_time(minutes):
        return (
            f"{int(minutes/60):02d}:{minutes%60:02d}"
            if minutes
            else "00:00"
        )


    result = [
        {
            "title": item.title,
            "description": item.description,
            "tags": ", ".join(item.tags),
            "location": [*item.location],
            "start": _get_time(getattr(item, f"d{day_of_week}").start),
            "finish": _get_time(getattr(item, f"d{day_of_week}").finish),
        }
        for item in search
    ]
    return JsonResponse(list(result), safe=False)
