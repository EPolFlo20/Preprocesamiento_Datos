document.addEventListener("DOMContentLoaded", function () {
    // Secuestra al envio del formulatio y espera la respuesta
    document.getElementById("search-form").addEventListener("submit", function (event) {
        event.preventDefault();

        // Recoger el texto a procesar y la opción de preprocesamiento 
        let inputText = document.getElementById("inputText").value;
        let operation = document.querySelector('select[name="operation"]').value;

        // Hacer la solicitud GET a Flask
        fetch(`/preprocessing?inputText=${encodeURIComponent(inputText)}&operation=${operation}`)
            .then(response => response.json())  // Convierte la respuesta en JSON
            .then(response_data => {
                // despliga los datos del JSON en la página
                display_data(response_data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
})

function display_data(response_data) {
    let insert = "<h2>Resultados del Preprocesamiento:</h2>";

    // Muestra los datos que estén en el Json
    if ("language_detection" in response_data) {
        let language = response_data.language_detection?.detected_language || "Desconocido";
        let similitud = response_data.language_detection?.similarities || "No disponible";
        let sim_es = "Español: " + similitud?.es || "0";
        let sim_en = "Inglés: " + similitud?.en || "0";
        let sim_fr = "Francés: " + similitud?.fr || "0";
        insert += "<div id=\"resultados\">" +
            "<h3>Identificación del Lenguaje:</h3>" +
            "<p><b>Lenguaje Detectado: </b>" + language + "</p>" +
            "<p><b>Similitud del Lenguaje: </b></p><ul>" +
            "<li>" + sim_es + "</li>" +
            "<li>" + sim_en + "</li>" +
            "<li>" + sim_fr + "</li>" +
            "</div>";

    } if ("filtered_text" in response_data) {
        let filtered_text = response_data?.filtered_text || "Desconocido";
        insert += "<div id=\"resultados\">" +
            "<h3>Resultados de la Eliminación de Stopwords:</h3>" +
            "<p><b>Texto Filtrado: </b>" + filtered_text + "</p >" +
            "</div>";

    } if ("Lemas" in response_data) {
        insert += "<div id=\"resultados\">" +
            "<h3>Lematización del Texto:</h3>" +
            "<table border=\"1\"><tr><th>Tokens</th><th>Lema</th><th>Etiqueta</th><th>Dependencia</th></tr>";
        // Iterar sobre Lema y obtener sus datos
        Object.keys(response_data.Lemas).forEach(key => {
            let token = response_data.Lemas[key];
            insert += "<tr><td>" + key + "</td><td>" + token.Lema + "</td><td>" + token.Etiqueta + "</td><td>" + token.Dependencia + "</td></tr>";
        });
        insert += "</table></div>";

    } if ("keywords" in response_data) {
        insert += "<div id=\"resultados\"><h3>Palabras Clave:</h3> <ul>";
        // Iterar sobre keywords y obtener cada una de las palabras clave
        response_data.keywords.forEach(key => {
            insert += "<li>" + key + "</li>";
        });
        insert += "</ul></div>";

    } if ("tesauro" in response_data) {
        let sustantivos = response_data.tesauro?.Sustantivos || ["No disponible"];
        let verbos = response_data.tesauro?.Verbos || ["No disponible"];
        let otros = response_data.tesauro?.Otros || ["No disponible"];
        insert += "<div id=\"resultados\">" +
            "<h3>Tesauro construido:</h3>" +
            "<p><b>Sustantivos: </b>" + sustantivos + "</p>" +
            "<p><b>Verbos: </b>" + verbos + "</p>" +
            "<p><b>Otros: </b>" + otros + "</p>" +
            "</div>";
    }

    document.getElementById("resultados_pre").innerHTML = insert;
}