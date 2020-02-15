
let rgx_username= /^[a-z]{5,9}$/
let rgx_password=/(?=.+[a-z])(?=.*[A-Z])(?=.{3,}[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/

function is_username_valid(username){
  return rgx_username.test(username)
}

function is_password_valid(pass){
    return rgx_password.test(pass)
}


//example
console.log("======= cek username =======")
console.log(is_username_valid('alenAAAA'))
console.log(is_username_valid('alenselly'))

console.log("======= cek password =======")
console.log(is_password_valid('123alenadf'))
console.log(is_password_valid('T3pungB#3r4s!'))

