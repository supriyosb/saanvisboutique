$(document).ready(function () {
    $('#btnSubmit').show();
    $('#btnUpdate').hide();
    $('#btnCancel').hide();
    BindCustomer();
    alert(getCookie("jwt-access-token"));
});

$('#btnCancel').click(function() {
    $('#btnSubmit').show();
    $('#btnUpdate').hide();
    $('#btnCancel').hide();
    $('#txtCustomerName').val('');
    $('#txtCustomerPhone').val('');
});

$('#btnSubmit').click(function () {

    let customerName = $('#txtCustomerName').val();
    let customerPhone = $('#txtCustomerPhone').val();

    $.ajax({
        type: 'POST',
        dataType: 'json',
        data: {
            "name": customerName,
            "phone_no": customerPhone
        },

        url: "http://127.0.0.1:8000/api/customer/create",
        beforeSend: function (xhr) {
            xhr.setRequestHeader("Authorization", "Basic YWRtaW46YWRtaW4=");
        },
        error: function (xhr, status, error) {

            var err_msg = ''
            for (var prop in xhr.responseJSON) {
                err_msg += prop + ': ' + xhr.responseJSON[prop] + '\n';
            }

            bootstrapFailureAlert(err_msg);
        },
        success: function (result) {
         
            BindCustomer();
            bootstrapSuccessAlert("Customer successfully added");

            $('#txtCustomerName').val("");
            $('#txtCustomerPhone').val("");
        }
    });
});

$('#btnUpdate').click(function () {

    let customerId = $('#custId').val()
    let customerName = $('#txtCustomerName').val();
    let customerPhone = $('#txtCustomerPhone').val();

    $.ajax({
        type: 'PUT',
        dataType: 'json',
        data: {
            "name": customerName,
            "phone_no": customerPhone
        },

        url: "http://127.0.0.1:8000/api/customer/update/"+customerId,
        beforeSend: function (xhr) {
            xhr.setRequestHeader("Authorization", "Basic YWRtaW46YWRtaW4=");
        },
        error: function (xhr, status, error) {

            var err_msg = ''
            for (var prop in xhr.responseJSON) {
                err_msg += prop + ': ' + xhr.responseJSON[prop] + '\n';
            }

            bootstrapFailureAlert(err_msg);
        },
        success: function (result) {
         
            BindCustomer();
            bootstrapSuccessAlert("Customer successfully updated");


            $('#txtCustomerName').val("");
            $('#txtCustomerPhone').val("");
            $('#btnSubmit').show();
            $('#btnUpdate').hide();
            $('#btnCancel').hide();
        }
    });
});

function BindCustomer() {
    $.ajax({
        type: 'GET',
        dataType: 'json',
        beforeSend: function (xhr) {
            xhr.setRequestHeader("Authorization", "Basic YWRtaW46YWRtaW4=");
        },
        url: "http://127.0.0.1:8000/api/customer/", success: function (result) {
           
            var totalCount = result.length;
            var structureDiv = "";
            for (let i = 0; i < totalCount; i++) {
                structureDiv += "<tr>" +
                    "     <td>" + result[i].id + "</td>" +
                    "      <td>" + result[i].name + "</td>" +
                    "              <td>" + result[i].phone_no + "</td>" +
                    "              <td><button class='btn btn-primary' onclick='EditRow(" + result[i].id + ", \"" + result[i].name + "\", \"" + result[i].phone_no + "\")'>Edit</button></td>" +
                    "              <td><button class='btn btn-primary' onclick='return confirm(\"Are you sure you want to delete this record?\",DeleteRow(" + result[i].id + "))'>Delete</button></td>" +
                    "           </tr>";
            }

            $("#divBody").html(structureDiv);
      
        }
    });

}

function EditRow(id, name, phoneNo) {
    $('#btnSubmit').hide();
    $('#btnUpdate').show();
    $('#btnCancel').show();
    $('#custId').val(id);
    $('#txtCustomerName').val(name);
    $('#txtCustomerPhone').val(phoneNo);
    $('#txtCustomerName').focus();
}

function DeleteRow(id) {
    
    $.ajax({
        type: 'DELETE',
        dataType: 'json',
        beforeSend: function (xhr) {
            xhr.setRequestHeader("Authorization", "Basic YWRtaW46YWRtaW4=");
        },
        url: "http://127.0.0.1:8000/api/customer/delete/"+id,
        error: function (xhr, status, error) {

            var err_msg = ''
            for (var prop in xhr.responseJSON) {
                err_msg += prop + ': ' + xhr.responseJSON[prop] + '\n';
            }

            bootstrapFailureAlert(err_msg);
        },
        success: function (result) {
            bootstrapSuccessAlert("Customer successfully deleted");
            BindCustomer();
        }
    });
}

function bootstrapSuccessAlert(msg){
    $.bootstrapGrowl(msg, {
        type: "success",
        offset: {from: "top", amount: 100},
        align: "center",
        width: "auto",
        delay: 2000,
        allow_dismiss: true,
        stackup_spacing: 10,
        allow_dismiss: false
    });
}

function bootstrapFailureAlert(msg){
    $.bootstrapGrowl(msg, {
        type: "danger",
        offset: {from: "top", amount: 100},
        align: "center",
        width: "auto",
        delay: 2000,
        allow_dismiss: true,
        stackup_spacing: 10,
        allow_dismiss: false
    });
}

function getCookie(cName) {
    const name = cName + "=";
    const cDecoded = decodeURIComponent(document.cookie); //to be careful
    const cArr = cDecoded .split('; ');
    let res;
    cArr.forEach(val => {
        if (val.indexOf(name) === 0) res = val.substring(name.length);
    })
    return res;
}