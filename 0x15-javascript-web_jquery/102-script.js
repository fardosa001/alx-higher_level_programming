$(document).ready(function() {
    // Event handler for fetching and displaying translation
    $('#btn_translate').click(function() {
      // Get the language code from the input field
        const languageCode = $('#language_code').val();

        // Fetch translation using the API
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            method: 'GET',
            data: { lang: languageCode },
            success: function(data) {
            // Display the translation in the #hello div
                $('#hello').text(data.hello);
            }
        });
    });
});