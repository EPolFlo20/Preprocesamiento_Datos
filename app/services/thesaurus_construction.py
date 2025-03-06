def thesaurus_construction(keywords_data, lemas_data):
    # Tesauro con categorías predefinidas
    tesauro = {
        "tesauro" : {
            "Sustantivos": [],
            "Verbos": [],
            "Otros": []
        }
    }

    keywords = keywords_data["keywords"]
    
    # Clasificación de términos clave según el tipo gramatical
    for keyword in keywords:
        # Extraemos la etiqueta gramatical de lemas_data
        for palabra, info in lemas_data.items():
            if info["Lema"] == keyword:
                pos_tag = info["Etiqueta"]
                
                if pos_tag == "NOUN":
                    tesauro["tesauro"]["Sustantivos"].append(keyword)
                elif pos_tag == "VERB":
                    tesauro["tesauro"]["Verbos"].append(keyword)
                else:
                    tesauro["tesauro"]["Otros"].append(keyword)
    
    return tesauro