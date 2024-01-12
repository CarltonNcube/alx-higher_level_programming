$(document).ready(function() {
  function fetchAndPrintTranslation() {
    var languageCode = $("#language_code").val();

    $.ajax({
      url: "https://www.fourtonfish.com/hellosalut/hello/",
      type: "GET",
      data: { lang: languageCode },
      success: function(response) {
        $("#hello").text(response.hello);
      },
      error: function(error) {
        $("#hello").text("Error fetching translation");
      }
    });
  }

  $("#btn_translate").click(fetchAndPrintTranslation);

  $("#language_code").keypress(function(event) {
    if (event.which === 13) {
      fetchAndPrintTranslation();
    }
  });
});
