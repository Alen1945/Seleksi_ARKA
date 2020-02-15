

function findHighestProfit(dataSaham){
    selisih=[]
    if(dataSaham.length>2){
        for(i=1;i<dataSaham.length;i++){
            onCheckData=dataSaham.slice(0,i)
            min=Math.min(...onCheckData)
            if(dataSaham[i]>min){
                selisih=[...selisih,dataSaham[i]-min]
            }
        }
    }

    return selisih.length>0? Math.max(...selisih): "Tidak Bisa mendapat profit pada hari-hari ini"
}

console.log(findHighestProfit([10, 2, 11, 20, 3, 5]))
console.log(findHighestProfit([33, 29, 11, 3]))