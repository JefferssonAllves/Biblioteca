function fetch_livros() {
  $("#tabela-livros #corpo-tabela tr").on("click", function () {
    id = $(this).find("td:first").text().trim();
    csrf_token = document.querySelector("[name=csrfmiddlewaretoken]");

    url = ("/livros/update/id=" + id + "/").replace(/\s+/g, "");
    window.location.href = url;

    fetch(url, {
      method: "POST",
      headers: {
        "X-CSRFToken": csrf_token.value,
        "Content-Type": "application/json",
      },
    })
      .then(function (result) {
        return result.json();
      })
      .then(function (data) {
        console.log(data);
      });
  });
}
$(document).ready(function () {
  fetch_livros();
});

$(document).ready(function () {
  $("#tabela-categorias tbody tr").on("click", function () {
    id = $(this).find("td:first").text().trim();
    csrf_token = document.querySelector("[name=csrfmiddlewaretoken]");

    url = ("/livros/categorias/update/id=" + id + "/").replace(/\s+/g, "");
    window.location.href = url;

    fetch(url, {
      method: "POST",
      headers: {
        "X-CSRFToken": csrf_token.value,
      },
    })
      .then(function (result) {
        return result.json();
      })
      .then(function (data) {
        console.log(data);
      });
  });
});
function mostrar_adicionar_livro() {
  container = document.getElementById("container-adicionar-livros");

  if (container.style.display == "block") {
    container.style.display = "none";
  } else {
    container.style.display = "block";
    window.scrollTo({
      top: 600,
      left: 0,
      behavior: "smooth",
    });
  }
}
function excluir_livro() {
  livro_id = document.getElementById("livro_id").value;
  csrf_token = document.querySelector("[name=csrfmiddlewaretoken]");

  data = new FormData();
  data.append("livro_id", livro_id);

  url = "/livros/delete/";
  fetch(url, {
    method: "POST",
    headers: {
      "X-CSRFToken": csrf_token.value,
    },
    body: data,
  })
    .then(function (result) {
      return result.json();
    })
    .then(function (data) {
      window.location.href = data["redirect"];
      container = document.getElementById("mensagem-livro");
      span = document.getElementById("mensagem-span");

      if (data["response"] == 200) {
        container.style.display = "block";
        span.innerHTML = 'Livro excluido com sucesso!';
      }
    });
}

function mostrar_adicionar_categoria() {
  container = document.getElementById("container-adicionar-categorias");

  console.log('teste')
  if (container.style.display == "block") {
    container.style.display = "none";
  } else {
    container.style.display = "block";
    window.scrollTo({
      top: 600,
      left: 0,
      behavior: "smooth",
    });
  }
}
function excluir_categoria() {
  categoria_id = document.getElementById("categoria_id").value;
  csrf_token = document.querySelector("[name=csrfmiddlewaretoken]");

  data = new FormData();
  data.append("categoria_id", categoria_id);

  url = "/livros/categorias/delete/";
  fetch(url, {
    method: "POST",
    headers: {
      "X-CSRFToken": csrf_token.value,
    },
    body: data,
  })
  .then(function (result) {
    return result.json();
  })
  .then(function (data) {
    window.location.href = data["redirect"];
    container = document.getElementById("mensagem-livro");
    span = document.getElementById("mensagem-span");

    if (data["response"] == 200) {
      container.style.display = "block";
      span.innerHTML = "Livro excluido com sucesso!";
    }
  });
}
function exibir_itens(livros) {
  $(document).ready(function () {
    fetch_livros();
  });
  const corpoTabela = document.getElementById("corpo-tabela");
  corpoTabela.innerHTML = "";

  if (livros.length === 0) {
    const novaLinha = $(`
      <tr>
        <td colspan="7">Nenhum livro encontrado</td>
      </tr>
    `);
    $("#corpo-tabela").append(novaLinha);
  } else {
    livros.forEach(livro => {
      class_button_status = ""
      if (livro.status == "Disponível"){
        class_button_status = "btn badge-outline-success";
      }else if (livro.status == "Alugado"){
        class_button_status = "btn badge-outline-warning";
      } else {
        class_button_status = "btn badge-outline-primary";
      }
      const novaLinha = $(`
        <tr>
          <td>${livro.id}</td>
          <td>${livro.titulo}</td>
          <td>${livro.autor}</td>
          <td>${livro.ISBN}</td>
          <td>${livro.categoria}</td>
          <td>${livro.preco_alugar}</td>
          <td>
            <button type="button"
              class="${class_button_status}"
              value="${livro.id}">
                ${livro.status}
            </button>
          </td>
        </tr>
      `);
      $("#corpo-tabela").append(novaLinha);
    });
  }
}
function get_url_livros() {
  return document.getElementById("url_busca").value;
}
function modal_devolver_livro(livro_id) {
  livro_id = livro_id.value;
  console.log('testeeeeeeeeeee')
  modal_escurecer = document.getElementById("container-modal-devolver");
  modal = document.getElementById("modal-devolver");

  if (modal_escurecer.style.display == "block") {
    modal_escurecer.style.display = "none";
    modal.style.display = "none";
  } else {
    document.getElementById("botao-confirmar-devolver").value = livro_id;
    modal_escurecer.style.display = "block";
    modal.style.display = "block";
  }
}