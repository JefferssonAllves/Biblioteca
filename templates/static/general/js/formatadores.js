function mascaraCPF(input) {
  var valor = input.value;

  valor = valor.replace(/\D/g, "");


  valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
  valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
  valor = valor.replace(/(\d{3})(\d{1,2})$/, "$1-$2");

  input.value = valor;
}
function mascaraTelefone(input) {
  let valor = input.value.replace(/\D/g, "");

  if (valor.length <= 10) {
    valor = valor.replace(/(\d{2})(\d{0,5})(\d{0,4})/, "($1) $2-$3");
  } else {
    valor = valor.replace(/(\d{2})(\d{5})(\d{4})/, "($1) $2-$3");
  }
  input.value = valor;
}