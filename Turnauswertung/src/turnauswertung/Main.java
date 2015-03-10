package turnauswertung;
import Model.dbConnection.DB_Connector;
import Model.dbConnection.JavaDB_Connector;
import Model.dbConnection.MySQL_Connector;

import java.io.FileReader;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import turnauswertung.view.MainFrame;

public class Main {

    public static void main(String[] args) {
        try {
            JSONParser jsonParser = new JSONParser();
            Object obj = jsonParser.parse(new FileReader(
                    "src/Model/JSON/settings.json"));

            JSONObject jsonObject = (JSONObject) obj;
            String dmbs = (String) jsonObject.get("dbms");
            String databaseName = (String) jsonObject.get("database");


            if(dmbs.equals("MySQL")) {
                String name = (String) jsonObject.get("name");
                String password = (String) jsonObject.get("password");
                String url = (String) jsonObject.get("url");
                DB_Connector con = new MySQL_Connector(databaseName, name, password);
                con.executeQuery("");
            } else if(dmbs.equals("JavaDB")){
                DB_Connector connection = new JavaDB_Connector(databaseName);
                connection.initializeScheme();
            } else{
                System.out.println("Couldn't connect to any DB.");
            }


            MainFrame window = new MainFrame();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
