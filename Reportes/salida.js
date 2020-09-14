// HOLA QUE TAL
var nombre = "Juan Solares"
var altura = 180
var concatenation = nombre + " " + altura + "cm"

/*
var datos = document.getElementById(datos)
datos.innerHTML = 
    <h1> Soy la caja de datos </h1>
    <h2> Mi nombre es: $nombre </h2>
    <h3> Mi altura es de: $altura </h3>


if(altura >= 190)
    datos.innerHTML += 
    <h1> Eres una persona alta</h1>
    
else
    datos.innerHTML += 
    <h1> Eres una persona baja </h1>
    


for(var i = 2000 i <= 2020 i++)
    //bloque de instrucciones
    datos.innerHTML += <h2>Estamos en el a�o: +i


*/
function MuestraMiNombrenombre, altura) {


    return misDatos
}

function imprimir) {
    var datos = document.getElementById"datos";
    datos.innerHTML = MuestraMiNombre"Juan Antonio Solares" 170;
}





imprimir();
//MuestraMiNombreJuan Antonio 170
var nombres = ['Juan' 'Antonio' 'Pablo';

document.write"h1 Listado de nombres /h1";
/*
for (var i = 0 i <nombres.length i++)
    document.write(nombres[i]+ '<br/>')
*/
nombres.forEachfunction(nombre) {
    document.writenombre + 'br/';
});


var coche = {
    modelo: 'Mercedes Clase A'
    maxima: 500
    antiguedad: 2020
    mostrarDatos) {
        console.log(this.modelo, this.maxima, this.antiguedad)
    },
    propiedad1: 'Color aleatorio'}


document.write'h1' + coche.antiguedad + '/h1';
coche.mostrarDatos);
console.logcoche);


//promesas
var saludar = new Promise(resolve, reject) = {
    setTimeout() = {
        let saludo = "Hola muy buenas a todos chavales"
        saludo = false
        if (saludo) {
    resolvesaludo);
} else {
    reject'No hay saludo disponible';
}
    }, 2000
});


saludar.thenresultado = {
    alertresultado);
})
.catcherror = {
    alerterror);
})

