function vender_livro() {
  console.log("teste");
}

function adicionar_carrinho(element) {
  livro_id = document.getElementById("livro_id").value;
  csrftoken = document.querySelector("[name=csrfmiddlewaretoken]");

  data = new FormData();
  data.append("livro_id", livro_id);


  if (element.className == "mdi mdi-heart-outline") {
    element.className = "mdi mdi-heart text-danger";
    url = "../clientes/add_livro_carrinho/";

  } else {
    element.className = "mdi mdi-heart-outline";
    url = "../clientes/rm_livro_carrinho/";
  }
  fetch(url, {
    method: "POST",
    headers: {
      "X-CSRFToken": csrftoken.value,
    },
    body:data
  })
}