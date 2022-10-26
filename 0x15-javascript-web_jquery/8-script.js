$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: (result) => {
    console.log(result);
    result.results.forEach(res => {
      $('UL#list_movies').append(`<li>${res.title}</li>`);
    });
  }
});
