package NA_Model.NA_Database_Connection;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

public abstract class NA_DB_Connector {
    private String databaseName;
    private Connection connection;

    protected Connection getConnection(){
        return connection;
    }

    protected void setConnection(Connection newConnection){
        connection = newConnection;
    }

    protected String getDatabaseName(){
        return databaseName;
    }

    protected void setDatabaseName(String newUrl){
        databaseName = newUrl;
    }

    protected abstract void connect();

    protected void disconnect(){
        try{
            getConnection().close();
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    public abstract void executeQuery(String query);

    public abstract List<String> retrieveData(String query);

    // Constants
    protected String urlPrefix(){
        return "jdbc:";
    }
}