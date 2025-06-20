### SPARQL Query examples according to Competency Questions

[SPARQL Documentation](https://www.w3.org/TR/rdf-sparql-query/).

CQ1:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bo: <http://w3id.org/BadmintONTO/>
PREFIX time: <http://www.w3.org/2006/time#>

SELECT ?m ?tournament ?matchtype ?y ?mm ?d ?minutes
WHERE {
  ?m a bo:MatchEvent .
  ?m bo:isDescribedBy ?info .
  ?info bo:inCompetition ?tournament .
  ?info bo:hasMatchType ?matchtype .
  ?m bo:occursAtTime ?te .
  ?te time:inDateTime ?dt .
  ?dt time:year ?y .
  ?dt time:month ?mm .
  ?dt time:day ?d .
  ?te time:hasDurationDescriprion ?dd . 
  ?dd time:minutes ?minutes
}
LIMIT 5
```

CQ2:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bo: <http://w3id.org/BadmintONTO/>

SELECT (COUNT(*) as ?count)
WHERE {
  ?m a bo:MatchEvent .
  ?m bo:isDescribedBy ?info .
  ?info bo:setNumber ?number .
  Filter (?number = 3)
}
```

CQ3:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bo: <http://w3id.org/BadmintONTO/>

SELECT ?shottype (COUNT(?shottype) as ?num)
WHERE {
  ?s a bo:StrokeEvent .
  ?s bo:isDescribedBy ?info .
  ?info bo:hasShotType ?shottype .
  ?info bo:hittingPlayer ?player .   
  ?player bo:personFullName "SHI Yuqi" .
}
GROUP BY ?shottype
```

CQ4:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bo: <http://w3id.org/BadmintONTO/> 

SELECT ?num_to_point
WHERE {
  ?s a bo:RallyEvent .
  ?s bo:isDescribedBy ?info .
  ?info bo:getPointByPlayer ?player .   
  ?player bo:personFullName "SHI Yuqi" .
  ?info bo:shotNumber ?num_to_point .
}
Order By (?num_to_point)
```

CQ5:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bo: <http://w3id.org/BadmintONTO/> 

SELECT ?r ?shottype
WHERE {
  ?r a bo:RallyEvent .
  ?r bo:hasSubEvent ?s .
  ?r bo:isDescribedBy ?r_info .
  ?r_info bo:getPointByPlayer <http://example.com/player-25> .   
  ?s bo:isDescribedBy ?s_info .
  ?info bo:hasShotType ?shottype .
  ?info bo:hittingPlayer <http://example.com/player-25> . 
}
```

CQ6:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bo: <http://w3id.org/BadmintONTO/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?player ?name ?num_to_point 
WHERE {
  ?s a bo:RallyEvent .
  ?s bo:isDescribedBy ?info .
  ?info bo:getPointByPlayer ?player . 
  ?player bo:personFullName ?name .
  ?info bo:shotNumber ?num_to_point .
}
ORDER BY DESC(xsd:integer(?num_to_point)) LIMIT 1

```

CQ7:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bo: <http://w3id.org/BadmintONTO/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?player ?num WHERE {
  ?s a bo:RallyEvent .
  ?s bo:isDescribedBy ?info .
  ?info bo:getPointByPlayer ?player .   
  ?info bo:shotNumber ?num .
  FILTER (xsd:integer(?num) <= 3)
}
```


