public class StringReverser {  
    public static void main(String[] args) {  
        String str = "Hello, world!";  
        StringBuilder sb = new StringBuilder(str);  
        sb.reverse();  
        String reversedStr = sb.toString();  
        System.out.println("The reversed string is: " + reversedStr);  
    }  
}  
