function setCurrentMonthInInput() {
  console.log("Tried to set month in input. Disabled right now");
  //FIXME: Set current month
  $('#failure-alert').hide();
}

function failureAlert() {
  return `<div class="alert alert-danger" role="alert" id="failure-alert">
    <!-- <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button> -->
    <strong>Error!</strong> Please choose a month before submitting.
  </div>`;
}

var table_index = 1;
function tableHead(value) {
  var h = document.createElement('th')
  h.appendChild(document.createTextNode(value));
  return h;
}
function createAndAppendRow(data) {
  var row = document.createElement('tr');
  row.appendChild(tableHead(table_index));
  table_index++;
  row.appendChild(tableHead(data.messageUids[0]));
  row.appendChild(tableHead(data.userName));
  row.appendChild(tableHead(data.userId));
  row.appendChild(tableHead(data.chatName));
  row.appendChild(tableHead(data.chat));
  row.appendChild(tableHead(data.reportTime));

  var tableBody = $('#table-body');
  tableBody.append(row);
}

$('#form-submit-button').click(function (event, c) {
  var month = $('#form-month-input').val();
  console.log("Form being submitted", event, c, month);
  if (typeof month === 'undefined' || month === '') {
    $('#failure-alert').show();
    setTimeout(function() {
      $('#failure-alert').hide();
    }, 2000);

    console.log("No month on page.");
    return false;
  }

  console.log("Got Month", month);

  var data = {'month': month};
  $.ajax({
    url: '/report-message/history',
    type: 'POST',
    data: JSON.stringify(data),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    success: function(UIDs) {
      // Empty old results from table
      $('#table-body').empty();
      table_index = 1;

      UIDs.forEach(function(UID, index, array) {

        var data = {'UID': UID};
        // FIXME: Refactor
        $.ajax({
          url: '/report-message/UID',
          type: 'POST',
          data: JSON.stringify(data),
          contentType: 'application/json; charset=utf-8',
          dataType: 'json',
          success: function(data) {
            console.log(data);
            createAndAppendRow(data);
          }
        });

      });

    }
  });
  return false;
});
