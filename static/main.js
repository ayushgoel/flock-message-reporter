function setCurrentMonthInInput() {
  console.log("Tried to set month in input. Disabled right now");
}

$('#form-submit-button').click(function (a, c) {
  console.log("Form being submitted", a, c);
  return false;
});
