const dragContainers = document.querySelectorAll(".livros-categoria");

dragContainers.forEach((dragContainer) => {
  let isDragging = false;
  let startX;
  let scrollStart;

  dragContainer.addEventListener("mousedown", (e) => {
    isDragging = true;
    dragContainer.style.cursor = "grabbing";
    startX = e.pageX;
    scrollStart = dragContainer.scrollLeft;
  });
  dragContainer.addEventListener("mousemove", (e) => {
    if (!isDragging) return;
    const x = e.pageX - startX;
    dragContainer.scrollLeft = scrollStart - x;
  });
  dragContainer.addEventListener("mouseup", () => {
    isDragging = false;
    dragContainer.style.cursor = "grab";
  });
  dragContainer.addEventListener("mouseleave", () => {
    isDragging = false;
  });
  window.addEventListener("mouseup", () => {
    isDragging = false;
  });
});


function vender_livro() {
  console.log('teste');
}