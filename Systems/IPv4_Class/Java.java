import java.util.Scanner;

public class Java {
    public static void main(String[] args){

        String ip;
        String ipSplit[];
        int ipTag;
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the IPv4 address: ");
        ip = input.nextLine();

        ipSplit = ip.split("\\.");

        if (ipSplit.length != 4) {
            System.out.println("Invalid IPv4 address");
            return;
        }

        ipTag = Integer.parseInt(ipSplit[0]);
        if (ipTag < 0 || ipTag > 255)
            System.out.println("Invalid IPv4 address");
        else if (ipTag >= 0 && ipTag < 128)
            System.out.println("This is a class A IPv4 address");
        else if (ipTag >= 128 && ipTag < 192)
            System.out.println("This is a class B IPv4 address");
        else if (ipTag >= 192 && ipTag < 224)
            System.out.println("This is a class C IPv4 address");
        else if (ipTag >= 224 && ipTag < 240)
            System.out.println("This is a class D IPv4 address");
        else if (ipTag >= 240 && ipTag < 256)
            System.out.println("This is a class E IPv4 address");
    }
}
