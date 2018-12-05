form fetcher import *


# Klasse zuordnen
crawledarticle = ArticleFetcher()
crawledarticle.fetch()
results = crawledarticle.fetch()


# Reulstate ausgeben lassen
for result in results:
    print(result.emoji + ": " + result.title)

for result in results:
    print(result.image)
    
