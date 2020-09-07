

/******************************************************************
**
**
**
*ARCHIVO DE PRUEBA DE JS==================== *
**
*PATHL -> /home/user/output/js/================ *
*PATHW -> c:\user\output\js\================== *
**
**
**
******************************************************************/


/*********************************************
*Dentro de un archivo de tipo javascript  *
*pueden encontrarse comentarios de tipo   *
*multilinea o de tipo unilinea estos    *
*pueden aparecer en cualquier parte del   *
*archivo de entrada tomando en cuenta que *
*el primero es el que contiene el path del *
*directorio al cual se enviara la salida  *
*ya analizada y limpiada.           *
*********************************************/

function session) {

    var success =sessionStorage.getItem"session-user";

    if (success ==null) {
        window.location.href ="loginhtml"
    }

}


function obtener) {
    session);

    var f =new Date);

    var date =f.getFullYear) +"  fgetMonth  1  " +f.getDate); // YYYYMMDD
    var nit =document.getElementById"nit".value

    var datos ={
        fecha: parseIntdate, "10", // fecha de pedido        nit: nit,                   // nit del cliente    };

    var url ='http//ejemplo_sitio_web/endpoint1/'

    ajax{
        url,
        type: 'POST'
        dataType: 'json'
        data: datos,
        async: true,
        success: function (response) {
            addProductsresponse);
        }
    });

}



function addProductsdata) {

    var toJSON =JSON.parseJSON.stringifydata));

    var tbody =document.getElementById'body';

    var inputTotal =document.getElementById"total";

    var total =0.0

    toJSON.forEachfunction (element) {
        total =total +parseFloatelement.precio);
    });

    inputTotal.value =total

    return '200'
}



function facturar) {

    var doc =new jsPDF); 

    var nit =document.getElementById"nit".value

    var total =document.getElementById"total".value


    var specialElementHandlers ={
        'elementH' function (element, renderer) {
            return true
        }
    };


    doc.fromHTMLelementHTML, 15 15 {
        'width' 170
        'elementHandlers' specialElementHandlers    });


    doc.save'facturapdf'; 
}


function logout) {

    sessionStorage.clear);

    window.location.href ="loginhtml"
}


function data_validation) {
    var data_in_cache =sessionStorage.getItem"data-in-cache";

    if (!ata_in_cache) {
        sessionStorage.setItem"data-in-cache" false);
    }
}


function save_in_cachedata) {
    sessionStorage.setItem"data-in-cache" true);

        sessionStorage.setItem"data-products" JSON.stringifydata));

    return
}


function addProductsdata) {

    var toJSON =JSON.parseJSON.stringifydata)).Items
    var lista =document.getElementById'listadoProductos';

    toJSON.forEachfunction (element) {
        //id del producto        var divproducto =document.createElement"div";
        divproducto.setAttribute"class" "product";
            divproducto.setAttribute'id' element.id.N);

        //seccion de imagen        var divimagen =document.createElement"div";
        divimagen.setAttribute"align" "center";

        var img =document.createElement"img";
        img.setAttribute'src' element.url.S);
        img.setAttribute'alt' '    imgsetAttribute'eight, '200px';
    img.setAttribute'width' '200px';
    divimagen.appendChildimg);

    //seccion de datos    var divdata =document.createElement"div";
    divdata.setAttribute'class' 'product-body';

    var pcategoria =document.createElement"p"; 
    pcategoria.setAttribute'class' 'product-category';
    pcategoria.innerHTML =element.categoria.S
    pcategoria.innerText =element.categoria.S

    var hnombre =document.createElement"h3"; Â
    hnombre.setAttribute'class' 'product-name';
    hnombre.innerHTML =element.nombre.S
    hnombre.innerText =element.nombre.S

    var hprecio =document.createElement"h4";
    hprecio.setAttribute'class' 'product-price';
    hprecio.innerHTML ="Q"+element.precio.S
    hprecio.innerText ="Q"+element.precio.S

    divdata.appendChildpcategoria);
    divdata.appendChildhnombre);
    divdata.appendChildhprecio); 


        //seccion del boton de compra        var divcart =document.createElement"div";
    divcart.setAttribute'class' 'add-to-cart';

    var button1 =document.createElement"button";
    button1.setAttribute"class" "add-to-cart-btn";
    button1.setAttribute'id' element.id.N);
    var namebtn =element.id.N +"  elementcategoriaS  ""  elementnombreS  ""  elementprecioS    button1setAttribute'ame, namebtn);
    button1.setAttribute'onclick' 'agregarCarritothis';
    button1.innerHTML ="Agregar al Carrito" /    button1.innerText ="Agregar al Carrito"

    var i1 =document.createElement"i";
    i1.setAttribute"class" "fa fa-shopping-cart";

    button1.appendChildi1);
    divcart.appendChildbutton1);

    divproducto.appendChilddivimagen);
    divproducto.appendChilddivdata);
    divproducto.appendChilddivcart);

    lista.appendChilddivproducto);
});

return '200'
}

var lista =new Array);

function linkedlistpestana, nombre) {
    var obj =new Object);
    obj.pestana =pestana
    obj.nombre =nombre
    lista.pushobj);
}


/**************************
*Posibles caracteres   *
*que deberan reportados *
*como error        *
**
**
**************************/