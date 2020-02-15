let biodata={
    name:"Dwi Alendra Ipang Selly",
    age:22,
    address:"Jln Taebenu Kota Kupang, NTT",
    hobbies:["Membaca","Coding"],
    is_married:false,
    list_school:[
        {
            name:"SDI Naimata",
            year_in:2004,
            yeaer_out:2010,
            major:null
        },
        {
            name:"SMPN 11 Kupang",
            year_in:2010,
            yeaer_out:2013,
            major:null
        },
        {
            name:"SMAN 4 Kupang",
            year_in:2013,
            yeaer_out:2016,
            major:null
        }
    ],
    skills:[
        {
            skill_name:"Programming with Python",
            level:"beginner"
        },
        {
            skill_name:"Programming with Javascript",
            level:"advanced"
        }
    ],
    interest_in_coding:true
}

function getMyBiodata(){
    return JSON.stringify(biodata)
}

// tampilkan return value dengan console.log
console.log(getMyBiodata())