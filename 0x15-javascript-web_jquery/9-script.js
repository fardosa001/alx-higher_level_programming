$(document).ready(function() {
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
      method: 'GET',
      success: function(data) {
        // Update the content of #hello with the fetched translation
        $('#hello').text(data.hello);
      },
    });
});