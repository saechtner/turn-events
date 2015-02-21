import NA_Model.NA_Database_Connection.NA_DB_Connector;
import NA_Model.NA_Database_Connection.NA_JavaDB_Connector;
import NA_View.NA_MainFrame;

import java.io.FileReader;
import java.sql.Connection;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

public class Main {

    public static void main(String[] args) {
        JSONParser parser = new JSONParser();

//        try {
//            Object obj = parser.parse(new FileReader(
//                    "src/NA_Model/NA_JSON/settings.json"));
//
//            JSONObject jsonObject = (JSONObject) obj;
//
//            String name = (String) jsonObject.get("name");
//            String password = (String) jsonObject.get("password");
//            String url = (String) jsonObject.get("url");
//
//            NA_DB_Connector con = new NA_DB_Connector(url,name,password);
//
//
//
//            NA_MainFrame window = new NA_MainFrame();
//
//        } catch (Exception e) {
//            e.printStackTrace();
//        }



        try {
            new NA_JavaDB_Connector("AuswertungDB").executeQuery("");
            System.out.println("Works");
        } catch (Exception e){
            System.out.println("Doesn't work");
        }
    }
}
