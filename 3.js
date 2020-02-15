
function countChar(text,char){
    let totalChar=0;
    for(i=0;i<text.length;i++){
        if(text[i]===char){
            totalChar++;
        }
    }
    if(totalChar){
        return totalChar
    }else{
        return "Not Found"
    }
}

//example
console.log(countChar("arka", "a"))
console.log(countChar('aalen','x'))