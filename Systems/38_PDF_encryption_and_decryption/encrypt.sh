#!/bin/bash

#usage
# ./encrypt.sh -i <input_file> -u <user_password> -o <owner_password>
#Generates the encrypted file

while getopts i:u:o: flag
do
    case "${flag}" in
        i) input_file=${OPTARG};;
        u) user_password=${OPTARG};;
		o) owner_password=${OPTARG};;
    esac
done

filename=$(basename -- "$input_file")
extension="${filename##*.}"
filename="${filename%.*}"

output_file="${filename}_enc.${extension}"

qpdf --encrypt $user_password $owner_password 40 -- $input_file $output_file

if [ $? -eq 0 ]; then
	echo "Successfully encrypted. Created ${output_file}"
else
	echo "Error while encrypting"
fi
