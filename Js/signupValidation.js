function validateForm() {
    var fname = document.forms["signForm"]["fname"].value;
    var lname = document.forms["signForm"]["lname"].value;
    var mobile = document.forms["signForm"]["mobile"].value;
    var email = document.forms["signForm"]["email"].value;
    var atposition = email.indexOf("@");
    var dotposition = email.lastIndexOf(".");
    var pass = document.forms["signForm"]["password"].value;
    var cpass = document.forms["signForm"]["cpassword"].value;

    if (fname.length < 3) {
        alert("First name must have more than 3 letters!");
        fname.focus();
        return false;
    }

    if (lname.length < 3) {
        alert("Last name must have more than 3 letters!");
        lname.focus();
        return false;
    }

    if (mobile.length != 10) {
        alert("Mobile number must have only 10 digit!");
        mobile.focus();
        return false;
    }

    if (atposition < 1 || dotposition < atposition + 2 || dotposition + 2 >= email.length) {
        alert("Please enter a valid e-mail address \n at postion:" + atposition + "\n dot position:" + dotposition);
        email.focus();
        return false;
    }

    if (pass.length < 6) {
        alert("Password must be at least 6 characters long!");
        pass.focus();
        return false;
    }

    if (pass != cpass) {
        alert("Password must be same!");
        cpass.focus();
        return false;
    }

    // alert("You are registered successfully!");
}

// function registermsg() {
//     if (validateForm() = true) {
//         alert("You are registered successfully!");
//     }
// }