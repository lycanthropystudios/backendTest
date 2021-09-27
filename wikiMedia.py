from urllib.request import urlopen, Request
import json

#scraping tool para obtener las imagenes de los personajes usando la API de Wikimedia
def getImg(imagen_buscada, json_file):
    #Request al API para obtener el titulo de la imagen del articulo de Wikipedia
    imagen_buscada = imagen_buscada.replace(" ", "+")
    request = Request('https://en.wikipedia.org/w/api.php?action=query&titles='+imagen_buscada+'&prop=images&format=json')

    r = urlopen(request).read()
    img = json.loads(r)
    pairs = img["query"]["pages"]

    fin = str(pairs).index(":")
    idx = str(pairs)[2:fin-1]

    img_name = pairs[idx]["images"][1]["title"][5:]
    img_name = img_name.replace(" ", "+")

    #Request al API para obtener el URL de la imagen en el articulo de Wikipedia
    img_url = Request('https://en.wikipedia.org/w/api.php?action=query&titles=Image:'+img_name+'&prop=imageinfo&iiprop=url&format=json')
    
    img_body = urlopen(img_url).read()
    img_path = json.loads(img_body)

    page = img_path["query"]["pages"]

    fin_1 = str(page).index(":")
    idx_2 = str(page)[2:fin_1-1]
    res = page[idx_2]["imageinfo"][0]["url"]
    print(res)
    return res