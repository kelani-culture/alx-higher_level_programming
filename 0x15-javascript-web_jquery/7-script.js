/** @format */

$.get(
  "https://swapi-api.alx-tools.com/api/people/5/?format=json",
  function (data, _) {
    $("#character").text(data.name);
  }
);
