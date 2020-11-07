/*
Vou chamar o JavaScript de JS
A função alert gera uma janela pop-up passando informações ao usuário
As informações que se quer mostrar no pop-up deve estar contidas na variável antes do alert.
O JS é tipagem dinâmica, o mesmo vai entender o que a variável é, se estiver dentro de aspas duplas o JS
 vai entender que é uma string e não um número.
*/


//var lista = ["jaca", "melão", "abacate"];
//lista.push("uva"); // o push insere a informação no final da lista
//lista.pop(); // o pop exclui o último elemento da lista. 
// console.log(lista.length); // se inserir o .length irá mostrar a quantidade de elementos na lista
//console.log(lista.reverse()); // o .reverse lista os elementos de trás para frente
//console.log(lista.toString()); // o .toString faz o elemento perder a condição de array.
//console.log(lista.join(' | ')); // o join transforma em string e insere um separador que vc escolheu.
//alert(lista[1]);


//var nome = "Jefferson Klamas"
//var idade = 25
//var idade2 = 15
//var frase = "Azerbaijão é o melhor time do mundo!!!"
// o sinal de mais dentro do alert diz ao JS que esta concatenando uma ou mais variáveis
//alert("Bem vindo " + nome + " você tem " + idade + " anos ");

/* Para ativar o console insira no arquivo a opção abaixo, assim poderá verificar a evolução de sua 
de sua página no próprio navegador, pressionando no navegador a tecla F12 ou no meio da página
pressionando o botão direito do mouse e ir em inspecionar.
console.log seguido do nome da variável
*/

//console.log(nome);
//console.log(nome + idade);

// Com os números é possível fazer todas as operações.

//console.log(idade + idade2);
//console.log( idade / idade2);

/* Caso se queira mudar o que a variável vai apresentar é possível alterar no console.log incluindo após
a variável o sinal de . seguido de replace
Pode ser usado também no alert.
*/
//console.log(frase.replace("Azerbaijão","Brasil"));
// deixando em caixa baixa ou alta
//console.log(frase.toLowerCase())
//console.log(nome.toUpperCase())
//alert(frase.replace("Azerbaijão", "Brasil"));

// criar um dicionário

/*
var carro = {nome:"Jeep", cor:"Azul"} // cria o dicionário fica entre {} em vez de usar uma posição, se usa o nome.
console.log(carro.nome); // neste caso podemos inserir a posição como ex: nome.
alert(carro.cor);
*/

/*
var carro = [{nome:"Jeep", cor:"Azul"}, {nome:"MiniCooper", cor:"Vermelho"}] // criando uma lista de dicionários inicia com [] e dentro dos {}
console.log(carro); // neste caso podemos inserir a posição como ex: nome.
alert(carro[1].nome);
*/

// Condicionais, laços de repetição e Date
/*
var idade = prompt("Informe a sua idade atual?"); // O comando prompt irá fazer uma pergunta ao usuário
                                                  // o que for respondido irá verificar na variável idade
//var idade = 18;
if( idade >= 18){
    alert("maior de idade");
}else{
    alert("menor de idade");
};
*/


// Laços de Repetição while e for

/*
var count = 0;
while (count <=5){
    console.log(count);
    // alert(count); // este alert vai criar uma janela onde vai contar de um em um. 
    count++; // o count também pode ser escrito como count++ irá fazer a mesma coisa que count = count +1
}
*/

// Outra estrutura de repetição for
/*
var count; // no for não é necessário declarar a variável  no próprio for você informa.
for (count=0; count <= 5; count++){
    alert(count);
}
*/

// Trabalhando com data
/*
var d = new Date(); // somente esta varipavel DATE vai informar um pop a data em formato americano
alert(d.getMonth()+1); // O getMonth vai sempre contar do zero então inclua o +1
alert(d.getDay());
alert(d.getHours());
alert(d.getMinutes());
*/

// Trabalhando com funções

/*
function soma (n1 , n2){
    return n1 + n2;
}


function validaIdade(idade){
    var valida;
    if (idade >=18){
        validar = true
    }else{
        validar = false
    }
    return validar;
}

var idade = prompt ("Qual é a sua idade?");
console.log(validaIdade(idade));

/*
function setReplace(frase, nome, nome2){
    return frase.replace(nome, nome2)
}
*/

///alert(soma(30,15));

// alert(setReplace("Vai Alemanha", "Atlético/PR", "Grêmio/RS"));

// Criando botões

function clicou(){
    document.getElementById("Opa, Obrigado").innerHTML="<b>Obrigado por clicar!!!</b>";
    //console.log(document.getElementById("Opa, Obrigado"));
    //alert("Obrigado por clicar ;)");
}

function redireciona(){
    window.open("https://pt.babbel.com/"); // esta abre uma nova janela
    //window.location.href = "https://pt.babbel.com/";  // esta abre o site substituindo o site atual..
}

function trocar(elemento){
    //document.getElementById("mousemove").innerHTML="<b>Obrigado por passar o mouse</b>";
    elemento.innerHTML = "<b>Obrigado por passar o mouse</b>";
    //alert("trocar texto"); // o onmouseover faz com que ao passar o mouse na tela abrirá uma pop. ou o que estiver definido.
}

function voltar(elemento){
    //document.getElementById("mousemove").innerHTML="<b>Passe o Mouse aqui!!!</b>";
    elemento.innerHTML = "<b>Passe o Mouse aqui!!</b>";
    //alert("trocar texto"); // o onmouseover faz com que ao passar o mouse na tela abrirá uma pop. ou o que estiver definido.
}

function load(){
    alert("Página carregada!!!!!");
}

function funcaoChange(elemento){
    console.log(elemento.value);
}


