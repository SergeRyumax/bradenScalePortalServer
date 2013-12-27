/**
 * Javascripts do Branden Scale Portal
 */

var urlBase = 'http://localhost:5000/';
var userToken = 'tokenFanfarrao';

$(document).ready(function() {
    cadastraActions();
    getAvalicoesBraden();
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

function getAvalicoesBraden(){
    var url = urlBase + 'user/' + userToken + '/calendario/2012-12-10';
    var type = 'GET';
    var data = null;

    var success = function(data, textStatus, jqXHR) {
        console.log('Sucesso ao recuperar Avaliações');
        buildIndex(data);
    };

    var error = function(jqXHR, textStatus, errorThrown) {
        console.log('Erro na chamada exampleRestCall() ');
        //montaPaginaDeErro();
    };
    
    restCall(url, type, data, success, error);  
}

function buildIndex(avaliacoes){
    for (var i = 0; i < avaliacoes.length; i++) {
        var avaliacao = avaliacoes[i];
        var div = $('#divAvaliacoes');
        var box = createBox(avaliacao, i);
        div.append(box);
        div.append('<br/><br>');
    }
}

function createBox(avaliacao, index){
    var brandenArray = avaliacao['avaliacoesBraden'];
    var box = $('<div></div>');
    box.attr('id', 'avaliacao_' + index);
    box.append('<p>Andar: ' + avaliacao['andar'] + '</p>');
    box.append('<p>Número: ' + avaliacao['numero'] + '</p>');
    for (var i = 0; i < brandenArray.length; i++) {
        var branden = brandenArray[i];
        var subbox = $('<div></div>');
        subbox.attr('id', 'branden_' + branden['id']);
        subbox.append('<p>Paciente: ' + branden['paciente'] + '</p>');
        subbox.append('<p>Enfermeiro: ' + branden['enfermeiro'] + '</p>');
        subbox.append('<p>Percepção Sensorial: ' + branden['percepcaoSensorial'] + '</p>');
        subbox.append('<p>Umidade: ' + branden['umidade'] + '</p>');
        subbox.append('<p>Nutrição: ' + branden['nutricao'] + '</p>');
        subbox.append('<p>Fricção: ' + branden['friccao'] + '</p>');
        subbox.append('<p>Mobilidade: ' + branden['mobilidade'] + '</p>');
        subbox.append('<p>Status: ' + branden['status'] + '</p>');
        subbox.append('<p>Hora: ' + branden['hora'] + '</p>');
        subbox.append('<p>Atividade: ' + branden['atividade'] + '</p>');
    }
    box.append(subbox);
    return box;
}