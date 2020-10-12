#!/bin/bash

#usage
# ./decrypt.sh -i <input_file> -u <user_password>
#Generates the decrypted file

while getopts i:u: flag
do
    case "${flag}" in
        i) input_file=${OPTARG};;
        u) user_password=${OPTARG};;
    esac
done

filename=$(basename -- "$input_file")
extension="${filename##*.}"
filename="${filename%.*}"

output_file="${filename}_dec.${extension}"

qpdf --decrypt --password=$user_password $input_file $output_file

if [ $? -eq 0 ]; then
	echo "Successfully decrypted. Created ${output_file}"
else
	echo "Error while decrypting"
fi
