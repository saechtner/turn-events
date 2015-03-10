package turnauswertung;

import java.io.FileReader;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import turnauswertung.model.dbConnection.DBConnector;
import turnauswertung.model.dbConnection.JavaDBConnector;
import turnauswertung.model.dbConnection.MySQLConnector;
import turnauswertung.view.MainFrame;

public class Main {

    public static void main(String[] args) {
        try {
            JSONParser jsonParser = new JSONParser();
            Object obj = jsonParser.parse(new FileReader("json/model_settings.json"));

            JSONObject jsonObject = (JSONObject) obj;
            String dbms = (String) jsonObject.get("dbms");
            String databaseName = (String) jsonObject.get("database");

            if(dbms.equals("MySQL")) {
                String name = (String) jsonObject.get("name");
                String password = (String) jsonObject.get("password");
                String url = (String) jsonObject.get("url");
                DBConnector con = new MySQLConnector(databaseName, name, password);
                con.executeQuery("");
            } else if(dbms.equals("JavaDB")){
                DBConnector connection = new JavaDBConnector(databaseName);
                connection.initializeSchema();
            } else{
                System.out.println("Couldn't connect to any DB.");
            }

            MainFrame window = new MainFrame();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
