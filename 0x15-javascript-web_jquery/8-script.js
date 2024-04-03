/** @format */

$.get(
  "https://swapi-api.alx-tools.com/api/films/?format=json",
  function (data, _) {
    $.each(data.results, function (_, el) {
      $("#list_movies").append(el.title + "</br>");
    });
  }
);
