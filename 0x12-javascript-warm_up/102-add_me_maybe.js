#!/usr/bin/node
module.exports = {
  addMeMaybe: function (number, theFunction) {
    return theFunction(number + 1);
  }
};
