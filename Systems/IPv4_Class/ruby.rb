puts "Enter the IPv4 address"
ip = gets.chomp.split('.')

def findClass(ip)
  if ip[0].to_i >= 1 and ip[0].to_i <= 126
		return "A"
  elsif ip[0].to_i >= 128 and ip[0].to_i <= 191
		return "B"
  elsif ip[0].to_i >= 192 and ip[0].to_i <= 223
		return "C"
  elsif ip[0].to_i >= 224 and ip[0].to_i <= 239
		return "D"
  elsif ip[0].to_i >= 240 and ip[0].to_i <= 255
    return "E"
  else
    return "INVALID"
  end
end

puts "This is a class #{findClass(ip)} IPv4 address"

exit
