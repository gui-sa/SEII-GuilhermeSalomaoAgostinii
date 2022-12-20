var valor;
var resultado;

//document se refere ao objeto total da pagina... o restante são os IDs/Class
function botao(num){
    valor = document.calc.visor.value += num;
}

function reseta(){
    valor = document.calc.visor.value = "";    
}

function calcula(){
    resultado = eval(valor);
    document.calc.visor.value = resultado.toLocaleString('pt-br');    

}