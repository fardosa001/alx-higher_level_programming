$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function(data) {
      // Update the content of #character with the character name
      $('#character').text(data.name);
    },
});