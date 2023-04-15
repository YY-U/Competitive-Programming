import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.*;

public class main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！

        // ファイルのパスを指定する
        /*File file = new File("./input1.txt");
        // ファイルが存在しない場合に例外が発生するので確認する
        if (!file.exists()) {
        System.out.print("ファイルが存在しません");
            return;
        }
        // BufferedReaderクラスのreadLineメソッドを使って1行ずつ読み込み表示する
        FileReader fileReader = new FileReader(file);*/

        Scanner sc = new Scanner(System.in);
        int[] intArray = Arrays.stream(sc.nextLine().split(" ")) //" "で区切ってString配列へ
            .mapToInt(Integer::parseInt) //数値にして
            .toArray(); //配列へ
        //System.out.println(intArray[0]);
        //System.out.println(intArray[1]);
        //System.out.println(intArray[0]+intArray[1]);
        
        //intArray[0]:number of cars
        //intArray[1]:threshold
        
        int car_d=0;
        int car_d_count=0;
        String[] strs= new String[intArray[0]];
        for (int i=0; i<intArray[0]-1; i++){
            strs[i] = sc.nextLine();
            car_d= Integer.parseInt(strs[i]);
            //System.out.println(car_d);
            if(car_d <= intArray[1]){
            car_d_count+=car_d;
            }
            
        }
        System.out.println(car_d_count);
        
    }
}
