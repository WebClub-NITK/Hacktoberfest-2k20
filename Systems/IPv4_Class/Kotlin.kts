print("Write anything here: ")

val address = readLine().toString()
fun ipv_class(inp : String) {

    val delim = '.'
    val arr = listOf(inp.split(delim))
    val cls = arr[0][0].toInt()


    val result = if (cls in 1..126)
        "A"
    else if (cls in 127..191)
        "B"
    else if (cls in 192..223)
        "C"
    else if (cls in 224.. 239)
        "D"
    else
        "E"
    println("Class is $result")
}


ipv_class(address)
