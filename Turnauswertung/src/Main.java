import NA_Model.NA_Database_Connection.NA_DB_Connector;
import NA_Model.NA_Database_Connection.NA_JavaDB_Connector;
import NA_Model.NA_Database_Connection.NA_MySQL_Connector;
import NA_View.NA_MainFrame;

import java.io.FileReader;
import java.sql.Connection;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

public class Main {

    public static void main(String[] args) {
        JSONParser parser = new JSONParser();

        try {
            Object obj = parser.parse(new FileReader(
                    "src/NA_Model/NA_JSON/settings.json"));

            JSONObject jsonObject = (JSONObject) obj;
            String dmbs = (String) jsonObject.get("dbms");
            String databaseName = (String) jsonObject.get("database");


            if(dmbs.equals("MySQL")) {
                String name = (String) jsonObject.get("name");
                String password = (String) jsonObject.get("password");
                String url = (String) jsonObject.get("url");
                NA_DB_Connector con = new NA_MySQL_Connector(databaseName, name, password);
                con.executeQuery("");
            } else if(dmbs.equals("JavaDB")){
                NA_DB_Connector con = new NA_JavaDB_Connector(databaseName);
                con.executeQuery("");
            } else{
                System.out.println("Couldn't connect to any DB.");
            }


            NA_MainFrame window = new NA_MainFrame();

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
