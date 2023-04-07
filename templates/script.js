

$('.navTrigger').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

}); 
$(window).scroll(function() {
    if ($(document).scrollTop() > 50) {
        $('.nav').addClass('affix');
        console.log("OK");
    } else {
        $('.nav').removeClass('affix');
    }
});
const loginFormEl = document.getElementById("loginForm");
const emailEL = document.getElementById("email");
const emailErrorMsgEl = document.getElementById("emailErrorMsg");
const pswEl = document.getElementById("psw");
const pswErrorMsgEl = document.getElementById("pswErrorMsg");

emailEL.addEventListener("change",function(event){
    if(event.target.value === ""){
        emailErrorMsgEl.textContent = "*Required";
    }else{
        emailErrorMsgEl.textContent = "";
    }
    loginFormEl.emailEL = event.target.value;
});
pswEl.addEventListener("change",function(event){
    if(event.target.value === ""){
        pswErrorMsgEl.textContent = "*Required";
    }else{
        pswErrorMsgEl.textContent = "";
    }
    loginFormEl.pswEl = event.target.value;
});

let formData = {
    email: "",
    psw: ""
}

function validateFormData(formData) {
    let {email, psw} = formData;
    if (email === "") {
      emailErrorMsgEl.textContent = "Required*";
    }
    if (psw === ""){
      pswErrorMsgEl.textContent = "Required*";
    }
  }

loginFormEl.addEventListener("submit",function(event){
    event.preventDefault();
    validateFormData(formData)
    console.log("HEllo");
})