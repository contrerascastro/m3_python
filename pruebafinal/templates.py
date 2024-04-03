from string import Template


template = Template("""
                    
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves Ninja</title>
</head>
<body>
    <div>
        <h1>Aguilucho chico</h1>
        <h2>Nombre en inglés</h2>
        <img src="https://aves.ninjas.cl/api/site/assets/files/3099/17082018024245aguilucho_chico_tomas_rivas_web.200x0.jpg" alt="aguilucho">
    </div>    

$contenido

</body>
</html>                                    
"""
)


template2 = Template ("""
                      
    <div>
        <h1>$titulo_esp</h1>
        <h2>$titulo_en</h2>
        <img src="img_full" alt="$titulo_esp">
    </div>                   
    
    """)