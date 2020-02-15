
let allowAlphabet="abcdefABCDEF"

function cekHastag(text){
    return text[0]=='#'? true:false
}
function isLengthTrue(text){
    return text.length==4 || text.length==7 ? true:false
}
function cekChar(text){
    statusValid=true
    for(i=0;i<text.length;i++){
        charToCheck=text[0]
        if(parseFloat(charToCheck==NaN)){
            if(!allowAlphabet.includes(charToCheck)){
                statusValid=false;
                break;
            }
        }
    }
    return statusValid
}

function is_Valid_CODEHEX(hex){
    return cekHastag(hex) && isLengthTrue(hex) && cekChar(hex) ? true:false
}


//example
console.log(is_Valid_CODEHEX('#fff'))
console.log(is_Valid_CODEHEX('#8bd0f0'))
console.log(is_Valid_CODEHEX('#azsdf'))