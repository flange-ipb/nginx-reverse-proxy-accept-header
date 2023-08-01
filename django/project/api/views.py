from django.http import HttpResponse, HttpResponseBadRequest
from rdflib import Graph


def get_graph(request):
    g = Graph().parse(location="api/resources/vc-db-1.rdf", format="application/rdf+xml")

    if request.accepts("text/turtle"):
        return HttpResponse(g.serialize(format="turtle"), headers={"Content-Type": "text/turtle"})
    elif request.accepts("application/ld+json"):
        return HttpResponse(g.serialize(format="json-ld"), headers={"Content-Type": "application/ld+json"})
    return HttpResponseBadRequest()
