function load_frame(target_url) {
  console.log("in load_frame() drin");
  url=target_url;
  document.getElementById("content").src=url;
}
console.log("sind in scripts.js")