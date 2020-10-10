package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"regexp"
	"strconv"
)

func IPClass(host string) string {
	byte_list := strings.Split(host, ".")
	
	first_byte, _ := strconv.ParseInt(byte_list[0], 10, 64)

	if first_byte >= 1 && first_byte <= 127 {
		return "A"
	}

	if first_byte >= 128 && first_byte <= 191 {
		return "B"
	}

	if first_byte >= 192 && first_byte <= 223 {
		return "C"
	}

	if first_byte >= 224 && first_byte <= 239 {
		return "D"
	}

	return "E"
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Printf("Type a valid IPv4: ")
	scanner.Scan()
	ip_value := scanner.Text()
	// checks if it's actually a good IPv4
	ip_value = strings.Trim(ip_value, " ")
	rgx, _ := regexp.Compile(`^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$`)
	if rgx.MatchString(ip_value) == false {
		fmt.Println("bad ip address :/")
		os.Exit(1)
	} 
	// gets the class
	ip_class := IPClass(ip_value)
	fmt.Printf("You IPv4 class is: %s\n", ip_class)
	os.Exit(0)
}