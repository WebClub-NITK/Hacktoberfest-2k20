using System;

namespace CSharp {

    class CSharp {

        static void Main(String[] args){

            String ipInput;

            Console.Write("Enter the IPv4 address: ");
            ipInput = Console.ReadLine();
            string[] ipSegments = ipInput.Split('.');

            if (ipSegments.Length != 4)
                Console.WriteLine("Invalid IPv4 address");

            int classifier = Int32.Parse(ipSegments[0]);

            if (classifier < 0 || classifier > 255)
                Console.WriteLine("Invalid IPv4 address");
            else if (classifier >= 0 && classifier < 128)
                Console.WriteLine("This is a class A IPv4 address");
            else if (classifier >= 128 && classifier < 192)
                Console.WriteLine("This is a class B IPv4 address");
            else if (classifier >= 192 && classifier < 224)
                Console.WriteLine("This is a class C IPv4 address");
            else if (classifier >= 224 && classifier < 240)
                Console.WriteLine("This is a class D IPv4 address");
            else if (classifier >= 240 && classifier < 256)
                Console.WriteLine("This is a class E IPv4 address");
            
        }
    }

}