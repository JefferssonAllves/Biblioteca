function switch_sidebar() {
  body = document.body;
  if (body.className == "sidebar-absolute" || body.className == "sidebar-icon-only") {
    document.body.className = "sidebar-hidden";
  } else {
    document.body.className = "sidebar-icon-only";
  }
}
