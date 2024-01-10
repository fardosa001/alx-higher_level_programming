$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(data) {
      // Iterate through each movie and append the title to #list_movies
      $.each(data.results, function(index, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
    });
    }
});