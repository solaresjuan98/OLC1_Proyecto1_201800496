// PATHW: C:\output2\js


/**COMENTARIO ****/
/**

COMENTARIO MULTILINEA

 */

class Coche {
    constructor(modelo, velocidad, antiguedad) {
        this.modelo =modelo;
        this.velocidad =velocidad;
        this.antiguedad =antiguedad;
    }

    aumentarVelocidad() {
        this.velocidad +=1
    }

    reducirVelocidad() {
        this.velocidad -=1
    }


}

//

class Autobus extends Coche {
    constructor(modelo, velocidad, antiguedad) {
        super(modelo, velocidad, antiguedad);

        this.altura =5
    }

    mostrarAltura() {
        return "La altura del bus es: "+this.altura;
    }
}


var autobus1 =new Autobus("Ford", 200, 2000);
console.log(autobus1.mostrarAltura());

var coche1 =new Coche('BMW', 200, 2017);
var coche2 =new Coche('Audi', 100, 2018);
var coche3 =new Coche('Toyota', 150, 2010);
var coche4 =new Coche('Mercedes', 200, 2015);

coche1.aumentarVelocidad();
coche1.aumentarVelocidad();
coche1.aumentarVelocidad();

console.log(coche1);

var x;

if (5==4) {
    return 5* 4
}
else if (10<=33) {
    return false;
}

Math.pow(4, 5);

while (2<=10) {
    return false;
}



if (5!=4) {
    return true;
}

do {

    coche1.aumentarVelocidad();

} while (4==true);







Â
