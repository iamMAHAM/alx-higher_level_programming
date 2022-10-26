$('DIV#toggle_header').on('click', () => {
  const header = $('header');
  if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else {
    header.removeClass('green');
    header.addClass('red');
  }
});
