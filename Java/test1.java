public class test1
{
    int i =10;
    public void display(){
        System.out.println("test1");
    }
}

class test2 extends test1
{
    int i=20;
    public void display(){
        System.out.println("test2");
    }
    
    public static void main(String[] args) {
        test1 t1= new test2();
        System.out.println(t1.i);
    }
    
}