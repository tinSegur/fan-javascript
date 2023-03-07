# Herramienta de visualización FAN
Esta herramienta es una herramienta de visualización para los datos de FAN utilizados en el Informe a las Naciones elaborado por el CR2.

## Funcionamiento
Esta herramienta utiliza plotly para su funcionamiento, y como tal está pensada para ser empotrada a través de un iframe. Funciona principalmente client-side, pero depende de un servidor que almacene una estructura de archivos a través de la cuál acceder a los datos. Esta estructura se debería poder modificar siempre y cuando se actualizen los regex correspondientes para el acceso.
Los archivos html y CSS en sí están ubicados en la carpeta plotly_visualization.
### Estructura de archivos
La estructura de archivos utilizada por la herramienta es la siguiente:
``` bash
├───index.json
├───variable1
│   ├───variable1_meta.json
│   ├───variable1_data
│   │   ├───variable1-mean-year1.json
│   │   ├───variable1-mean-year2.json
│   │   ├───...
│   ├───variable1_geo
│   │   ├───variable1-geo-year1.json
│   │   ├───variable1-geo-year2.json
│   │   ├───...
├───variable2
│   ├───variable2_meta.json
│   ├───variable2_data
│   └───variable2_geo
├───...
```

Donde index.json es un archivo json con un arreglo de aspecto:
```
["variable1", "variable2", ...]
```
El programa utiliza el archivo index.json para obtener los nombres de las carpetas que contienen las variables disponibles para ser visualizadas.
Cada una de las carpetas debe contener:
- Un archivo de metadatos que son utilizados para obtener el intervalo de años disponible para la visualización, así como el nombre completo de la variable para el desplegable de selección. Debe contener también la unidad de medida para mostar esta información al usuario. [TODO: Adaptar el programa de forma que se obtenga la agregación/regex de nombramiento de archivos y permitir que se grafiquen agregaciones más allá de promedios]
- Una carpeta que contenga los datos rasterizados de variable a visualizar.
  - Esta carpeta debe contener archivos que tengan el formato siguiente:
    ```
        {
        data: [...], -> arreglo de datos. debe tener largo igual a la multiplicación
                        de los largos de los arreglos de longitud y latitud.  
        lat: [...],  -> arreglo de valores de longitud
        lon: [...]   -> arreglo de valores de latitud
        year: 9999   -> año del que proceden estos datos  
    }
    ```
- Una carpeta que contenga los datos geométricos de los contornos a visualizar sobre los datos rasterizados.
  - Esta carpeta debe contener archivos de formato GeoJSON, del tipo de formato generado por la librería d3-contours.
