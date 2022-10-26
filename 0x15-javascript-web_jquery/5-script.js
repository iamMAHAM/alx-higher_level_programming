$('DIV#add_item').on('click', () => {
  const ul = $('UL.my_list');
  ul.append('<li>Item</li>');
});
