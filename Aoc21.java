package course;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class HelloWorld {

    public static void main(String[] args) {
        String fileName = "C:\\Users\\shaij\\Documents\\input.txt";
        List<String> listOfDepths = new ArrayList<>();
        try (BufferedReader br = Files.newBufferedReader(Paths.get(fileName))) {
            listOfDepths = br.lines().collect(Collectors.toList());
            System.out.println(listOfDepths);
        } catch (IOException e) {
            e.printStackTrace();
        }

        int count = 0;
        int prev = 0;

        for (String depth: listOfDepths) {
            if (prev == 0){
                System.out.println("Do nothing");
            } else if (Integer.parseInt(depth) > prev){
                count++;
            }
            prev = Integer.parseInt(depth);
        }
        System.out.println(count);
    }
}
