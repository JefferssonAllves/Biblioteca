function fetch_clientes() {
  $("#tabela-clientes tbody tr").on("click", function () {
    id = $(this).find("td:first").text().trim();
    csrf_token = document.querySelector("[name=csrfmiddlewaretoken]");

    url = ("/clientes/update/id=" + id + "/").replace(/\s+/g, "");
    window.location.href = url;

    fetch(url, {
      method: "GET",
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
}

$(document).ready(function () {
  fetch_clientes();
});

function mostrar_adicionar_cliente() {
  container = document.getElementById("container-adicionar-clientes");

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

function excluir_cliente() {
  cliente_id = document.getElementById("cliente_id").value;
  csrf_token = document.querySelector("[name=csrfmiddlewaretoken]");

  data = new FormData();
  data.append("cliente_id", cliente_id);

  url = "/clientes/delete/";
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
    });
}
function buscar_clientes(){

}
function exibir_itens(clientes) {
  $(document).ready(function () {
    fetch_clientes();
  });
  const corpoTabela = document.getElementById("corpo-tabela");
  corpoTabela.innerHTML = "";
  console.log(clientes.length);

  if (clientes.length === 0) {
    const novaLinha = $(`
      <tr>
        <td colspan="7">Nenhum cliente encontrado</td>
      </tr>
    `);
    $("#corpo-tabela").append(novaLinha);
  } else {
    clientes.forEach((cliente) => {
      const novaLinha = $(`
        <tr>
          <td>${cliente.id}</td>
          <td>${cliente.nome}</td>
          <td>${cliente.cpf}</td>
          <td>${cliente.email}</td>
          <td>${cliente.telefone}</td>
          <td>${cliente.endereco}</td>
        </tr>
      `);
      $("#corpo-tabela").append(novaLinha);
    });
  }
}

function get_url_clientes() {
  return document.getElementById("url_busca").value;
}

function alugar_livro(id) {
  livro_id = id.value;
  csrf_token = document.querySelector("[name=csrfmiddlewaretoken]");

  data = new FormData();
  data.append("livro_id", livro_id);
  url = window.location.href + "alugar_livro/";

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
      window.location.href = window.location.href;
    });
}
function modal_alugar_livro(livro_id) {
  livro_id = livro_id.value;
  modal_escurecer = document.getElementById("container-modal-alugar");
  modal = document.getElementById("modal-alugar");

  if (modal_escurecer.style.display == "block") {
    modal_escurecer.style.display = "none";
    modal.style.display = "none";
  } else {
    document.getElementById("botao-confirmar-alugar").value = livro_id;
    modal_escurecer.style.display = "block";
    modal.style.display = "block";
  }
}
function devolver_livro(emprestimo_id) {
  emprestimo_id = emprestimo_id.value;
  csrf_token = document.querySelector("[name=csrfmiddlewaretoken]");

  data = new FormData();
  data.append("emprestimo_id", emprestimo_id);
  url = window.location.href + "devolver_livro/";
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
      window.location.href = window.location.href;
    });
}
function modal_devolver_livro(livro_id) {
  livro_id = livro_id.value;
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