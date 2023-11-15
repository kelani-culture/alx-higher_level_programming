#!/usr/bin/node

const fs = require('fs');
arg = process.argv

const files = arg.slice(2);

function concatFile(files) {
    
    for (file of files) {
        fs.readFile(file, "utf-8", (err, data) => {
            if (err){
                console.error(err);
            }
            const content = data
            fs.appendFile(files[files.length-1], content, 'utf-8', (err) => {
                if (err){
                    console.error(err)
                }
                });
            
        });
    }
}
console.log(files)
concatFile(files)