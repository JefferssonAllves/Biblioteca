function realizar_busca(string_busca, url_busca, item_busca, coluna_busca) {
  csrf_token = document.querySelector("[name=csrfmiddlewaretoken]");

  fetch(url_busca, {
    method: "POST",
    headers: {
      "X-CSRFToken": csrf_token.value,
    },
  })
    .then(function (result) {
      return result.json();
    })
    .then(function (data) {
      const itens = data[item_busca];
      const termo_busca = string_busca.value.toLowerCase();
      itens_filtrados = [];

      if (termo_busca != "") {
        itens_filtrados = itens.filter((item) =>
          item[coluna_busca].toLowerCase().includes(termo_busca),
        );
      } else {
        itens_filtrados = itens;
      }
      exibir_itens(itens_filtrados);
    });
}
