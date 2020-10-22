import Foundation

print("Enter the IP address")
let IP_Addr = readLine()
// Converts input into a string, and seperates the 4 parts into an array
var IP_Addr_Str = String(IP_Addr!)
let parts = IP_Addr_Str.components(separatedBy: ".")
// Warning: input must be made up of only numbers and '.'

// Validates user input
var valid_IP = true
for var part in parts {
  let partInt = Int(part)
  if partInt! < 0 || partInt! > 255 {
    print("Please enter a valid IP address.")
    valid_IP = false
  }
}

// Finds class of IP address
let firstPart = parts[0]
let firstPartInt = Int(firstPart)
if firstPartInt! <= 127 && firstPartInt! >= 1 {
  print("This is a class A IPv4 address.")
} else if firstPartInt! <= 191 && firstPartInt! >= 128 {
  print("This is a class B IPv4 address.")
} else if firstPartInt! <= 223 && firstPartInt! >= 192 {
  print("This is a class C IPv4 address.")
} else if firstPartInt! <= 239 && firstPartInt! >= 224 {
  print("This is a class D IPv4 address.")
} else if firstPartInt! <= 255 && firstPartInt! >= 240 {
  print("This is a class E IPv4 address.")
}