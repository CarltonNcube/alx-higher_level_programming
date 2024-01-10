$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    $('#list_movies').empty();
    movies.forEach(function (movie) {
      $('<li>').text(movie.title).appendTo('#list_movies');
    });
  });
});
