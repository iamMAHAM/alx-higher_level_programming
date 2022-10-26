$('document').ready(() => {
  const LI = '<li>Item</li>';
  const ul = $('UL.my_list');

  $('DIV#add_item').on('click', () => {
    ul.append(LI);
  });

  $('DIV#remove_item').on('click', () => {
    ul.find('li:last').remove();
  });

  $('DIV#clear_list').on('click', () => {
    ul.empty();
  });
});
