/**
 * Javascripts do Branden Scale Portal
 */

var urlBase = 'http://localhost:5000/';

$(document).ready(function() {
    cadastraActions();
});

function restCall(url, type, data, success, error){
    var request = $.ajax({
            type: type,
            url: url,
            data: data,
            success: success,
            error: error
    });
}

function cadastraActions(){
    /*$('#mybutton').click(myfunction);*/
}

function exampleRestCall(){
    var url = urlBase + 'resturi?parameter=value';
    var type = 'GET';
    var data = null;

    var success = function(data, textStatus, jqXHR) {
        //trataResultado(data);
    };

    var error = function(jqXHR, textStatus, errorThrown) {
        console.log('Erro na chamada exampleRestCall() ');
        //montaPaginaDeErro();
    };
    
    restCall(url, type, data, success, error);  
}

