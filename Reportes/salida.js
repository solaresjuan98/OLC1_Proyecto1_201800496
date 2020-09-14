
var nombre ="Juan Solares";
var altura =180
var concatenation =nombre +" "+altura +"cm";

function imprimir() {
    var datos =document.getElementById("datos");
    datos.innerHTML =MuestraMiNombre("Juan Antonio Solares", 170);
}


imprimir();
//MuestraMiNombreJuan Antonio 170

var nombres =['Juan', 'Antonio', 'Pablo';

document.write("h1> Listado de nombres /h1>");
/*
for (var i = 0 i <nombres.length i++)
    document.write(nombres[i]+ '<br/>')
*/
nombres.forEach(function (nombre) {
    document.write(nombre +'br/>');
});


var coche ={
    modelo: 'Mercedes Clase A',
    maxima: 500,
    antiguedad: 2020,
    mostrarDatos() {
        console.log(this.modelo, this.maxima, this.antiguedad)
    },
    propiedad1: 'Color aleatorio'}


document.write('h1>'+coche.antiguedad +'/h1>');
coche.mostrarDatos();
console.log(coche);


//promesas

var saludar =new Promise((resolve, reject) => {
    setTimeout(() => {
        let saludo ="Hola muy buenas a todos chavales";
        saludo =false;
        if (saludo) {
            resolve(saludo);
        } else {
            reject('No hay saludo disponible');
        }
    }, 2000)
});


saludar.then(resultado =>{
    alert(resultado);
})
.catch(error => {
    alert(error);
})