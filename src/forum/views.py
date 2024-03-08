from datetime import date, timedelta

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from forum.documents import PostDocument
from forum.models import SubForum


# Create your views here.
def forum_search_view(request):
    sub_forums = SubForum.objects.prefetch_related("section_set").all()
    return render(request, "index.html", {
        "sub_forums": sub_forums,
    })


def get_posts_view(request):
    keywords = request.GET.get("keywords")
    author = request.GET.get("author")
    search_in = request.GET.get("search_in")
    sort = request.GET.get("sort")
    time = request.GET.get("time")
    sections = request.GET.getlist('sections[]')

    search = PostDocument.search()

    if sections:
        search = search.filter("terms", **{"topic.section.id": sections})

    fields = ["topic.title", "content"]

    if search_in == "messages":
        fields = ["content"]
    elif search_in == "topics":
        fields = ["topic.title"]

    if author:
        search = search.query("match", **{"author.nickname": author})

    if keywords:
        search = search.query("multi_match", query=keywords, fields=fields, fuzziness=1).highlight(
            "content",
            "topic.title",
            fragment_size=10000,
        )

    search = (
        search.sort("created")
        if sort == "asc"
        else search.sort("-created")
    )

    last_date = date(2017, 5, 5)

    if time == "year":
        search = search.filter("term", created__gte=last_date - timedelta(days=365))
    elif time == "month":
        search = search.filter("term", created__gte=last_date - timedelta(days=30))

    result = [
        {
            "topic__title": (
                "".join(item.meta.highlight["topic.title"])
                if "topic.title" in item.meta.highlight
                else item.topic.title
            ),
            "created": item.created,
            "topic__section__title": item.topic.section.title,
            "author__nickname": item.author.nickname,
            "content": (
                "".join(item.meta.highlight["content"])
                if "content" in item.meta.highlight
                else item.content
            ),
        }
        for item in search
    ]
    return JsonResponse(list(result), safe=False)
