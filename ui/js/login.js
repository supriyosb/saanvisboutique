$('#btnSubmit').click(function () {

    let username = $('#txtUsername').val();
    let password = $('#txtPassword').val();

    $.ajax({
        type: 'POST',
        dataType: 'json',
        data: {
            "username": username,
            "password": password
        },
        url: "http://127.0.0.1:8000/api/token/",
        error: function (xhr, status, error) {

            var err_msg = ''
            for (var prop in xhr.responseJSON) {
                err_msg += prop + ': ' + xhr.responseJSON[prop] + '\n';
            }

            bootstrapFailureAlert(err_msg);
        },
        success: function (result) {
            bootstrapSuccessAlert("Login successful");
            document.cookie = "jwt-token=srgf";
            //setCookie("jwt-access-token", result.access, 1);
            //alert(getCookie("jwt-access-token"));
            //location.href = "customer.html";
            //alert(result.access);
        }
    });
});

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

function setCookie(cName, cValue, expDays) {
    let date = new Date();
    date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = cName + "=" + cValue + "; " + expires + "; path=/";
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