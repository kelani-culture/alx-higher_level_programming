/** @format */

$.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data, _) {
  $("#hello").text(data.hello);
});
