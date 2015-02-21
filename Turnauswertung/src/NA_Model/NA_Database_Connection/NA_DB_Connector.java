package NA_Model.NA_Database_Connection;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.List;

public class NA_DB_Connector {
    String name, password, url;
    Connection con;

    public NA_DB_Connector(String url, String name, String password){
        this.url = url;
        this.name = name;
        this.password = password;
        con = null;
    }

    private void connect(){
        try {
            con = DriverManager.getConnection("jdbc:mysql://"+url,name,password);
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    private void disconnect(){
        try{
            con.close();
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    void executeQuery(String query){
        connect();


        disconnect();
    }

    List<String> retrieveData(String query){
        connect();


        disconnect();
        return null;
    }

}