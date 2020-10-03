const username = document.getElementById('username')
const password = document.getElementById('password')
const form = document.getElementById('form')
const PasswordCheck = document.getElementById('PasswordCheck')
const dot =document.getElementById('dot')

username.focus();
password.addEventListener("keydown", checkPassword,false);
password.addEventListener("keyup", checkPassword,false);

function checkPassword() {
    console.log(password.value);
    if (password.value == null || password.value == ''){ 
        PasswordCheck.innerText ="Enter Password";
        dot.style.backgroundColor = '#f6f6f6';
    }
    else {
        if (password.value.length < 7 ){
            PasswordCheck.innerText ="Easy";
            dot.style.backgroundColor = 'red';
        }
        else if (password.value.match(/[a-z]/g) && password.value.match(/[A-Z]/g) && password.value.match(/[0-9]/g)) {
            if (password.value.length < 12){
                PasswordCheck.innerText = "Hard";
                dot.style.backgroundColor = 'Purple';
            } else {
                PasswordCheck.innerText = "Very Hard";
                dot.style.backgroundColor = 'Green';
            }
        }
        else if (password.value.match(/[a-z]/g) && password.value.match(/[A-Z]/g)) {
            PasswordCheck.innerText = "Hard";
            dot.style.backgroundColor = 'Purple';
        }
        else if(password.value.match(/[a-z]/g) && password.value.length > 10){
            PasswordCheck.innerText = "Medium";
            dot.style.backgroundColor = 'Blue';
        }
        else if(password.value.match(/[a-z]/g)&& password.value.length < 7){
            PasswordCheck.innerText = "Easy";
            dot.style.backgroundColor = 'Red';
        }

} }

function ShowPassword() {
    if (password.type == "password") {
        password.type = "text";
    } else {
        password.type = "password";
    }
}
