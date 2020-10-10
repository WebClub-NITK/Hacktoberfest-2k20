const readline = require('readline')
const reader = readline.createInterface(process.stdin, process.stdout)

function findClass(str){ 
    // Calculating first occurrence of '.' in str 
    const index = str.indexOf('.'); 
    // First octate in str in decimal form 
    const ipsub = str.substring(0,index); 
    const ip = parseInt(ipsub); 
    // Class A 
    if (ip>=1 && ip<=126) 
        return "A"; 
    // Class B 
    if (ip>=128 && ip<=191) 
        return "B"; 
    // Class C 
    if (ip>=192 && ip<223) 
        return "C"; 
    // Class D 
    if (ip >=224 && ip<=239) 
        return "D"; 
    // Class E 
    return "E"; 
}

reader.question("Enter the IPv4 address: ", data => {
    console.log("This is a class " + findClass(data) + " IPv4 address.")
    reader.close()
})